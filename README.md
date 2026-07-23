# Annual Report RAG Pipeline

A full Retrieval-Augmented Generation (RAG) pipeline built on financial annual reports from five companies: Apple, Amazon, NVIDIA, Tesla, and Berkshire Hathaway (~222,925 words).

## What This Covers

| Stage | Method | Key Result |
|-------|--------|-----------|
| Chunking | Fixed-size, Sliding Window, Semantic | Semantic selected (7.6% broken sentences vs ~95% for others) |
| Dense Retrieval | FAISS IndexFlatIP + all-MiniLM-L6-v2 | Avg relevance 2.70/3.0, 21ms latency |
| Sparse Retrieval | BM25Okapi | Avg relevance 2.00/3.0, 5ms latency |
| Hybrid Retrieval | Reciprocal Rank Fusion (RRF) | Avg relevance 2.40/3.0 |
| Reranking | cross-encoder/ms-marco-MiniLM-L-6-v2 | 20% rank-change rate, 104ms latency |
| Tabular RAG | pdfplumber + extended FAISS index | 94 tables, 1046 rows; pure table hits for structured queries |

## Repo Structure

```
rag_pipeline_annual_reports.ipynb   # Main notebook (all outputs populated)
tables_chunks.csv                    # Serialised table rows (1046 rows)
corpus/                              # 5 company annual report text files
openspec/                            # Design specs and task tracking
LESSONS_LEARNED.md                   # Implementation lessons
TOI.md                               # Useful commands reference
```

## How to Run

1. Upload `rag_pipeline_annual_reports.ipynb` and corpus zip to Google Colab
2. Run all cells top to bottom
3. Pinned versions: `sentence-transformers==2.7.0`, `transformers==4.40.2`, `protobuf==3.20.3`

> **Note:** Local execution requires ~4GB RAM. Google Colab recommended.

## Pipeline Architecture

```
Corpus (5 txt files)
        │
        ▼
  Semantic Chunker ──────────────── 1,311 chunks
        │
        ├──▶ FAISS Dense Index (all-MiniLM-L6-v2, 384-dim)
        │         │
        │         ▼
        │   Dense Retrieval (top-5)
        │         │
        ├──▶ BM25 Sparse Index
        │         │
        │         ▼
        │   Sparse Retrieval (top-5)
        │         │
        └──▶ Hybrid RRF (k=60, union of Dense+BM25 top-5)
                  │
                  ▼
        Cross-Encoder Reranker (top-3 reranked)
                  │
        pdfplumber Table Extraction
                  │
        Extended FAISS Index ──── 1,861 vectors (1311 text + 550 table)
```
