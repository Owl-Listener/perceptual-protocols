# situation.md format spec

A `situation.md` captures the conditional perceptual logic of a product — how the qualities defined in `mood.md` and `vocab.md` should weight differently across surfaces, user roles, and moments. Any agent that can read text can use it.

## Top-level structure

```markdown
# Situations

[Optional: a one-paragraph introduction naming the product and the
baseline mood.md it builds on. State the principle that holds across
all situations.]

## [Situation name]

**When this applies:** [The triggering conditions — surface, user role,
moment, task, or any combination of these.]

**Weighted qualities:**
- [quality from vocab.md]: HEAVY | MODERATE | LIGHT
- [quality]: HEAVY | MODERATE | LIGHT
- ...

**Situation-specific qualities** *(optional):*
- [quality name] — [one-line definition + brief anchor]

**Why this weighting:** [Short rationale. Helps the agent reason, and
helps the next designer understand the intent.]

[Repeat for each situation.]
```

## Rules

**Every situation has a clear "When this applies."** Without it, the agent has no way to decide which situation matches the work it's generating. The trigger can be about surface, user role, moment in flow, task, or a combination — but it must be specific enough that the agent can pattern-match.

**Weights are coarse, not numeric.** Use HEAVY, MODERATE, and LIGHT. The coarseness is intentional — "more warmth" is a clearer instruction to an agent than "warmth at 7." Finer-grain weighting can be added by teams that need it, but the canonical vocabulary is three levels.

**Every weighted quality must already exist in vocab.md.** Situation-protocol doesn't invent new vocabulary. If a quality isn't in vocab.md, add it there first.

**Situation-specific qualities are allowed but should be rare.** Most situations should weight the canonical vocabulary differently. A new quality that applies in only one situation is fine, but be honest about whether it actually belongs in vocab.md instead.

**Aim for 3–8 situations per file.** A `situation.md` with more than ten contexts is usually a sign that the brand is fragmented (consider splitting into multiple products) or that the file is doing the job of a design system. Resist the temptation to enumerate every screen.

**Every situation has a "Why this weighting" rationale.** Even one sentence. Future-you will not remember why the patient portal weighted warmth heavy, and an agent reading the file cold needs the rationale to reason about edge cases.

## What makes a good situation

A useful situation has three things:

1. **A clear trigger** — the agent can tell when this situation applies.
2. **A meaningful weighting** — at least two qualities differ in weight from the product-wide baseline.
3. **A defensible rationale** — the weighting reflects an actual decision, not a guess.

If a situation doesn't change the weighting from the baseline, it doesn't need its own entry. The baseline lives in `mood.md`.

## Composing situations

Sometimes a piece of work falls under more than one situation — a patient-portal alert, for example. The agent should:

1. Identify all situations that apply
2. Combine the weights — generally taking the heavier weight for each quality
3. Surface any contradictions for human review

For example: patient portal weights warmth HEAVY; alert state weights urgency HEAVY and warmth LIGHT. A patient-portal alert would weight urgency HEAVY (from alert state) but also retain some warmth (from patient portal) — the work needs to be both urgent and kind. The agent should flag this combination explicitly rather than silently resolving it.

## Weighting language

For consistency, the three weights should be read as:

- **HEAVY** — this quality dominates the work. If the output doesn't embody this quality clearly, it has failed the situation.
- **MODERATE** — this quality is present and visible, but other qualities lead.
- **LIGHT** — this quality is in the background, contributing to coherence but not driving decisions.

Qualities not listed for a situation default to whatever they are in `mood.md`.
