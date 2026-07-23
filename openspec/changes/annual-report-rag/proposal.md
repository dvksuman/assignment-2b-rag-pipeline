## Why

Build a production-grade RAG pipeline on a financial annual reports corpus, progressing from document chunking through dense/sparse/hybrid retrieval to cross-encoder reranking and tabular RAG. The corpus consists of 5 `.txt` files (Berkshire Hathaway, NVIDIA, Tesla, Amazon, Apple) totalling ~1.7MB. Original PDFs are used for tabular extraction.

## What Changes

- Implement three chunking strategies (Fixed-Size, Sliding Window, Semantic) with quality metrics
- Build and benchmark three retrieval systems: Dense (FAISS), Sparse (BM25), Hybrid (RRF)
- Add cross-encoder reranking stage and measure rank-change metrics
- Extract tables from domain PDFs, serialise rows, and index alongside text chunks for tabular RAG
- Produce a single Jupyter notebook (.ipynb + .html export) and `tables_chunks.csv` as deliverables

## Capabilities

### New Capabilities

- `chunking-strategies`: Fixed-Size, Sliding Window, and Semantic chunking of domain `.txt` corpus with quality metrics (total chunks, avg size, std dev, broken sentences %)
- `dense-retrieval`: Sentence-transformer embeddings + FAISS IndexFlatIP index; top-5 retrieval with latency benchmarking
- `sparse-retrieval`: BM25 index using `rank_bm25`; top-5 retrieval with latency benchmarking
- `hybrid-retrieval`: Reciprocal Rank Fusion (RRF) combining dense and BM25 scores; benchmarked against 10 domain queries
- `cross-encoder-reranking`: Cross-encoder model reranking top-3 results; measures latency and rank-change rate
- `tabular-rag`: Table extraction from PDFs via `pdfplumber`, row serialisation to text, indexing alongside text chunks, demo of 3 structured queries

### Modified Capabilities

## Impact

- New directory: `ASSIGNMENT2/` containing `assignment_2b_rag_pipeline.ipynb`
- New file: `tables_chunks.csv`
- Dependencies: `sentence-transformers`, `faiss-cpu`, `rank_bm25`, `pdfplumber`, `pandas`, `numpy`, `transformers` (cross-encoder)
- No existing code modified
