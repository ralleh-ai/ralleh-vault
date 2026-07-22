# Phase 3 Release Checklist — ralleh-vault

Use this checklist before the first public/internal release cut.

## 1) Architecture and contracts

- [ ] Confirm `skills/vault/SKILL.md` capability map matches implementation (`capture/process/crystallize/retrieve/maintain/status/promote`).
- [ ] Confirm approval gates are explicit and enforced in docs + runbooks.
- [ ] Confirm client boundary rules are explicit for multi-tenant roots.

## 2) Validation and CI quality

- [ ] `python3 skills/vault/scripts/vault_doctor.py --vault-root scaffold/vault --strict` passes.
- [ ] Add fixture vaults for failing cases (broken links, missing frontmatter, stale inbox, approval-gate missing).
- [ ] Add CI matrix for Python 3.10/3.11/3.12 for doctor script compatibility.

## 3) Security and data handling

- [ ] Confirm `raw/` immutability policy in all docs and role prompts.
- [ ] Confirm no secrets in scaffold/templates/examples.
- [ ] Confirm cross-client link policy requires explicit approval.

## 4) Agent operations

- [ ] Validate VAULT session-start ritual against expected workspace layout.
- [ ] Validate VAULT-FAST handoff packet format with at least 3 realistic samples.
- [ ] Add one end-to-end integration scenario: inbox batch → handoff → crystallization → index/log update.

## 5) Git and release hygiene

- [ ] Add `CHANGELOG.md` with initial release entry.
- [ ] Add semantic versioning policy (e.g., `v0.1.0` bootstrap).
- [ ] Confirm branch protection and required status check (`validate-vault`).

## 6) Documentation completeness

- [ ] Add root-level quickstart with copy/paste commands for OpenClaw workspace install.
- [ ] Add migration guide from ad-hoc notes to canonical vault layout.
- [ ] Add FAQ: wikilinks, approval gates, confidence semantics, strict mode behavior.

## 7) Launch gate

- [ ] Dry run with one internal client and one multi-client simulation.
- [ ] Fix all blockers from dry run.
- [ ] Tag initial release and publish release notes.

---

## Suggested next implementation slice

1. Add doctor test fixtures + CI matrix.
2. Add migration guide + FAQ.
3. Run end-to-end scenario and record outputs in `docs/`.
