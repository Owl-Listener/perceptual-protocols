# situation-protocol

> Same brand. Different weighting. Per situation, per moment.

A protocol for capturing the conditional perceptual logic of a product — how the same brand identity should weight its qualities differently across surfaces, user roles, and moments. The output is a `situation.md` that any agent can read alongside `mood.md` and `vocab.md` to know not just what the product should feel like, but how that feeling adapts to who is using it, where, and when.

Part of the [Perceptual Protocols](../) family.

## What this is for

mood-protocol declares baseline intent — the perceptual identity of a product across everything it does. vocab-protocol gives that intent shared language. But most products have to inhabit that identity differently in different situations.

A hospital interface needs warmth and precision throughout. But on the patient portal, warmth dominates. On the clinical dashboard, precision dominates. On an alert state, neither is the point — urgency is. The same brand, weighted differently, depending on who is looking and what is happening.

situation-protocol is the file where you write that down so an agent can read it.

Four common uses:

**Multi-surface products.** Healthcare, finance, education, government — anything with multiple user types and contexts has this problem. A `situation.md` lets you encode the brand-wide identity and the situational variation in one place.

**Generative UI.** When the interface is regenerated per user per moment, the agent needs to know the weighting for *this* moment. situation-protocol is the conditional layer that makes contextually appropriate generation possible.

**Adaptive critique.** With `situation.md` in the loop, critique-protocol can assess the work against the right weighting for the context, not against a one-size-fits-all standard.

**Onboarding new collaborators.** A `situation.md` makes implicit team knowledge ("we use a different tone for clinicians than for patients") explicit and shareable.

## How to use it

1. Gather your inputs:
   - The `mood.md` for your product (the baseline identity)
   - The `vocab.md` whose terms you'll weight per situation
   - A list of situations your product encounters — surfaces, user roles, moments. Optionally: example screens or copy from each.
2. Open Claude, Gemini, or ChatGPT. Upload the above.
3. Paste the prompt from [`PROMPT.md`](./PROMPT.md).
4. Save the output as `situation.md` in your project, alongside `mood.md` and `vocab.md`.
5. When briefing an agent on a specific surface, point it at all three files. The agent reads `situation.md` to know which qualities to lean into for this situation.

## Output format

The output is a `situation.md`, defined in [`FORMAT.md`](./FORMAT.md). It is its own format — different from `mood.md` (which is product-wide) and `vocab.md` (which is term-definitions).

## How it composes with the family

```
mood.md       baseline intent for the product
vocab.md      shared language for the qualities
situation.md  conditional weighting per context
    ↓
agent reads all three to generate for THIS situation
    ↓
critique.md   assesses against situation-appropriate weighting
```

The agent stops trying to satisfy every quality equally and starts making context-sensitive trade-offs. The critique stops asking "did the output deliver warmth?" and starts asking "did the output deliver warmth in a context where warmth was supposed to dominate?" Much sharper.

## When situation-protocol is the wrong tool

If your product genuinely has one mood across all surfaces and users, you don't need this protocol. `mood.md` alone is enough.

If your "situations" feel like genuinely different products with different audiences and different identities, that's a sign you have multiple `mood.md` files, not a single `situation.md`. The protocol is for *one identity, weighted differently* — not for *multiple identities masquerading as one*.

A `situation.md` with thirty entries is probably a design smell. Either the brand is fragmented (consider splitting into multiple products with their own mood.md files), or the file is doing the job of a design system rather than a perceptual protocol. Aim for 3–8 situations per file. If you genuinely have more, split.

## A worked example

See [`examples/example-hospital.md`](./examples/example-hospital.md) for a full `situation.md` of a synthetic hospital product with three situations: patient portal, clinical dashboard, and alert state. Useful as a calibration reference when reading your own first drafts.

## License

MIT — see the family root.
