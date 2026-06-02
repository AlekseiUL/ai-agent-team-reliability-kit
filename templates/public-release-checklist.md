# Public Release Checklist

Project:
Repository:
Privacy level: public-safe
External side-effect policy:

## Required files

- [ ] README.md
- [ ] LICENSE
- [ ] NOTICE.md
- [ ] SECURITY.md

## Checks

- [ ] Tests / offline checks pass
- [ ] `agent-team-reliability scan-repo .` returns ok
- [ ] No secrets or auth stores
- [ ] No private local paths
- [ ] No runtime media outside public assets
- [ ] No generated cache/bytecode
- [ ] Canonical source link present
- [ ] Attribution present
- [ ] Release notes prepared if publishing a tag

## Verification output

Commands run:
Results:
Remaining risks:
