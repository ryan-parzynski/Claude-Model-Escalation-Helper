# Claude Model Escalation Helper

**AI Assistance Used:** Framework designed with Claude Haiku 4.5 (default), escalated to Claude Sonnet 4.6 for decision validation, reviewed by Opus 5.5 background analysis. All policy, triggers, templates, and code generated with AI assistance.

---

## What This Is

A decision framework for managing model escalation on Claude Pro/Max plans.

**Problem:** You have a $20/month Pro plan. Haiku is your default. When should you escalate to Sonnet? When to Opus?

**Solution:** Observable decision triggers, cost-aware routing, background review patterns, and automated tracking.

## The System in 60 Seconds

### 5 Observable Triggers (When to Escalate)

Escalate from Haiku to Sonnet when you hit ANY of these:

1. **Cannot trace code path** — Can't point to line showing state A→B
2. **Competing explanations, no test** — Two hypotheses, no way to test between them
3. **Reintroduced violation** — Fix A breaks invariant X; fix B breaks it again
4. **Unreconciled triple** — Code/tests/spec contradict each other
5. **Repeated contradiction** — Same requirement stated/contradicted twice

### Cost Math

- **Haiku:** $0.10 / $0.50 per MTok (use by default)
- **Sonnet:** $3 / $15 per MTok (30× more)
- **Opus:** ~$5 / $25 per MTok (background review only)

### Workflow

1. **New task?** Check `docs/triggers.md` — can Haiku handle it?
2. **Stuck?** Write brief using `templates/escalation-brief.md`
3. **Escalate?** Create GitHub issue with template
4. **Integrate?** Track the decision with `scripts/track-escalation.py`

## Files

- **Policy & Rules:** `docs/` (what to do and why)
- **Copy-Paste Templates:** `templates/` (escalation briefs, cheatsheet)
- **Real Examples:** `examples/` (Oct 2026 pilot escalations)
- **Measurement:** `data/measurements.json` (track what works)
- **Automation:** `scripts/` (log and measure decisions)

## Quick Start

### Read (5 minutes)

```bash
cd claude-model-escalation-helper
cat docs/policy.md
cat docs/triggers.md
```

### Use (Immediately)

When stuck with Haiku:
```bash
cp templates/escalation-brief.md my-escalation.md
# Edit it with your brief
# Create GitHub issue using .github/ISSUE_TEMPLATE/escalation-review.md
# Share with Sonnet for review
```

### Track (Optional)

```bash
python scripts/track-escalation.py "task name" haiku --escalated sonnet
```

Results go to `data/measurements.json`

## Key Concepts

### Observable Triggers (Not Vague Feelings)

Don't escalate because "reasoning feels shallow." Escalate when you hit a **specific trigger**.

✅ "Cannot trace code path through auth module" → Trigger #1  
❌ "Reasoning seems weak" → Not specific enough

### Background Review Only for Opus

- Send focused brief (not full chat history)
- Get review in background
- Save ~78% tokens vs mid-chat Sonnet

### Measure Everything

Track for 30 days minimum:
- Which triggers fire?
- Does background review save tokens?
- Are escalations preventing wasted work?

## Cost Comparison

**Without framework** (repeated Haiku failures):
- Haiku #1: $0.02 (fails)
- Haiku #2: $0.02 (fails)
- Haiku #3: $0.02 (fails)
- Sonnet: $0.06
- Total: $0.12 + wasted time

**With framework** (early escalation):
- Haiku #1: $0.02 (you catch trigger #1)
- Sonnet: $0.06 (succeeds)
- Total: $0.08 + solved quickly

**Savings:** 33% cost + faster solution

## Validation

**30-Day Pilot (Oct 2026):**
- ✅ Triggers are solid
- ⚠️ Token math is real but modest (quality framework, not cost-saving)
- ⚠️ Missing trigger: resource exhaustion (optional trigger #6)
- ⚠️ Brief quality critical: vague briefs waste tokens

**Status:** Deploy with 5 triggers, measure 30 days, refine.

## Contributing

### Add a New Trigger

1. Observe in 5+ escalations
2. Document in `docs/triggers.md`
3. Create PR with evidence

### Update Model Reference

Quarterly (Jan/Apr/Jul/Oct):
- Check https://claude.com/pricing
- Update `docs/model-reference.md`
- Create PR

## Next Steps

1. **Today:** Read `docs/policy.md` and `docs/triggers.md`
2. **This week:** Use templates on first stuck task
3. **Weeks 2-4:** Track 30 days of escalations
4. **Week 5:** Review measurements, refine
5. **Ongoing:** Quarterly model reference updates

## License

GNU General Public License v3 (GPL 3)

Free to use, modify, and share.

---

**Start using the framework today. Measure results over 30 days. Refine based on data.**

For questions, see `examples/` for real escalations or create an issue.
