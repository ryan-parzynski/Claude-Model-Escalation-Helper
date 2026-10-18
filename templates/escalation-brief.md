# Escalation Brief Template

Use this when you're stuck with Haiku and need Sonnet/Opus review.

## Goal and Question

[Write 1-2 sentences answering:]
- What's the decision being gated?
- What precise question do you need answered?

Example: "Haiku can't trace how user state flows through the auth module. Question: is my state machine implementation correct, or am I missing a transition?"

## Evidence

[Exact excerpts with provenance:]

**From:** [file path] (commit/date, [context])
[Code snippet or requirement text]

**From:** [file path]
[Another excerpt]

Keep it decision-relevant. Don't dump everything.

## Uncertainties and Decision Points

[What's still unclear?]

**Needs testing:** [What test would resolve the uncertainty?]
**Needs measurement:** [What data would help decide?]
**Depends on:** [What other decision or context matters?]

---

**Target:** 1,000–1,500 tokens

Ready to send? Create a GitHub issue with this brief using `.github/ISSUE_TEMPLATE/escalation-review.md`
