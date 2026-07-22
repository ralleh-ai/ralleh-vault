# Git workflow policy

## Branching

- `main` is always releasable.
- Feature branches:
  - `feat/vault-*`
  - `fix/vault-*`
  - `docs/vault-*`

## Commit prefixes

- `feat(vault): ...`
- `fix(vault): ...`
- `docs(vault): ...`
- `chore(vault): ...`
- `refactor(vault): ...`
- `test(vault): ...`

## Safety

- Never force push protected branches.
- Never rewrite history for audit-critical note migrations.
- Prefer small, reviewable commits.
- Run doctor before commit.

## Suggested pre-commit gate

```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root scaffold/vault --strict
```
