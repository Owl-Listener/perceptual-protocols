# vocab.md format spec

A `vocab.md` is a structured collection of aesthetic qualities, each with a definition and references that anchor it to something specific. Any agent that can read text can use it.

## Top-level structure

```markdown
# Vocabulary

[Optional: a one-paragraph introduction naming the project, brand, or context.]

## term-name

**One line:** [One-sentence definition.]

**When it applies:** [Longer description — when this quality is relevant and what it does for the work.]

**References:**
- [Specific example] — [short note on why it embodies this]
- [Specific example] — [short note]

**Anti-references:**
- [Specific anti-example] — [short note on why it isn't this]
- [Specific anti-example] — [short note]

**Pairs well with:** [comma-separated list of related terms in this vocab]
**Tensions with:** [comma-separated list of terms in tension]

[Repeat for each term.]
```

## Rules

**Term names are lowercase, single-word where possible.** `warmth`, not "Warmth" or "warmth-and-glow". The vocabulary is meant to compose — single tokens combine more cleanly than phrases.

**Every term has at least two references and two anti-references.** A term without anti-references is not yet a useful term. Designers define spaces by their boundaries.

**References are concrete, recognisable, named.** A brand, product, person, era, place, or material. Not "warm websites" — "Are.na's interaction texture." The agent uses these to anchor what the term actually means in practice.

**Anti-references should be specific too, but not punching down.** The aim is to mark a boundary, not to mock. "A government tax form" works because the form is doing its job correctly by being un-warm. "Brand X is bad at this" doesn't work.

**Pairs and tensions are optional but recommended.** They let an agent reason about combinations. "Warm + precise" should be possible. "Irreverent + authoritative" is harder, and naming the tension lets the agent ask for guidance instead of guessing.

**Order doesn't matter.** Terms can be alphabetical, grouped by theme, or in the order they came to mind. Agents will read whatever order you choose.

## What makes a good term

The bar for a canonical term (one that lives in the family's `vocab.md`) is high. The bar for a project-specific term is much lower — anything that's useful for your project is fair.

A canonical term should be:

1. **Designer-recognisable** — designers say this word already when describing work.
2. **High information density** — it covers significant aesthetic ground, not a narrow stylistic slice.
3. **Orthogonal to existing terms** — it isn't a near-synonym for something already in the vocabulary.
4. **Agent-actionable** — the agent produces a different output when asked for more or less of the quality.

To propose a new canonical term, send a pull request to the family root. To add a project-specific term, just add it to your local `vocab.md`.

## Combining terms

A brief that says *"this product is warm + restrained + intimate"* gives the agent three terms it can read in `vocab.md`. The agent should be able to:

- Look up each term's definition and references
- Notice that all three pair well with each other (low tension)
- Apply all three when generating output

A brief that says *"this product is irreverent + authoritative"* should trigger the agent to notice the named tension between those two terms and either ask for guidance or surface the tension explicitly in its proposed solution.

This is the simplest version of perceptual composition. Future protocols may formalise it further.
