# Phase 3 Release Checklist — ralleh-vault

Use this checklist before the first public/internal release cut.

## 1) Architecture and contracts

- [x] Confirm `skills/vault/SKILL.md` capability map matches implementation (`capture/process/crystallize/retrieve/maintain/status/promote`).
- [x] Confirm approval gates are explicit and enforced in docs + runbooks.
- [x] Confirm client boundary rules are explicit for multi-tenant roots.

## 2) Validation and CI quality

- [x] `python3 skills/vault/scripts/vault_doctor.py --vault-root scaffold/vault --strict` passes.
- [x] Add fixture vaults for failing cases (broken links, missing frontmatter, stale inbox, approval-gate missing).
- [x] Add CI matrix for Python 3.10/3.11/3.12 for doctor script compatibility.
- [x] Add role precision audit and enforce it in local + CI validation.

## 3) Security and data handling

- [x] Confirm `raw/` immutability policy in all docs and role prompts.
- [x] Confirm no secrets in scaffold/templates/examples.
- [x] Confirm cross-client link policy requires explicit approval.

## 4) Agent operations

- [x] Validate VAULT session-start ritual against expected workspace layout.
- [x] Validate VAULT-FAST handoff packet format with realistic samples.
- [x] Add one end-to-end integration scenario: inbox batch → handoff → crystallization → index/log update.

## 5) Git and release hygiene

- [x] Add `CHANGELOG.md` with initial release entry.
- [x] Add semantic versioning policy (bootstrap phase documented).
- [ ] Confirm branch protection and required status check (`validate-vault`). **[manual: GitHub repo settings]**

## 6) Documentation completeness

- [x] Add root-level quickstart with copy/paste commands for OpenClaw workspace install.
- [x] Add migration guide from ad-hoc notes to canonical vault layout.
- [x] Add FAQ: wikilinks, approval gates, confidence semantics, strict mode behavior.
- [x] Add role quality contract documentation for contributors/reviewers.

## 7) Launch gate

- [x] Dry run with one internal client and one multi-client simulation. **[completed: see `docs/release-dry-run-2026-07-22.md`]**
- [x] Fix all blockers from dry run.
- [ ] Tag initial release and publish release notes.

---

## Final status summary

Engineering hardening and quality gates are complete for repository readiness.
Remaining manual item: release tagging/publishing (and optional branch-protection/ruleset upgrade path for private-repo governance).
