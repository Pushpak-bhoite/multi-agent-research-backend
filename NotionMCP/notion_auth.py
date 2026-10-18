import json
from collections.abc import Awaitable, Callable
from pathlib import Path

from mcp.client.auth import OAuthClientProvider
from mcp.shared.auth import (
    OAuthClientInformationFull,
    OAuthClientMetadata,
    OAuthToken,
)
from mcp.shared.auth_utils import calculate_token_expiry
from pydantic import AnyUrl

SERVER_URL = "https://mcp.notion.com/mcp"
CALLBACK_PORT = 3030
REDIRECT_URI = f"http://localhost:{CALLBACK_PORT}/callback"
STORE_FILE = Path(__file__).with_name("notion_oauth.json")


class FileTokenStorage:
    """Persists the registered client and its tokens so re-runs skip the browser."""

    def __init__(self, path: Path) -> None:
        self._path = path

    def _read(self) -> dict:
        if self._path.exists():
            return json.loads(self._path.read_text())
        return {}

    def _write(self, data: dict) -> None:
        self._path.write_text(json.dumps(data, indent=2))
        self._path.chmod(0o600)

    async def get_tokens(self) -> OAuthToken | None:
        raw = self._read().get("tokens")
        return OAuthToken.model_validate(raw) if raw else None

    async def set_tokens(self, tokens: OAuthToken) -> None:
        data = self._read()
        data["tokens"] = tokens.model_dump(mode="json", exclude_none=True)
        data["expires_at"] = calculate_token_expiry(tokens.expires_in)
        self._write(data)

    def get_expires_at(self) -> float | None:
        return self._read().get("expires_at")

    async def get_client_info(self) -> OAuthClientInformationFull | None:
        raw = self._read().get("client_info")
        return OAuthClientInformationFull.model_validate(raw) if raw else None

    async def set_client_info(self, client_info: OAuthClientInformationFull) -> None:
        data = self._read()
        data["client_info"] = client_info.model_dump(mode="json", exclude_none=True)
        self._write(data)


class PersistentOAuthClientProvider(OAuthClientProvider):
    """The SDK restores tokens but not their expiry, so a stale token is sent, gets a
    401, and triggers a full browser re-auth instead of a silent refresh."""

    async def _initialize(self) -> None:
        await super()._initialize()

        storage = self.context.storage
        if isinstance(storage, FileTokenStorage):
            self.context.token_expiry_time = storage.get_expires_at()


def build_notion_auth(
    redirect_handler: Callable[[str], Awaitable[None]] | None = None,
    callback_handler: Callable[[], Awaitable[tuple[str, str | None]]] | None = None,
) -> OAuthClientProvider:
    """Reuses the stored token. Handlers are only needed by authorize.py; without them
    an expired refresh token raises instead of silently waiting on a browser."""
    return PersistentOAuthClientProvider(
        server_url=SERVER_URL,
        client_metadata=OAuthClientMetadata(
            client_name="Multi-Agent Research Backend",
            redirect_uris=[AnyUrl(REDIRECT_URI)],
            grant_types=["authorization_code", "refresh_token"],
            response_types=["code"],
            # Public PKCE client: Notion rejects client_id in the body alongside a Basic header.
            token_endpoint_auth_method="none",
        ),
        storage=FileTokenStorage(STORE_FILE),
        redirect_handler=redirect_handler,
        callback_handler=callback_handler,
    )