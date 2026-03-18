# Project Scope

## Project Title

**Cited ML Study Assistant**

---

## 1. Project Summary

The Cited ML Study Assistant is a portfolio-focused LLM application designed to help users learn machine learning from trusted educational sources. The system will answer machine learning questions by retrieving relevant content from curated study materials and generating grounded responses with citations.

The project is intended to demonstrate practical LLM engineering skills beyond simple prompt-based chatbot behavior. It will include source curation, document ingestion, chunking, retrieval, grounded generation, citation rendering, evaluation, and deployment.

This project is both a learning exercise and a software engineering portfolio project. Its purpose is to deepen understanding of retrieval-augmented generation (RAG) systems while producing a usable end product that can be presented in GitHub, resumes, and interviews.

---

## 2. Problem Definition

Students and self-learners often study machine learning using multiple resources such as textbooks, lecture notes, course materials, and personal notes. This creates several challenges:

- Important concepts are spread across different sources
- Finding the most relevant explanation takes time
- Learners may struggle to judge which answer is trustworthy
- General-purpose chatbots may provide answers without citing evidence

This project addresses those problems by building an assistant that uses selected machine learning learning materials as the source of truth and provides answers with visible source citations.

---

## 3. Why This Project Matters

This project is valuable for two reasons.

### Educational value
It provides hands-on experience with the core building blocks of modern LLM applications, including:
- document ingestion
- text chunking
- embeddings
- vector retrieval
- grounded prompting
- citation handling
- evaluation of LLM output

### Portfolio value
It demonstrates the ability to build a real AI application with:
- clear problem framing
- structured system design
- real data handling
- measurable output quality
- documentation and deployment

The project is intentionally designed to be more credible than a generic chatbot clone.

---

## 4. Project Objectives

The main objectives of this project are:

- Build a working LLM-powered study assistant for machine learning
- Use trusted educational sources as the knowledge base
- Generate answers grounded in retrieved source material
- Show citations for transparency and trust
- Evaluate system quality instead of relying only on subjective impressions
- Produce a clean, portfolio-ready repository and demo

---

## 5. Target Users

This project is primarily designed for:

### Primary users
- Beginner machine learning students
- Self-learners studying from books and lecture notes
- Learners preparing for internships, technical interviews, or coursework

### Secondary users
- Anyone who wants a quick way to review core ML concepts from trusted sources
- Developers interested in studying how a RAG pipeline works in practice

---

## 6. User Needs

The project should help users do the following:

- Ask questions about machine learning concepts in plain language
- Receive concise and understandable answers
- See which source materials were used
- Trust that answers are grounded in the selected corpus
- Study faster without manually searching through multiple documents

---

## 7. Project Scope

### In scope
The first version of the project will include:

- A curated corpus of machine learning educational materials
- A document ingestion pipeline
- Text extraction and cleaning
- Chunking with metadata preservation
- Embedding generation
- Retrieval of relevant source chunks
- LLM-based answer generation using retrieved context only
- Citation display in the final answer
- A simple user interface
- A basic evaluation workflow

### Out of scope for the MVP
The following are intentionally excluded from the initial version:

- User authentication and account management
- Multi-user collaboration
- Voice input or speech output
- Mobile app support
- Multi-agent orchestration
- Highly polished UI/UX design
- Real-time document upload by users
- Large-scale production deployment
- Fine-tuning custom language models

These may be considered later, but they are not part of the first release.

---

## 8. Core Deliverables

By the end of the project, the expected deliverables are:

- A public GitHub repository
- A working frontend and backend
- A curated source corpus or documented source manifest
- A retrieval-based question-answering pipeline
- Citation-aware response formatting
- An evaluation dataset and basic quality analysis
- A professional README
- Screenshots or demo materials
- A deployed version if feasible

---

## 9. Functional Requirements

The system should be able to:

1. Accept a user question about machine learning
2. Search the source corpus for relevant content
3. Retrieve the most relevant chunks
4. Pass retrieved context into an LLM
5. Generate a concise grounded answer
6. Return citations showing which source material was used
7. Handle cases where the answer is not supported by the corpus

---

## 10. Non-Functional Requirements

The project should also aim for the following qualities:

- Clear project structure
- Readable and maintainable code
- Reproducible setup
- Transparent handling of sources
- Reasonable latency for small-scale use
- Basic testing for critical components
- Clear documentation for setup and usage

---

## 11. Example User Questions

The system should eventually support questions such as:

- What is the difference between classification and regression?
- What is overfitting?
- What is one-hot encoding?
- What is the bias-variance tradeoff?
- What is the purpose of a validation set?
- How does gradient descent work?
- What is regularization?

These questions help define the type of content and retrieval behavior the project must support.

---

## 12. Source Strategy

The assistant will use a curated set of machine learning study resources. These may include:

- textbooks
- lecture notes
- course handouts
- open educational resources
- selected personal study notes if appropriate

The initial corpus should stay small and manageable, ideally 3 to 5 high-quality sources.

Each source should be tracked with:
- title
- author
- document type
- source path or URL
- usage or license note
- reason for inclusion

This is important both for reproducibility and for safe public sharing on GitHub.

---

## 13. Technical Direction

The project is expected to use a retrieval-augmented generation architecture.

### Planned technical components
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Language:** Python
- **Document parsing:** PyMuPDF or pypdf
- **Embeddings:** API-based embeddings model
- **Vector search:** FAISS, Chroma, or pgvector
- **Data formats:** JSON, CSV, or lightweight database storage
- **Testing:** pytest
- **Version control:** Git + GitHub

The stack may evolve during implementation, but the architectural direction should remain stable.

---

## 14. Development Stages

### Stage 1 — Project Definition and Setup
Define the problem, users, scope, and success criteria. Create the repository, documentation, and basic project structure.

### Stage 2 — Source Collection
Choose the first set of machine learning sources, track provenance, and organize raw data.

### Stage 3 — Ingestion Pipeline
Extract text from source documents, clean it, preserve metadata, and prepare it for chunking.

### Stage 4 — Chunking and Retrieval Foundation
Split documents into chunks, generate embeddings, and build an initial retrieval system.

### Stage 5 — Grounded Answer Generation
Connect the LLM, generate answers only from retrieved context, and return citations.

### Stage 6 — Frontend Integration
Build the study assistant interface so users can enter questions and view answers with sources.

### Stage 7 — Evaluation and Improvement
Create a small evaluation set, test retrieval and answer quality, and improve weak areas.

### Stage 8 — Portfolio Polish and Deployment
Refine the project structure, improve documentation, add screenshots and diagrams, and deploy the project if possible.

---

## 15. Success Criteria

The project will be considered successful if it can:

- answer a set of predefined ML questions using selected sources
- retrieve relevant source chunks reliably
- generate answers grounded in those chunks
- show clear citations
- document its architecture and limitations
- present enough engineering depth to serve as a strong portfolio project

A successful version does not need to be perfect. It needs to be functional, explainable, measurable, and well-documented.

---

## 16. Risks and Constraints

Potential risks include:

- poor PDF extraction quality
- weak retrieval from bad chunking choices
- hallucinated answers when prompts are poorly constrained
- citation formatting issues
- unclear source licensing for public sharing
- spending too much time on UI instead of core retrieval quality

To manage these risks, the project should prioritize:
- a small high-quality corpus
- simple architecture first
- frequent manual testing
- early evaluation
- clear source tracking

---

## 17. Guiding Principles

During development, the project should follow these principles:

- Build the smallest useful version first
- Prioritize retrieval quality over UI polish
- Keep the corpus small before scaling up
- Treat citations as a required feature, not an extra
- Measure quality instead of assuming it
- Keep the repository clean and professional

---

## 18. Current Focus

**Current stage:** Week 1 — Project definition and setup

Current priorities:
- finalize scope
- create repository structure
- write core planning documents
- prepare for implementation in later weeks

---

## 19. Future Expansion Possibilities

After the MVP is complete, future versions could include:

- topic-based filtering
- reranking
- quiz and flashcard generation
- user-uploaded documents
- richer evaluation dashboards
- study-path recommendations
- support for comparing multiple sources

These are optional improvements and should not distract from the core MVP.

---

## 20. Final Scope Statement

This project will build a practical, citation-aware machine learning study assistant using a retrieval-augmented generation pipeline over curated educational resources. The MVP will focus on grounded answers, transparent citations, and measurable quality, with a simple interface and clean engineering structure suitable for portfolio use.
