# voice-protocol

> Brand strategists think in personality. Agents think in rules. `voice.md` bridges the gap.

A protocol for capturing the verbal identity of a brand — how it writes, not just what it values — and turning it into a `voice.md` an agent can read.

Part of the [Perceptual Protocols](../) family.

## Why this exists

Mood boards and design tokens tell agents what something should look like. Nothing tells them what it should sound like. Brand voice guidelines exist — but they live in PDFs no agent reads, written in language too impressionistic to act on.

The result is AI-generated copy that is structurally correct and tonally wrong. Every string is grammatical. None of them sound like you.

`voice.md` is the **verbal** modality of the family. `vocab.md` covers how a product looks standing still, `motion.md` how it moves, `sound.md` how it sounds. `voice.md` covers how it talks.

## What this gives you

- A template covering the five sections of a voice — see [`VOICE.md`](./VOICE.md)
- A prompt for extracting a `voice.md` from writing you already have — see [`PROMPT.md`](./PROMPT.md)
- A format spec you can extend — see [`FORMAT.md`](./FORMAT.md)
- A filled-in worked example — see [`example-clearline.md`](./example-clearline.md)

## How to use it

### The minimum — sixty seconds

1. Copy [`VOICE.md`](./VOICE.md) into your project root and rename it `voice.md`.
2. Fill in each section for your brand.
3. Reference it in your agent context, system prompt, or workflow brief.

No tooling. No schema validation. No build step. Any LLM, any coding agent, any writing tool.

### Extracting a voice from writing you already have

Most brands don't need to invent a voice — they need to describe the one they already have. To extract it:

1. Open [`PROMPT.md`](./PROMPT.md).
2. Gather samples — five to ten pieces of copy that sound right, and two or three that sound wrong.
3. Upload them to Claude, Gemini, or ChatGPT along with `FORMAT.md`.
4. Paste the prompt.
5. Save the output as `voice.md` in your project.

The agent will infer personality descriptors from the samples, propose enforceable mechanics, and anchor every rule to a line it actually found in your writing.

## The five sections

| Section | What it captures |
|---|---|
| `## Personality` | What this brand sounds like at its core — 3 to 5 descriptors, each with a clarifying contrast |
| `## Tonal range` | How voice shifts by context — same brand, different register |
| `## Mechanics` | Specific, enforceable writing rules |
| `## Vocabulary` | Words to use, words to avoid, brand-specific terms |
| `## Reference` | One example of the voice done right, one done wrong |

Full definitions and rules live in [`FORMAT.md`](./FORMAT.md).

## Design principles

**Contrasts over adjectives.** "Warm" means nothing to an agent. "Warm but never gushing" is a constraint it can apply. This is the same move the rest of the family makes with anti-references — a quality is defined by the boundary it doesn't cross.

**Context-aware tone.** A brand that sounds the same in an error message as in a campaign headline hasn't been thought through. The tonal range section forces that thinking, and it is the section `situation.md` reaches for when it weights qualities by context.

**Enforceable mechanics.** Personality is hard to evaluate. Rules are not. `voice.md` separates the two so an agent can be held to the second half even when it's guessing at the first.

**One file, no dependencies.** Place it anywhere, reference it anywhere.

## Composing with the rest of the family

`voice.md` is one of four modality vocabularies. A coherent identity uses them to reinforce each other:

- [`vocab.md`](../vocab-protocol) — what the product feels like standing still
- [`motion.md`](../motion-protocol) — how it moves
- [`sound.md`](../listen-protocol) — how it sounds
- **`voice.md`** — how it writes

A brand briefed as *restrained + precise* in `vocab.md` and *snappy, mechanical, invisible* in `motion.md` should not be writing exclamation-marked onboarding copy. When `voice.md` sits alongside the others, that contradiction becomes visible instead of shipping.

Upstream, [`mood.md`](../mood-protocol) captures the atmospheric intent the voice has to live inside. Downstream, [`tokens.md`](../tokens-protocol) captures the systematic grammar that implements it in UI. Read together, they give an agent a complete brand context.

## License

MIT — see the family root.
