# Session Handoff — Assignment 2B RAG Pipeline

**Date:** 2026-07-22  
**Next action:** Start Group 5 — Cross-Encoder Reranking

---

## Project Location
```
/Users/dvksuman/Desktop/Semester3/LLM/ASSIGNMENT2
```

## GitHub Repo
https://github.com/dvksuman/assignment-2b-rag-pipeline

---

## Progress: 19/34 tasks complete

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

### ✅ Group 3 — Done (Part B: Dense Retrieval)
- Embedded 1,311 semantic chunks with all-MiniLM-L6-v2 (384-dim, batch_size=32)
- Built FAISS IndexFlatIP with L2-normalised vectors (cosine similarity)
- Defined 10 domain queries (NVIDIA×3, Apple×2, Amazon×2, Berkshire×2, Tesla×1)
- Dense retrieval top-5 per query with per-query latency logged
- Manual relevance scoring (3=best) and avg relevance computed for Table B2
- `chunks_index` built; `tables_index` deferred to Group 6 (separate index design)

### ✅ Group 4 — Done (Sparse BM25 + Hybrid RRF)
- BM25 index: 1,311 chunks, 26,432 vocab, 74ms build
- BM25 avg relevance: 2.00/3.0, avg latency: 5.01ms
- Hybrid RRF (k=60) avg relevance: 2.40/3.0, avg latency: 21.52ms
- Table B2 complete: Dense=2.70, BM25=2.00, Hybrid=2.40
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
2. Go to colab.research.google.com
3. Upload `assignment_2b_rag_pipeline.ipynb`
4. Upload `ASSIGNMENT1stuff/domain_corpus (2).zip` via Colab Files sidebar
5. Run all cells top to bottom — Groups 1–3 first, then continue with Group 4

## Environment Issue (resolved by moving to Colab)
- Local Mac has only 0.1GB free RAM — kernel crashes during SentenceTransformer embedding
- `sentence-transformers==2.7.0` + `transformers==4.40.2` + `protobuf==3.20.3` are the pinned versions that fix the import error
- Add `os.environ["TOKENIZERS_PARALLELISM"] = "false"` and `os.environ["HF_HUB_OFFLINE"] = "1"` before embedding cell
