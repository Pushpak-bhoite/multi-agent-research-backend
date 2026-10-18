import json
import os
import re

# The Notion page that every generated report is filed under.
PARENT_PAGE_ID = "3fb66497f2ca809f95d0febf911e8e38"

DEBUG = os.getenv("NOTION_MCP_DEBUG") == "1"

# Child pages appear in the parent's fetch text as <page url="...">Title</page>.
_CHILD_PAGE = re.compile(r'<page url="([^"]+)"[^>]*>([^<\n]*)</page>')
_CONTENT_BLOCK = re.compile(r"<content>\n?(.*?)\n?</content>", re.DOTALL)
_HEX_ID = re.compile(
    r"([0-9a-fA-F]{32})|([0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12})"
)


def report_title(topic: str) -> str:
    return f"Research - {topic.strip()}"


def _normalise(text: str) -> str:
    return " ".join(text.split()).casefold()


def _result_text(result) -> str:
    return "\n".join(
        text
        for item in getattr(result, "content", [])
        if (text := getattr(item, "text", None))
    )

def _failed(result) -> bool:
    # Attribute spelling differs between mcp SDK versions.
    return bool(getattr(result, "isError", False) or getattr(result, "is_error", False))


def _payload(result) -> dict:
    """Notion MCP wraps a JSON document inside the text content block."""
    body = _result_text(result)

    if DEBUG:
        print("---- notion raw ----")
        print(body)
        print("---- end ----")

    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return {"text": body}

    return data if isinstance(data, dict) else {"text": body}


def _page_id(value: str | None) -> str | None:
    """Normalise a page URL or dashed UUID to a bare 32-character id."""
    if not value:
        return None

    match = _HEX_ID.search(value)
    if not match:
        return None

    return (match.group(1) or match.group(2)).replace("-", "").lower()


async def find_existing_report(session, topic: str) -> dict | None:
    """Return metadata for a previously saved report, or None.

    Reads the parent page first, because Notion's search index lags behind page
    creation by minutes.
    """
    title = report_title(topic)
    wanted = _normalise(title)

    result = await session.call_tool("notion-fetch", {"id": PARENT_PAGE_ID})

    if _failed(result):
        raise RuntimeError(f"Reading the parent page failed: {_result_text(result)}")

    for url, child_title in _CHILD_PAGE.findall(_payload(result).get("text", "")):
        if _normalise(child_title) == wanted:
            return {"title": child_title, "id": _page_id(url), "url": url}

    # Fallback: the report may have been moved out of the parent page.
    result = await session.call_tool(
        "notion-search",
        {"query": title, "query_type": "internal"},
    )

    if _failed(result):
        raise RuntimeError(f"Notion search failed: {_result_text(result)}")

    for hit in _payload(result).get("results", []):
        if _normalise(hit.get("title", "")) == wanted:
            return {
                "title": hit["title"],
                "id": _page_id(hit.get("id") or hit.get("url")),
                "url": hit.get("url"),
            }

    return None


async def read_existing_report(session, page_id: str) -> str:
    """Read a saved report's body as Markdown."""
    result = await session.call_tool("notion-fetch", {"id": page_id})

    if _failed(result):
        raise RuntimeError(f"Reading the Notion report failed: {_result_text(result)}")

    text = _payload(result).get("text", "")
    block = _CONTENT_BLOCK.search(text)

    return block.group(1) if block else text


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
        },
    )

    if _failed(result):
        raise RuntimeError(f"Saving the report to Notion failed: {_result_text(result)}")

    pages = _payload(result).get("pages") or []
    page = pages[0] if pages else {}

    return {
        "title": report_title(topic),
        "id": _page_id(page.get("id") or page.get("url")),
        "url": page.get("url"),
    }
