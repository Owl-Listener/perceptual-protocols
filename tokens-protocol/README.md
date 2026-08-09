# tokens-protocol

> Agents can read your token values. They can't read your intent. `tokens.md` fills the gap.

A protocol for annotating a design system you already have with the semantic intent an agent is missing, and turning it into a `tokens.md` an agent can read.

Part of the [Perceptual Protocols](../) family.

## Why this exists

Design tokens exist in most mature projects — as Figma variables, CSS custom properties, Tailwind configs, or style-dictionary outputs. The values are there. What's missing is the layer above the values: the semantic intent, the usage rules, the constraints that tell an agent *why* a token exists and *when* to reach for it.

The result is AI-generated UI that uses the right design system and makes the wrong choices. Correct hex, wrong context. Valid spacing value, wrong scale level. Functional — but off.

`tokens.md` doesn't replace your tokens. It makes them legible.

## Where it sits in the family

Most of this family points upstream, at intent that exists before a system does. `tokens-protocol` points the other way. It is the protocol for projects that already have a design system and need an agent to apply it with judgement rather than autocomplete.

```
   [intent]                    [system]                [delivery]
   mood.md      ────────►      tokens.md    ────────►  shipped UI
   voice.md                    (the values you
   vocab.md                     already have,
                                annotated with why)
```

If `mood.md` is what the product should feel like before there is a system, `tokens.md` is what the system means now that there is one. A project that runs both gives an agent the whole arc: the intent, and the grammar that implements it.

## What this gives you

- A template covering the seven sections of a token system — see [`TOKENS.md`](./TOKENS.md)
- A prompt for generating a `tokens.md` from a token file you already have — see [`PROMPT.md`](./PROMPT.md)
- A format spec you can extend — see [`FORMAT.md`](./FORMAT.md)
- A filled-in worked example — see [`example-clearline.md`](./example-clearline.md)

## How to use it

### The minimum — sixty seconds

1. Copy [`TOKENS.md`](./TOKENS.md) into your project root and rename it `tokens.md`.
2. Fill in the `## Source` section first — point at where your real values live.
3. Fill in the sections that matter for your product. Delete the ones that don't.
4. Reference it in your agent context, system prompt, or workflow brief.

No tooling. Works alongside any token format: Figma variables, CSS custom properties, Tailwind, style-dictionary, or plain JSON.

### Generating it from tokens you already have

If your values already live in a file, you don't need to retype them:

1. Open [`PROMPT.md`](./PROMPT.md).
2. Gather your token source — `tokens.json`, `tailwind.config.ts`, a CSS custom-property block, or a Figma variables export.
3. Upload it to Claude, Gemini, or ChatGPT along with `FORMAT.md`.
4. Paste the prompt.
5. Save the output as `tokens.md` in your project root and correct the usage rules the model guessed at.

The model can read your values. It cannot read your intent, so expect to rewrite the "Use for" and "Do not use for" columns — that editing pass *is* the protocol. What you get from the model is the scaffolding and the tedium.

## The seven sections

| Section | What it captures |
|---|---|
| `## Source` | Where your actual token values live |
| `## Color` | Semantic roles with values and usage rules |
| `## Typography` | Type scale with semantic labels and context |
| `## Spacing` | Scale with intent — component, layout, page |
| `## Elevation` | Shadow levels and what they signal |
| `## Motion` | Duration and easing with usage context |
| `## Radius` | Border radius scale with component guidance |

Full definitions and rules live in [`FORMAT.md`](./FORMAT.md).

## Design principles

**Intent over values.** An agent can import your Tailwind config. What it can't import is the decision that `red-600` means destructive and `red-400` means warning. Capture the decisions, not just the values.

**Semantic over primitive.** Name tokens by role, not by appearance. `color.surface.danger` tells an agent more than `#fee2e2`. Where you have both, map primitive to semantic.

**Usage rules, not just definitions.** Every entry says what a token is for *and* what it is not for. The second column is the one that prevents bad output, and it is the same instinct as the anti-reference rule everywhere else in this family.

**Thin by design.** `tokens.md` points at your source of truth — it does not duplicate it. Keep it short enough to paste into a context window. A `tokens.md` that has drifted out of sync with the real values is worse than no file at all, so the less it restates, the longer it stays true.

## Composing with the rest of the family

`tokens.md` implements in UI what the other protocols describe in intent:

- [`mood.md`](../mood-protocol) — the atmospheric feel the system is meant to produce
- [`vocab.md`](../vocab-protocol) — what the shared quality words mean
- [`voice.md`](../voice-protocol) — how the brand writes
- **`tokens.md`** — the specific values and rules that implement all of it

There is deliberate overlap with [`motion-protocol`](../motion-protocol). `tokens.md` carries the *values* — `motion.duration.fast` is 150ms. `motion.md` carries the *character* — this product moves snappily, mechanically, invisibly. An agent needs both, and the two files should agree: if `motion.md` says calm and glassy while `tokens.md` tops out at 150ms, one of them is lying. Where they conflict, `motion.md` describes the intent and `tokens.md` describes what shipped — which is usually a signal that the system drifted from the brief.

## License

MIT — see the family root.
