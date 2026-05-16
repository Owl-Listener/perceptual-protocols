# critique.md format spec

A `critique.md` is a structured aesthetic assessment of a specific piece of work, against a specific mood. It is anchored, two-sided, actionable, and honest about uncertainty. Any agent that can read text can use it. So can a human collaborator.

## Top-level structure

```markdown
# Critique: [what was critiqued]

**Date:** [date]
**Critiqued against:** [link or reference to mood.md and vocab.md]
**Input:** [what was reviewed — description, link, or reference]

## Verdict

[1–3 sentences. How well does this output embody the intent?
Where on the spectrum from "wrong" to "right" does it land?]

## What's working

### [quality name from vocab.md]
- **Where:** [specific element in the output]
- **Why it works:** [tied back to mood.md or vocab.md]

### [next quality]
- ...

## What's not working

### [quality name from vocab.md]
- **Where:** [specific element]
- **Mismatch:** [what's happening vs what the brief called for]
- **Suggested move:** [actionable change]

### [next quality]
- ...

## Tensions surfaced

[Places where the critique uncovered tensions in the original intent.
e.g., "mood.md called for both warmth and authority — this output
leans authority, sacrificing warmth. Question for the brief:
is that the right trade-off, or did we want both?"]

## What I'm unsure about

[Places where the critique itself is uncertain. Either the criterion
is ambiguous, or the output is doing something interesting that may
be right or wrong depending on context. Flag rather than hide.]

## Next iteration

[2–3 concrete suggestions for the next pass. Each one specific enough
that an agent can act on it.]
```

## Rules

**Anchored, not abstract.** Every observation must point to a specific element ("the hero typography," "the spacing between the second and third cards," "the colour of the CTA button") and to a named quality from `vocab.md`. No floating adjectives. "Lacks warmth" is not a critique. "Lacks warmth — the headline uses a system sans-serif which reads efficient but not generous; the brief called for warmth via serif-leaning typography" is.

**Two-sided.** Always note what works alongside what doesn't. Pure negative critique is neither useful nor in keeping with the family's spirit. If you genuinely can't find anything working, say so explicitly — and consider whether the brief itself was unachievable.

**Actionable.** Every entry in "What's not working" must come with a "Suggested move." If the agent can't propose a move, it is not yet a critique — it's an observation. Note the observation under "What I'm unsure about" and flag that further thought is needed.

**Aware of intent ambiguity.** Sometimes the output is fine and the mood was unclear. The critique should surface that under "Tensions surfaced," not punish the agent for a gap that lives in the brief.

**Honest about uncertainty.** A critique that pretends to be definitive about everything is suspect. Mark the claims you're confident about and the claims you're not. Graded confidence makes the rest of the document more trustworthy.

**Format-stable.** A `critique.md` should be readable weeks later as a record, not just as feedback in the moment. The same way a code review thread is. Date it. Link the inputs. Make it findable.

## What makes a good entry

For "What's working" and "What's not working" entries, each one needs three things:

1. **Where:** the specific element in the output
2. **Why / Mismatch:** the connection back to mood.md or vocab.md
3. **Suggested move** (for what's not working): a concrete change

An entry without all three is unfinished. Better to omit it than to ship it vague.

## Combining with the family

A `critique.md` is most useful when it reads the brief it's critiquing against. The prompt in [`PROMPT.md`](./PROMPT.md) assumes you've uploaded the `mood.md` and `vocab.md` that the work was briefed with. Without those inputs, the critique becomes a free-floating opinion — which has its place, but is not what this protocol is for.

The critique can be passed back to the same agent that produced the output, as the brief for the next pass. This is the canonical iteration loop.

## What about a "passing" critique?

A critique where the output genuinely embodies the intent is short. It might have one paragraph in "What's working," nothing in "What's not working," and a "Next iteration" section that says "Ship it." That is a valid critique. It is also rare.
