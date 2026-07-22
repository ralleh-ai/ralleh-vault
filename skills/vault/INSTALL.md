# Vault Installation & Onboarding

## 1) Copy packages

- Skill package: `ralleh-skills/skills/vault`
- Agent roles:
  - `ralleh-agents/roles/vault`
  - `ralleh-agents/roles/vault-fast`
- Vault root scaffold: `vault/`

## 2) Configure agents

- `VAULT`: strong reasoning profile.
- `VAULT-FAST`: cheapest reliable instruction-following profile.

## 3) Connect workflow

- Route high-volume ingest and process tasks to VAULT-FAST.
- Route crystallization and strategic synthesis tasks to VAULT.

## 4) Git setup (recommended)

```bash
cd vault
git init
git add .
git commit -m "chore(vault): initialize scaffold"
```

## 5) Health check

```bash
python ../ralleh-skills/skills/vault/scripts/vault_doctor.py --vault-root .
```
