# motion-protocol

> How something moves is as important as how it looks.

A protocol for capturing the perceptual qualities of motion — speed, weight, easing, choreography, rhythm — and turning them into a `motion.md` an agent can read. Sibling to vocab-protocol, but for the temporal dimension of design.

Part of the [Perceptual Protocols](../) family.

## What this is for

vocab-protocol captures how the *static* qualities of a product should be named. mood-protocol declares the overall intent. But motion is a perceptual layer the static protocols cannot reach.

Apple feels like Apple in significant part because of spring physics. Linear feels like Linear because nothing waits. Stripe Press feels like Stripe Press because the type fades in like a slow exhale. Removing the motion from any of these would leave you with a stranger wearing their clothes. The perceptual content of how something moves is enormous, and screenshots cannot carry it.

motion-protocol is the file where you write down how your product moves, in language an agent can read and act on.

## What this gives you

- A canonical starter vocabulary of eight motion qualities — see [`motion.md`](./MOTION.md)
- A prompt for extracting a project-specific motion vocabulary from references — see [`PROMPT.md`](./PROMPT.md)
- A format spec you can extend — see [`FORMAT.md`](./FORMAT.md)

## The relationship to designer-skills

If you've used [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills), you already have execution-side coverage of motion: `animation-principles`, `micro-interaction-spec`, `gesture-patterns`, `feedback-patterns`, `loading-states`, `state-machine`. Those skills tell Claude *how to produce well-formed motion*.

motion-protocol is the perceptual brief that sits one layer above. It tells Claude *what the motion should feel like* before the skills execute against it. The composition is clean:

```
motion.md             "this should feel snappy, mechanical, invisible"   (perceptual intent)
        ↓
animation-principles  "here's how to make it actually feel that way"     (craft execution)
micro-interaction-spec
gesture-patterns
```

The skills become more powerful with a perceptual brief to anchor to. The brief becomes more useful with skills that can execute against it. Neither is competing with the other.

## How to use it

### The minimum — sixty seconds

Drop `motion.md` into your project. When you brief an agent, you can now say things like *"this product moves snappily and invisibly"* and the agent has a file to read for what each of those means, with references, anti-references, and technical anchors.

### Extending the vocabulary for your project

The canonical eight won't cover everything. To extract a project-specific motion vocabulary from your own work or references:

1. Open [`PROMPT.md`](./PROMPT.md).
2. Gather inputs — short videos or GIFs of motion you want to capture, OR CSS / animation code samples, OR live URLs you can describe, OR written descriptions of how things should move. Any of these. Combine them.
3. Upload to Claude, Gemini, or ChatGPT along with `motion.md` and `FORMAT.md`.
4. Paste the prompt.
5. Save the output as `motion.md` in your project.

## On the input problem (worth being honest about)

Motion is harder to capture than colour. The current generation of vision models reads video at variable quality — some handle a 5-second clip well, others extract a few key frames and lose the timing. The protocol is designed to be pragmatic about this:

- **Video / GIF** — most complete when the model handles it well
- **CSS or animation code** — lossless for the technical anchors (durations, easing curves)
- **Live URLs** — if you can describe what you see, the model can use that
- **Written descriptions** — what designers do informally; perfectly valid here

The PROMPT explicitly accepts any combination, and falls back to written description when richer inputs aren't available. Don't let perfect be the enemy of useful.

## The canonical vocabulary

Eight terms, chosen because they cover distinct motion territory and are immediately recognisable:

- **snappy** — decisive, fast, no waiting *(≤200ms, ease-out)*
- **springy** — physical, weighted, alive *(spring physics, slight overshoot)*
- **glassy** — smooth, frictionless, continuous *(longer durations, gentle ease)*
- **calm** — slow, patient, gives breath *(>400ms, no rush)*
- **mechanical** — exact, predictable, repeats identically *(linear or single-easing)*
- **playful** — surprising, characterful, slightly disobedient *(custom curves, anticipation)*
- **theatrical** — sequenced, choreographed, narrative *(dependent timing, total >1s)*
- **invisible** — present without announcement *(150–250ms, ease, no flourish)*

Full definitions, references, technical anchors, and anti-references live in [`motion.md`](./MOTION.md).

## Composing with the rest of the family

```
mood.md       what the product should feel like (baseline)
vocab.md      shared language for static qualities
motion.md     shared language for motion qualities   ← this protocol
situation.md  conditional weighting per context
trace.md      reads existing work
critique.md   assesses output against the brief
```

motion.md and vocab.md sit parallel — both are vocabularies, both define qualities the agent can apply. Cross-references between them are common ("a 'warm' brand often expresses motion as 'calm + organic'") but not required.

A brief that says *"this product is warm + intimate (vocab); calm + invisible (motion)"* gives the agent both the static and temporal perceptual layers it needs to generate coherent work.

## A worked example

See [`examples/example-linear-motion.md`](./example-linear-motion.md) for a `motion.md` decoded from Linear's product interface. Complements the static [Linear trace](../trace-protocol/examples/example-linear.md) — read together, the two files describe how Linear's identity expresses across both spatial and temporal dimensions.

## License

MIT — see the family root.
