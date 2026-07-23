## ADDED Requirements

### Requirement: Cross-encoder reranking stage
The system SHALL rerank the top-3 chunks from the best first-stage retriever using `cross-encoder/ms-marco-MiniLM-L-6-v2` and record reranking latency per query.

#### Scenario: Reranking applied
- **WHEN** top-3 chunks from the first-stage retriever are passed to the cross-encoder with the query
- **THEN** chunks SHALL be re-scored and re-sorted by cross-encoder logit score

### Requirement: Rank-change rate metric
The system SHALL compute the rank-change rate: percentage of queries where the top-1 result changes after reranking.

#### Scenario: Rank change rate computed
- **WHEN** reranking is applied to 10 queries
- **THEN** rank-change rate SHALL be reported as (queries where rank-1 changed / 10) × 100%

### Requirement: Manual relevance verification
The system SHALL manually verify top-1 relevance before and after reranking for 5 queries and report whether reranking improved, maintained, or reduced relevance.

#### Scenario: Verification table shown
- **WHEN** 5 queries are manually verified
- **THEN** a table SHALL show: query, pre-rerank top-1, post-rerank top-1, relevance change (improved/same/worse)
