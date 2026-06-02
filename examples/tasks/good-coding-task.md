# Good Coding Task

Owner: builder
Goal: Add an offline CLI smoke test for the package entrypoint.
Context: The repository already has a Python package and pytest tests.
Allowed paths: src/, tests/, pyproject.toml
Forbidden paths: .env, auth files, user home directories, generated build artifacts
Privacy level: public-safe
External side-effect policy: Local edits only. No push or publish.
Verification required: pytest passes and CLI `--help` exits 0.
Expected final summary/report: changed files, commands run, test result, follow-up risks.
