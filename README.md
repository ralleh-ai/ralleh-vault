# Ralleh Vault

A local-first, plain-Markdown knowledge system for OpenClaw.

Ralleh Vault converts scattered operational memory (chats, meeting notes, transcripts, docs, exports) into trusted, durable knowledge that agents and humans can retrieve quickly with provenance.

---

## Why use this skill

### The problem it solves

Teams usually lose context in five ways:
1. Decisions are buried in chat.
2. Procedures drift and become folklore.
3. Raw source files and polished docs are mixed together.
4. Knowledge quality is hard to measure.
5. Retrieval is slow and confidence is unknown.

### What Ralleh Vault gives you

- **Durable memory**: canonical notes live in `wiki/`, not ephemeral chat.
- **Auditability**: canonical notes require `sources`; raw provenance is preserved.
- **Faster answers**: retrieval works from a linked knowledge graph.
- **Quality gates**: `vault_doctor.py` catches structural drift early.
- **Operational scale**: two-agent split (VAULT-FAST + VAULT) separates throughput from judgment.
- **No platform lock-in**: Markdown + folders + Git.

If you want reliable institutional memory without adding a heavy database product, this is the sweet spot.

---

## What this repository contains

```text
ralleh-vault/
├── skills/vault/                # Skill contract, runbooks, templates, schema, doctor
├── agents/roles/vault/          # VAULT role (high-judgment crystallization)
├── agents/roles/vault-fast/     # VAULT-FAST role (high-throughput processing)
├── scaffold/vault/              # Drop-in canonical vault folder scaffold
├── tests/                       # Doctor tests + fixtures
├── docs/                        # Operating docs (migration, integration, retrieval, etc.)
├── .github/workflows/           # CI quality gates
└── Makefile                     # Local validation shortcuts
```

---

## How to utilize it (day-to-day)

Ralleh Vault runs as an operating loop:

1. **Capture**
   - Land source-of-truth artifacts into `vault/raw/*`.
   - Land transient triage notes into `vault/Inbox/*`.

2. **Process (VAULT-FAST)**
   - Triage high-volume items.
   - Normalize to templates.
   - Escalate ambiguity to VAULT.

3. **Crystallize (VAULT)**
   - Resolve ambiguity.
   - Produce canonical notes in `vault/wiki/*`.
   - Update `wiki/index.md` and `wiki/log.md`.

4. **Retrieve**
   - Query canonical notes first.
   - Return concise answers with citations.

5. **Maintain + Validate**
   - Keep Inbox trending to zero.
   - Run doctor checks continuously.

---

## Quickstart (5 minutes)

### 1) Install scaffold

```bash
cp -R scaffold/vault /path/to/workspace/vault
```

### 2) Validate baseline

```bash
python3 skills/vault/scripts/vault_doctor.py --vault-root /path/to/workspace/vault --strict
```

### 3) Start operating

- Feed new source material into `vault/raw/` and `vault/Inbox/`
- Run `vault.process` (VAULT-FAST)
- Run `vault.crystallize` (VAULT)
- Run `vault.retrieve` for answers with citations

---

## How to integrate with OpenClaw

### Integration model

- Install the Vault skill package from `skills/vault/`
- Use role packages:
  - `agents/roles/vault`
  - `agents/roles/vault-fast`
- Point both roles at the same vault root (or approved client-scoped roots)

### Capability map

- `vault.capture`
- `vault.process`
- `vault.crystallize`
- `vault.query` / `vault.retrieve`
- `vault.maintain`
- `vault.status`

Primary contract: `skills/vault/SKILL.md`

Detailed integration guidance: `docs/integration-guide.md`

---

## How to feed it data correctly

### Raw source ingestion (immutable)

Use `vault/raw/` buckets:
- `raw/transcripts/`
- `raw/documents/`
- `raw/research/`
- `raw/exports/`

Rules:
- Do not rewrite originals after ingest.
- Keep filenames stable and traceable.
- Record provenance in canonical note `sources`.

### Inbox triage inputs (mutable)

Use `vault/Inbox/` for:
- meeting takeaways
- unresolved ideas
- partial notes requiring processing

Detailed ingestion patterns: `docs/data-ingestion.md`

---

## How to validate quality

### Local commands

```bash
make test
make doctor
make doctor-strict
make validate
```

### CI gate

Workflow: `.github/workflows/validate-vault.yml`
- unit tests
- strict doctor
- Python matrix 3.10 / 3.11 / 3.12

### What validation enforces

- required vault structure and required files
- frontmatter completeness and schema values
- broken wikilinks
- stale Inbox detection
- log freshness checks
- approval-gate checks for active/stable decision/procedure notes

---

## How to retrieve knowledge

Retrieval strategy:
1. search canonical `wiki/` notes first
2. traverse `related` links for context expansion
3. pull raw sources only when canonical coverage is weak
4. return concise answers + explicit citations

Retrieval runbook: `skills/vault/runbooks/query.md`  
Retrieval examples: `skills/vault/examples/agent-call-examples.md`  
Deep retrieval guide: `docs/retrieval-guide.md`

---

## Non-negotiable standards

1. Never edit `raw/` files after ingest.
2. Canonical durable knowledge belongs in `wiki/`.
3. Canonical notes require valid frontmatter.
4. Active/stable decisions and procedures require approval section + approver.
5. No cross-client blending without explicit approval.
6. Strict validation must pass for release-quality merges.

Schema: `skills/vault/schemas/frontmatter.md`

---

## Documentation map

- `docs/migration-guide.md` — migrate ad-hoc notes safely
- `docs/integration-guide.md` — OpenClaw integration patterns
- `docs/data-ingestion.md` — how to feed source data and Inbox batches
- `docs/retrieval-guide.md` — retrieval patterns and citation formats
- `docs/client-scoping.md` — tenant boundary strategy
- `docs/e2e-inbox-handoff-crystallize.md` — end-to-end operational scenario
- `docs/git-policy.md` — Git conventions and safety
- `docs/faq.md` — practical Q&A
- `docs/engineering-principles.md` — Carmack-leaning design posture
- `docs/phase-3-release-checklist.md` — release hardening checklist

---

## Design posture

This project favors:
- simple and inspectable systems
- deterministic checks over vague quality claims
- measurable outputs
- fast validation loops
- minimal dependencies

See `docs/engineering-principles.md`.

---

## Contributing

1. Branch with `feat/vault-*`, `fix/vault-*`, or `docs/vault-*`
2. Keep commits focused and reviewable
3. Run `make validate`
4. Include validation output in PR summary

Commit style:
- `feat(vault): ...`
- `fix(vault): ...`
- `docs(vault): ...`
- `test(vault): ...`

Git policy: `docs/git-policy.md`
