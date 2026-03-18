from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="LLM ML Study Assistant API")


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="User question")


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
        answer="This is a placeholder answer. Week 2+ will add real LLM and RAG logic.",
        citations=["placeholder_source_1"],
    )

