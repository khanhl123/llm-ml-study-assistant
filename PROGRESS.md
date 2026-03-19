# Learning Journal

This is not just a progress tracker. This is a **learning journal** for the LLM ML Study Assistant project.

Each week documents what was built, but more importantly, it **teaches the concepts** behind the code through explanations, real code snippets from this project, self-check questions, and connections to the bigger picture.

**How to use this file:**
1. Complete the week's coding tasks first.
2. Read through that week's journal entry to solidify your understanding.
3. Try the "Test yourself" questions without looking at the answers.
4. Review the "Bigger picture" section to see how this week connects to the full RAG pipeline.

## Roadmap

```
Week 1          Week 2             Week 3          Week 4                Week 5
Project Setup -> Source Collection -> Ingestion -> Chunking + Retrieval -> LLM Generation
                                                                              |
                                                                              v
                                                   Week 8           Week 7           Week 6
                                                   Polish + Deploy <- Evaluation <- Frontend Integration
```

---

## Week 1 — Project Setup and Starter App

**Status:** Completed

### What was built

- Repository structure: `services/`, `apps/`, `src/`, `data/`, `tests/`
- Planning documents: `README.md`, `PROJECT_SCOPE.md`
- FastAPI backend with 3 endpoints (`services/api/main.py`)
- Streamlit frontend wired to the backend (`apps/streamlit_app/app.py`)
- Minimal dependency file (`requirements.txt`)
- Environment template (`.env.example`) with placeholder values only

---

### Concepts explained

#### 1. What is an API and why do LLM apps need one?

An API (Application Programming Interface) is how two programs talk to each other over a network. One program sends a **request**, the other sends back a **response**.

In this project, Streamlit (the frontend) sends requests to FastAPI (the backend). This is the exact same pattern that real LLM services use. When you call ChatGPT, your browser sends a POST request to OpenAI's API server and receives a JSON response. Our project works identically — just with a placeholder answer for now.

Why not put everything in one file? Because separation lets you **swap parts independently**. In Week 5, you will replace the placeholder logic with a real LLM call. The frontend will not need a single line of change because the response shape stays the same.

#### 2. HTTP methods: GET vs POST

HTTP defines several methods. This project uses two:

- **GET** — ask the server for information. No data sent in the body.
- **POST** — send data to the server for processing.

From `services/api/main.py`:

```python
@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}
```

This is a GET endpoint. The client simply asks "are you alive?" and receives `{"status": "ok"}`. No data needs to be sent.

```python
@app.post("/query", response_model=QueryResponse)
def query_assistant(payload: QueryRequest) -> QueryResponse:
    ...
```

This is a POST endpoint. The client sends a question (data) and the server processes it and returns an answer. Every LLM API in production uses POST for this reason — you are always **sending a prompt** to the server.

#### 3. FastAPI basics

FastAPI is a Python web framework for building APIs. You create an app, then register endpoints using decorators.

```python
app = FastAPI(
    title="LLM ML Study Assistant API",
    description="Week 1 skeleton — placeholder responses only.",
    version="0.1.0",
)
```

The `title`, `description`, and `version` fields are metadata. FastAPI uses them to auto-generate a **Swagger UI** at `http://localhost:8000/docs`. This is a free, interactive page where you can test every endpoint directly in the browser — no frontend needed.

The decorator `@app.get("/health")` tells FastAPI: "when someone sends a GET request to `/health`, run this function and return its output as JSON." FastAPI handles all the HTTP parsing, serialization, and error responses automatically.

#### 4. Data validation with Pydantic

Pydantic enforces that incoming data matches a defined schema **before** your code runs.

```python
class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="The user's study question.")
```

This says: the request body must be JSON with a `question` field that is a non-empty string. If the client sends `{"question": ""}` or `{}` or `{"wrong_field": 123}`, FastAPI returns a **422 Unprocessable Entity** error automatically. Your function `query_assistant()` never executes.

Why this matters for LLM apps: every API call to OpenAI or similar services **costs money**. Validation prevents wasted calls from bad input. It also protects against injection or malformed prompts reaching your LLM.

```python
class QueryResponse(BaseModel):
    question: str
    answer: str
    citations: List[str]
```

This defines the output contract. FastAPI checks that your function returns data matching this shape. If you accidentally forget to include `citations`, FastAPI will catch it.

#### 5. Response shape design for RAG apps

The response shape you choose determines what information your frontend can display:

```json
{
  "question": "What is overfitting?",
  "answer": "This is a placeholder answer...",
  "citations": [
    "Introduction to Machine Learning, Chapter 1, page 4",
    "Hands-On Machine Learning with Scikit-Learn, page 12"
  ]
}
```

Three fields, each with a purpose:
- `question` — echo back what was asked (useful for logging and display)
- `answer` — the generated response (placeholder now, LLM-generated in Week 5)
- `citations` — the sources used (placeholder now, retrieved documents in Week 4-5)

This is the **contract** between your backend and frontend. The frontend trusts this shape. When you replace the placeholder with real RAG logic later, the frontend code will not need to change at all — as long as you keep returning the same three fields.

A regular chatbot might only return `answer`. A RAG app **always** needs `citations` because grounded answers with sources are its core value.

#### 6. Client-server architecture

This project runs as two separate processes:

```
Terminal 1: uvicorn services.api.main:app --port 8000   (backend)
Terminal 2: streamlit run apps/streamlit_app/app.py      (frontend on port 8501)
```

The frontend does not know or care what happens inside the backend. It only knows:
- Send POST to `http://localhost:8000/query` with `{"question": "..."}`.
- Expect JSON back with `question`, `answer`, `citations`.

This means you can completely rewrite the backend — switch from placeholder to OpenAI to a local LLM — and the frontend works unchanged. This is the principle of **separation of concerns**.

#### 7. Streamlit basics

Streamlit is a Python library that turns a script into a web app. There is no HTML, CSS, or JavaScript. You write Python top to bottom, and Streamlit renders each call as a UI element.

From `apps/streamlit_app/app.py`:

```python
st.set_page_config(page_title="LLM ML Study Assistant", page_icon="📚")
st.title("LLM ML Study Assistant")
st.caption("A cited ML study assistant — ...")
st.divider()

question = st.text_input("Your question", placeholder="e.g. What is the bias-variance tradeoff?")
submit_clicked = st.button("Submit", type="primary")
```

Each `st.*` call creates a UI element in order:
- `st.title()` — large heading
- `st.caption()` — small gray description
- `st.divider()` — horizontal line
- `st.text_input()` — text box that returns whatever the user typed
- `st.button()` — button that returns `True` when clicked

Streamlit re-runs the **entire script** from top to bottom every time the user interacts with any widget. This is its execution model — simple but important to understand.

#### 8. Calling an API from the frontend

The frontend uses the `requests` library to call the backend:

```python
response = requests.post(
    f"{API_BASE_URL}/query",
    json={"question": question},
    timeout=10,
)
response.raise_for_status()
data = response.json()
```

Step by step:
1. `requests.post(...)` — sends a POST request with JSON body to `http://localhost:8000/query`
2. `timeout=10` — if the server does not respond within 10 seconds, raise an exception
3. `response.raise_for_status()` — if the server returned an error status (4xx, 5xx), raise an exception
4. `response.json()` — parse the response body as a Python dictionary

This is identical to how you would call the OpenAI API, except the URL and payload format differ.

#### 9. Error handling for network calls

Network calls fail. Servers go down, connections time out, APIs return errors. If you don't handle these, your app crashes and the user sees a stack trace.

```python
except requests.exceptions.ConnectionError:
    st.error("Could not connect to the backend. ...")
except requests.exceptions.HTTPError as e:
    st.error(f"Backend returned an error: {e}")
except requests.exceptions.RequestException as e:
    st.error(f"Unexpected error: {e}")
```

Three layers of specificity:
- `ConnectionError` — the server is not running at all (most common during development)
- `HTTPError` — the server responded but with an error code (e.g. 422 for bad input)
- `RequestException` — catch-all for anything else unexpected

In production LLM apps, you would add **retry logic** (try again 2-3 times before giving up) and **fallback responses** ("Sorry, the service is temporarily unavailable"). Those come in later weeks.

#### 10. Dependency management

`requirements.txt` lists every Python package your project needs:

```
fastapi
uvicorn
pydantic
streamlit
requests
```

Each has a specific role:
- **fastapi** — the web framework that handles HTTP routing and request parsing
- **uvicorn** — the ASGI server that actually runs the FastAPI app and listens on a port
- **pydantic** — data validation library (used by FastAPI for request/response models)
- **streamlit** — the frontend framework that turns Python into a web UI
- **requests** — HTTP client library used by Streamlit to call the backend

Only packages that your code directly imports should be listed. Transitive dependencies (packages that your packages depend on) are installed automatically.

---

### Test yourself

1. What HTTP method would you use to send a user's question to an LLM API: GET or POST? Why?
2. If you send `{"question": ""}` to the `/query` endpoint, what happens? What status code is returned?
3. Why does the response include a `citations` field even though we don't have real sources yet?
4. If you change the backend from a placeholder to a real OpenAI call, does the Streamlit frontend need to change? Why or why not?
5. What is the difference between `ConnectionError` and `HTTPError` in the context of calling an API?

---

### Connection to the bigger picture

The response shape (`question`, `answer`, `citations`) defined this week is the **exact contract** that real RAG responses will follow starting in Week 5. The only thing that will change is what happens **inside** `query_assistant()` — the function signature, the request model, the response model, and the entire frontend stay the same.

This is the principle of **designing for extensibility**: define the interface first, fill in the implementation later. Every professional software project works this way.

### Further reading

- [FastAPI official tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic documentation](https://docs.pydantic.dev/latest/)
- [Streamlit get started](https://docs.streamlit.io/get-started)
- [HTTP request methods (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

---

## Week 2 — Source Collection

**Status:** Not started

---