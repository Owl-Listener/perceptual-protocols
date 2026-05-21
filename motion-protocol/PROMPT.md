# motion-protocol extraction prompt

A prompt for extracting a project-specific motion vocabulary from references you supply. Works with Claude, Gemini, or ChatGPT — any model that can read images, video where supported, and text.

## How to use

1. Gather your inputs (any combination of these — more is better, but any one of them is enough to start):
   - **Short videos or GIFs** of motion you want to capture (5–15 seconds each, ideally)
   - **CSS or animation code samples** — lossless for the technical anchors
   - **Live URLs** you can describe in writing
   - **Written descriptions** of how things should move — what designers do informally
   - **Reference screenshots** with timing notes ("this transition takes about 300ms")
2. Open Claude, Gemini, or ChatGPT.
3. Upload everything you've gathered.
4. Also upload (or paste in) the canonical `motion.md` and `FORMAT.md` from this folder.
5. Paste the prompt below.
6. Save the output as `motion.md` in your project.

## The prompt

```
You are helping me extract a motion vocabulary for my product from the references I've uploaded.

A motion vocabulary is a small set of motion qualities — terms like "snappy," "calm," "mechanical," "springy" — that describe how a product should move. The vocabulary is used to brief AI agents so they can apply the right motion qualities when generating animations, transitions, or interactive behaviour.

I've uploaded:
- A canonical starter motion vocabulary of 8 terms (motion.md)
- The format spec for motion.md files (FORMAT.md)
- References that capture how the project should move — these may be videos, GIFs, code samples, URLs, written descriptions, or any combination

Your job:

1. Identify which of the 8 canonical terms apply to my project, based on the references. Don't include canonical terms that aren't supported by what I've uploaded — a smaller, sharper vocabulary is the goal.

2. Propose 2–5 new project-specific terms if the canonical vocabulary doesn't cover qualities that show up repeatedly in the references. These should:
   - Show up in multiple references (not just one)
   - Be distinctive to this project's motion identity
   - Be designer-recognisable (a real word designers would say about motion)
   - Be agent-actionable (the agent can produce a measurably different output when asked for more or less of this)
   - Be technically anchorable (there's a range of durations / easings / sequencing patterns that consistently produce it)

3. For each term in your output (canonical and new), include:
   - A one-sentence definition
   - A "When it applies" paragraph
   - 2–3 references drawn from the work I've uploaded, with timing details where observable
   - Technical anchors — duration ranges, easing curves, gesture response times, what the term avoids
   - 2–3 anti-references — specific or category-level
   - Pairs and tensions with other motion terms

4. Format the output exactly as FORMAT.md specifies. The output is a single complete motion.md file.

5. If a reference is a video or GIF I uploaded but you can't access motion data directly, work from the key frames and ask me to confirm timing details rather than guessing.

6. Be opinionated. A motion.md that says "everything is moderately snappy" has done none of the work. Make actual calls about what motion this product does and doesn't do.

7. Name tensions explicitly. If the references contain conflicting motion identities (the marketing site is theatrical, the product is mechanical), surface that — don't smooth it over.

Write in the voice of a careful design critic. Specific. Anchored. The agent reading this file later will only have your words to go on. Make them earn their place.
```

## Notes on iteration

Motion is harder to extract on a first pass than static qualities. Push back specifically. Useful re-prompts:

- "You said snappy — what's the actual timing in the reference? Anchor it."
- "You included 'glassy' but I don't see it in the references. Either anchor it to a specific moment or drop it."
- "You missed the springiness of the [specific element]. Re-examine."
- "Your technical anchors are too vague. 'Fast' is not a timing. Give me ranges."
- "Take the CSS samples I uploaded seriously — the easing values are right there."

## Notes on input quality

The output is only as good as what you upload. Some tips:

- **Short clips beat long ones.** A 5-second video of a single interaction is more useful than a 60-second screen recording.
- **Code samples are gold.** If you have actual CSS, animation library config, or motion specs, include them. Easing values and durations are lossless in code.
- **Don't apologise for written descriptions.** "Buttons feel slightly bouncy on press, about 250ms with overshoot" is a perfectly usable input.
- **Include the non-motion too.** Static moments and pauses are part of a motion identity. A product that mostly doesn't animate has a motion vocabulary of `invisible` and that's worth saying.

## A note on multimodal model variability

Vision models vary in how well they handle video as of 2026. If your model returns generic descriptions of your video uploads ("animations appear smooth"), fall back to:

1. Frame-by-frame screenshots with your own timing annotations
2. Written descriptions paired with code samples
3. Linking to public reference URLs and describing what you see there

The protocol is designed to work with whatever input modality your model handles best. Don't fight the tool.

## Notes on output

The output is a single `motion.md` file. Save it in your project alongside `vocab.md` and `mood.md` if you have them. All three are intended to be read together by any agent generating design work.

If you find a term in your custom motion vocabulary that you think belongs in the canonical set, send a pull request to the family root with the entry.
