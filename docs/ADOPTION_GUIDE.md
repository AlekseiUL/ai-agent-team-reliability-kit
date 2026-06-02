# Adoption Guide

Use this guide to add the reliability layer to an existing AI agent workflow in about 30 minutes.

## 0. Pick the coordination surface (5 minutes)

Use whatever your team already has:

- Hermes Kanban;
- GitHub Issues / Projects;
- Linear, Trello, Notion, or a local Markdown board;
- a custom queue, MCP server, or scheduler.

This kit does not require a specific board. It requires a task contract.

## 1. Define roles (5 minutes)

Start small:

```text
Coordinator: receives the human goal, creates bounded tasks, routes work, owns final synthesis.
Researcher: collects sources and evidence.
Builder: edits code, scripts, docs, or automations.
Reviewer: checks output and blocks on missing proof.
Writer: turns verified facts into user-facing output.
```

Copy and adapt:

```text
templates/specialist-roster.md
```

## 2. Make every durable task use the contract (10 minutes)

Copy:

```text
templates/task-contract.md
```

Minimum fields:

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

If a task is missing those fields, it is not ready for autonomous execution.

## 3. Add the approval boundary (5 minutes)

Decide which actions require explicit human approval.

Recommended default:

```text
Local reads and safe local edits are allowed inside Allowed paths.
No public posting, sending, publishing, deletion, billing, credential access, or live config changes without explicit approval.
```

## 4. Require proof before done (3 minutes)

Every task must close with:

```text
Outcome:
Artifacts:
Verification:
Follow-up:
Memory/Wiki candidate:
```

Copy:

```text
templates/done-summary.md
```

## 5. Treat blocked as a success state (2 minutes)

If context, access, or approval is missing, the agent should block instead of guessing.

Copy:

```text
templates/blocked-report.md
```

## 6. Decide where knowledge goes (3 minutes)

Do not dump everything into memory.

Use:

```text
templates/memory-wiki-report-decision.md
```

Default rule:

```text
Task progress -> task board
Dated evidence -> reports
Durable operating rules -> wiki/docs
Short stable correction -> memory
Raw logs/secrets/private data -> nowhere
```

## 7. Add the CLI checks (5 minutes)

Install:

```bash
python -m pip install -e .
```

Run:

```bash
agent-team-reliability audit-tasks path/to/tasks
agent-team-reliability scan-repo path/to/public/repo
```

## 8. Start with one workflow

Good first adoption targets:

- public GitHub release review;
- coding-agent task handoff;
- research brief with evidence grading;
- content/report pipeline;
- local automation with side effects.

See:

```text
examples/scenarios/
```

## 9. Keep it small

Do not start by building a new platform. Start by making one real task safe, bounded, and verifiable.
