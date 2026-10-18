import os
import re

# The Notion page that every generated report is filed under.
PARENT_PAGE_ID = "3fb66497f2ca809f95d0febf911e8e38"

DEBUG = os.getenv("NOTION_MCP_DEBUG") == "1"

_PAGE_URL = re.compile(r"https://www\.notion\.so/\S*?([0-9a-f]{32})")


def report_title(topic: str) -> str:
    return f"Research - {topic.strip()}"


def _normalise(text: str) -> str:
    return " ".join(text.split()).casefold()


def _locate(body: str, title: str) -> dict | None:
    """Find the line mentioning `title` and the page URL nearest to it."""
    wanted = _normalise(title)
    lines = body.splitlines()

    for index, line in enumerate(lines):
        if wanted not in _normalise(line):
            continue

        # The URL may sit on the matching line or just after it.
        window = "\n".join(lines[index : index + 3])
        match = _PAGE_URL.search(window)
        if match:
            return {"title": title, "id": match.group(1), "url": match.group(0)}

    return None


def _result_text(result) -> str:
    return "\n".join(
        text
        for item in getattr(result, "content", [])
        if (text := getattr(item, "text", None))
    )


def _failed(result) -> bool:
    # Attribute spelling differs between mcp SDK versions.
    return bool(getattr(result, "isError", False) or getattr(result, "is_error", False))


async def find_existing_report(session, topic: str) -> dict | None:
    """Return metadata for a previously saved report, or None.

    Reads the parent page rather than searching, because Notion's search index
    lags behind page creation by minutes.
    """
    title = report_title(topic)

    result = await session.call_tool("notion-fetch", {"id": PARENT_PAGE_ID})

    if _failed(result):
        raise RuntimeError(f"Reading the parent page failed: {_result_text(result)}")

    body = _result_text(result)

    if DEBUG:
        print("---- notion-fetch(parent) raw ----")
        print(body)
        print("---- end ----")

    hit = _locate(body, title)
    if hit:
        return hit

    # Fallback: the report may live outside the parent page.
    result = await session.call_tool(
        "notion-search",
        {"query": title, "page_size": 10},
    )

    if _failed(result):
        raise RuntimeError(f"Notion search failed: {_result_text(result)}")

    body = _result_text(result)

    if DEBUG:
        print("---- notion-search raw ----")
        print(body)
        print("---- end ----")

    return _locate(body, title)


async def read_existing_report(session, page_id: str) -> str:
    """Read a saved report's content as Markdown."""
    result = await session.call_tool("notion-fetch", {"id": page_id})

    if _failed(result):
        raise RuntimeError(f"Reading the Notion report failed: {_result_text(result)}")

    return _result_text(result)


async def save_report(session, topic: str, report) -> dict:
    """Create a child page under PARENT_PAGE_ID holding the report."""
    content = report if isinstance(report, str) else getattr(report, "content", str(report))

    result = await session.call_tool(
        "notion-create-pages",
        {
            "parent": {"page_id": PARENT_PAGE_ID},
            "pages": [
                {"properties": {"title": report_title(topic)}, "content": content}
            ],
            # Synchronous so the page URL is available immediately.
            "allow_async": False,
        },
    )

    if _failed(result):
        raise RuntimeError(f"Saving the report to Notion failed: {_result_text(result)}")

    body = _result_text(result)
    match = _PAGE_URL.search(body)

    return {
        "title": report_title(topic),
        "id": match.group(1) if match else None,
        "url": match.group(0) if match else None,
        "raw": body,
    }
