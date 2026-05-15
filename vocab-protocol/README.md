# vocab-protocol

> Designers don't have a vocabulary problem. We have a sharing problem. The vocabulary lives in our heads.

A protocol for capturing the perceptual vocabulary that already lives in a designer's head, and turning it into a `vocab.md` an agent can read.

Part of the [Perceptual Protocols](../) family.

## What this gives you

- A canonical starter vocabulary of ten aesthetic qualities — see [`vocab.md`](./vocab.md)
- A prompt for extracting a project-specific vocabulary from your work or references — see [`PROMPT.md`](./PROMPT.md)
- A format spec you can extend — see [`FORMAT.md`](./FORMAT.md)

## How to use it

### The minimum — sixty seconds

Drop `vocab.md` into your project. From now on, when you brief an agent, you can say things like *"this product is warm + restrained + intimate"* and the agent has a file to read for what each of those means, with references and anti-references that anchor the terms in something specific.

That's it. No setup. No script.

### Extending the vocabulary for your project

The canonical ten won't cover everything. Most projects have a few qualities that are distinctive, recurring, and worth naming. To extract them:

1. Open [`PROMPT.md`](./PROMPT.md).
2. Gather references — three to five examples of work that feels right for the project, two or three anti-references that feel wrong.
3. Upload them to Claude, Gemini, or ChatGPT along with `vocab.md` and `FORMAT.md`.
4. Paste the prompt.
5. Save the output as `vocab.md` in your project, either alongside the canonical file or replacing it.

The agent will identify which canonical terms apply, propose new project-specific terms, and anchor every term to the references you supplied.

## The canonical vocabulary

Ten terms, each chosen because they cover distinct perceptual territory and are immediately recognisable to designers:

- **warmth** — emotional temperature, generosity of welcome
- **density** — informational and visual compression
- **restraint** — what is deliberately not shown
- **irreverence** — willingness to break conventions, levity
- **materiality** — the sense of stuff, texture, physical presence
- **precision** — exactness of intent, sharpness of decision
- **authority** — confidence and gravitas, how settled the voice is
- **intimacy** — closeness, vulnerability, small-scale care
- **friction** — productive resistance, the texture of slowness
- **rhythm** — pacing, repetition, cadence of elements

Full definitions, references, and anti-references live in [`vocab.md`](./vocab.md).

## Why these ten

They were chosen against four criteria:

1. **Designer-recognisable.** Every term is something designers already say when they're describing a piece of work. The vocabulary should not require an introduction before it can be used.
2. **High information density.** Each term covers significant aesthetic ground. "Warmth" carries more information than "uses warm colours."
3. **Orthogonal.** Terms do not collapse into each other. You can have a high-warmth, high-precision product without contradiction.
4. **Agent-actionable.** The agent can produce a different output when asked for more or less of the quality. "More restraint" produces a different draft than "more warmth."

The list is a starting point. It will grow. Send a pull request with new terms — each entry should include a definition, a one-paragraph description, two to three references, and two to three anti-references.

## Composing with mood-protocol

`vocab-protocol` and [`mood-protocol`](../mood-protocol) are designed to be used together.

- `mood.md` says **what this specific project should feel like** — with images, atmospheres, anti-references, all anchored to one body of work.
- `vocab.md` says **what the words in mood.md actually mean** — a shared, agent-readable definition layer that travels across projects.

An agent reading both has the closest thing yet to a designer's brief.

## License

MIT — see the family root.
