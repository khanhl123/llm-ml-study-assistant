# CHECKPOINT — AI Project State

> **For the AI chatbot.** This file is the single source of truth for project progress.
> Read this file at the start of every session.

## AI Instructions

1. Read this file first when the user opens the project.
2. Identify the current stage — the first stage that is NOT marked `[COMPLETED]`.
3. Plan today's tasks from that stage's unchecked items.
4. Work through the tasks one by one with the user.
5. After completing each task, run the verification steps for that task.
6. If verification passes, mark the task `[x]` in this file.
7. When ALL tasks and verifications in a stage pass, change the stage status to `[COMPLETED]`.
8. After completing a stage, update `PROGRESS.md` with a learning journal entry for that stage.
9. Append a one-line entry to the Session Log at the bottom of this file.

## Project Overview

**Repo:** llm-ml-study-assistant
**What:** An LLM-powered ML study assistant that answers questions from curated sources with citations.
**Stack:** FastAPI (backend) + Streamlit (frontend) + OpenAI API + FAISS/Chroma (vector search)
**Architecture:** Retrieval-Augmented Generation (RAG) pipeline built incrementally over 8 stages.

---

## Stage 1 — Project Setup [COMPLETED]

**Tasks:**
- [x] Create repo structure (`services/`, `apps/`, `src/`, `data/`, `tests/`)
- [x] Write `README.md` with project overview, goals, and architecture
- [x] Write `PROJECT_SCOPE.md` with full scope definition
- [x] Build FastAPI backend with `GET /`, `GET /health`, `POST /query`
- [x] Build Streamlit frontend wired to backend `/query`
- [x] Create `requirements.txt` with starter dependencies
- [x] Create `.env.example` with placeholder values

**Verification:**
- [x] `uvicorn services.api.main:app` starts without errors
- [x] `GET /health` returns `{"status": "ok"}`
- [x] `POST /query` returns valid JSON with `question`, `answer`, `citations`
- [x] Streamlit displays answer and citations from backend response

Ghi chu: Week 1 hoan tat. Placeholder responses, chua co LLM hay vector search.

---

## Stage 2 — Source Collection [NOT STARTED]

**Tasks:**
- [ ] Chon 3-5 tai lieu ML dang tin cay (textbook, lecture notes, open resources)
- [ ] Tao file `data/source_manifest.json` luu thong tin tung tai lieu (title, author, type, license, URL)
- [ ] Download hoac copy tai lieu vao `data/raw/`
- [ ] Ghi chu license/usage rights cho tung tai lieu
- [ ] Update `data/README.md` voi huong dan ve data folder

**Verification:**
- [ ] `data/source_manifest.json` ton tai va co du thong tin cho moi tai lieu
- [ ] `data/raw/` chua it nhat 3 file tai lieu
- [ ] Moi tai lieu trong manifest co ghi chu license
- [ ] `data/README.md` mo ta cach su dung data folder

Ghi chu: Chon tai lieu nho, chat luong cao. Uu tien open-access.

---

## Stage 3 — Ingestion Pipeline [NOT STARTED]

**Tasks:**
- [ ] Cai dat PyMuPDF hoac pypdf vao `requirements.txt`
- [ ] Viet script extract text tu PDF trong `src/ingestion/`
- [ ] Giu metadata cho moi trang (source title, page number, author)
- [ ] Lam sach text (xoa header/footer, fix encoding, loai bo noise)
- [ ] Luu output da xu ly vao `data/processed/` (JSON format)
- [ ] Viet test co ban cho ingestion pipeline trong `tests/`

**Verification:**
- [ ] Script chay duoc tren moi file trong `data/raw/`
- [ ] Output JSON co du cac field: `text`, `source`, `page`, `author`
- [ ] Text sach, khong co ky tu la hoac header/footer thua
- [ ] Test pass khi chay `pytest tests/`

Ghi chu: Bat dau voi 1 file PDF truoc, roi mo rong ra cac file khac.

---

## Stage 4 — Chunking and Retrieval Foundation [NOT STARTED]

**Tasks:**
- [ ] Viet logic chunking trong `src/retrieval/` (split text thanh cac doan nho)
- [ ] Chon kich thuoc chunk phu hop (vd: 500 tokens, overlap 100)
- [ ] Giu metadata cho moi chunk (source, page, chunk_id)
- [ ] Tao embeddings bang OpenAI Embeddings API hoac sentence-transformers
- [ ] Luu embeddings vao FAISS hoac Chroma
- [ ] Viet function retrieval: nhan question, tra ve top-k chunks
- [ ] Them FAISS/Chroma va embedding dependencies vao `requirements.txt`

**Verification:**
- [ ] Chunking tao ra cac chunk co do dai hop ly
- [ ] Moi chunk giu nguyen metadata (source, page)
- [ ] Retrieval tra ve top-k chunks lien quan khi hoi cau hoi test
- [ ] Vector store luu va load duoc tu disk
- [ ] Test co ban pass trong `tests/`

Ghi chu: Day la buoc quan trong nhat — chat luong retrieval quyet dinh chat luong cua ca he thong.

---

## Stage 5 — Grounded Answer Generation [NOT STARTED]

**Tasks:**
- [ ] Them `openai` vao `requirements.txt`
- [ ] Tao prompt template trong `src/generation/` (system prompt + retrieved context + user question)
- [ ] Goi OpenAI Chat Completions API de generate answer
- [ ] Chi cho phep LLM tra loi dua tren context da retrieve (grounded)
- [ ] Extract citations tu retrieved chunks va tra ve cung answer
- [ ] Thay the placeholder trong `POST /query` bang RAG logic that
- [ ] Xu ly truong hop khong tim duoc context phu hop

**Verification:**
- [ ] `POST /query` tra ve answer dua tren retrieved context (khong phai placeholder)
- [ ] Citations chinh xac — tro dung ve source va page
- [ ] Khi hoi cau hoi ngoai pham vi corpus, he thong tra loi "khong du thong tin"
- [ ] API key doc tu `.env`, khong hardcode trong code
- [ ] Streamlit hien thi answer that tu LLM

Ghi chu: Su dung OpenAI API key tu `.env`. Khong commit key that vao git.

---

## Stage 6 — Frontend Integration [NOT STARTED]

**Tasks:**
- [ ] Cap nhat Streamlit UI hien thi real answers tu LLM
- [ ] Format citations ro rang (source name, page number)
- [ ] Them loading state khi cho LLM response
- [ ] Hien thi thong bao khi khong tim duoc context phu hop
- [ ] Test end-to-end: nhap cau hoi → nhan answer + citations

**Verification:**
- [ ] Nhap cau hoi ML → nhan duoc answer co citations
- [ ] Citations hien thi dung format (ten sach, so trang)
- [ ] UI khong crash khi backend tra loi cham hoac loi
- [ ] End-to-end flow hoat dong tu Streamlit → FastAPI → LLM → Streamlit

Ghi chu: Giu UI don gian. Khong can dep, can dung va ro rang.

---

## Stage 7 — Evaluation and Improvement [NOT STARTED]

**Tasks:**
- [ ] Tao evaluation dataset: 10-20 cap (question, expected_answer, expected_source)
- [ ] Viet eval script trong `src/evals/` do retrieval quality (precision, recall)
- [ ] Do answer groundedness (answer co dua tren context khong?)
- [ ] Do answer correctness (answer co dung khong?)
- [ ] Ghi ket qua evaluation vao file (JSON hoac markdown)
- [ ] Xac dinh diem yeu va cai thien (chunking, prompt, retrieval)

**Verification:**
- [ ] Eval dataset co it nhat 10 cau hoi voi expected answers
- [ ] Eval script chay duoc va tra ve metric ro rang
- [ ] Ket qua duoc luu lai de so sanh sau nay
- [ ] It nhat 1 vong cai thien dua tren ket qua eval

Ghi chu: Khong can perfect. Can do duoc, giai thich duoc, va co con so cu the.

---

## Stage 8 — Portfolio Polish and Deployment [NOT STARTED]

**Tasks:**
- [ ] Don dep code: xoa comment thua, format lai, sap xep imports
- [ ] Cap nhat README voi screenshots, architecture diagram, huong dan setup
- [ ] Them tests cho cac component chinh trong `tests/`
- [ ] Tao `.github/` workflows neu can (optional)
- [ ] Deploy len cloud neu kha thi (Streamlit Cloud, Railway, hoac Render)
- [ ] Commit cuoi cung voi message ro rang

**Verification:**
- [ ] README co screenshots va diagram
- [ ] `pytest tests/` pass toan bo
- [ ] Repo sach, khong co file thua hoac secret
- [ ] Project co the clone va chay duoc tu scratch theo README
- [ ] (Optional) Deployed URL hoat dong

Ghi chu: Day la buoc cuoi. Tap trung lam cho project "presentable" cho portfolio va phong van.

---

## Session Log

- 2026-03-18: Hoan tat Stage 1. FastAPI + Streamlit skeleton chay duoc. Tao PROGRESS.md va CHECKPOINT.md.