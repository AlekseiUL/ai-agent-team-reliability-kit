# Task Contract

A task contract is the minimum safe packet of work an agent can execute.

Required fields:

```text
Owner:
Goal:
Context:
Allowed paths:
Forbidden paths:
Privacy level:
External side-effect policy:
Verification required:
Expected final summary/report:
```

## Why these fields matter

- **Owner** prevents orphan tasks.
- **Goal** prevents vague execution.
- **Context** avoids forcing the worker to guess.
- **Allowed paths** keeps work scoped.
- **Forbidden paths** protects secrets and private data.
- **Privacy level** controls how much detail can be shared.
- **External side-effect policy** prevents surprise sends, pushes, deletes, purchases, or live config changes.
- **Verification required** defines what “done” means.
- **Expected final summary/report** makes handoff readable.
