
# okay main changes while implementing NLP is we are not using scraping agent and scrape_url tool as well 
# rather using direct fetch function to scrape url's becoz nlp node require that structured
# data to process -> create embedding -> apply cosine similarity search and find most relavent passages from all scrapping -> writer

# search_node   → search agent + web_search tool  → summary text + URL list (regex over all messages)
# reader_node   → fetch_page in parallel, no LLM  → [{title, url, content}]
# nlp_node      → TF-IDF + cosine, no LLM         → top-k relevant passages
# writer_node   → writer_chain                    → report
# critic_node   → critic_chain                    → feedback

import re
from concurrent.futures import ThreadPoolExecutor
from typing import TypedDict
from rich import print
from langgraph.graph import StateGraph, START, END
from langchain_core.callbacks import get_usage_metadata_callback
from agents import (
    build_search_agent,
    writer_chain,
    critic_chain
)
from tools import SEARCH_RESULTS, fetch_page
from nlp import select_relevant

MIN_PAGES = 4

class ResearchState(TypedDict):
    topic: str
    search_results: str
    urls: list
    scraped_content: list
    relevant_content: list
    report: str
    feedback: str

_URL = re.compile(r"https?://[^\s)\]>\"'`]+")


def _urls_from(messages, limit: int) -> list[str]:
    # read every message, not just the summary, so the LLM cannot drop URLs
    joined = "\n".join(m.content for m in messages if isinstance(m.content, str))
    found = (u.rstrip(".,);") for u in _URL.findall(joined))
    return list(dict.fromkeys(found))[:limit]


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
# ======================================= START ===============================================





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
        ),
        "urls": _urls_from(search_result["messages"], SEARCH_RESULTS)
    }

def reader_node(state: ResearchState):

    urls = state["urls"]

    with ThreadPoolExecutor(max_workers=max(len(urls), 1)) as pool:
        pages = [p for p in pool.map(fetch_page, urls) if p]

    print(f"================ scraped {len(pages)}/{len(urls)} pages ===============>")
    if len(pages) < MIN_PAGES:
        print(f"warning: only {len(pages)} pages readable, wanted at least {MIN_PAGES}")
    print("pages in reader ================>\n", pages)
    return {
        "scraped_content": pages
    }

def nlp_node(state: ResearchState):

    passages = select_relevant(
        state["topic"],
        state["scraped_content"]
    )
    
    kept = sum(len(p["text"]) for p in passages)
    raw = sum(len(d["content"]) for d in state["scraped_content"])
    print(f"================ nlp kept {len(passages)} passages, {kept}/{raw} chars ========")
    print("passages ================>\n",passages)
    return {
        "relevant_content": passages
    }

def writer_node(state: ResearchState):

    passages = "\n".join(
        f"- ({p['url']}) {p['text']}"
        for p in state["relevant_content"]
    )

    research_combined = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"MOST RELEVANT PASSAGES (ranked by similarity to the topic):\n{passages}"
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
graph.add_node("nlp", nlp_node)
graph.add_node("writer", writer_node)
graph.add_node("critic", critic_node)

# Define workflow
graph.add_edge(START, "search")
graph.add_edge("search", "reader")
graph.add_edge("reader", "nlp")
graph.add_edge("nlp", "writer")
graph.add_edge("writer", "critic")
graph.add_edge("critic", END)

# Compile
research_graph = graph.compile()


def run_research_pipeline(topic: str) -> dict:
    
    with get_usage_metadata_callback() as cb:
        result = research_graph.invoke({"topic": topic})

    usage = cb.usage_metadata  # {model_name: {input_tokens, output_tokens, total_tokens}}
    totals = {
        "input_tokens": sum(u["input_tokens"] for u in usage.values()),
        "output_tokens": sum(u["output_tokens"] for u in usage.values()),
        "total_tokens": sum(u["total_tokens"] for u in usage.values()),
    }
    print(f"================ tokens ================ {totals} per-model: {usage}")
    result = research_graph.invoke({"topic": topic})
    # scraped_content is tens of thousands of chars, so it stays out of the response
    return {
        "topic": topic,
        "report": result["report"],
        "feedback": result["feedback"],
        "sources": [
            {"title": d["title"], "url": d["url"]}
            for d in result["scraped_content"]
        ],
    }

if __name__ == "__main__":

    topic = input("\nPlease enter a research topic: ")

    result = research_graph.invoke({
        "topic": topic
    })

    print("\nFINAL REPORT:\n")
    print(result["report"])

    print("\nCRITIC FEEDBACK:\n")
    print(result["feedback"])