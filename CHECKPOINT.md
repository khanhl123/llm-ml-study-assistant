# CHECKPOINT — AI Project State

> **For the AI chatbot.** This file is the single source of truth for project progress.
> Read this file at the start of every session.

---

## AI Instructions

1. Read this file first when the user opens the project.
2. Identify the current stage — the first stage that is NOT marked `[COMPLETED]`.
3. Summarize to the user: what was done last time, and what is next.
4. Plan today's tasks from that stage's unchecked items.
5. Work through the tasks one by one with the user.
6. After completing each task, run the verification commands listed for that task.
7. If verification passes, mark the task `[x]` in this file.
8. When ALL tasks and verifications in a stage pass, change the stage status to `[COMPLETED]`.
9. After completing a stage, update `PROGRESS.md` with a learning journal entry for that stage (concepts explained, code snippets, test-yourself questions, further reading).
10. Append a one-line entry to the Session Log at the bottom of this file.
11. If a session ends mid-stage, note in the Session Log which tasks are done and which remain.

---

## Project Overview

| Field          | Value                                                                                  |
| -------------- | -------------------------------------------------------------------------------------- |
| **Repo**       | `llm-ml-study-assistant`                                                               |
| **Goal**       | An LLM-powered ML study assistant that answers questions with citations from sources    |
| **Stack**      | Python, FastAPI, Streamlit, OpenAI API, FAISS/Chroma, Pydantic, pytest                 |
| **Pattern**    | Retrieval-Augmented Generation (RAG) — retrieve relevant docs, then generate an answer  |
| **Stages**     | 8 incremental stages from skeleton to deployed portfolio project                        |
| **Key files**  | `CHECKPOINT.md` (this file), `PROGRESS.md` (learning journal), `PROJECT_SCOPE.md` (scope) |

---

## How this file works

Each stage below has four sections:

- **Goal** — what this stage achieves and why it matters in the RAG pipeline
- **Tasks** — concrete checklist items with file paths and descriptions
- **Verification** — specific commands or checks to confirm the task is done correctly
- **Ghi chu** — notes in Vietnamese for additional context

When a task is done: `- [ ]` becomes `- [x]`.
When all tasks and verifications pass: `[NOT STARTED]` or `[IN PROGRESS]` becomes `[COMPLETED]`.

---

## Stage 1 — Project Setup [COMPLETED]

**Goal:** Tao ra bo khung (skeleton) co ban cho du an. Backend va frontend chay duoc, giao tiep voi nhau qua API, tra ve placeholder response. Chua co LLM hay vector search — chi la co cau truc va pipeline hoat dong end-to-end.

**Key files created/modified:**
- `services/api/main.py` — FastAPI backend
- `apps/streamlit_app/app.py` — Streamlit frontend
- `requirements.txt` — dependencies
- `.env.example` — environment template
- `README.md` — project overview
- `PROJECT_SCOPE.md` — full scope definition

**Tasks:**
- [x] Tao cau truc repo: `services/`, `apps/`, `src/`, `data/`, `tests/`
- [x] Viet `README.md` voi project overview, goals, tech stack, architecture
- [x] Viet `PROJECT_SCOPE.md` voi 20 sections dinh nghia pham vi du an
- [x] Xay dung FastAPI backend voi 3 endpoints:
  - `GET /` — welcome message
  - `GET /health` — health check tra ve `{"status": "ok"}`
  - `POST /query` — nhan question, tra ve placeholder answer + citations
- [x] Xay dung Streamlit frontend:
  - Hien thi title va mo ta
  - Text input cho cau hoi
  - Nut Submit goi `POST /query` den backend
  - Hien thi answer va citations tu response
  - Xu ly loi ket noi (ConnectionError, HTTPError, RequestException)
- [x] Tao `requirements.txt` voi 5 dependencies: fastapi, uvicorn, pydantic, streamlit, requests
- [x] Tao `.env.example` voi placeholder values (OPENAI_API_KEY=your_api_key_here)

**Verification:**
- [x] Chay `uvicorn services.api.main:app --port 8000` — server khoi dong khong loi
- [x] Truy cap `http://localhost:8000/health` — tra ve `{"status": "ok"}`
- [x] Gui POST request den `http://localhost:8000/query` voi `{"question": "test"}` — tra ve JSON co `question`, `answer`, `citations`
- [x] Chay `streamlit run apps/streamlit_app/app.py` — UI hien thi, nhap cau hoi, nhan answer tu backend

Ghi chu: Week 1 hoan tat. Placeholder responses only. Response shape (question, answer, citations) la contract se giu nguyen xuyen suot du an — chi thay doi logic ben trong.

---

## Stage 2 — Source Collection [NOT STARTED]

**Goal:** Chon va to chuc tai lieu ML se lam "knowledge base" cho assistant. Day la buoc nen tang — chat luong tai lieu quyet dinh chat luong cua toan bo he thong. Neu tai lieu khong tot, retrieval se khong chinh xac, va answer se khong dang tin.

**Why this matters for RAG:** RAG = Retrieval-Augmented Generation. "Retrieval" can co data de retrieve. Khong co data = khong co gi de tra loi. Stage nay tao ra corpus (kho tai lieu) de cac stage sau su dung.

**Key files created/modified:**
- `data/source_manifest.json` — danh sach tai lieu voi metadata
- `data/raw/` — chua cac file tai lieu goc (PDF, txt, etc.)
- `data/README.md` — huong dan ve data folder

**Tasks:**
- [ ] Nghien cuu va chon 3-5 tai lieu ML chat luong cao, uu tien:
  - Textbook open-access (vd: "Mathematics for Machine Learning", "An Introduction to Statistical Learning")
  - Lecture notes tu cac khoa hoc uy tin
  - Tai lieu co license cho phep su dung (Creative Commons, MIT, etc.)
- [ ] Tao file `data/source_manifest.json` voi format:
  ```json
  [
    {
      "id": "source_01",
      "title": "Ten tai lieu",
      "author": "Ten tac gia",
      "type": "textbook | lecture_notes | paper",
      "format": "pdf | txt | md",
      "license": "CC BY 4.0 | MIT | Fair Use",
      "url": "link download hoac trang chinh thuc",
      "filename": "ten_file_trong_data_raw",
      "notes": "Ly do chon tai lieu nay"
    }
  ]
  ```
- [ ] Download hoac copy tung tai lieu vao `data/raw/`, dat ten file theo quy tac ro rang (vd: `intro_to_statistical_learning.pdf`)
- [ ] Kiem tra license cua tung tai lieu — ghi ro vao manifest. Neu khong chac, ghi "Fair Use — educational purpose only" va khong commit file goc len GitHub
- [ ] Cap nhat `data/README.md`:
  - Giai thich cau truc `raw/` va `processed/`
  - Ghi chu rang raw files co the khong duoc commit (vi license)
  - Huong dan cach tai lai data neu can

**Verification:**
- [ ] File `data/source_manifest.json` ton tai, la valid JSON, co it nhat 3 entries
- [ ] Moi entry trong manifest co day du cac fields: id, title, author, type, format, license, filename
- [ ] Thu muc `data/raw/` co it nhat 3 files tuong ung voi manifest
- [ ] `data/README.md` co noi dung mo ta ro rang cau truc va cach su dung

Ghi chu: Bat dau voi 2-3 tai lieu ngan (50-100 trang) de test pipeline truoc. Mo rong sau khi pipeline chay on dinh. Uu tien tai lieu ma ban dang thuc su hoc — vua lam project vua on bai.

---

## Stage 3 — Ingestion Pipeline [NOT STARTED]

**Goal:** Doc va extract text tu cac tai lieu trong `data/raw/`, giu nguyen metadata (source, page, author), lam sach text, va luu ket qua vao `data/processed/`. Day la buoc "bien tai lieu thanh data ma may tinh doc duoc".

**Why this matters for RAG:** LLM khong doc duoc PDF truc tiep. Can phai chuyen PDF thanh text truoc, giu metadata de sau nay biet doan text nay tu dau ra (citation). Neu extract sai hoac mat metadata, citation se sai.

**Key files created/modified:**
- `src/ingestion/__init__.py` — module init
- `src/ingestion/extract.py` — script doc PDF, extract text + metadata
- `src/ingestion/clean.py` — script lam sach text
- `data/processed/*.json` — output da xu ly
- `tests/test_ingestion.py` — tests cho ingestion
- `requirements.txt` — them PyMuPDF hoac pypdf

**Tasks:**
- [ ] Cai dat thu vien doc PDF: them `pymupdf` (hoac `pypdf`) vao `requirements.txt`, chay `pip install -r requirements.txt`
- [ ] Tao file `src/ingestion/__init__.py` (co the de trong)
- [ ] Viet `src/ingestion/extract.py`:
  - Function nhan duong dan PDF, tra ve list cac pages
  - Moi page la dict co: `text`, `page_number`, `source_title`, `source_author`
  - Doc metadata tu `data/source_manifest.json` de biet source info
- [ ] Viet `src/ingestion/clean.py`:
  - Function nhan raw text, tra ve clean text
  - Xoa header/footer lap lai, fix encoding errors, loai bo ky tu dac biet
  - Giu nguyen noi dung chinh, khong cat thong tin quan trong
- [ ] Chay ingestion tren toan bo files trong `data/raw/`, luu output vao `data/processed/`:
  - Moi file output la JSON, format:
    ```json
    {
      "source_id": "source_01",
      "source_title": "Ten tai lieu",
      "pages": [
        {"page_number": 1, "text": "Noi dung da lam sach..."},
        {"page_number": 2, "text": "..."}
      ]
    }
    ```
- [ ] Viet `tests/test_ingestion.py`:
  - Test extract function tra ve dung so trang
  - Test clean function loai bo duoc header/footer
  - Test output JSON co day du cac fields bat buoc

**Verification:**
- [ ] Chay `python -m src.ingestion.extract` tren 1 file PDF — khong loi, tra ve text
- [ ] Kiem tra output trong `data/processed/` — moi file JSON co du fields: `source_id`, `source_title`, `pages`
- [ ] Moi page co `page_number` va `text` khong rong
- [ ] Text sach: khong co ky tu la (`\x00`, `\ufffd`), khong co header/footer lap lai
- [ ] Chay `pytest tests/test_ingestion.py` — tat ca tests pass

Ghi chu: Bat dau voi 1 file PDF de debug truoc. PDF extraction thuong gap nhieu loi (bang bi vo, hinh bi bo qua, encoding sai). Kiem tra output bang mat truoc khi chay tren nhieu file.

---

## Stage 4 — Chunking and Retrieval Foundation [NOT STARTED]

**Goal:** Chia text da extract thanh cac doan nho (chunks), tao embeddings (vector representation), luu vao vector database, va xay dung function retrieval de tim chunks lien quan nhat voi cau hoi cua user.

**Why this matters for RAG:** LLM co gioi han context window (so luong text co the xu ly 1 luc). Khong the dua ca cuon sach vao prompt. Can phai tim dung doan lien quan (retrieval) va chi dua doan do vao. Chat luong retrieval quyet dinh chat luong answer — neu retrieve sai doan, LLM se tra loi sai.

**Key files created/modified:**
- `src/retrieval/__init__.py` — module init
- `src/retrieval/chunker.py` — logic chia text thanh chunks
- `src/retrieval/embeddings.py` — tao vector embeddings
- `src/retrieval/search.py` — tim kiem chunks lien quan
- `tests/test_retrieval.py` — tests
- `requirements.txt` — them faiss-cpu/chromadb, openai (cho embeddings)

**Tasks:**
- [ ] Tao file `src/retrieval/__init__.py`
- [ ] Viet `src/retrieval/chunker.py`:
  - Function nhan text + metadata, tra ve list chunks
  - Moi chunk co: `text`, `source_id`, `source_title`, `page_number`, `chunk_id`
  - Chon kich thuoc chunk (bat dau voi ~500 tokens, overlap ~100 tokens)
  - Giu metadata nguyen ven cho moi chunk
- [ ] Viet `src/retrieval/embeddings.py`:
  - Function nhan list chunks, tra ve list embeddings (vectors)
  - Su dung OpenAI Embeddings API (`text-embedding-ada-002` hoac `text-embedding-3-small`)
  - Hoac dung sentence-transformers (chay local, mien phi)
- [ ] Viet `src/retrieval/search.py`:
  - Tao FAISS index hoac Chroma collection tu embeddings
  - Function `retrieve(question, top_k=5)` — nhan cau hoi, tra ve top-k chunks lien quan nhat
  - Luu va load vector store tu disk (de khong can rebuild moi lan)
- [ ] Them dependencies vao `requirements.txt`: `faiss-cpu` (hoac `chromadb`), `openai`
- [ ] Chay full pipeline: processed JSON -> chunks -> embeddings -> vector store -> retrieval
- [ ] Viet `tests/test_retrieval.py`:
  - Test chunker tao ra chunks co do dai hop ly
  - Test retrieval tra ve ket qua khi hoi cau hoi don gian

**Verification:**
- [ ] Chunking: moi chunk co `text` dai ~500 tokens, co day du metadata
- [ ] Embeddings: moi chunk co 1 vector tuong ung (kiem tra dimension)
- [ ] Retrieval: hoi "What is overfitting?" — top-5 chunks co lien quan den overfitting
- [ ] Vector store: luu xuong disk, load lai duoc, va retrieval van hoat dong
- [ ] Chay `pytest tests/test_retrieval.py` — tat ca tests pass

Ghi chu: Day la stage kho nhat va quan trong nhat. Debug nhieu, thu nhieu cach chunk, so sanh ket qua. Neu retrieval tra ve sai doan, thi LLM se tra loi sai — "garbage in, garbage out".

---

## Stage 5 — Grounded Answer Generation [NOT STARTED]

**Goal:** Ket noi OpenAI API, truyen retrieved chunks vao prompt, va generate answer chi dua tren context da retrieve. Day la buoc "RAG" that su — ket hop Retrieval (Stage 4) voi Generation (Stage 5).

**Why this matters for RAG:** Khac voi chatbot thuong (tra loi tu training data), RAG app chi tra loi tu tai lieu da cung cap. Dieu nay giup: (1) giam hallucination, (2) co the trich dan nguon, (3) user tin tuong hon vi biet answer tu dau ra.

**Key files created/modified:**
- `src/generation/__init__.py` — module init
- `src/generation/prompt.py` — prompt template
- `src/generation/generate.py` — goi OpenAI API va tao answer
- `services/api/main.py` — thay placeholder bang real RAG logic
- `.env` — them OPENAI_API_KEY that (khong commit)
- `requirements.txt` — them `openai` (neu chua co tu Stage 4)

**Tasks:**
- [ ] Them `openai` vao `requirements.txt` (neu chua co)
- [ ] Tao `src/generation/__init__.py`
- [ ] Viet `src/generation/prompt.py`:
  - Tao system prompt: "Ban la ML study assistant. Chi tra loi dua tren context duoc cung cap. Neu khong du thong tin, noi ro la khong biet."
  - Tao function build prompt: nhan question + retrieved chunks, tra ve messages list cho OpenAI API
  - Format context ro rang: moi chunk co ghi source va page
- [ ] Viet `src/generation/generate.py`:
  - Function nhan question, goi retrieval (Stage 4), build prompt, goi OpenAI Chat Completions API
  - Tra ve dict co: `answer`, `citations` (list source + page tu chunks da dung)
  - Xu ly truong hop khong tim duoc context: tra ve "Khong du thong tin tu tai lieu hien co de tra loi cau hoi nay."
  - Doc API key tu bien moi truong (`os.getenv("OPENAI_API_KEY")`)
- [ ] Cap nhat `services/api/main.py`:
  - Import generate function
  - Thay the `PLACEHOLDER_ANSWER` va `PLACEHOLDER_CITATIONS` bang real RAG call
  - Giu nguyen response shape (question, answer, citations) — frontend khong can thay doi
- [ ] Tao file `.env` (local only, da co trong `.gitignore`) voi API key that
- [ ] Test thu: hoi 3-5 cau hoi ML va kiem tra answer + citations

**Verification:**
- [ ] `POST /query` voi `{"question": "What is overfitting?"}` — tra ve answer dua tren content tu tai lieu, khong phai placeholder
- [ ] Citations tro dung: "Introduction to Statistical Learning, page 32" — kiem tra thu cong rang noi dung dung o trang do
- [ ] Hoi cau hoi ngoai pham vi (vd: "What is the weather today?") — tra ve "khong du thong tin"
- [ ] API key khong xuat hien trong bat ky file nao duoc commit (kiem tra `git diff`)
- [ ] Streamlit hien thi answer that tu LLM voi citations

Ghi chu: Day la luc project "song" that su. Tu placeholder thanh real answer. Chu y: moi query ton tien API (khoang $0.01-0.05). Test it, test dung, khong spam.

---

## Stage 6 — Frontend Integration [NOT STARTED]

**Goal:** Cap nhat Streamlit UI de hien thi real answers mot cach ro rang, dep mat. Format citations chinh xac, them loading states, va dam bao end-to-end flow hoat dong muot ma.

**Why this matters:** Du backend tra ve answer dung, neu frontend hien thi xau hoac khong ro, user se khong tin tuong. Citations can hien thi dung format de user co the tra nguon. Day cung la phan "nhìn thấy được" khi demo portfolio.

**Key files created/modified:**
- `apps/streamlit_app/app.py` — cap nhat UI

**Tasks:**
- [ ] Cap nhat Streamlit UI hien thi real answers tu LLM:
  - Answer hien thi trong khung ro rang (dung `st.info()` hoac `st.container()`)
  - Phan biet placeholder vs real answer (neu can)
- [ ] Format citations chi tiet:
  - Hien thi: "[1] Ten sach, Trang X"
  - Neu co nhieu citations, danh so thu tu
- [ ] Them UX improvements:
  - `st.spinner("Dang tim kiem va tao cau tra loi...")` — co message cu the
  - Hien thi thoi gian xu ly (optional)
  - Hien thi thong bao khi khong tim duoc context: "Khong du thong tin de tra loi cau hoi nay."
- [ ] Test end-to-end flow:
  - Nhap cau hoi ML -> nhan answer co citations -> citations dung format
  - Nhap cau hoi ngoai pham vi -> nhan thong bao "khong du thong tin"
  - Tat backend -> Streamlit hien thi loi ket noi (khong crash)

**Verification:**
- [ ] Nhap "What is the bias-variance tradeoff?" — nhan answer co citations dang "[1] Source, page X"
- [ ] Nhap "What is the weather?" — nhan thong bao khong du thong tin
- [ ] Tat uvicorn, bam Submit — hien thi error message, UI khong crash
- [ ] Toan bo flow tu nhap cau hoi den hien thi answer mat duoi 30 giay

Ghi chu: Giu UI don gian nhung chuyen nghiep. Khong can nhieu mau sac hay animation. Can: ro rang, dung, va nhanh. Day la phan se duoc screenshot cho portfolio.

---

## Stage 7 — Evaluation and Improvement [NOT STARTED]

**Goal:** Tao bo cau hoi test, do luong chat luong retrieval va answer, tim diem yeu, va cai thien. Day la buoc chung minh rang project khong chi "chay duoc" ma con "chay dung".

**Why this matters for portfolio:** Bat ky ai cung co the lam 1 cai chatbot chay duoc. Nhung do luong chat luong va cai thien — do la dieu nha tuyen dung muon thay. No cho thay ban hieu he thong, biet do luong, va biet cai thien.

**Key files created/modified:**
- `src/evals/__init__.py` — module init
- `src/evals/dataset.py` — evaluation dataset
- `src/evals/evaluate.py` — evaluation script
- `src/evals/results/` — luu ket qua evaluation
- `tests/test_evals.py` — tests cho eval scripts

**Tasks:**
- [ ] Tao `src/evals/__init__.py`
- [ ] Tao evaluation dataset (`src/evals/dataset.py` hoac `src/evals/eval_questions.json`):
  - 10-20 cap (question, expected_answer_keywords, expected_source)
  - Vi du: `{"question": "What is overfitting?", "expected_keywords": ["training", "generalization", "error"], "expected_source": "source_01"}`
  - Chon cau hoi tu de den kho, bao phu nhieu chu de
- [ ] Viet `src/evals/evaluate.py`:
  - Chay tung cau hoi qua pipeline (retrieve -> generate)
  - Do **retrieval quality**: retrieved chunks co chua thong tin lien quan khong? (precision@k)
  - Do **answer groundedness**: answer co dua tren context khong? Hay hallucinate?
  - Do **answer correctness**: answer co chua expected keywords khong?
  - Luu ket qua vao `src/evals/results/` (JSON format voi timestamp)
- [ ] Phan tich ket qua, xac dinh diem yeu:
  - Retrieval sai: co the chunk size khong phu hop, hoac embeddings khong tot
  - Answer sai: co the prompt chua du ro rang, hoac context khong du
- [ ] Thuc hien it nhat 1 vong cai thien:
  - Dieu chinh chunk size, overlap, hoac prompt template
  - Chay lai evaluation, so sanh ket qua truoc va sau

**Verification:**
- [ ] Eval dataset co it nhat 10 cau hoi voi expected answers
- [ ] Chay `python -m src.evals.evaluate` — script chay thanh cong, output ket qua
- [ ] Ket qua luu trong `src/evals/results/` co cac metrics ro rang (retrieval precision, answer correctness %)
- [ ] Co it nhat 2 file ket qua (truoc va sau cai thien) de so sanh

Ghi chu: Khong can perfect score. Can: (1) co so lieu cu the, (2) giai thich duoc tai sao, (3) cho thay ban da thu cai thien. Nha tuyen dung muon thay tu duy, khong phai 100% accuracy.

---

## Stage 8 — Portfolio Polish and Deployment [NOT STARTED]

**Goal:** Bien project tu "code chay duoc" thanh "portfolio project chuyen nghiep". Don dep code, viet documentation tot, them screenshots, va deploy neu kha thi.

**Why this matters:** Recruiter/hiring manager nhin vao GitHub cua ban trong 30 giay. Neu README khong ro, khong co screenshot, khong co huong dan — ho se chuyen sang ung vien khac. Stage nay dam bao project cua ban "presentable".

**Key files created/modified:**
- `README.md` — cap nhat voi screenshots, diagram, setup guide
- `tests/` — them tests cho cac component chinh
- Code cleanup toan bo repo
- (Optional) deployment config

**Tasks:**
- [ ] Don dep code toan bo repo:
  - Xoa comment thua, print statements con sot
  - Format code nhat quan (dung `black` hoac `ruff format`)
  - Sap xep imports (dung `isort`)
  - Kiem tra khong co API key hay secret trong code
- [ ] Cap nhat `README.md`:
  - Them screenshot cua Streamlit UI (luu trong `docs/` hoac repo)
  - Them architecture diagram (co the dung mermaid)
  - Viet huong dan setup tu A-Z: clone, install, set env, run backend, run frontend
  - Them section "What I learned" hoac "Technical highlights"
  - Them section "Limitations and future work"
- [ ] Them tests trong `tests/`:
  - `test_api.py` — test 3 endpoints cua FastAPI
  - `test_ingestion.py` — test extract va clean (neu chua co)
  - `test_retrieval.py` — test chunking va search (neu chua co)
  - Dam bao `pytest tests/` pass toan bo
- [ ] (Optional) Tao CI workflow `.github/workflows/test.yml` chay pytest tu dong
- [ ] (Optional) Deploy:
  - Streamlit Cloud (mien phi, de nhat)
  - Hoac Railway / Render cho FastAPI backend
  - Cap nhat README voi deployed URL
- [ ] Commit cuoi cung voi message: "Complete portfolio project — Week 8 final polish"

**Verification:**
- [ ] `README.md` co: overview, screenshot, architecture diagram, setup guide, tech stack, limitations
- [ ] Chay `pytest tests/` — tat ca tests pass, khong co failures
- [ ] Chay `rg "api_key\|secret\|password" --ignore-case` — khong co secret trong code
- [ ] Clone repo vao folder moi, theo README setup — project chay duoc tu scratch
- [ ] (Optional) Deployed URL truy cap duoc va hoat dong

Ghi chu: Day la buoc cuoi cung. Sau khi xong, project san sang de: (1) dua vao resume, (2) chia se tren LinkedIn, (3) demo trong phong van. Tap trung vao "first impression" — README va screenshot la thu dau tien nguoi ta nhin.

---

## Session Log

- 2026-03-18: Hoan tat Stage 1. FastAPI + Streamlit skeleton chay duoc. Tao PROGRESS.md va CHECKPOINT.md.