## ADDED Requirements

### Requirement: BM25 index
The system SHALL build a BM25 index using `rank_bm25` (BM25Okapi) over whitespace-tokenised chunks.

#### Scenario: BM25 index built
- **WHEN** the tokenised chunk list is passed to BM25Okapi
- **THEN** the index SHALL contain all N chunks and be ready for scoring

### Requirement: BM25 top-5 retrieval with latency
The system SHALL retrieve top-5 chunks per query using BM25 scoring and record per-query latency in milliseconds.

#### Scenario: Top-5 BM25 results returned
- **WHEN** a query string is tokenised and scored against the BM25 index
- **THEN** exactly 5 chunks with highest BM25 scores SHALL be returned

### Requirement: BM25 top-1 relevance scoring
The system SHALL manually score the top-1 BM25-retrieved chunk per query on the 1–3 scale.

#### Scenario: BM25 relevance scores recorded
- **WHEN** 10 queries are run
- **THEN** 10 top-1 relevance scores SHALL be recorded and averaged
