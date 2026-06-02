# Scenario: Public GitHub Release Gate

Use this scenario when an agent team prepares a public repository for release.

## Roles

```text
Coordinator: defines release scope and approval boundary.
Builder: updates docs, tests, metadata, and packaging.
Reviewer: checks privacy, quality, claims, and install path.
Human owner: approves push, release, or package publication.
```

## Task contract

```text
Owner: release-reviewer
Goal: Verify the repository is safe and useful enough to publish.
Context: Public product repository; release candidate is staged locally.
Allowed paths: repository root and temporary directories for fresh clone/install smoke.
Forbidden paths: .env, auth stores, browser profiles, cookies, recordings, transcripts, screenshots outside docs/assets, private task logs.
Privacy level: public-safe.
External side-effect policy: Read-only verification. No push, tag, package publish, or public posting without explicit approval.
Verification required: tests pass, repository scan returns ok, README/NOTICE/SECURITY/LICENSE exist, install or CLI smoke passes, final git status reviewed.
Expected final summary/report: RELEASE YES/NO, blockers, commands run, residual risks.
```

## Verification commands

```bash
python scripts/repository_quality.py
python -m pytest -q
agent-team-reliability scan-repo .
git diff --check
git status --short
```

Optional fresh clone smoke for an already-pushed branch or tag:

```bash
tmp=$(mktemp -d)
git clone https://github.com/OWNER/REPO "$tmp/repo"
python -m venv "$tmp/venv"
"$tmp/venv/bin/python" -m pip install -e "$tmp/repo"
"$tmp/venv/bin/<cli-name>" --help
```

## Done summary shape

```text
Outcome: RELEASE YES / RELEASE NO.
Artifacts: repository URL, release URL, commit hash.
Verification: commands and results.
Follow-up: non-blocking polish or explicit blockers.
Memory/Wiki candidate: usually no; release verification is dated task state.
```
