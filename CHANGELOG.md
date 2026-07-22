# Changelog

## Unreleased

### Changed
- CI reliability fixes for Python 3.10 compatibility and clean-checkout fixtures

## v0.1.0 - 2026-07-22

### Added
- Local-first Ralleh Vault scaffold (`scaffold/vault`) with canonical `wiki/` + immutable `raw/` model
- Vault skill package (`skills/vault`) with runbooks, templates, schema, and doctor tooling
- VAULT and VAULT-FAST full role packages with golden-standard operating overlays
- Strict validation gates: unit tests, strict doctor checks, and role precision audit
- CI matrix for Python 3.10 / 3.11 / 3.12 (`validate-vault` workflow)
- Integration, ingestion, retrieval, migration, FAQ, and role-quality documentation

### Changed
- Hardened core runbooks for deterministic output contracts and escalation criteria
- Tightened approval-gate and provenance expectations across docs and role protocols

### Fixed
- Doctor runtime compatibility for Python 3.10 (`datetime.UTC` fallback)
- Fixture setup reliability on clean CI checkouts
- Scaffold strict-check reliability by tracking empty required roots (`Inbox/`, `raw/`)

### Added
- Phase 2 hardening baseline for Ralleh Vault
- Strict vault doctor checks
- Client-scoping conventions
- Git policy, commit template, and CI validation workflow
- Phase 3 release checklist
