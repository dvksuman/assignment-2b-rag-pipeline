## 1. Environment & Corpus Setup

- [x] 1.1 Install dependencies: `sentence-transformers`, `faiss-cpu`, `rank_bm25`, `pdfplumber`, `pandas`, `numpy`, `transformers`
- [x] 1.2 Unzip `ASSIGNMENT1stuff/domain_corpus (2).zip` → 5 financial `.txt` files (Berkshire, NVIDIA, Tesla, Amazon, Apple, ~1.7MB total)
- [x] 1.3 Re-download the original 5 financial annual report PDFs (same URLs as Assignment 1B notebook) for tabular extraction in Part C
- [x] 1.4 Load all `.txt` files into a single corpus string; log total word count

## 2. Part A — Chunking Strategies

- [x] 2.1 Implement `fixed_size_chunker(text, max_words=200)` — splits by word count, no overlap
- [x] 2.2 Implement `sliding_window_chunker(text, max_words=200, overlap=20)` — sliding window with 10% overlap
- [x] 2.3 Implement `semantic_chunker(text, max_words=200)` — sentence-boundary-aware, use `nltk.sent_tokenize` or regex
- [x] 2.4 Compute quality metrics for each strategy: total chunks, avg size (words), std dev size, broken sentences %
- [x] 2.5 Display metrics comparison table (Step A2 table from assignment)
- [x] 2.6 Select best chunking strategy for Part B (justify choice in a markdown cell)

## 3. Part B — Dense Retrieval (FAISS)

- [x] 3.1 Load `all-MiniLM-L6-v2` from `sentence-transformers`; embed all chunks; L2-normalise vectors
- [x] 3.2 Build FAISS `IndexFlatIP`; time the index build; log embedding config (model, dims, metric, batch size)
- [x] 3.3 Define 10 domain queries; run each through dense retrieval (top-5); record per-query latency (ms)
- [x] 3.4 Manually score top-1 chunk per query on 1–3 scale; compute average top-1 relevance

## 4. Part B — Sparse & Hybrid Retrieval

- [x] 4.1 Build BM25Okapi index over whitespace-tokenised chunks using `rank_bm25`
- [x] 4.2 Run same 10 queries through BM25 (top-5); record per-query latency; score top-1 relevance
- [x] 4.3 Implement RRF fusion (`k=60`): merge dense and BM25 top-5 ranked lists; re-rank by RRF score
- [x] 4.4 Run same 10 queries through hybrid retrieval (top-5); record total latency; score top-1 relevance
- [x] 4.5 Compute top-3 coverage for each method; fill benchmark comparison table (Step B2 table)

## 5. Part C — Cross-Encoder Reranking

- [x] 5.1 Load `cross-encoder/ms-marco-MiniLM-L-6-v2` from HuggingFace
- [x] 5.2 For each of 10 queries: take top-3 from best first-stage retriever → rerank with cross-encoder → record reranking latency
- [x] 5.3 Compute rank-change rate: % of queries where top-1 result changed after reranking
- [x] 5.4 Manually verify 5 queries: display pre/post reranking top-1 chunk and note relevance change (improved/same/worse)
- [x] 5.5 Display reranking metrics summary and analysis markdown cell

## 6. Part C — Tabular RAG

- [x] 6.1 Use `pdfplumber` to extract tables from the 5 financial annual report PDFs; filter to tables with ≥2 cols and ≥2 rows; save each as a CSV (financial PDFs are rich in tables: income statements, balance sheets, segment data)
- [x] 6.2 Serialise each table row as `Col1: val1 | Col2: val2 | ...` text strings
- [x] 6.3 Save all serialised rows to `tables_chunks.csv`
- [x] 6.4 Embed serialised rows with same `all-MiniLM-L6-v2` embedder; add to existing FAISS index (or new mixed index)
- [x] 6.5 Run 3 structured tabular queries; show top retrieved results and highlight table-row hits
- [x] 6.6 Write 100-word markdown analysis: when does tabular RAG outperform text-chunk RAG, with concrete example

## 7. Finalisation & Submission

- [x] 7.1 Run all notebook cells in sequence; verify no errors and all output tables populated
- [x] 7.2 Export notebook to HTML: `jupyter nbconvert --to html assignment_2b_rag_pipeline.ipynb`
- [x] 7.3 Verify `tables_chunks.csv` exists and has correct serialised format
- [x] 7.4 Review all assignment requirement tables are filled (A2, B2, C1 metrics, C2 demo)
