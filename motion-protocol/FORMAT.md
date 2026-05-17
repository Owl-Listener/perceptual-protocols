# motion.md format spec

A `motion.md` is a structured collection of motion qualities, each with a perceptual definition and technical anchors that translate the feeling into actual animation choices. Any agent that can read text can use it.

## Top-level structure

```markdown
# Motion Vocabulary

[Optional: a one-paragraph introduction naming the project and any
project-specific motion principles that hold across all entries.]

## term-name

**One line:** [One-sentence definition.]

**When it applies:** [Longer description — when this quality is relevant
and what it does for the work.]

**References:**
- [Specific example] — [short note on why it embodies this, with timing
  details where observable]
- [Specific example]

**Technical anchors:**
- Duration: [range in ms]
- Easing: [curve family — linear, ease-out, spring, cubic-bezier with values]
- Gesture response: [first-frame timing if relevant]
- Avoids: [what kinds of motion this quality is incompatible with]
- Other: [secondary motion, sequencing, etc.]

**Anti-references:**
- [Specific counter-example] — [short note on why it isn't this]
- [Specific counter-example]

**Pairs well with:** [comma-separated list of related motion terms,
or brand-quality references]
**Tensions with:** [comma-separated list of terms in tension]

[Repeat for each term.]
```

## Rules

**Term names are lowercase, single-word where possible.** `snappy`, not `Snappy` or `snappy-motion`. The vocabulary is meant to compose.

**Every term has both perceptual description and technical anchors.** This is what distinguishes motion-protocol from a pure perceptual vocabulary. The technical anchors give an agent something concrete to translate into CSS, animation libraries, or motion specs.

**Technical anchors should be ranges, not exact values.** Snappy isn't "exactly 200ms" — it's "≤200ms." This leaves room for context-appropriate variation.

**References should include timing where observable.** Not "Linear's command palette" alone, but "Linear's command palette — opens in roughly 120ms, no springiness." The timing anchors the perceptual claim.

**Every term has at least two references and two anti-references.** A term without anti-references is not yet a useful term. Motion is especially prone to vague description; the boundary definitions force specificity.

**Anti-references should describe categories, not punching down.** "A bank dashboard with bouncy modal — wrong category" works because it names a mismatch, not a brand. "Brand X is bad at this" doesn't work.

**Pairs and tensions are required, not optional.** Motion qualities compose in non-obvious ways (snappy + mechanical reinforce each other; snappy + springy fight). Naming the relationships helps the agent reason about combinations.

## What makes a good term

A canonical motion term should be:

1. **Designer-recognisable** — a word designers already say when describing motion. Not jargon.
2. **High information density** — the term covers significant motion ground, not a narrow stylistic slice.
3. **Orthogonal to existing terms** — not a near-synonym for something already in the vocabulary.
4. **Agent-actionable** — the agent can produce a measurably different output when asked for more or less of the quality.
5. **Technically anchorable** — there's a range of durations / easings / sequencing patterns that consistently produce the quality.

A term that fails #5 (no technical anchors) probably belongs in `vocab.md` rather than `motion.md`.

## Combining motion qualities

A brief that says *"this product moves snappily + mechanically + invisibly"* gives the agent three motion terms it can read in `motion.md`. The agent should:

- Look up each term's definition, references, and technical anchors
- Notice that all three pair well with each other (low tension — they reinforce)
- Generate motion that satisfies the union of the technical anchors (≤200ms, consistent easing, no flourish)

A brief that says *"this product moves snappily + springy"* should trigger the agent to notice the named tension and either ask for guidance or surface the tension explicitly in its proposed solution. Snappy and springy pull in opposite directions on timing and easing — the agent shouldn't silently average them.

## Composing with vocab.md

motion-protocol and vocab-protocol are sibling vocabularies. Cross-references are useful but not required. Some common pairings:

- A *warm* brand (vocab) often expresses motion as *calm + organic* (motion-adjacent qualities)
- A *precise* brand (vocab) often expresses motion as *snappy + mechanical + invisible*
- An *irreverent* brand (vocab) often expresses motion as *playful + springy*

These are observations, not rules. A motion identity can deliberately contradict the static identity for effect — a precise brand with playful motion is doing something specific.

## Extending the vocabulary

To add a term, follow the same bar as vocab-protocol's:

- Canonical terms (in the family's `motion.md`) need to clear all five criteria above
- Project-specific terms (in your own `motion.md`) only need to be useful for your work

Send a pull request for canonical terms. Add freely for project-specific ones.
