# Assignment 2B — RAG Pipeline: Project Rules

## Core Rule: Everything Goes Through OpenSpec

Do NOT write or edit notebook code unless it implements a task marked `[ ]` or `[~]` in
`openspec/changes/assignment-2b-rag-pipeline/tasks.md`. No undocumented quick fixes.

## Workflow

1. **Before starting any new task group: run `/opsx:explore` first.** Think through best practices, pitfalls, and tradeoffs. No coding until explore is complete.
2. Mark task `[~]` (in-progress) before editing any file
3. Complete the 7-step checklist before moving to the next task (see below)

## 8-Step Task Completion Checklist

Before marking any task `[x]` and moving on:

- [ ] Run the relevant notebook cell(s) and verify output
- [ ] Mark task complete in tasks.md (`[ ]` → `[x]`)
- [ ] Append any non-trivial fix to `LESSONS_LEARNED.md`
- [ ] Append any useful command to `TOI.md`
- [ ] Record any design decision made to `design.md`
- [ ] Update `SESSION_HANDOFF.md` — progress count, what's done, what's next
- [ ] Git commit with a clear message
- [ ] Verify commit landed (`git log --oneline -1`)

## Documentation Rules

- **LESSONS_LEARNED.md** — append immediately after any non-trivial problem is solved; do not wait to be asked
- **TOI.md** — append any useful command or trick discovered during implementation
- **design.md** — record any decision made during implementation that wasn't in the original design

## Code Quality

- Every significant code block in the notebook must have a plain English markdown cell above it explaining what it does and why
- All output cells must be populated before submission (run all cells top to bottom)
- Final notebook must export cleanly to HTML

## Submission Checklist

- [ ] `assignment_2b_rag_pipeline.ipynb` — all cells executed, outputs visible
- [ ] `assignment_2b_rag_pipeline.html` — exported via `jupyter nbconvert`
- [ ] `tables_chunks.csv` — serialised table rows present
- [ ] All assignment tables filled (A2, B2, C1 metrics, C2 demo)
