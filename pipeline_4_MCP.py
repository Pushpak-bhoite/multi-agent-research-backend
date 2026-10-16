
# pipeline_4_MCP.py

import asyncio
from rich import print

from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain,
)

from drive_mcp import (
    find_existing_report,
    read_existing_report,
    save_report,
)


def _text(message) -> str:
    """Extract text from an agent message."""

    content = getattr(message, "content", message)

    if isinstance(content, list):
        return "".join(
            part.get("text", "")
            for part in content
            if isinstance(part, dict)
        )

    return str(content)


async def run_research_pipeline(topic: str, session) -> dict:
    print(f"\nResearch topic: {topic}")

    # STEP 1: Check Drive before running any research agents.
    print("Checking Google Drive...")

    existing = await find_existing_report(session, topic)

    if existing:
        print(f"Found existing report: {existing.get('title')}")

        report = await read_existing_report(
            session,
            existing["id"],
        )

        return {
            "topic": topic,
            "report": report,
            "source": "google_drive",
            "drive_url": existing.get("viewUrl"),
        }

    print("No existing report found. Starting research...")

    state = {"topic": topic}

    # STEP 2: Search agent
    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            (
                "user",
                f"Find recent, reliable and detailed information about: {topic}",
            )
        ]
    })

    state["search_results"] = _text(
        search_result["messages"][-1]
    )

    # STEP 3: Reader agent
    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"Research '{topic}' using these search results:\n"
                f"{state['search_results'][:800]}",
            )
        ]
    })

    state["scraped_content"] = _text(
        reader_result["messages"][-1]
    )

    # STEP 4: Writer generates the report
    research = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"SCRAPED CONTENT:\n{state['scraped_content']}"
    )

    report_result = writer_chain.invoke({
        "topic": topic,
        "research": research,
    })

    state["report"] = _text(report_result)

    # STEP 5: Critic reviews the report
    state["feedback"] = critic_chain.invoke({
        "report": state["report"],
    })

    # STEP 6: Save the generated report to Drive
    saved_file = await save_report(
        session=session,
        topic=topic,
        report=state["report"],
    )

    state["source"] = "generated"
    state["drive_url"] = saved_file.get("url")

    print(f"Report saved: {saved_file.get('filename')}")
    print(f"Drive URL: {state['drive_url']}")

    return state


# ===================================================================================

import os

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from google_auth import get_access_token

async def main():
    topic = input("Enter research topic: ").strip()

    access_token = get_access_token()
    if not access_token:
        raise RuntimeError(
            "Set GOOGLE_ACCESS_TOKEN using your Google OAuth flow."
        )

    server_url = "https://drivemcp.googleapis.com/mcp/v1"

    async with streamablehttp_client(
        server_url,
        headers={"Authorization": f"Bearer {access_token}"},
    ) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            result = await run_research_pipeline(topic, session)

            print("\n========== REPORT ==========\n")
            print(result["report"])

            print("\nSource:", result["source"])
            print("Drive URL:", result.get("drive_url"))


if __name__ == "__main__":
    asyncio.run(main())
