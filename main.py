import logging
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from pipeline import run_research_pipeline
load_dotenv()
logger = logging.getLogger(__name__)
app = FastAPI(title="Multi-Agent Research API")
CORS_ORIGIN = os.getenv("CORS_ORIGIN", "").split(",")
# browser blocks the frontend's requests without this
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGIN,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    topic: str


@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/api/research")
def research(req: ResearchRequest):
    try:
        return run_research_pipeline(req.topic)
    except Exception as exc:
        # without this the UI only sees a bare 500 for things like Gemini quota errors
        logger.exception("Research pipeline failed for topic %r", req.topic)
        raise HTTPException(status_code=502, detail=f"{type(exc).__name__}: {str(exc)[:300]}")
