# trace-protocol extraction prompt

A prompt for tracing the implicit perceptual mood of an existing UI, brand, or design artifact. Works with Claude, Gemini, or ChatGPT — any model that can read images and text.

## How to use

1. Gather your inputs:
   - 1 or more screenshots/images of the artifact you want to trace
   - Optional: copy samples (if the artifact has text — paste in plain text, or include screenshots with readable typography)
   - Optional: `vocab.md` and `FORMAT.md` from the family root
2. Open Claude, Gemini, or ChatGPT.
3. Upload all of the above.
4. Paste the prompt below.
5. Save the output as a `trace.md`, named for what you traced.

## The prompt

```
You are helping me trace the implicit perceptual mood of an existing UI, brand, or design artifact. I want you to follow its lines and decisions and produce a trace.md — the perceptual brief that would have produced this output, read backwards from the artifact.

I've uploaded:
- [N] images of the artifact
- [optional: copy samples]
- [optional: vocab.md and FORMAT.md from the perceptual-protocols family]

Your job:

Observe carefully. Then produce a trace.md that captures what this artifact is implicitly doing perceptually.

Pay attention to:
- Typography choices — faces, weights, sizes, line heights, system vs hand
- Spatial rhythm — density, breath, hierarchy, the use of negative space
- Colour temperature and saturation
- Materiality — texture, shadow, depth, or their deliberate absence
- Iconography and ornament — or the absence of them
- The voice of any copy visible
- Interaction affordances and their texture — sharpness of corners, button styles, hover states if visible
- Composition and rhythm — how the eye moves
- What is emphasised, what is downplayed, what is deliberately missing

Structure your output as a trace.md (which uses the mood.md format) with these sections:

1. Mood summary — a single paragraph capturing what this artifact feels like.
2. Implied vocabulary — which qualities from vocab.md (or your own perceptual vocabulary if vocab.md isn't provided) does this artifact embody? For each, anchor to specific observations from the images.
3. Implied anti-references — what is this artifact deliberately NOT doing? What would feel wrong here? Be specific. This section is the most useful part of the output. Designers define spaces by their boundaries.
4. Choices that produced this mood — name the specific design decisions that create the feeling. Typography choice. Spacing system. Restraint patterns. Anything worth naming.
5. Cultural or temporal context — if the artifact is of a particular era, region, design tradition, or technological generation, name it.
6. Confidence and uncertainty — flag observations where you're not sure whether the effect is intentional or accidental. Flag observations the images don't have enough information to verify.

Write in the voice of a careful design critic. Specific. Anchored. Not hedging more than necessary. Do not invent qualities the artifact doesn't show. If you can't see something, don't claim it.

The output is a single complete trace.md. Don't wrap it in commentary, summary, or apology.
```

## Notes on iteration

The first pass will be useful but generic. The second pass, after specific pushback, will be much sharper.

Useful re-prompts:

- "You said warmth — anchor that to a specific element. What in the image makes you feel that?"
- "I don't see materiality here. Re-examine."
- "Add more anti-references. What would this design definitely not do?"
- "Take the copy seriously as part of the mood, not as filler."
- "You're hedging too much. Commit to a reading."

## Notes on input quality

The output is only as good as what you upload. Some tips:

- **More than one screen.** A single homepage misleads. A homepage plus a dashboard plus an empty state plus an email gives the real signature.
- **Don't crop creatively.** Let the agent see the full surface, including the parts that might seem incidental. Footers, marginalia, and empty states are often where the mood is most honest.
- **Include the copy.** A UI without its words is half a UI. Paste copy in plain text alongside, or screenshot pages with their typography readable.
- **For brand archaeology especially:** include the oldest surfaces alongside the newest. Drift is usually visible in the gap between them.

## A note on respect

The output of trace-protocol is a reading of someone else's work. Be careful with it. Treat the traced mood as something to learn from, not something to mock. Anti-references should be specific but not punching down — name categories ("a typical SaaS dashboard," "a consumer task app") rather than competitor brands when the contrast is the point.
