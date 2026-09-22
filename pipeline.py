from rich import print
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain


def _text(message) -> str:
    """Gemini can return content as a list of blocks instead of a plain string."""
    content = message.content
    if isinstance(content, list):
        return "".join(part.get("text", "") for part in content if isinstance(part, dict))
    return content

def run_research_pipeline(topic: str) -> dict:

    state = {"topic": topic}
    
    print("==================== step - 1 search agent working ==================  ")

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    print("\nsearch results:----------------->\n", search_result)
    state["search_results"] = _text(search_result['messages'][-1])  # [-1] becoz we get the ai res at last -1 position

    print("step - 2 ========= Reader agent is scraping top resources =============")
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

    print("========== step 3 - Writer is drafting the report ==========")
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

    return state  # returned so the API can send it to the frontend

if __name__ == "__main__":
    topic = input("\n Please enter a research topic : ")
    run_research_pipeline(topic)
