# Ralleh Vault Skill

Ralleh Vault is a local-first, plain-Markdown second brain for OpenClaw teams and agents.

## What this package contains

- `SKILL.md` — canonical operating contract.
- `schemas/frontmatter.md` — required note metadata.
- `templates/` — note templates by type.
- `runbooks/` — procedural playbooks for capture/process/crystallize/query/maintain.
- `examples/` — usage snippets.
- `scripts/vault_doctor.py` — health and consistency checks.

## Design commitments

- Markdown on disk is source of truth.
- `raw/` is immutable.
- Durable knowledge belongs in `wiki/`.
- Provenance and links are first-class.
- VAULT + VAULT-FAST split throughput from judgment.

## Quick start

1. Scaffold vault root using `vault/` layout in this workspace.
2. Start capture into `Inbox/` and `raw/`.
3. Run processing with VAULT-FAST.
4. Run crystallization with VAULT.
5. Run doctor checks regularly:

```bash
python ralleh-skills/skills/vault/scripts/vault_doctor.py --vault-root vault
```
