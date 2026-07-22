# ADR-0001: Two-agent Vault model and Markdown source of truth

## Status

Accepted

## Context

The system needs both high throughput and high judgment while staying auditable and portable.

## Decision

1. Use plain Markdown files on disk as canonical source of truth.
2. Split responsibilities:
   - `VAULT-FAST`: high-volume triage, normalization, and prep.
   - `VAULT`: deep synthesis, conflict resolution, and canonical quality.

## Consequences

- Better cost/performance through model specialization.
- Stronger graph quality for strategic notes.
- Git-friendly history and human inspectability.
- Slightly higher coordination overhead, solved via explicit handoff protocol.
