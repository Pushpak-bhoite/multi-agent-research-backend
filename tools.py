from langchain.tools import tool
import httpx #its alternative for both Request and aiohttps
from urllib.parse import urlparse
MAX_CHARS = 3000 
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
import pandas as pd

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# ### This is without pandas, we are manually preparing data.
# @tool # to make this function tool use this decorator
# def web_search(query: str) -> str : 
#     """Search the web for recent and reliable information on any topic. Returns Titles, URLs and snippets  """
#     results = tavily.search(query=query, max_results=5)
#     out = []
    
#     for r in results["results"]:
#         out.append(f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}") # content only 300 lines as we gonna retrive more data with BeautifulSoup
    
#     return "\n-----\n".join(out) 

# **** Now with pandas version i dont need to limit description as well.

@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on any topic.
    Returns cleaned and relevant titles, URLs and snippets.
    """

    results = tavily.search(
        query=query,
        max_results=5
    )
    
    # ============ Pandas (dataframe) Pipeline ==============
    print("tavily results ==========>", results)
    # Convert Tavily results into a DataFrame
    df = pd.DataFrame(results["results"])
    print("df===========>\n", df)
    # Remove duplicate URLs
    df = df.drop_duplicates(subset=["url"])

    # Remove results without URLs
    df = df.dropna(subset=["url"])

    # Sort by Tavily relevance score if available
    if "score" in df.columns:
        df = df.sort_values(
            by="score",
            ascending=False
        )

    # Keep only top 3 useful results
    df = df.head(3)

    # Convert the cleaned results back into text
    out = []

    for _, row in df.iterrows():

        out.append(
            f"Title: {row['title']}\n"
            f"URL: {row['url']}\n"
            f"Snippet: {str(row['content'])[:300]}"
        )
    print("out=======>", out)
    return "\n-----\n".join(out)

print(web_search.invoke(" Impact of ai on jobs in 2026 "))
     
@tool # we dont need this much big code, we can reduce code for understanding. it's ai given code
def scrape_url(url: str) -> str:
    """Fetch a web page and return its readable text content. Use after web_search to read a promising URL in full."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return f"Error: unsupported URL scheme '{parsed.scheme}'. Only http/https allowed."

    try:
        resp = httpx.get(
            url,
            timeout=15.0,
            follow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ResearchBot/1.0)"}, #this make feel like real user reading web. otherwise website blocks the page. 
        )
        resp.raise_for_status()
    except httpx.HTTPStatusError as e:
        return f"Error: {url} returned HTTP {e.response.status_code}"
    except httpx.RequestError as e:
        return f"Error fetching {url}: {e}"

    if "html" not in resp.headers.get("content-type", ""):
        return f"Error: {url} is not an HTML page."

    soup = BeautifulSoup(resp.text, "html.parser") #resp.text includes everything (tags and all)
    for tag in soup(["script", "style", "nav", "header", "footer", "aside", "noscript", "form"]):
        tag.decompose()

    text = "\n".join(line for line in soup.get_text("\n").splitlines() if line.strip()) # soup.get_text("\n") replace each tag new line

    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS] + "\n\n[...truncated]"
        
    title = soup.title.string.strip() if soup.title and soup.title.string else "Untitled"
    return f"Title: {title}\nURL: {url}\n\n{text}"
    
# print(scrape_url.invoke("https://edition.cnn.com/world/middleeast/israel"))