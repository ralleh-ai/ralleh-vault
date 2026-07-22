# Ralleh Vault

Local-first, plain-Markdown company memory for OpenClaw.

Ralleh Vault turns scattered notes, transcripts, and research into durable, linked, cited knowledge that both humans and agents can trust.

---

## Why this exists

Most teams lose decisions and context because knowledge is split across chats, docs, and memory.

Ralleh Vault solves this with:
- **Markdown as source of truth** (portable, inspectable, Git-friendly)
- **strict provenance** (`sources` are required on canonical notes)
- **graph discipline** (`[[wikilinks]]`, MOCs, index + log)
- **two-agent operating model** optimized for both throughput and quality

---

## Core operating model

### Agents

- **VAULT** (`agents/roles/vault`)  
  Deep synthesis + final crystallization quality.
- **VAULT-FAST** (`agents/roles/vault-fast`)  
  High-volume inbox triage, templating, and normalization.

### Workflow

1. **Capture** → land signals in `Inbox/` or immutable `raw/`
2. **Process (VAULT-FAST)** → classify, template, draft, escalate ambiguity
3. **Crystallize (VAULT)** → resolve conflicts, create canonical notes, update graph
4. **Validate** → run doctor checks and keep `Inbox/` healthy

---

## Repository layout

```text
ralleh-vault/
├── skills/vault/                # Skill contract, runbooks, templates, schema, doctor
├── agents/roles/vault/          # Deep knowledge role package
├── agents/roles/vault-fast/     # Fast processing role package
├── scaffold/vault/              # Drop-in canonical vault folder scaffold
├── tests/                       # Doctor test suite + fixtures
├── docs/                        # Migration, policy, FAQ, operating guidance
├── .github/workflows/           # CI validation
└── Makefile                     # Local validation commands
```

---

## Quickstart (5 minutes)

### 1) Copy scaffold into your OpenClaw workspace

```bash
cp -R scaffold/vault /path/to/workspace/vault
```

### 2) Validate scaffold quality

```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root /path/to/workspace/vault --strict
```

### 3) Start the operating loop

- Put fresh material in `vault/Inbox/` and `vault/raw/`
- Run `vault.process` with VAULT-FAST
- Run `vault.crystallize` with VAULT
- Keep `vault/wiki/index.md` and `vault/wiki/log.md` current

---

## Non-negotiable standards

1. **Never edit files in `raw/` after ingest**
2. **Durable knowledge lives in `wiki/`**
3. **Canonical `wiki/` notes require valid frontmatter**
4. **Decisions/Procedures (active/stable) require approval block**
5. **No silent cross-client blending**
6. **Doctor gates must pass before release merges**

Frontmatter schema: `skills/vault/schemas/frontmatter.md`  
Primary skill contract: `skills/vault/SKILL.md`

---

## Validation and quality gates

### Local

```bash
make test
make doctor
make doctor-strict
make validate
```

### CI

GitHub Actions workflow: `.github/workflows/validate-vault.yml`
- runs unit tests
- runs strict doctor
- Python matrix: 3.10 / 3.11 / 3.12

### What doctor enforces

- required vault structure (`wiki/`, `raw/`, index/log)
- frontmatter presence + required fields
- field format/value checks (`date`, `type`, `status`, `confidence`)
- broken wikilinks
- inbox staleness thresholds
- log freshness signal
- approval-gate compliance for active/stable decisions/procedures

---

## Documentation index

- `docs/migration-guide.md` — move ad-hoc notes into Vault safely
- `docs/client-scoping.md` — single-root vs multi-client boundary model
- `docs/git-policy.md` — branch and commit conventions
- `docs/e2e-inbox-handoff-crystallize.md` — full operational scenario
- `docs/faq.md` — operational FAQ
- `docs/engineering-principles.md` — design posture
- `docs/phase-3-release-checklist.md` — release hardening checklist

---

## Design posture (Carmack-leaning)

- Keep systems **simple and inspectable**
- Prefer **deterministic checks** over vague quality claims
- Expose state and quality with measurable outputs
- Build fast local feedback loops (tests + doctor)
- Avoid unnecessary runtime dependencies

See `docs/engineering-principles.md`.

---

## Current maturity

- ✅ Skill + role packages scaffolded
- ✅ Validation tooling with fixtures and CI matrix
- ✅ Migration, FAQ, and end-to-end docs
- ✅ Release checklist baseline

Next hardening targets are tracked in `docs/phase-3-release-checklist.md`.

---

## Contributing

1. Create a focused branch (`feat/vault-*`, `fix/vault-*`, `docs/vault-*`)
2. Keep commits small and reviewable
3. Run `make validate`
4. Open PR with summary + validation output

Commit style examples:
- `feat(vault): ...`
- `fix(vault): ...`
- `docs(vault): ...`
- `test(vault): ...`

See `docs/git-policy.md`.
