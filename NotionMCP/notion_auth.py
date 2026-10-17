import asyncio
import json
import webbrowser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from mcp.client.auth import OAuthClientProvider
from mcp.shared.auth import (
    AuthorizationCodeResult,
    OAuthClientInformationFull,
    OAuthClientMetadata,
    OAuthToken,
)
from pydantic import AnyUrl

SERVER_URL = "https://mcp.notion.com/mcp"
CALLBACK_PORT = 3030
REDIRECT_URI = f"http://localhost:{CALLBACK_PORT}/callback"
STORE_FILE = Path(__file__).with_name("notion_oauth.json")
CALLBACK_TIMEOUT_SECONDS = 300


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
        self._write(data)

    async def get_client_info(self) -> OAuthClientInformationFull | None:
        raw = self._read().get("client_info")
        return OAuthClientInformationFull.model_validate(raw) if raw else None

    async def set_client_info(self, client_info: OAuthClientInformationFull) -> None:
        data = self._read()
        data["client_info"] = client_info.model_dump(mode="json", exclude_none=True)
        self._write(data)


async def _open_browser(authorization_url: str) -> None:
    print(f"\nAuthorize this app in your browser:\n{authorization_url}\n")
    webbrowser.open(authorization_url)


async def _wait_for_callback() -> AuthorizationCodeResult:
    params: dict[str, str] = {}
    done = asyncio.Event()

    async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        request_line = await reader.readline()
        target = request_line.decode("latin-1").split(" ")[1]
        params.update({k: v[0] for k, v in parse_qs(urlparse(target).query).items()})

        body = b"<html><body><h2>Authorization complete. You can close this tab.</h2></body></html>"
        writer.write(
            b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: "
            + str(len(body)).encode()
            + b"\r\n\r\n"
            + body
        )
        await writer.drain()
        writer.close()
        done.set()

    server = await asyncio.start_server(handle, "127.0.0.1", CALLBACK_PORT)
    async with server:
        await asyncio.wait_for(done.wait(), timeout=CALLBACK_TIMEOUT_SECONDS)

    if "code" not in params:
        raise RuntimeError(f"Authorization failed: {params}")

    return AuthorizationCodeResult(
        code=params["code"],
        state=params.get("state"),
        iss=params.get("iss"),
    )


def build_notion_auth() -> OAuthClientProvider:
    """Notion's remote MCP server supports dynamic client registration, so no
    pre-registered client ID or secret is needed."""
    return OAuthClientProvider(
        server_url=SERVER_URL,
        client_metadata=OAuthClientMetadata(
            client_name="Multi-Agent Research Backend",
            redirect_uris=[AnyUrl(REDIRECT_URI)],
            grant_types=["authorization_code", "refresh_token"],
            response_types=["code"],
        ),
        storage=FileTokenStorage(STORE_FILE),
        redirect_handler=_open_browser,
        callback_handler=_wait_for_callback,
    )