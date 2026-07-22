# ralleh-vault

Ralleh Vault is a production-focused, local-first Markdown knowledge vault for OpenClaw.

It ships:
- `skills/vault` — vault skill package
- `agents/roles/vault` — deep synthesis role (VAULT)
- `agents/roles/vault-fast` — throughput role (VAULT-FAST)
- `scaffold/vault` — canonical vault folder scaffold

## Quickstart

```bash
cp -R scaffold/vault /path/to/workspace/vault
python3 skills/vault/scripts/vault_doctor.py --vault-root /path/to/workspace/vault
```

## Phase 2 hardening included

- Stricter doctor checks
- Client-scoped root conventions
- Git workflow policy and commit templates
- Cross-agent integration examples

## Local validation commands

```bash
make test
make doctor
make doctor-strict
make validate
```

## Engineering style

See `docs/engineering-principles.md` for the practical design posture used in this repo.
