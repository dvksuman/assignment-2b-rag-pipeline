## ADDED Requirements

### Requirement: Reciprocal Rank Fusion
The system SHALL combine dense and BM25 ranked lists using RRF: `score(d) = Σ 1/(k + rank(d))` with k=60, then re-rank by combined score.

#### Scenario: RRF scores computed
- **WHEN** dense top-5 and BM25 top-5 ranked lists are available for a query
- **THEN** each unique chunk SHALL receive an RRF score and the merged list SHALL be re-sorted descending

### Requirement: Hybrid top-5 retrieval with latency
The system SHALL return top-5 chunks from the RRF-merged list and record total hybrid retrieval latency (dense + BM25 + fusion time).

#### Scenario: Hybrid results returned
- **WHEN** a query is processed through hybrid retrieval
- **THEN** exactly 5 chunks SHALL be returned with their RRF scores

### Requirement: Benchmark comparison table
The system SHALL display a table comparing Dense, Sparse, and Hybrid across: Avg Query Latency (ms), Top-1 Relevance (avg 1–3), Top-3 Coverage for all 10 queries.

#### Scenario: Benchmark table filled
- **WHEN** all 10 queries are run through all 3 retrievers
- **THEN** the 3×3 benchmark table SHALL be fully populated with numeric values
