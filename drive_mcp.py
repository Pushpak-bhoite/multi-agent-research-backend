
# drive_mcp.py

import json
import re


def extract_result(result) -> dict:
    """Parse the response returned by an MCP tool."""

    structured = getattr(result, "structured_content", None)
    if structured:
        return structured

    for item in getattr(result, "content", []):
        text = getattr(item, "text", None)
        if text:
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                continue

    raise RuntimeError(f"Could not parse MCP result: {result}")


def report_filename(topic: str) -> str:
    """Build a consistent filename from a research topic."""

    safe_topic = re.sub(r'[\\/*?:"<>|]', "", topic).strip()
    return f"Research - {safe_topic}.txt"


async def find_existing_report(session, topic: str):
    """Return matching report metadata, or None if no report exists."""

    filename = report_filename(topic)
    escaped_filename = filename.replace("\\", "\\\\").replace("'", "\\'")

    result = await session.call_tool(
        "search_files",
        arguments={
            "query": f"title = '{escaped_filename}'",
            "pageSize": 10,
            "excludeContentSnippets": True,
        },
    )

    if result.is_error:
        raise RuntimeError(f"Drive search failed: {result.content}")

    data = extract_result(result)

    for file in data.get("files", []):
        if file.get("title") == filename:
            return file

    return None


async def read_existing_report(session, file_id: str) -> str:
    """Read the report's contents from Google Drive."""

    result = await session.call_tool(
        "read_file_content",
        arguments={
            "fileId": file_id,
            "includeComments": False,
        },
    )

    if result.is_error:
        raise RuntimeError(f"Reading the Drive report failed: {result.content}")

    data = extract_result(result)
    content = data.get("fileContent", "")

    if not content:
        raise RuntimeError(
            "The report was found, but its content was empty or unavailable."
        )

    return content


async def save_report(session, topic: str, report: str) -> dict:
    """Create a text file containing the generated report in Drive."""

    result = await session.call_tool(
        "create_file",
        arguments={
            "title": report_filename(topic),
            "contentMimeType": "text/plain",
            "textContent": report,
            "disableConversionToGoogleType": True,
        },
    )

    if result.is_error:
        raise RuntimeError(f"Saving the report failed: {result.content}")

    data = extract_result(result)

    return {
        "file_id": data.get("id"),
        "filename": data.get("title"),
        "url": data.get("viewUrl"),
    }
