import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/drive.file",
]
TOKEN_FILE = "token.json"

# run_local_server can only emit "http://localhost:<port>/", so this must be registered verbatim.
REDIRECT_PORT = 3030

def get_access_token() -> str:
    """ we  need to run OAuth consent flow to access token """
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    elif not creds or not creds.valid:
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
        creds = flow.run_local_server(port=REDIRECT_PORT)

    with open(TOKEN_FILE, "w") as f:
        f.write(creds.to_json())

    return creds.token