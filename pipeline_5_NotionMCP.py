import asyncio

from rich import print
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.shared._httpx_utils import create_mcp_http_client

from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain
from NotionMCP.notion_auth import SERVER_URL, build_notion_auth
from NotionMCP.notion_mcp import (
    find_existing_report,
    read_existing_report,
    save_report,
)


def _text(message) -> str:
    """Gemini can return content as a list of blocks instead of a plain string."""
    content = message.content
    if isinstance(content, list):
        return "".join(part.get("text", "") for part in content if isinstance(part, dict))
    return content

async def run_research_pipeline(topic: str, session) -> dict:

    state = {"topic": topic}

    print("============== step - 0 checking Notion for an existing report ==============")
    existing = await find_existing_report(session, topic)

    if existing:
        print("Found existing report:", existing["url"])
        return {
            "topic": topic,
            "report": await read_existing_report(session, existing["id"]),
            "source": "notion",
            "notion_url": existing["url"],
        }
    print("print - existing ", existing)
    print("==================== step - 1 search agent working ==================  ")

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    print("\nsearch results:----------------->\n", search_result)
    state["search_results"] = _text(search_result['messages'][-1])  # [-1] becoz we get the ai res at last -1 position


    print("================== step - 2 Reader agent is scraping top resources =============")
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
                      f"Based on the following search results about '{topic},"
                      f"pick the most relevant URL and scrape it for deeper content.\n\n"
                      f"Search Results:\n{state['search_results'][:800]}"  # Only send first 800 chars becoz those only contains urls
                      )]
    })
    print("\nreader_result:----------->\n", reader_result)
    state['scraped_content'] = _text(reader_result['messages'][-1])

    print("====================== step 3 - Writer is drafting the report ==================")
    research_combined = (
        f"SEARCH RESULTS: \n {state['search_results']}"
        f"DETAILED SCRAPPED CONTENT: \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    print("\n Final Report ----------------->\n", state["report"])

    print("==================== step - 4 critic is reviewing the report ====================")
    state["feedback"] = critic_chain.invoke({
        "report": state['report']
    })
    print("\n critic report-----------------> \n", state['feedback'])

    print("==================== step - 5 saving the report to Notion ==================")
    saved = await save_report(session, topic, state["report"])
    state["source"] = "generated"
    state["notion_url"] = saved["url"]
    print("Saved to Notion:", saved["url"])

    return state  # returned so the API can send it to the frontend

async def main():
    topic = input("\n Please enter a research topic : ")

    http_client = create_mcp_http_client(auth=build_notion_auth())

    async with streamable_http_client(SERVER_URL, http_client=http_client) as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            await run_research_pipeline(topic, session)

if __name__ == "__main__":
    asyncio.run(main())
