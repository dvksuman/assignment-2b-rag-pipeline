#!/usr/bin/env python3
"""
PreToolUse hook for Assignment 2B.

Gate 1 (Write/Edit/NotebookEdit): Blocks edits to the main notebook unless
a task marked [~] exists in tasks.md.

Gate 2 (Bash): Blocks git commit if LESSONS_LEARNED.md or TOI.md haven't
been updated more recently than the notebook.
"""

import json
import sys
import os
import glob

PROJECT_ROOT = "/Users/dvksuman/Desktop/Semester3/LLM/ASSIGNMENT2"
TASKS_FILE = os.path.join(PROJECT_ROOT, "openspec/changes/assignment-2b-rag-pipeline/tasks.md")
LESSONS_FILE = os.path.join(PROJECT_ROOT, "LESSONS_LEARNED.md")
TOI_FILE = os.path.join(PROJECT_ROOT, "TOI.md")
NOTEBOOK = os.path.join(PROJECT_ROOT, "assignment_2b_rag_pipeline.ipynb")


def has_in_progress_task():
    """Check if any task is marked [~] in tasks.md."""
    if not os.path.exists(TASKS_FILE):
        return True  # fail open if file missing
    with open(TASKS_FILE) as f:
        return "[~]" in f.read()


def docs_updated_after_notebook():
    """Check that LESSONS_LEARNED and TOI were modified after the notebook."""
    if not os.path.exists(NOTEBOOK):
        return True  # notebook doesn't exist yet, no gate needed
    nb_mtime = os.path.getmtime(NOTEBOOK)
    ll_mtime = os.path.getmtime(LESSONS_FILE) if os.path.exists(LESSONS_FILE) else 0
    toi_mtime = os.path.getmtime(TOI_FILE) if os.path.exists(TOI_FILE) else 0
    return ll_mtime >= nb_mtime and toi_mtime >= nb_mtime


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # fail open

    tool = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    # Gate 1: notebook edits require an in-progress task
    if tool in ("Write", "Edit", "NotebookEdit"):
        file_path = tool_input.get("file_path", "")
        if "assignment_2b_rag_pipeline" in file_path or file_path.endswith(".ipynb"):
            if not has_in_progress_task():
                print(
                    "BLOCKED: No task marked [~] in tasks.md.\n"
                    "Mark a task as in-progress before editing the notebook:\n"
                    f"  {TASKS_FILE}\n"
                    "Change '- [ ]' to '- [~]' for the task you are working on.",
                    file=sys.stderr,
                )
                sys.exit(2)

    # Gate 2: git commit requires docs updated after notebook
    if tool == "Bash":
        command = tool_input.get("command", "")
        if "git commit" in command:
            if not docs_updated_after_notebook():
                print(
                    "BLOCKED: git commit requires LESSONS_LEARNED.md and TOI.md\n"
                    "to be updated after the last notebook change.\n"
                    "Update both files first, then commit.",
                    file=sys.stderr,
                )
                sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
