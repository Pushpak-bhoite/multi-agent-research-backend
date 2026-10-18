import os
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.file",
]

# Absolute so the MCP server subprocess resolves the same file as the pipeline.
TOKEN_FILE = str(Path(__file__).resolve().parent / "token.json")

# run_local_server can only emit "http://localhost:<port>/", so this must be registered verbatim.
REDIRECT_PORT = 3030


def load_credentials(interactive: bool = True) -> Credentials:
    """Return usable Drive credentials, running the OAuth consent flow if needed."""
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        if not interactive:
            raise RuntimeError(
                "No valid Google credentials. Run `python google_auth.py` first."
            )

        flow = InstalledAppFlow.from_client_config(
            {
                "installed": {
                    "client_id": os.environ["GOOGLE_DRIVE_MCP_CLIENT_ID"],
                    "client_secret": os.environ["GOOGLE_DRIVE_MCP_CLIENT_SECRET"],
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": ["http://localhost"],
                }
            },
            SCOPES,
        )
        creds = flow.run_local_server(
            port=REDIRECT_PORT,
            access_type="offline",
            prompt="consent",
        )

    with open(TOKEN_FILE, "w") as f:
        f.write(creds.to_json())

    return creds


def get_access_token() -> str:
    return load_credentials().token


if __name__ == "__main__":
    load_credentials()
    print(f"Google Drive authorization complete. Token stored at {TOKEN_FILE}")