# Project Progress

This file tracks what was completed each week and what skills or concepts can be learned from that week's work.
It is updated at the end of each development stage.

---

## Week 1 — Project Setup and Starter App

**Status:** Completed

### What was done

- Created the repository structure (`services/`, `apps/`, `src/`, `data/`, `tests/`)
- Wrote `README.md` with project overview, goals, tech stack, and architecture
- Wrote `PROJECT_SCOPE.md` with full scope definition (20 sections)
- Built a minimal FastAPI backend (`services/api/main.py`) with three endpoints:
  - `GET /` — welcome message
  - `GET /health` — health check
  - `POST /query` — accepts a question, returns placeholder answer and citations
- Built a minimal Streamlit frontend (`apps/streamlit_app/app.py`) that:
  - shows a title and description
  - accepts a user question via text input
  - calls the backend `/query` endpoint
  - displays the answer and citations
  - handles connection errors gracefully
- Created `requirements.txt` with five dependencies: fastapi, uvicorn, pydantic, streamlit, requests
- Created `.env.example` with placeholder values (no real keys)
- Committed all work to git

### Skills and concepts to learn from this week

#### 1. API fundamentals
- What an API is and why LLM applications need one
- HTTP methods: `GET` (read data) vs `POST` (send data)
- How a client (Streamlit) sends a request and a server (FastAPI) returns a response
- JSON as the standard data format between frontend and backend

#### 2. FastAPI basics
- Creating a FastAPI app with metadata (`title`, `description`, `version`)
- Defining route handlers with `@app.get()` and `@app.post()`
- Using `response_model` to enforce output shape
- Auto-generated Swagger UI at `/docs`

#### 3. Data validation with Pydantic
- Defining request and response schemas with `BaseModel`
- Using `Field(...)` for required fields and constraints like `min_length`
- How FastAPI automatically rejects invalid input (422 error) before the handler runs
- Why input validation matters for LLM apps (bad input = wasted API calls)

#### 4. Designing response shape for LLM apps
- Structuring output as `question`, `answer`, `citations`
- Why RAG apps always need a citations field
- Defining the contract between frontend and backend early
- Making the shape extensible for future fields like `confidence_score`

#### 5. Client-server architecture
- Why frontend and backend are separate processes
- Frontend only handles display; backend handles logic
- Changing the backend (e.g. swapping LLM provider) does not require frontend changes
- Running two services locally on different ports (8000 and 8501)

#### 6. Streamlit basics
- Page config with `st.set_page_config()`
- Layout components: `st.title()`, `st.caption()`, `st.divider()`, `st.text_input()`, `st.button()`
- Calling an external API with `requests.post()` from within Streamlit
- Displaying dynamic results: `st.subheader()`, `st.write()`, `st.markdown()`
- Showing a spinner with `st.spinner()` during a network call

#### 7. Error handling
- Why network calls can fail: server down, timeout, bad response
- Catching specific exceptions: `ConnectionError`, `HTTPError`, general `RequestException`
- Showing user-friendly error messages instead of crashing
- Setting a timeout on API calls (`timeout=10`)

#### 8. Dependency management
- What `requirements.txt` is and why every Python project needs one
- Only listing packages that are actually used in the code
- Understanding each dependency's role: fastapi (framework), uvicorn (server), pydantic (validation), streamlit (UI), requests (HTTP client)

#### 9. Project structure and Git hygiene
- Organizing code into clear folders: `services/`, `apps/`, `src/`, `data/`, `tests/`
- Using `.gitkeep` to track empty directories in git
- Writing commit messages with a summary line and descriptive bullet points
- Keeping `.env.example` with placeholder values, never committing real secrets

#### 10. Thinking ahead — why this skeleton matters
- The placeholder response has the exact same shape that real RAG responses will have
- Week 2+ only needs to replace the inside of `query_assistant()` — everything else stays
- This is called designing for extensibility: build the contract first, fill in the logic later

---

## Week 2 — (upcoming)

**Status:** Not started

---