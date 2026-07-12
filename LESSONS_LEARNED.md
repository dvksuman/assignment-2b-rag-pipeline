# Lessons Learned — Assignment 2B RAG Pipeline

This file is auto-updated during implementation. Each entry documents a problem encountered, its root cause, and the fix.

---

<!-- Entries will be appended below as implementation progresses -->

## LL-01 — pip dependency conflict with pillow
**Problem:** `pip install` reported a conflict: `streamlit 1.46.0 requires pillow<12` but `pillow 12.3.0` is installed.  
**Root cause:** Streamlit pinned to an older pillow range; our install has a newer version.  
**Fix:** Conflict is non-fatal — all required packages (sentence-transformers, faiss-cpu, etc.) install successfully. The streamlit conflict does not affect this assignment.  
**Lesson:** Always check that the conflict is with an unused package before spending time resolving it.

## LL-02 — Tesla corpus is very small (5,554 words)
**Problem:** Tesla file is ~16× smaller than NVIDIA (92K words). This may skew chunking metrics.  
**Root cause:** Assignment 1B used a Tesla quarterly update PDF, not a full annual report.  
**Fix:** No fix needed — note this disparity in the chunking analysis. The small size means Tesla contributes only ~27 fixed-size chunks.  
**Lesson:** Always check per-document word counts before assuming uniform corpus distribution.
