# Observable Escalation Triggers

When to escalate from Haiku to Sonnet.

## The 5 Concrete Triggers

| # | Trigger | What It Means | Why Escalate |
|---|---------|---|---|
| 1 | Cannot trace code path | Can't point to specific line showing state A→B | Missing mental model of implementation |
| 2 | Competing explanations, no test | Two hypotheses, but no way to test between them | Hypothesis generation without validation |
| 3 | Reintroduced violation | Fix A breaks invariant X; fix B breaks it again | Incomplete understanding of constraints |
| 4 | Unreconciled triple | Implementation, tests, and spec contradict each other | Missing cross-domain understanding |
| 5 | Repeated contradiction | Same requirement stated/contradicted/re-stated | Stable misunderstanding or attention loss |

## Optional Trigger (Under Validation)

| 6 | Resource exhaustion | Reasoning halts/loops without proposing next step | Hit context or inference limits |

Status: Pilot phase — add if observed in 5+ escalations

## Task Upfront Signals (Skip Haiku Entirely)

Don't wait for Haiku to fail. Use Sonnet from the start if:

- Ambiguous problem with interacting components
- High consequence of error (production, financial, security)
- Requires novel algorithm or architecture
- Multi-step reasoning across unfamiliar codebase

---

**See:** `docs/policy.md` for full policy context
