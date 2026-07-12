## ADDED Requirements

### Requirement: PDF table extraction
The system SHALL extract at least 3 tables from domain PDFs using `pdfplumber` and save each as a CSV file.

#### Scenario: Tables extracted and saved
- **WHEN** pdfplumber processes domain PDFs
- **THEN** at least 3 tables with ≥2 columns and ≥2 rows SHALL be extracted and saved as CSV files

### Requirement: Row serialisation
The system SHALL serialise each table row as a text string in format: `Column1: val1 | Column2: val2 | ...` and store all serialised rows in `tables_chunks.csv`.

#### Scenario: Serialised rows in CSV
- **WHEN** all extracted tables are serialised
- **THEN** `tables_chunks.csv` SHALL contain one row per table row with the pipe-delimited text format

### Requirement: Tabular chunks indexed alongside text chunks
The system SHALL embed serialised table rows using the same embedder and add them to the FAISS index alongside text chunks.

#### Scenario: Mixed index contains tabular rows
- **WHEN** tabular serialised rows are embedded and added to the index
- **THEN** the index SHALL contain both text chunk vectors and table row vectors

### Requirement: Tabular query demonstration
The system SHALL demonstrate 3 structured queries where the top-1 retrieved result is a table row, showing the precise answer enabled by tabular indexing.

#### Scenario: Tabular queries answered precisely
- **WHEN** 3 structured queries (e.g., asking for specific values, counts, or comparisons) are run
- **THEN** at least one of the top-3 results SHALL be a serialised table row containing the answer

### Requirement: Tabular vs text-chunk analysis
The system SHALL include a 100-word written analysis of when tabular RAG outperforms text-chunk RAG, with at least one concrete example from the results.

#### Scenario: Written analysis present
- **WHEN** the notebook is complete
- **THEN** a markdown cell SHALL contain the ~100-word analysis with a specific query example
