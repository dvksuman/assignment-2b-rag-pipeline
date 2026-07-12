# Session Handoff — Assignment 2B RAG Pipeline

**Date:** 2026-07-12  
**Next action:** Start Group 3 — Part B: Dense Retrieval (FAISS)

---

## Project Location
```
/Users/dvksuman/Desktop/Semester3/LLM/ASSIGNMENT2
```

## GitHub Repo
https://github.com/dvksuman/assignment-2b-rag-pipeline

---

## Progress: 10/34 tasks complete

### ✅ Group 1 — Done
- Dependencies installed (sentence-transformers, faiss-cpu, rank_bm25, pdfplumber, transformers, nltk)
- Corpus unzipped → 5 `.txt` files in `corpus/` folder (222,925 total words)
- PDF download cells written (with fallback handling for failed downloads)
- Corpus loading with per-company word count logging

### ✅ Group 2 — Done (Part A: Chunking Strategies)
- Fixed-size chunker: 1,117 chunks, avg=199.6w, broken=94.9%
- Sliding window chunker: 1,240 chunks, avg=199.7w, broken=94.9%
- Semantic chunker: 1,311 chunks, avg=170.1w, broken=7.6% ← selected for Part B
- Quality metrics table (Step A2) displayed
- Best strategy justification written (semantic wins on broken sentence %)
- Full inline comments and justifications added to all cells

### ⏳ Group 3 — Next (Part B: Dense Retrieval)
Tasks 3.1–3.4 in `openspec/changes/assignment-2b-rag-pipeline/tasks.md`:
- Load `all-MiniLM-L6-v2`, embed all 1,311 semantic chunks, L2-normalise
- Build FAISS IndexFlatIP, time the index build
- Define 10 domain queries, run dense retrieval (top-5), record per-query latency
- Manually score top-1 chunk per query on 1–3 scale, compute avg relevance

### ⏳ Group 4 — Sparse (BM25) + Hybrid (RRF)
### ⏳ Group 5 — Cross-Encoder Reranking
### ⏳ Group 6 — Tabular RAG
### ⏳ Group 7 — Finalisation & Submission

---

## Key Files
| File | Purpose |
|------|---------|
| `assignment_2b_rag_pipeline.ipynb` | Main notebook — add all new cells here |
| `openspec/changes/assignment-2b-rag-pipeline/tasks.md` | Task tracker |
| `LESSONS_LEARNED.md` | Auto-update after every non-trivial fix |
| `TOI.md` | Auto-update with useful commands |
| `openspec/changes/assignment-2b-rag-pipeline/design.md` | Design decisions |
| `CLAUDE.md` | Project rules |

---

## Corpus & Chunking Facts
- 5 companies: Apple (41,760w), Amazon (42,077w), NVIDIA (92,722w), Tesla (5,554w), Berkshire (40,812w)
- Total: 222,925 words
- **Active chunk list: `chunks_semantic` — 1,311 chunks**
- Tesla note: tiny corpus + two-column PDF artifact → higher broken % than expected

## Design Decisions Made
- Embedder: `all-MiniLM-L6-v2` (384-dim, cosine via IndexFlatIP)
- Chunking: semantic per-company, merged with company metadata tag
- BM25: `rank_bm25` (BM25Okapi, whitespace tokenised)
- Hybrid: RRF with k=60
- Cross-encoder: `cross-encoder/ms-marco-MiniLM-L-6-v2`
- Table extraction: `pdfplumber` (NVIDIA, Apple, Amazon PDFs — skip Berkshire)

## Workflow Rules (from CLAUDE.md)
1. Mark task `[~]` before editing notebook
2. Complete all 8 checklist steps after each group (see CLAUDE.md) — includes SESSION_HANDOFF update
3. Cell outputs left empty — will be populated in Step 7.1 final run
4. `git push origin master` after every commit

---

## To Resume in New Session
1. Open this file first
2. `cd /Users/dvksuman/Desktop/Semester3/LLM/ASSIGNMENT2`
3. Continue with Group 3 — add FAISS embedding cells to `assignment_2b_rag_pipeline.ipynb`
