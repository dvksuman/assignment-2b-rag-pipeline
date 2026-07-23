## ADDED Requirements

### Requirement: Fixed-size chunking
The system SHALL split the corpus into non-overlapping chunks of exactly max_tokens=200 words, with no sentence boundary preservation.

#### Scenario: Fixed-size chunks produced
- **WHEN** fixed-size chunking is applied to the corpus
- **THEN** all chunks SHALL have ≤200 words and total chunks × avg size ≈ total corpus words

### Requirement: Sliding window chunking
The system SHALL split the corpus using a sliding window of max_tokens=200 words with 10% overlap (20 words).

#### Scenario: Sliding window overlap verified
- **WHEN** sliding window chunking is applied
- **THEN** consecutive chunks SHALL share the last 20 words of the previous chunk as their first 20 words

### Requirement: Semantic chunking
The system SHALL split the corpus at sentence boundaries, grouping sentences until the 200-word limit is reached, never breaking mid-sentence.

#### Scenario: No broken sentences
- **WHEN** semantic chunking is applied
- **THEN** broken sentences percentage SHALL be 0% (every chunk starts and ends at a sentence boundary)

### Requirement: Chunking quality metrics table
The system SHALL compute and display a table with: Total Chunks, Avg Chunk Size (words), Std Dev Size, Broken Sentences (%) for each strategy.

#### Scenario: Metrics table populated
- **WHEN** all three strategies have been applied
- **THEN** a metrics table SHALL be displayed with all 4 columns filled for each of the 3 strategies
