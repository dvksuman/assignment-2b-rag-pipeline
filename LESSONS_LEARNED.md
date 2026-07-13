# Lessons Learned — Assignment 2B RAG Pipeline

This file is auto-updated during implementation. Each entry documents a problem encountered, its root cause, and the fix.

---

<!-- Entries will be appended below as implementation progresses -->

## LL-01 — pip dependency conflict with pillow
**Problem:** `pip install` reported a conflict: `streamlit 1.46.0 requires pillow<12` but `pillow 12.3.0` is installed.  
**Root cause:** Streamlit pinned to an older pillow range; our install has a newer version.  
**Fix:** Conflict is non-fatal — all required packages (sentence-transformers, faiss-cpu, etc.) install successfully. The streamlit conflict does not affect this assignment.  
**Lesson:** Always check that the conflict is with an unused package before spending time resolving it.

## LL-03 — Broken sentence % much higher than expected for fixed/sliding chunkers
**Problem:** Fixed-size and sliding window both showed ~95% broken sentence rate (expected ~65%).  
**Root cause:** Financial annual report text is dense prose — long sentences with few terminal punctuation marks per 200 words. Most 200-word windows don't end on a `.`.  
**Fix:** No code fix needed. The metric is correct. Acknowledge in analysis: financial text has longer sentences than general prose, making arbitrary cuts even more harmful.  
**Lesson:** Benchmark expectations from domain characteristics, not general text assumptions.

## LL-04 — `jupyter execute` runs but does not save cell outputs to notebook
**Problem:** `jupyter execute notebook.ipynb` returned RC=0 but all cells showed `outputs=[]`.  
**Root cause:** Unknown nbclient/nbconvert interaction — outputs not flushed to file.  
**Fix:** Verified correctness by re-running the core Python logic directly via `/opt/anaconda3/bin/python3`. Cell outputs will be populated when the notebook is opened and run in Jupyter.  
**Lesson:** Use `jupyter nbconvert --to notebook --execute --inplace` for output saving, but watch for permission errors on `/usr/local/share/jupyter/conf.json`.

## LL-05 — L2-normalisation must be applied to both corpus AND query vectors
**Problem:** IndexFlatIP gives cosine similarity only if vectors are unit-length. Normalising corpus but forgetting query vectors gives wrong ranking silently.  
**Root cause:** Normalisation is a two-step responsibility: once at index-build time, once at each query.  
**Fix:** Call `faiss.normalize_L2()` in both Step 3.1 (corpus) and inside `dense_retrieve()` (query).  
**Lesson:** Any time you L2-normalise at index build, normalise queries too — test by checking norms equal 1.0.

## LL-06 — Separate embedding time from index build time in benchmarks
**Problem:** Conflating corpus embedding time (~30s) with FAISS index build time (~ms) gives misleading latency numbers.  
**Root cause:** The assignment asks to "time the index build" specifically — `index.add()` not `encode()`.  
**Fix:** Use two separate `time.perf_counter()` blocks; log both values distinctly.  
**Lesson:** Always scope timing blocks to exactly the operation being benchmarked.

## LL-02 — Tesla corpus is very small (5,554 words)
**Problem:** Tesla file is ~16× smaller than NVIDIA (92K words). This may skew chunking metrics.  
**Root cause:** Assignment 1B used a Tesla quarterly update PDF, not a full annual report.  
**Fix:** No fix needed — note this disparity in the chunking analysis. The small size means Tesla contributes only ~27 fixed-size chunks.  
**Lesson:** Always check per-document word counts before assuming uniform corpus distribution.
