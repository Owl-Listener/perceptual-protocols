# trace-protocol

> Capture the mood from something you like.

A protocol for tracing the implicit perceptual logic of an existing UI, brand, or design artifact, and turning it into a `trace.md` that an agent can read.

Part of the [Perceptual Protocols](../) family.

## What this is for

mood-protocol captures what you want a thing to feel like. trace-protocol captures what something else already feels like — by following its lines, observing its decisions, and writing the result down in a structured form.

The output is a `trace.md`. Same format as `mood.md`, different default filename because the source is different — you traced it from someone else's work, you didn't author it.

Four common uses:

**Competitive analysis.** You want to understand why a competitor's product feels the way it does. Trace their key surfaces. You now have a structured perceptual portrait you can argue with, copy from, or contrast against.

**Brand archaeology.** You inherit a product or brand without a clear mood document. Trace the existing surfaces to extract the perceptual DNA that is already there. Now you can decide what to preserve, what to evolve, and what to drop.

**Inspiration capture.** You see something you love. Instead of bookmarking the screenshot and forgetting about it, trace it. You now have a structured artifact you can hand to an agent, not just a folder of pretty pictures.

**Self-audit.** Trace your own product, then compare to the `mood.md` you wrote when you started. The gap is where reality drifted from intent. The conversation it provokes is often the most useful thing the protocol produces.

## How to use it

1. Gather your inputs:
   - One or more screenshots of the artifact you're tracing. More is better — a single homepage tells you less than a homepage plus a dashboard plus an email.
   - Copy samples, if the artifact uses text. The voice is part of the mood.
   - Optional: `vocab.md` from the family, so the agent uses shared terminology.
2. Open Claude, Gemini, or ChatGPT. Upload all of the above.
3. Paste the prompt from [`PROMPT.md`](./PROMPT.md).
4. Save the output as a `trace.md`, named for what you traced — e.g. `linear-trace.md` or `competitor-acme-trace.md`.

## Output format

The output is a `trace.md`, using the same structure as `mood.md`. See [`mood-protocol/FORMAT.md`](../mood-protocol/SPEC.md) for the spec.

This means a `trace.md` and a `mood.md` are interchangeable on the consuming side. Any agent that knows how to read one knows how to read the other. The different default filename is just for organisation — when you have a project with three competitor traces and your own mood file, the filenames tell you which is which.

## How it composes with the family

```
existing UI ───► trace-protocol ───► trace.md ─┐
                                                ├─► agent reads either as input
your moodboard ─► mood-protocol ───► mood.md ──┘
```

The two protocols meet in the middle. They produce structurally identical files. They start from different places — your own intent, or someone else's already-out-in-the-world.

A nice composed workflow:

1. Trace three competitors. Get three `trace.md` files.
2. Trace three brands you admire from outside your category. Three more.
3. Make your own moodboard. Run mood-protocol on it.
4. You now have seven structurally identical files in conversation with each other. Read them together to find your own position.

This is what good competitive design strategy looks like, and it has never before been possible to get to in less than a week.

## A worked example

See [`examples/example-linear.md`](./examples/example-linear.md) for a `trace.md` extracted from [Linear](https://linear.app)'s product interface. Useful as a reference for what good output looks like and as a calibration tool when reading your own first drafts.

## A caution

The output of trace-protocol is a reading, not a fact. Two careful designers can produce different `trace.md` files from the same screenshots, and they can both be right. Treat the output as a starting point for argument, not a settled finding. The most useful thing trace-protocol produces is often the disagreement it provokes.

## License

MIT — see the family root.
