# Public Release Task

Owner: release-reviewer
Goal: Verify the repository is safe to publish publicly.
Context: This is a public GitHub product release gate.
Allowed paths: repository root
Forbidden paths: .env, auth stores, browser profiles, cookies, private transcripts, recordings, screenshots outside docs/assets
Privacy level: public-safe
External side-effect policy: No push, tag, package publish, or public posting until verification passes and approval is explicit.
Verification required: tests pass, repository scan returns ok, README/LICENSE/NOTICE/SECURITY exist, git status reviewed.
Expected final summary/report: checks run, findings, release readiness verdict, remaining risks.
