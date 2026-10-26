# Offline verification boundary

Require exact exit=1 and the complete known bad-task receipt, instead of swallowing every error.

## Reproduce

`python scripts/check_audit_fixture.py; python -m pytest`

Unexpected exit codes, invalid JSON, missing or extra findings fail the CI gate.

## Rollback

Review the commit diff and use a new checkout of the pre-change commit for source rollback. Keep user data and live installations untouched. A source rollback is not permission to restore unsafe network exposure or bypass approval.
