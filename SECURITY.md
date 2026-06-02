# Security Policy

## Scope

This repository contains public-safe templates, documentation, and lightweight local audit scripts. It does not require API keys and should not contain secrets, private task logs, customer data, credentials, session files, recordings, screenshots, or private agent memory.

## Reporting security issues

If you find a security issue, please avoid posting sensitive details in a public issue. Use the contact routes listed in the repository README or open a minimal issue that does not include secrets.

## Sensitive data boundary

Do not commit:

- `.env` files;
- API keys or OAuth tokens;
- browser profiles, cookies, auth stores, or session files;
- raw private transcripts, recordings, screenshots, or meeting outputs;
- local operator paths;
- customer/client confidential data;
- private agent memory or internal task boards.

Run before publishing changes:

```bash
agent-team-reliability scan-repo .
```

The scanner is a guardrail, not a guarantee. Manual review is still required before publishing public repositories.
