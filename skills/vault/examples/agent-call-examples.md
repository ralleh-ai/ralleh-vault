# Example calls

## Other agent asks VAULT-FAST to process inbox

- "Run `vault.process` on `vault/Inbox` and prepare escalation notes for VAULT where confidence is low."

## Other agent asks VAULT for crystallization

- "Run `vault.crystallize` for project migration notes in `wiki/Projects/` and update related Decisions + index/log."

## Retrieval

- "Run `vault.retrieve` for all canonical decisions tied to `[[Project Apollo]]` and return citations."

## Maintain

- "Run `vault.maintain` and report inbox size, broken links, frontmatter compliance score, and approval-gate violations."

## Cross-agent orchestration (OpenClaw)

- "Spawn `VAULT-FAST` to process today’s inbox batch; keep output in handoff note under `wiki/Resources/` and escalate unresolved items to `VAULT`."
- "Spawn `VAULT` to finalize all escalated items with `confidence=high|medium`, update MOCs, and append `wiki/log.md`."
