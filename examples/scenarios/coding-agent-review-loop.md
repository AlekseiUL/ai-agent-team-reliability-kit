# Scenario: Coding Agent Review Loop

Use this scenario when one agent implements and another verifies before merge or release.

## Roles

```text
Coordinator: defines scope, allowed paths, and merge/release boundary.
Builder: edits code only inside allowed paths.
Reviewer: checks diff, security, tests, and user-facing behavior.
Human owner: approves merge/push when required.
```

## Builder task contract

```text
Owner: builder
Goal: Implement one scoped change.
Context: Include the bug/feature, expected behavior, and relevant files.
Allowed paths: exact repo paths or worktree.
Forbidden paths: credentials, unrelated projects, generated caches, private data.
Privacy level: code-private or public-safe.
External side-effect policy: Local edits only. No push, merge, release, service restart, or destructive command without approval.
Verification required: targeted tests, lint/syntax check, manual smoke if applicable, git diff reviewed.
Expected final summary/report: changed files, test commands, result, residual risk.
```

## Reviewer task contract

```text
Owner: reviewer
Goal: Independently review the builder's diff.
Context: Include expected behavior and builder summary.
Allowed paths: repository/worktree and temporary test directories.
Forbidden paths: credentials, unrelated files, production data.
Privacy level: same as builder task.
External side-effect policy: Read-only unless explicitly asked to apply a fix. No push/merge.
Verification required: inspect diff, run tests if feasible, scan for secrets/path traversal/shell injection/unsafe side effects.
Expected final summary/report: APPROVE / BLOCK, findings, tests run, next action.
```

## Review checklist

- Does the diff match the task goal?
- Are there unrelated changes?
- Are secrets or private paths introduced?
- Are shell commands safe?
- Are file paths bounded?
- Do tests cover the changed behavior?
- Does `--help` or dry-run behavior avoid side effects?
- Is the final user-facing behavior clear?

## Done summary shape

```text
Outcome: APPROVE / BLOCK.
Artifacts: diff, commit, PR, or changed files.
Verification: commands and result.
Follow-up: fix list or merge/release recommendation.
Memory/Wiki candidate: only for reusable implementation lessons.
```
