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

## Corpus word count (quick check)
```python
import os
for f in sorted(os.listdir('corpus')):
    if f.endswith('.txt'):
        wc = len(open(f'corpus/{f}').read().split())
        print(f'{f}: {wc:,} words')
```

## Run notebook cells via anaconda python (when system python lacks packages)
```bash
/opt/anaconda3/bin/python3 your_script.py
/opt/anaconda3/bin/jupyter execute notebook.ipynb
```

## Download NLTK punkt tokenizer data
```python
import nltk
nltk.download('punkt_tab', quiet=True)  # newer NLTK
nltk.download('punkt', quiet=True)       # fallback
```

## Verify chunking metrics quickly (outside notebook)
```python
sizes = [len(c['text'].split()) for c in chunks]
import numpy as np
print(np.mean(sizes), np.std(sizes))
ENDINGS = ('.', '!', '?', '"', ')')
broken_pct = 100 * sum(1 for c in chunks if not c['text'].rstrip().endswith(ENDINGS)) / len(chunks)
```

## Check installed packages
```bash
pip show sentence-transformers faiss-cpu rank_bm25 pdfplumber transformers | grep -E "^Name|^Version"
```
