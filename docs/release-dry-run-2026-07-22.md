# Release Dry Run Report — 2026-07-22

## Scope
Manual release operations validation before tagging initial release.

## A) Internal client dry run (single root)

Command:
```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root scaffold/vault --strict
```

Result:
- status: `ok`
- strict validation passed

Additional gate:
```bash
python3 scripts/audit_roles.py
```
- VAULT verdict: `golden`
- VAULT-FAST verdict: `golden`

## B) Multi-client simulation dry run

Setup:
- cloned scaffold into:
  - `/tmp/rv-dryrun/multi/vault/clients/acme`
  - `/tmp/rv-dryrun/multi/vault/clients/zenith`

Commands:
```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root /tmp/rv-dryrun/multi/vault/clients/acme --strict
python3 skills/vault/scripts/vault_doctor.py --vault-root /tmp/rv-dryrun/multi/vault/clients/zenith --strict
```

Results:
- acme: `status: ok`
- zenith: `status: ok`

## C) Blockers found

- None in runtime validation gates.

## D) Follow-up release ops

- CI status check `validate-vault` passing on latest `main` commit.
- Branch protection/rulesets API unavailable on current GitHub plan for this private repo (GitHub returns 403 upgrade-required for protection endpoints).
- Release tag and GitHub release can proceed.
\n## Appendix: command outputs
\n### internal_doctor.txt
vault_root: scaffold/vault
wiki_notes: 8
moc_files: 5
inbox_markdown_count: 0
raw_file_count: 1
log_freshness_days: 0
decision_procedure_active_or_stable_count: 0
decision_procedure_approval_failures: 0
checked_at: 2026-07-22T20:01:23.259182+00:00

status: ok
\n### internal_roles.txt
ROLE vault
  Verdict: golden
  README.md: 57 words
  SOUL.md: 130 words
  IDENTITY.md: 86 words
  AGENTS.md: 125 words
  TOOLS.md: 80 words
  DOCTOR.md: 123 words
  GUIDELINES.md: 66 words
  WORKFLOWS.md: 68 words
  MEMORY.md: 45 words
  USER.md: 38 words
  PATTERNS.md: 59 words
  OK
ROLE vault-fast
  Verdict: golden
  README.md: 41 words
  SOUL.md: 103 words
  IDENTITY.md: 80 words
  AGENTS.md: 116 words
  TOOLS.md: 78 words
  DOCTOR.md: 108 words
  GUIDELINES.md: 59 words
  WORKFLOWS.md: 56 words
  MEMORY.md: 36 words
  USER.md: 35 words
  PATTERNS.md: 58 words
  OK
\n### acme_doctor.txt
vault_root: /tmp/rv-dryrun/multi/vault/clients/acme
wiki_notes: 8
moc_files: 5
inbox_markdown_count: 0
raw_file_count: 1
log_freshness_days: 0
decision_procedure_active_or_stable_count: 0
decision_procedure_approval_failures: 0
checked_at: 2026-07-22T20:01:23.358806+00:00

status: ok
\n### zenith_doctor.txt
vault_root: /tmp/rv-dryrun/multi/vault/clients/zenith
wiki_notes: 8
moc_files: 5
inbox_markdown_count: 0
raw_file_count: 1
log_freshness_days: 0
decision_procedure_active_or_stable_count: 0
decision_procedure_approval_failures: 0
checked_at: 2026-07-22T20:01:23.398684+00:00

status: ok
