#!/usr/bin/env python3
"""
Stop hook for Assignment 2B.
Reminds about the 7-step post-task checklist when the session ends.
"""

import os

PROJECT_ROOT = "/Users/dvksuman/Desktop/Semester3/LLM/ASSIGNMENT2"
TASKS_FILE = os.path.join(PROJECT_ROOT, "openspec/changes/assignment-2b-rag-pipeline/tasks.md")


def count_tasks():
    if not os.path.exists(TASKS_FILE):
        return 0, 0, 0
    total = done = in_progress = 0
    with open(TASKS_FILE) as f:
        for line in f:
            if "- [ ]" in line:
                total += 1
            elif "- [x]" in line:
                total += 1
                done += 1
            elif "- [~]" in line:
                total += 1
                in_progress += 1
    return total, done, in_progress


total, done, in_progress = count_tasks()
remaining = total - done - in_progress

print("\n" + "=" * 55)
print("  POST-TASK CHECKLIST — Assignment 2B")
print("=" * 55)
print(f"  Tasks: {done}/{total} complete | {in_progress} in-progress | {remaining} remaining")
print()
print("  Before closing, verify:")
print("  [ ] Notebook cells run and outputs visible")
print("  [ ] tasks.md updated ([ ] → [x])")
print("  [ ] LESSONS_LEARNED.md updated")
print("  [ ] TOI.md updated")
print("  [ ] design.md updated (if decisions made)")
print("  [ ] git commit done")
print("  [ ] git log --oneline -1 verified")
print("=" * 55 + "\n")
