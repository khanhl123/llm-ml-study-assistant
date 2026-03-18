from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="LLM ML Study Assistant API",
    description="Week 1 skeleton — placeholder responses only. RAG logic added in later weeks.",
    version="0.1.0",
)

PLACEHOLDER_ANSWER = (
    "This is a placeholder answer. "
    "Real retrieval and LLM generation will be added in Week 2 and beyond."
)

PLACEHOLDER_CITATIONS = [
    "Introduction to Machine Learning, Chapter 1, page 4",
    "Hands-On Machine Learning with Scikit-Learn, page 12",
]


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="The user's study question.")


class QueryResponse(BaseModel):
    question: str
    answer: str
    citations: List[str]


@app.get("/")
def read_root() -> dict:
    return {"message": "Welcome to the LLM ML Study Assistant API."}


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query_assistant(payload: QueryRequest) -> QueryResponse:
    return QueryResponse(
        question=payload.question,
        answer=PLACEHOLDER_ANSWER,
        citations=PLACEHOLDER_CITATIONS,
    )