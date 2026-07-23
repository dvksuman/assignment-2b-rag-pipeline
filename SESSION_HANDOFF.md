# Session Handoff — Assignment 2B RAG Pipeline

**Date:** 2026-07-22
**Next action:** Paste Group 6 cells into Colab and run top-to-bottom; mark tasks [x] after successful run

---

## Project Location
```
/Users/dvksuman/Desktop/Semester3/LLM/ASSIGNMENT2
```

## GitHub Repo
https://github.com/dvksuman/assignment-2b-rag-pipeline

---

## Progress: 24/34 tasks complete

| Group | Status | Summary |
|-------|--------|---------|
| Group 1 — Setup | ✅ Done | 5 txt files loaded, 222,925 words |
| Group 2 — Chunking | ✅ Done | Semantic chunker selected, 1,311 chunks, 7.6% broken |
| Group 3 — Dense Retrieval | ✅ Done | FAISS IndexFlatIP, avg relevance 2.70/3.0, 21ms latency |
| Group 4 — BM25 + Hybrid | ✅ Done | BM25=2.00/3.0, Hybrid RRF=2.40/3.0 |
| Group 5 — Cross-Encoder | ✅ Done | Rank-change rate 20%, avg rerank latency 104.74ms |
| Group 6 — Tabular RAG | 🔄 In Progress | 6 cells written; pending Colab run |
| Group 7 — Finalisation | ⏳ Pending | |

---

## Table B2 Results (already computed)

| Method | Avg Latency (ms) | Avg Top-1 Relevance | Top-3 Coverage |
|--------|-----------------|---------------------|----------------|
| Dense (FAISS) | 21.13 | 2.70 | 10/10 |
| Sparse (BM25) | 5.01 | 2.00 | 7/10 |
| Hybrid (RRF) | 21.52 | 2.40 | 9/10 |

## Manual Relevance Scores (1=irrelevant, 2=partial, 3=perfect)
```
DENSE_RELEVANCE  = [3, 3, 3, 2, 2, 3, 3, 3, 3, 2]  # avg=2.70
BM25_RELEVANCE   = [3, 1, 2, 3, 1, 2, 1, 2, 3, 2]  # avg=2.00
HYBRID_RELEVANCE = [3, 2, 2, 2, 1, 3, 3, 2, 3, 3]  # avg=2.40
```

## 10 Queries Used
```python
QUERIES = [
    "What were NVIDIA's data center revenue figures?",       # Q01
    "How does Apple generate services revenue?",              # Q02
    "What is Amazon Web Services growth rate?",               # Q03
    "Describe Tesla vehicle delivery numbers",                # Q04
    "What companies does Berkshire Hathaway own?",            # Q05
    "How is NVIDIA positioned in the AI chip market?",        # Q06
    "What risks does Apple face in supply chain?",            # Q07
    "How does Amazon use advertising as a revenue stream?",   # Q08
    "What is NVIDIA's gaming segment performance?",           # Q09
    "How does Berkshire Hathaway approach capital allocation?" # Q10
]
```

---

## How to Resume in Colab

1. Go to colab.research.google.com
2. Upload `assignment_2b_rag_pipeline.ipynb`
3. Upload `ASSIGNMENT1stuff/domain_corpus (2).zip` via Files sidebar
4. Run all cells top to bottom (Groups 1–4 re-run fine)
5. Then paste new Group 5 cells from Claude

## Key Variables in Notebook (must exist before Group 5)
- `chunks_semantic` — list of 1,311 chunk dicts with 'text' and 'company'
- `chunk_embeddings` — numpy array (1311, 384) L2-normalised
- `chunks_index` — FAISS IndexFlatIP with 1,311 vectors
- `embedder` — SentenceTransformer('all-MiniLM-L6-v2')
- `bm25` — BM25Okapi index over tokenised chunks
- `dense_results`, `bm25_results`, `hybrid_results` — list of dicts per query
- `DENSE_RELEVANCE`, `BM25_RELEVANCE`, `HYBRID_RELEVANCE` — score lists
- `df_comparison` — Table B2 DataFrame

## Environment Notes
- Use Colab — local Mac only has 0.1GB free RAM, kernel crashes
- Do NOT set `HF_HUB_OFFLINE=1` in Colab (blocks model download)
- Pinned versions: `sentence-transformers==2.7.0`, `transformers==4.40.2`, `protobuf==3.20.3`

## Design Decisions
- Embedder: `all-MiniLM-L6-v2` (384-dim, cosine via IndexFlatIP)
- Chunking: semantic per-company, merged with company tag
- BM25: BM25Okapi, lowercase + whitespace tokenisation
- Hybrid: RRF with k=60, union of Dense top-5 + BM25 top-5
- Cross-encoder (Group 5): `cross-encoder/ms-marco-MiniLM-L-6-v2`
- Table extraction (Group 6): pdfplumber (NVIDIA, Apple, Amazon — skip Berkshire)

## What Group 5 Needs to Do
- Load `cross-encoder/ms-marco-MiniLM-L-6-v2`
- For each of 10 queries: take top-3 from best first-stage retriever (Dense) → rerank with cross-encoder
- Record reranking latency
- Compute rank-change rate (% queries where top-1 changed after reranking)
- Manually verify 5 queries: show pre/post top-1 chunk
