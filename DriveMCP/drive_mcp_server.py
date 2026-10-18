# drive_mcp_server.py
"""Local MCP server (stdio) exposing the Drive tools the pipeline needs.

It mirrors the tool names/fields of Google's hosted Drive MCP server, so the
client code in drive_mcp.py works against either one.
"""

import io
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from mcp.server.fastmcp import FastMCP

from google_auth import TOKEN_FILE, load_credentials

mcp = FastMCP("local-drive")

# Google Docs/Sheets/Slides have no bytes to download; they must be exported.
GOOGLE_EXPORT_MIME = {
    "application/vnd.google-apps.document": "text/plain",
    "application/vnd.google-apps.spreadsheet": "text/csv",
    "application/vnd.google-apps.presentation": "text/plain",
}

_service = None


def _drive():
    global _service

    if _service is None:
        if not os.path.exists(TOKEN_FILE):
            raise RuntimeError(
                f"{TOKEN_FILE} not found. Run `python google_auth.py` once to "
                "complete the OAuth consent flow before starting this server."
            )

        _service = build(
            "drive",
            "v3",
            credentials=load_credentials(interactive=False),
            cache_discovery=False,
        )

    return _service


def _to_v3_query(query: str) -> str:
    """The hosted server speaks Drive v2 field names; v3 renamed a few."""

    query = re.sub(r"\btitle\b", "name", query)
    return re.sub(r"\bmodifiedDate\b", "modifiedTime", query)


def _as_file(item: dict) -> dict:
    return {
        "id": item.get("id"),
        "title": item.get("name"),
        "mimeType": item.get("mimeType"),
        "viewUrl": item.get("webViewLink"),
        "modifiedTime": item.get("modifiedTime"),
    }


@mcp.tool()
def search_files(
    query: str,
    pageSize: int = 10,
    excludeContentSnippets: bool = True,
) -> dict:
    """Search Drive files with a Drive query string, e.g. title = 'Report.txt'."""

    response = (
        _drive()
        .files()
        .list(
            q=f"{_to_v3_query(query)} and trashed = false",
            pageSize=pageSize,
            fields="files(id, name, mimeType, webViewLink, modifiedTime)",
            spaces="drive",
        )
        .execute()
    )

    return {"files": [_as_file(item) for item in response.get("files", [])]}


@mcp.tool()
def read_file_content(fileId: str, includeComments: bool = False) -> dict:
    """Return the text content of a Drive file."""

    service = _drive()

    meta = service.files().get(fileId=fileId, fields="id, name, mimeType").execute()
    mime_type = meta.get("mimeType", "")

    if mime_type in GOOGLE_EXPORT_MIME:
        data = service.files().export(
            fileId=fileId,
            mimeType=GOOGLE_EXPORT_MIME[mime_type],
        ).execute()
    else:
        data = service.files().get_media(fileId=fileId).execute()

    content = data.decode("utf-8", errors="replace") if isinstance(data, bytes) else str(data)

    return {
        "fileId": fileId,
        "title": meta.get("name"),
        "mimeType": mime_type,
        "fileContent": content,
    }


@mcp.tool()
def create_file(
    title: str,
    textContent: str,
    contentMimeType: str = "text/plain",
    disableConversionToGoogleType: bool = True,
) -> dict:
    """Create a new file in Drive containing the given text."""

    metadata = {"name": title}

    folder_id = os.environ.get("GOOGLE_DRIVE_FOLDER_ID")
    if folder_id:
        metadata["parents"] = [folder_id]

    if not disableConversionToGoogleType and contentMimeType == "text/plain":
        metadata["mimeType"] = "application/vnd.google-apps.document"

    media = MediaIoBaseUpload(
        io.BytesIO(textContent.encode("utf-8")),
        mimetype=contentMimeType,
        resumable=False,
    )

    created = (
        _drive()
        .files()
        .create(
            body=metadata,
            media_body=media,
            fields="id, name, mimeType, webViewLink, modifiedTime",
        )
        .execute()
    )

    return _as_file(created)


if __name__ == "__main__":
    mcp.run()
