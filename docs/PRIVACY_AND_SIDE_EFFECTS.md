# Privacy and Side Effects

Agents fail dangerously when they are allowed to act without a boundary.

## Privacy levels

Adapt these names to your system:

- `public-safe` — safe for public GitHub/docs.
- `team-private` — internal team context, not public.
- `client-confidential` — private customer/client data.
- `finance-private` — money, billing, subscriptions, bank data.
- `personal-private` — personal, emotional, medical, or sensitive material.

## Side-effect policy examples

```text
No external side effects. Read-only inspection only.
```

```text
Local file edits allowed inside Allowed paths. No push/publish/send/delete without approval.
```

```text
GitHub push approved to this repository only after tests and privacy scan pass.
```

## Actions that should require explicit approval

- deletion/removal/pruning of user data;
- public posting or sending from a user's account;
- payment, purchase, billing, subscriptions;
- live service restarts or config changes;
- publishing to GitHub/package registries;
- credentials, secrets, OAuth, session files;
- irreversible migrations.
