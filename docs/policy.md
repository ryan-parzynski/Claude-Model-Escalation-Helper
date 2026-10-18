# Escalation Policy

## Principle

Use the lightest capable model for each task.

- **Haiku:** Default for routine work
- **Sonnet:** When Haiku hits a trigger
- **Opus:** For hardest problems (background review only)

## Observable Triggers

See `docs/triggers.md` for the 5 concrete triggers.

Don't escalate for vague reasons ("reasoning feels shallow"). Escalate when you hit a specific trigger.

## Review Brief Format

When escalating to Sonnet/Opus, write a brief with three sections:

1. **Goal and Question** (1-2 sentences)
   - What's the decision being gated?
   - What precise question do you need answered?

2. **Evidence** (exact excerpts with sources)
   - Code snippets, requirement text, error messages
   - Label each: file path, commit/date, context
   - Distinguish observations from assumptions

3. **Uncertainties** (what's unclear)
   - What test or measurement would resolve it?
   - What do you still need to know?

**Target:** 1,000–1,500 tokens (shorter is better)

## Background Review Only for Opus

When escalating to Opus:
- Send a focused brief (not your whole chat history)
- Get review in background (don't wait mid-chat)
- Saves ~78% tokens vs mid-chat Sonnet switching

## Don't Escalate For

- Clarification questions → ask in same turn
- Format/style fixes → Haiku handles these
- Unclear tasks → clarify first, escalate later
- Just polishing → not worth the tokens

## Anti-Overengineering

Don't recommend additional layers/abstractions/retries to address hypothetical concerns.

Every fix must:
- Connect to an applicable requirement
- Include a credible failure scenario
- Weigh complexity vs risk removed

---

**See:** `docs/triggers.md` for trigger definitions
**See:** `templates/escalation-brief.md` for brief template
