# llm-ml-study-assistant
LLM-powered ML study assistant with retrieval, grounded answers, and citations from trusted sources. (self-project)

# Cited ML Study Assistant

A portfolio-ready LLM application that answers machine learning questions using trusted educational resources and provides grounded answers with citations.

---

## Overview

Learning machine learning often requires switching between textbooks, lecture notes, papers, and personal notes. This project aims to reduce that friction by building an AI study assistant that can retrieve relevant content from selected ML sources, generate a concise answer, and cite the material used.

The long-term goal is to build a reliable retrieval-augmented generation (RAG) system that is not only useful for studying, but also demonstrates practical LLM engineering skills such as data ingestion, chunking, embeddings, retrieval, answer generation, citation handling, evaluation, and deployment.

---

## Problem Statement

Students and self-learners often face three common problems when studying machine learning:

1. Important concepts are spread across multiple sources.
2. It takes time to find a trustworthy explanation.
3. Standard chatbots may answer without showing where the information came from.

This project addresses those problems by building an assistant that answers questions from curated machine learning materials and shows source citations for transparency and trust.

---

## Project Goals

The main goals of this project are:

- Build a real LLM-powered application, not just a prompt demo
- Use trusted machine learning study materials as the source of truth
- Generate answers grounded in retrieved context
- Display citations for every answer
- Evaluate answer quality and retrieval quality
- Deploy the project as a portfolio-ready application

---

## Target Users

This project is designed for:

- Beginner machine learning students
- Self-learners studying from textbooks and lecture notes
- Learners preparing for interviews or internships
- Anyone who wants faster access to grounded ML explanations

---

## Core Features

### Planned MVP
The minimum viable product will include:

- Question input interface
- Document ingestion pipeline for selected ML sources
- Text chunking and metadata storage
- Embedding generation and vector search
- Retrieval of relevant source passages
- LLM-generated answers based only on retrieved context
- Citation display for source transparency
- Basic evaluation pipeline for testing answer quality

### Planned Later Improvements
Future versions may include:

- Source filtering by book/course/topic
- Multi-document comparison
- Flashcard or quiz generation
- Study-plan generation
- Uploading new documents directly through the UI
- Improved retrieval with reranking
- Better evaluation dashboards

---

## Non-Goals

To keep the project focused, the following are not part of the initial MVP:

- Multi-agent workflows
- Voice interface
- Authentication system
- Complex UI design
- Mobile app support
- Social or collaborative features

---

## Example Questions

The assistant should eventually support questions such as:

- What is the difference between classification and regression?
- What is overfitting?
- Why do we use one-hot encoding?
- What is the bias-variance tradeoff?
- How does gradient descent work?
- What is the role of a validation set?

---

## Project Architecture

The project is planned as a retrieval-augmented generation pipeline:

1. **Source Collection**  
   Curate trusted machine learning learning materials.

2. **Ingestion**  
   Extract text from source documents and preserve metadata such as source title and page number.

3. **Chunking**  
   Split documents into smaller searchable units.

4. **Embeddings and Indexing**  
   Convert chunks into vector representations and store them in a vector database.

5. **Retrieval**  
   Given a user question, retrieve the most relevant chunks.

6. **Generation**  
   Pass retrieved chunks to an LLM and generate a grounded answer.

7. **Citation Rendering**  
   Show the sources used in the answer.

8. **Evaluation**  
   Measure retrieval quality, groundedness, and answer correctness.

---

## Planned Tech Stack

The current planned stack is:

- **Language:** Python
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Document Parsing:** PyMuPDF / pypdf
- **LLM Integration:** OpenAI API
- **Vector Storage:** FAISS / Chroma / pgvector
- **Data Handling:** pandas, JSON
- **Testing:** pytest
- **Deployment:** To be decided during later stages

This stack may evolve as the project matures.

---

## Repository Structure

```bash
cited-ml-study-assistant/
│── README.md
│── PROJECT_SCOPE.md
│── .env.example
│── apps/
│   └── streamlit_app/
│       └── app.py
│── services/
│   └── api/
│       └── main.py
│── src/
│   ├── ingestion/
│   ├── retrieval/
│   ├── generation/
│   ├── evals/
│   └── utils/
│── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│── tests/
