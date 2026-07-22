# Ralleh Vault

A local-first, plain-Markdown knowledge system for OpenClaw.

Ralleh Vault turns scattered operational memory (chats, meetings, transcripts, docs, exports) into durable, linked, and cited knowledge that humans and agents can trust.

---

## Quick navigation

- [Why this skill exists](#why-this-skill-exists)
- [Benefits you get](#benefits-you-get)
- [Start here by role](#start-here-by-role)
- [How to utilize it day-to-day](#how-to-utilize-it-day-to-day)
- [How to integrate with OpenClaw](#how-to-integrate-with-openclaw)
- [How to feed it data](#how-to-feed-it-data)
- [How to validate quality](#how-to-validate-quality)
- [How to retrieve knowledge](#how-to-retrieve-knowledge)
- [Repository layout](#repository-layout)
- [Documentation map](#documentation-map)

---

## Why this skill exists

Most teams do not have a writing problem — they have a **knowledge reliability** problem.

Without a system, important context decays:
- decisions disappear into chat
- procedures drift into folklore
- source evidence gets lost
- retrieval depends on who remembers what

Ralleh Vault is built to stop this decay with a simple but strict model:
- immutable sources in `raw/`
- canonical knowledge in `wiki/`
- explicit provenance (`sources`)
- explicit relationships (`[[wikilinks]]`)
- deterministic quality checks (`vault_doctor.py`)

---

## Benefits you get

### Strategic
- **Institutional memory that survives people and tools**
- **Auditable decisions and procedures** (who/what/when traceability)
- **Reduced operational risk** from stale or conflicting knowledge

### Operational
- **Faster retrieval** via linked canonical notes
- **Higher throughput** with VAULT-FAST triage
- **Higher quality** with VAULT crystallization and approval gates
- **Release-grade confidence** from strict validation in CI

### Technical
- **No lock-in** (Markdown + folders + Git)
- **Low complexity** (inspectable filesystem model)
- **Automation-friendly** (deterministic script checks)

---

## Start here by role

### 1) Operator (I just need this working now)

1. Copy scaffold:
   ```bash
   cp -R scaffold/vault /path/to/workspace/vault
   ```
2. Validate:
   ```bash
   python3 skills/vault/scripts/vault_doctor.py --vault-root /path/to/workspace/vault --strict
   ```
3. Start feeding data into `vault/raw/` and `vault/Inbox/`.
4. Run `vault.process` (VAULT-FAST), then `vault.crystallize` (VAULT).

### 2) Team Lead (I need dependable memory for a team)

- Read: `docs/migration-guide.md`
- Set boundary model: `docs/client-scoping.md`
- Enforce Git policy: `docs/git-policy.md`
- Track operating loop: `docs/e2e-inbox-handoff-crystallize.md`

### 3) Agent Integrator (I need role orchestration)

- Install skill: `skills/vault/`
- Load roles:
  - `agents/roles/vault`
  - `agents/roles/vault-fast`
- Follow integration choreography: `docs/integration-guide.md`

---

## How to utilize it day-to-day

Ralleh Vault runs as a repeatable loop:

1. **Capture**
   - Land source artifacts into `vault/raw/*`
   - Land transient triage notes into `vault/Inbox/*`

2. **Process (VAULT-FAST)**
   - classify and normalize quickly
   - generate draft canonical candidates
   - escalate ambiguity and high-risk items

3. **Crystallize (VAULT)**
   - resolve conflicts across sources
   - produce canonical notes under `vault/wiki/*`
   - update `wiki/index.md` and append `wiki/log.md`

4. **Retrieve**
   - query canonical notes first
   - answer with concise output + explicit citations

5. **Maintain + Validate**
   - keep Inbox age controlled
   - fix graph drift and run strict doctor

---

## How to integrate with OpenClaw

### Components

- Skill package: `skills/vault/`
- Role package (judgment): `agents/roles/vault/`
- Role package (throughput): `agents/roles/vault-fast/`
- Data root: `vault/` (from `scaffold/vault/`)

### Capability map

- `vault.capture`
- `vault.process`
- `vault.crystallize`
- `vault.query` / `vault.retrieve`
- `vault.maintain`
- `vault.status`

Primary contract: `skills/vault/SKILL.md`  
Integration details: `docs/integration-guide.md`

---

## How to feed it data

### Immutable source ingestion (`raw/`)

Use buckets:
- `vault/raw/transcripts/`
- `vault/raw/documents/`
- `vault/raw/research/`
- `vault/raw/exports/`

Rules:
- do not rewrite originals after ingest
- keep filenames stable and traceable
- cite source paths in canonical note `sources`

### Mutable triage inputs (`Inbox/`)

Use `vault/Inbox/` for:
- meeting takeaways
- unresolved notes
- draft findings awaiting synthesis

Ingestion details and conventions: `docs/data-ingestion.md`

---

## How to validate quality

### Local

```bash
make test
make doctor
make doctor-strict
make validate
```

### CI

Workflow: `.github/workflows/validate-vault.yml`
- unit tests
- strict doctor checks
- Python matrix: 3.10 / 3.11 / 3.12

### Doctor enforces

- required vault structure (`wiki/`, `raw/`, index/log)
- frontmatter completeness + schema constraints
- valid enums (`type`, `status`, `confidence`) and dates
- wikilink integrity (no broken internal links)
- Inbox staleness threshold
- log freshness signal
- approval-gate compliance for active/stable decision/procedure notes

---

## How to retrieve knowledge

Retrieval contract:
1. search canonical `wiki/` first
2. expand via `related` links
3. pull `raw/` only when canonical coverage is weak
4. return answer + citations + confidence

Retrieval docs:
- runbook: `skills/vault/runbooks/query.md`
- examples: `skills/vault/examples/agent-call-examples.md`
- guide: `docs/retrieval-guide.md`

---

## Non-negotiable standards

1. Never edit `raw/` files after ingest.
2. Durable canonical knowledge lives in `wiki/`.
3. Canonical notes require valid frontmatter.
4. Active/stable decisions and procedures require approval metadata.
5. No cross-client blending without explicit approval.
6. Strict validation must pass for release-quality merges.

Schema: `skills/vault/schemas/frontmatter.md`

---

## Repository layout

```text
ralleh-vault/
├── skills/vault/                # Skill contract, runbooks, templates, schema, doctor
├── agents/roles/vault/          # VAULT role (high-judgment crystallization)
├── agents/roles/vault-fast/     # VAULT-FAST role (high-throughput processing)
├── scaffold/vault/              # Drop-in canonical vault scaffold
├── tests/                       # Doctor tests + fixtures
├── docs/                        # Migration, integration, ingestion, retrieval
├── .github/workflows/           # CI quality gates
└── Makefile                     # Local validation shortcuts
```

---

## Documentation map

- `docs/getting-started.md` — first-day rollout checklist
- `docs/migration-guide.md` — migrate ad-hoc notes safely
- `docs/integration-guide.md` — OpenClaw integration choreography
- `docs/data-ingestion.md` — ingestion model, naming, anti-patterns
- `docs/retrieval-guide.md` — retrieval output contract and confidence
- `docs/client-scoping.md` — tenant boundary strategy
- `docs/e2e-inbox-handoff-crystallize.md` — full operating scenario
- `docs/git-policy.md` — branch and commit rules
- `docs/faq.md` — practical Q&A
- `docs/engineering-principles.md` — Carmack-leaning design posture
- `docs/phase-3-release-checklist.md` — release hardening checklist

---

## Design posture

This repository favors:
- simple and inspectable architecture
- deterministic checks over subjective quality claims
- measurable operational signals
- short, reliable feedback loops
- minimal dependencies

See `docs/engineering-principles.md`.

---

## Contributing

1. Create a branch (`feat/vault-*`, `fix/vault-*`, `docs/vault-*`)
2. Keep commits focused and reviewable
3. Run `make validate`
4. Include validation output in PR summary

Commit style:
- `feat(vault): ...`
- `fix(vault): ...`
- `docs(vault): ...`
- `test(vault): ...`

Git policy: `docs/git-policy.md`
