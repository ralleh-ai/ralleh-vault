# Runbook: vault.promote (stub)

This is a reserved integration hook for future source promotion (for example Engram exports).

Current behavior:
1. Accept external source manifest/reference.
2. Validate source is treated as immutable raw input.
3. Route material into `vault/raw/exports/`.
4. Trigger `vault.process` for normalization.

Non-goals:
- No hard dependency on Engram.
- No direct write into canonical `wiki/` from promotion step.
