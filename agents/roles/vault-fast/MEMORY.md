# MEMORY.md — Lessons & Patterns

# MEMORY.md — Lessons & Patterns

## Throughput Quality

- **Template discipline is the primary quality lever.** Batches that skip the template step have 3–5× the schema error rate. The template overhead per item is trivial; the rework cost downstream is not.
- **Provenance is the most expensive defect to fix later.** When a draft has no `sources`, the originating file must be rediscovered, re-read, and re-linked. The cost is paid by VAULT, not VAULT-FAST. Don't create the debt.
- **Batch size discipline matters.** Batches over 30 items produce lower per-item validation quality. Keep batches small enough that you can verify each item before moving on.

## Escalation Lessons

- **Escalate early.** Attempting to resolve an ambiguity that belongs to VAULT costs 2–3× as much as creating a clean escalation packet. Delayed escalation creates rework for VAULT and BRAIN both.
- **Incomplete escalation packets are worse than no escalation.** VAULT cannot process an escalation without source path, candidate type, reason, and unresolved questions. A skeleton packet is just noise.
- **Never guess at classification.** If content might be `confidential` or `restricted`, it is. Assign conservatively and escalate. Downgrading classification requires human authorization.

## BRAIN Integration Lessons

- **100% path coverage is a hard requirement.** A BRAIN batch query with 10 paths expects 10 entries in `processed` + `escalations`. Silent drops break BRAIN's entity coverage tracking silently.
- **`confidence` is data, not encouragement.** Assign 0.3–0.5 for partial-source drafts, 0.7–0.85 for clean template drafts, 0.9+ only for complete frontmatter with real sources and no conflicts.
- **BRAIN caches VAULT-FAST responses.** Inflated confidence values get cached and propagated. A `0.9` confidence on a draft with one weak source is a lie BRAIN will repeat.

## Backlog Control

- **Oldest age is more important than total count.** 50 items at 1 day old is fine. 5 items at 14 days old is a problem. Always reduce oldest age before reducing count.
- **Recurring deferrals are a signal.** If the same item keeps getting skipped, it belongs in an escalation packet, not the batch queue.
