"""Classical NLP relevance layer (TF-IDF + cosine similarity, not an LLM).

Scraped pages are split into sentence-level chunks and ranked against the research
topic, so the writer only sees the passages that actually matter.
"""
# TF-IDF - is a Statistical algorithm (not neural modal) : "car" and "automobile" look different with TD-IDF vectors bt with LLM vectors  "car" and "automobile" can be close
import re
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import httpx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MIN_CHUNK_CHARS = 40
MAX_CHUNK_CHARS = 400

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")

# splits each page on sentence endings (.!?) and keeps only sentences between 40 and 400 characters.
def chunk_text(text: str) -> list[str]:
    parts = (s.strip().replace("\n", " ") for s in _SENT_SPLIT.split(text))
    # length bounds drop nav links, cookie banners and other scraped boilerplate
    return [s for s in parts if MIN_CHUNK_CHARS <= len(s) <= MAX_CHUNK_CHARS]

# Vectorise — turns the topic and every sentence into a TF-IDF vector:
# "Python machine learning"
#         ↓
# [0.7, 0.4, 0.6, 0, 0, ...]   # it's sparse TF-IDF vector not vector embedding "all-MiniLM-L6-V2"

# TF (term frequency) — how often a word appears in this sentence
# IDF (inverse document frequency) — how rare that word is across all sentences
# Multiply them and common words like "the" get crushed to near-zero weight, while distinctive words carry the signal. Each sentence becomes a sparse vector with one slot per unique word in the whole collection — tens of thousands of slots, almost all zeros.
def score_tfidf(topic: str, chunks: list[str]):
    """Word-overlap relevance of every chunk against the topic."""
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), sublinear_tf=True)
    print(" vectorizer  ==============>", vectorizer)
    matrix = vectorizer.fit_transform([topic] + chunks)
    return cosine_similarity(matrix[0:1], matrix[1:])[0]


def select_relevant(
    topic: str,
    documents: list[dict],
    top_k: int = 25,
    per_source: int = 5,
    near_duplicate: float = 0.75,
    scorer=score_tfidf,
) -> list[dict]:
    """Rank chunks from all documents together and return the best ones.

    `scorer` is swappable: any callable taking (topic, chunks) and returning one
    score per chunk works, so embeddings can replace TF-IDF without other changes.
    """
    pool = [
        {"title": doc["title"], "url": doc["url"], "text": chunk}
        for doc in documents
        for chunk in chunk_text(doc["content"])
    ]
    if not pool:
        return []

    texts = [item["text"] for item in pool]

    try:
        scores = scorer(topic, texts)
        # l2-normalised by default, so a dot product between rows is their cosine
        vectors = TfidfVectorizer(stop_words="english").fit_transform(texts)
    except ValueError:
        return []

    order = sorted(range(len(pool)), key=lambda i: scores[i], reverse=True)

    selected: list[dict] = []
    picked_rows: list[int] = []
    per_url: dict[str, int] = {}

    for i in order:
        if len(selected) >= top_k or scores[i] <= 0:
            break
        url = pool[i]["url"]
        # cap per source so one verbose page cannot fill every slot
        if per_url.get(url, 0) >= per_source:
            continue
        if picked_rows and (vectors[i] @ vectors[picked_rows].T).max() > near_duplicate:
            continue

        pool[i]["score"] = float(scores[i])
        selected.append(pool[i])
        picked_rows.append(i)
        per_url[url] = per_url.get(url, 0) + 1

    return selected



# =====================================================



# Temp im keeping this func here
MAX_CHARS = 8000 # the NLP layer does the real trimming now, so keep more raw text
SEARCH_RESULTS = 6
def fetch_page(url: str) -> dict | None:
    """Scrape one URL. Returns {title, url, content}, or None if the page could not be read."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return None

    try:
        resp = httpx.get(
            url,
            timeout=15.0,
            follow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ResearchBot/1.0)"}, #this make feel like real user reading web. otherwise website blocks the page. 
        )
        resp.raise_for_status()
    except (httpx.HTTPStatusError, httpx.RequestError) as e:
        print(f"skipped {url} -> {type(e).__name__}")
        return None

    if "html" not in resp.headers.get("content-type", ""):
        print(f"skipped {url} -> not HTML")
        return None

    soup = BeautifulSoup(resp.text, "html.parser") #resp.text includes everything (tags and all)
    for tag in soup(["script", "style", "nav", "header", "footer", "aside", "noscript", "form"]):
        tag.decompose()

    text = "\n".join(line for line in soup.get_text("\n").splitlines() if line.strip()) # soup.get_text("\n") replace each tag new line
    title = soup.title.string.strip() if soup.title and soup.title.string else "Untitled"

    return {"title": title, "url": url, "content": text[:MAX_CHARS]}

