# TOI — Tools & Commands Reference (Assignment 2B)

Quick reference for commands discovered during this project.

---

## Environment Setup

```bash
# Unzip the corpus
unzip "ASSIGNMENT1stuff/domain_corpus (2).zip" -d corpus/

# Install all dependencies
pip install sentence-transformers faiss-cpu rank_bm25 pdfplumber pandas numpy transformers nltk

# Export notebook to HTML
jupyter nbconvert --to html assignment_2b_rag_pipeline.ipynb
```

## Jupyter

```bash
# Start Jupyter notebook
jupyter notebook

# Run all cells from command line (non-interactive)
jupyter nbconvert --to notebook --execute assignment_2b_rag_pipeline.ipynb --output assignment_2b_rag_pipeline.ipynb
```

---

<!-- Commands will be appended below as implementation progresses -->
