# Quick Reference

## Should I Escalate?

**YES if:**
- Can't trace code path
- Two explanations, no test between them
- Made a fix that reintroduced same violation
- Can't reconcile impl/tests/spec
- Keep contradicting the requirement

**NO if:**
- Just need clarification (ask in same turn)
- Fixing format/style
- Task itself is unclear (clarify first)
- Just polishing

## Cost Quick Math

- Haiku: $0.10 / $0.50 per MTok (use this)
- Sonnet: $3 / $15 per MTok (30× more)
- Opus: ~$5 / $25 per MTok (use background only)

## Writing a Brief

1. Goal & Question (1-2 sentences)
2. Evidence (exact excerpts with sources)
3. Uncertainties (what test would resolve?)

Target: 1,000–1,500 tokens

## GitHub Issue

Use `.github/ISSUE_TEMPLATE/escalation-review.md` template.

Sonnet reviews in the issue. You integrate findings.

## Track It

```bash
python scripts/track-escalation.py "task name" haiku --escalated sonnet
```

Results in `data/measurements.json`

---

See `docs/` for full policy.
