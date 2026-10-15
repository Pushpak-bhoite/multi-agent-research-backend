
import asyncio
import json
import os

from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

load_dotenv()

DRIVE_MCP_URL = "https://drivemcp.googleapis.com/mcp/v1"


def extract_text(result) -> str:
    """Convert MCP text content into a string."""
    parts = []

    for item in result.content:
        if hasattr(item, "text"):
            parts.append(item.text)

    return "\n".join(parts)


async def search_drive_files(session, topic: str) -> list[dict]:
    # Escape apostrophes for the Drive search query.
    safe_topic = topic.replace("\\", "\\\\").replace("'", "\\'")

    result = await session.call_tool(
        "search_files",
        arguments={
            "query": f"fullText contains '{safe_topic}'",
            "pageSize": 5,
        },
    )

    if result.isError:
        raise RuntimeError(extract_text(result))

    raw = extract_text(result)
    data = json.loads(raw)

    return data.get("files", [])


async def read_drive_file(session, file_id: str) -> str:
    result = await session.call_tool(
        "read_file_content",
        arguments={
            "fileId": file_id,
            "includeComments": False,
        },
    )

    if result.isError:
        raise RuntimeError(extract_text(result))

    raw = extract_text(result)

    try:
        data = json.loads(raw)
        return data.get("fileContent", raw)
    except json.JSONDecodeError:
        return raw


async def search_and_read_drive(topic: str) -> str:
    token = os.getenv("GOOGLE_DRIVE_ACCESS_TOKEN")

    if not token:
        raise RuntimeError(
            "Set GOOGLE_DRIVE_ACCESS_TOKEN in your .env file"
        )

    async with streamable_http_client(
        DRIVE_MCP_URL,
        headers={"Authorization": f"Bearer {token}"},
    ) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            files = await search_drive_files(session, topic)

            if not files:
                return "No relevant Google Drive files found."

            research_material = []

            for file in files[:3]:
                file_id = file.get("id")
                title = file.get("title", "Untitled")

                if not file_id:
                    continue

                content = await read_drive_file(session, file_id)

                research_material.append(
                    f"DOCUMENT: {title}\n"
                    f"FILE ID: {file_id}\n"
                    f"CONTENT:\n{content}"
                )

            return "\n\n".join(research_material)


def get_drive_research(topic: str) -> str:
    """Synchronous wrapper for the existing pipeline."""
    return asyncio.run(search_and_read_drive(topic))


if __name__ == "__main__":
    topic = input("Enter a search topic: ")
    print(get_drive_research(topic))
