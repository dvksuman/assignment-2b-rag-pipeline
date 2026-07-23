## ADDED Requirements

### Requirement: Chunk embedding
The system SHALL embed all chunks using `sentence-transformers` (`all-MiniLM-L6-v2`, 384 dims, cosine similarity via inner product on L2-normalised vectors).

#### Scenario: Embeddings generated
- **WHEN** the best-performing chunk set is passed to the embedder
- **THEN** each chunk SHALL produce a 384-dimensional float32 vector

### Requirement: FAISS IndexFlatIP index
The system SHALL build a FAISS `IndexFlatIP` index from L2-normalised chunk embeddings and record index build time in milliseconds.

#### Scenario: Index built and timed
- **WHEN** all embeddings are added to the index
- **THEN** index SHALL contain exactly N vectors (N = number of chunks) and build time SHALL be logged

### Requirement: Dense top-5 retrieval with latency
The system SHALL retrieve top-5 chunks per query and record per-query latency in milliseconds.

#### Scenario: Top-5 chunks returned
- **WHEN** a query string is embedded and searched against the index
- **THEN** exactly 5 chunk indices and scores SHALL be returned

### Requirement: Top-1 relevance scoring
The system SHALL manually score the top-1 retrieved chunk for each of 10 queries on a 1–3 scale (1=not relevant, 2=partial, 3=highly relevant).

#### Scenario: Relevance scores recorded
- **WHEN** 10 queries are run
- **THEN** 10 top-1 relevance scores SHALL be recorded and averaged
