# So the accurate interview statement is:
# "Pandas was used for preprocessing the structured search results. I used it to clean and deduplicate results, 
# filter low-relevance sources, and select the most relevant results before passing them to the downstream agent.
# This also helps reduce unnecessary context being sent to the LLM."



from typing import TypedDict
from rich import print
from langgraph.graph import StateGraph, START, END

from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain
)

class ResearchState(TypedDict):
    topic: str
    search_results: str
    scraped_content: str
    report: str
    feedback: str

def _text(message) -> str:
    content = message.content

    if isinstance(content, list):
        print("------------_text() called ----------------")
        return "".join(
            part.get("text", "")
            for part in content
            if isinstance(part, dict)
        )

    return content


def search_node(state: ResearchState):

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            (
                "user",
                f"Find recent, reliable and detailed information about: "
                f"{state['topic']}"
            )
        ]
    })

    print(" ================ search_result ===============>", search_result)    
    return {
        "search_results": _text(
            search_result["messages"][-1]
        )
    }

def reader_node(state: ResearchState):

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"Based on the following search results about "
                f"'{state['topic']}', pick the most relevant URL "
                f"and scrape it for deeper content.\n\n"
                f"Search Results:\n"
                f"{state['search_results'][:800]}"
            )
        ]
    })
    print("================ reader_result ===============>", reader_result)    
    return {
        "scraped_content": _text(
            reader_result["messages"][-1]
        )
    }

def writer_node(state: ResearchState):

    research_combined = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
    )

    print("================ research_combined ============>", research_combined)
    report = writer_chain.invoke({
        "topic": state["topic"],
        "research": research_combined
    })

    print("================ report ==============>", report)
    return {
        "report": report
    }

def critic_node(state: ResearchState):
    feedback = critic_chain.invoke({
        "report": state["report"]
    })

    print("================ critic (feedback) ================", feedback)
    return {
        "feedback": feedback
    }

# Create graph
graph = StateGraph(ResearchState)

graph.add_node("search", search_node)
graph.add_node("reader", reader_node)
graph.add_node("writer", writer_node)
graph.add_node("critic", critic_node)

# Define workflow
graph.add_edge(START, "search")
graph.add_edge("search", "reader")
graph.add_edge("reader", "writer")
graph.add_edge("writer", "critic")
graph.add_edge("critic", END)

# Compile
research_graph = graph.compile()

if __name__ == "__main__":

    topic = input("\nPlease enter a research topic: ")

    result = research_graph.invoke({
        "topic": topic
    })

    print("\nFINAL REPORT:\n")
    print(result["report"])

    print("\nCRITIC FEEDBACK:\n")
    print(result["feedback"])