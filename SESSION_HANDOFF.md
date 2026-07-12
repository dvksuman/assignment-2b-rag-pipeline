# Session Handoff — Assignment 2B RAG Pipeline

**Date:** 2026-07-12  
**Next action:** Start Group 2 — Part A: Chunking Strategies

---

## Project Location
```
/Users/dvksuman/Desktop/Semester3/LLM/ASSIGNMENT2
```

## GitHub Repo
https://github.com/dvksuman/assignment-2b-rag-pipeline

---

## Progress: 4/34 tasks complete

### ✅ Group 1 — Done
- Dependencies installed (sentence-transformers, faiss-cpu, rank_bm25, pdfplumber, transformers, nltk)
- Corpus unzipped → 5 `.txt` files in `corpus/` folder (222,925 total words)
- PDF download cells written (with fallback handling for failed downloads)
- Corpus loading with per-company word count logging

### ⏳ Group 2 — Next (Part A: Chunking Strategies)
Tasks 2.1–2.6 in `openspec/changes/assignment-2b-rag-pipeline/tasks.md`:
- Implement Fixed-Size chunker (200 words, no overlap)
- Implement Sliding Window chunker (200 words, 20-word overlap)
- Implement Semantic chunker (sentence-boundary-aware, max 200 words)
- Compute quality metrics: total chunks, avg size, std dev, broken sentences %
- Display Step A2 metrics table
- Select best strategy with justification

### ⏳ Group 3 — Dense Retrieval (FAISS)
### ⏳ Group 4 — Sparse (BM25) + Hybrid (RRF)
### ⏳ Group 5 — Cross-Encoder Reranking
### ⏳ Group 6 — Tabular RAG
### ⏳ Group 7 — Finalisation & Submission

---

## Key Files
| File | Purpose |
|------|---------|
| `assignment_2b_rag_pipeline.ipynb` | Main notebook — add all new cells here |
| `openspec/changes/assignment-2b-rag-pipeline/tasks.md` | Task tracker — mark `[~]` before editing, `[x]` when done |
| `LESSONS_LEARNED.md` | Auto-update after every non-trivial fix |
| `TOI.md` | Auto-update with useful commands |
| `openspec/changes/assignment-2b-rag-pipeline/design.md` | Auto-update with design decisions |
| `CLAUDE.md` | Project rules — read this first |

---

## Corpus Facts
- 5 companies: Apple (41,760w), Amazon (42,077w), NVIDIA (92,722w), Tesla (5,554w), Berkshire (40,812w)
- Total: 222,925 words
- Expected chunks @ 200 words: ~1,114 (fixed-size), ~1,237 (sliding window)
- Tesla is very small — only ~27 chunks. Note this in chunking analysis.

## Design Decisions Made
- Embedder: `all-MiniLM-L6-v2` (384-dim, cosine via IndexFlatIP)
- BM25: `rank_bm25` (BM25Okapi, whitespace tokenised)
- Hybrid: RRF with k=60
- Cross-encoder: `cross-encoder/ms-marco-MiniLM-L-6-v2`
- Table extraction: `pdfplumber` (NVIDIA, Apple, Amazon PDFs — skip Berkshire)
- PDF fallback: allowed per assignment if download fails

## Workflow Rules (from CLAUDE.md)
1. Mark task `[~]` before editing notebook
2. Complete all 7 checklist steps automatically after each group:
   - Run cells & verify output
   - Mark `[x]` in tasks.md
   - Update LESSONS_LEARNED.md
   - Update TOI.md
   - Update design.md (if decisions made)
   - `git commit`
   - `git log --oneline -1` to verify
3. `git push origin master` after every commit

## Hooks Active
- **PreToolUse**: blocks notebook edits without `[~]` task; blocks `git commit` without docs update
- **Stop**: shows post-task checklist summary at session end

---

## To Resume in New Session
1. Open this file first
2. Run: `cd /Users/dvksuman/Desktop/Semester3/LLM/ASSIGNMENT2`
3. Run: `openspec status --change "assignment-2b-rag-pipeline"`
4. Continue with Group 2 — add chunking cells to `assignment_2b_rag_pipeline.ipynb`
