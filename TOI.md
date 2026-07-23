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

## FAISS dense retrieval — quick pattern
```python
import faiss
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = embedder.encode(texts, batch_size=32, convert_to_numpy=True).astype('float32')
faiss.normalize_L2(embeddings)                  # normalise corpus

index = faiss.IndexFlatIP(384)
index.add(embeddings)                           # build index

q = embedder.encode([query], convert_to_numpy=True).astype('float32')
faiss.normalize_L2(q)                           # normalise query too
scores, indices = index.search(q, k=5)          # returns top-5
```

## Verify L2 normalisation
```python
import numpy as np
norms = np.linalg.norm(embeddings[:5], axis=1)
print(norms)   # should all be ~1.0
```

## Check installed packages
```bash
pip show sentence-transformers faiss-cpu rank_bm25 pdfplumber transformers | grep -E "^Name|^Version"
```

## BM25 useful commands
# Build BM25 index
bm25 = BM25Okapi([text.lower().split() for text in corpus])

# Score all chunks against a query
scores = bm25.get_scores(query.lower().split())
top5 = np.argsort(scores)[::-1][:5]

# Vocab size
len(bm25.idf)
