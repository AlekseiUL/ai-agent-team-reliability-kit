# Scenario: Multi-Agent Research Brief

Use this scenario when several agents collect sources and one agent synthesizes the result.

## Roles

```text
Coordinator: splits the question into angles and owns final answer.
Researcher A/B/C: collect sources for separate angles.
Reviewer: checks source quality and unsupported claims.
Writer: creates the final brief from verified evidence.
```

## Flow

```text
Question
  -> coordinator creates source-gathering tasks
  -> researchers return evidence ledgers
  -> reviewer blocks weak or uncited claims
  -> writer produces final brief
  -> coordinator sends final result
```

## Researcher task contract

```text
Owner: researcher
Goal: Collect evidence for one clearly scoped angle.
Context: Include the exact question, time horizon, geography, and excluded sources.
Allowed paths: research workspace and public web sources.
Forbidden paths: private messages, private customer data, credentials, unrelated local files.
Privacy level: public-safe or team-private, depending on topic.
External side-effect policy: Read-only source collection. No posting, messaging, signups, or account actions.
Verification required: source list with URLs, claim-to-source mapping, uncertainty and gaps.
Expected final summary/report: top findings, evidence ledger, weak signals, risks, open questions.
```

## Reviewer checklist

- Does every major claim have a source?
- Are dates current enough for the question?
- Are source types mixed instead of one-source monoculture?
- Are weak signals labeled as weak?
- Are recommendations separated from evidence?
- Are private or confidential sources excluded?

## Done summary shape

```text
Outcome: Research angle completed / blocked.
Artifacts: report path or source ledger.
Verification: sources checked, claims mapped, gaps stated.
Follow-up: what the writer/coordinator should do next.
Memory/Wiki candidate: only if this changes a durable research workflow.
```
