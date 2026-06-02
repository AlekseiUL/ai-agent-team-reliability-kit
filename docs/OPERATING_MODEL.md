# Operating Model

Use this kit when an AI task is durable, multi-step, cross-agent, or capable of side effects.

## Roles

- **Coordinator** — accepts the human goal, creates task contracts, routes work, and synthesizes the final result.
- **Specialist worker** — executes one bounded task in its lane.
- **Reviewer / verifier** — checks output before it is called done.
- **Human owner** — approves irreversible or external side effects.

## Basic flow

```text
Goal -> Coordinator -> Task Contract -> Specialist -> Verification -> Done/Blocked -> Memory/Wiki/Report decision
```

## Default rule

If the next step can be fully prewritten, use a script or deterministic workflow.
If the next step depends on discovered evidence, use an agent task.

## Do not let every agent dispatch

A team needs one coordination surface. Multiple dispatchers can create races, duplicate work, and unclear ownership.

Recommended shape:

```text
one coordinator/dispatcher
many specialist workers
clear task contracts
```
