## Context

Assignment 2B builds a full RAG pipeline on a domain text corpus. The pipeline progresses through three phases: chunking → retrieval → reranking + tabular RAG. All work is delivered as a single self-contained Jupyter notebook with HTML export, plus a `tables_chunks.csv`. No existing codebase exists — this is a greenfield notebook.

Domain corpus: 5 financial annual report `.txt` files from Assignment 1A — Apple, Amazon, NVIDIA, Tesla, Berkshire Hathaway — totalling 222,925 words. NVIDIA dominates at 92,722 words; Tesla is smallest at 5,554 words (quarterly update, not full annual report).

## Goals / Non-Goals

**Goals:**
- Implement and compare 3 chunking strategies with measurable quality metrics
- Build Dense (FAISS), Sparse (BM25), and Hybrid (RRF) retrievers and benchmark all 3
- Add cross-encoder reranking and measure rank-change rate over 10 queries
- Extract tables from PDFs, serialise, index, and demonstrate tabular RAG
- Produce clean, reproducible notebook output suitable for academic submission

**Non-Goals:**
- Deployment or production hosting
- Fine-tuned embedding models (use off-the-shelf sentence-transformers)
- Evaluation with ground-truth labels (manual 1–3 relevance scoring is sufficient)
- Multi-turn conversational RAG

## Decisions

### D1: Corpus source
Use publicly available domain text (e.g., AI/ML Wikipedia dumps or any domain with available PDFs for tabular part). **Why**: Assignment requires `.txt` files and PDF tables — these are easy to source without copyright concerns and relevant to the course domain.

### D2: Embedding model — `all-MiniLM-L6-v2`
**Why**: Small (80MB), fast, well-supported by `sentence-transformers`, 384-dim vectors work well with FAISS IndexFlatIP. Alternatives: `all-mpnet-base-v2` (better quality, 4× slower) — overkill for assignment benchmarking.

### D3: FAISS index type — `IndexFlatIP`
**Why**: Assignment specifies IndexFlatIP. Inner product with L2-normalised vectors equals cosine similarity. No approximate search needed at corpus sizes typical of an assignment.

### D4: BM25 library — `rank_bm25`
**Why**: Pure Python, no Java dependency (vs Elasticsearch/Solr), easy to install and use in Colab/local notebooks.

### D5: Hybrid fusion — Reciprocal Rank Fusion (RRF)
**Why**: Assignment specifies RRF. Formula: `score(d) = Σ 1/(k + rank(d))` with k=60. No learned weights needed, robust and parameter-free.

### D6: Cross-encoder — `cross-encoder/ms-marco-MiniLM-L-6-v2`
**Why**: Standard HuggingFace cross-encoder, small and fast, directly applicable to passage reranking. No fine-tuning required.

### D7: Table extraction — `pdfplumber`
**Why**: Pure Python, no Java, handles diverse PDF table layouts, returns structured data as list of lists. `camelot` requires Ghostscript; `pdfplumber` has fewer install friction points.

### D8: Single notebook architecture
All parts (A, B, C) in one `.ipynb` with clear section headers. **Why**: Assignment requires `.ipynb` + `.html` deliverable — one file is easier to submit and verify outputs.

### D9: PDF download fallback strategy
If any of the 5 annual report PDFs fail to download (large file size, network timeout, or URL change), the notebook gracefully logs the failure and continues. For Part C2 tabular extraction, we prioritise NVIDIA, Apple, Amazon (clean grid-based tables). Skip Berkshire (huge PDF, narrative-heavy). The assignment explicitly permits using alternate finance PDFs as fallback. **Why**: Robustness over completeness — a failed download should not block the rest of the notebook.

### D10: Chunking granularity — per-company, not concatenated
All chunkers operate on each company's text separately, then merge into a flat list with `company` metadata tag. **Why**: Concatenating all 5 files before chunking creates chunks that straddle company boundaries (Apple data mixed with Amazon data in one chunk), contaminating both embeddings and retrieval results.

### D11: Selected chunking strategy for Part B — Semantic
Semantic chunking selected over fixed-size and sliding window. Actual measured metrics: Fixed=94.9% broken, Sliding=94.9% broken, Semantic=7.6% broken. Semantic has higher std dev (40.1w vs 7.3w) but produces coherent chunks — better for embedding quality. **Why**: Broken sentence rates in financial text are much higher than general prose (~95% vs expected ~65%) because financial sentences are long relative to 200-word chunks.

### D12: Broken sentence % definition
A chunk is "broken" if it does not end with `.`, `!`, `?`, `"`, or `)`. Checked on the last character after `rstrip()`. Start-of-chunk detection (lowercase first word) was rejected as unreliable in financial text (table values, numbers, ticker symbols all start without capitals).

## Risks / Trade-offs

- [Small corpus → low chunk count] → Mitigation: Use at least 5–10 documents totalling >10K words to get meaningful chunking statistics
- [BM25 tokenisation differs from embedding tokenisation] → Mitigation: Use same whitespace tokenisation for BM25; document this in notebook
- [Cross-encoder is slow on CPU] → Mitigation: Only rerank top-3 candidates per query; note latency in benchmark table
- [PDF tables may be irregular] → Mitigation: Filter out tables with <2 columns or <2 rows; handle missing cells with empty string
- [Manual relevance scoring is subjective] → Mitigation: Define 1–3 scale clearly in notebook; be consistent across queries
