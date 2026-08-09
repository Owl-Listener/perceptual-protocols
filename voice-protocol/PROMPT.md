# voice-protocol extraction prompt

A prompt for extracting a `voice.md` from writing your brand has already published. Works with Claude, Gemini, or ChatGPT — any model that can read text.

Most brands don't need to invent a voice. They need to describe the one already showing up in their best writing, so an agent can keep doing it.

## How to use

1. Gather your samples:
   - **5 to 10 pieces of copy that sound right** — landing page sections, onboarding flows, error messages, release notes, a founder's post, support replies. Spread them across surfaces if you can; the tonal range section depends on it.
   - **2 to 3 counter-samples** — copy that is technically fine and tonally wrong. Drafts you rejected work well. So does competitor copy you'd never ship.
   - **Optional:** an existing brand voice guideline, an existing `mood.md`, or a `vocab.md`.
2. Open Claude, Gemini, or ChatGPT.
3. Upload the samples and the `FORMAT.md` from this folder. The model needs the format spec to know the target shape.
4. Paste the prompt below.
5. Save the output as `voice.md` in your project root.

## The prompt

```
You are helping me extract a voice specification from writing my brand has already published.

A voice.md is a structured description of how a brand writes — personality, how the tone shifts by context, enforceable mechanics, vocabulary, and a calibration pair. It is used to brief AI agents so the copy they generate sounds like us instead of sounding like an AI.

I've uploaded:
- The format spec for voice.md files (FORMAT.md)
- 5-10 samples of copy that sound right
- 2-3 counter-samples that sound wrong

Your job:

1. Read the samples and infer 3-5 personality descriptors. Each descriptor must carry a contrast — the line the voice doesn't cross ("Direct — but never blunt"). Derive the contrast from the samples where you can: if the writing is direct but consistently softens the landing, the contrast is real and you should name what it is. Don't pad to five. Three sharp descriptors beat five vague ones.

2. Build the tonal range table from the surfaces actually represented in my samples. Add a row only where I gave you evidence. If I gave you no error messages, don't invent an error-message register — instead, list the missing surfaces at the end so I know what to go and collect.

3. Extract mechanics that are genuinely enforceable — rules a reviewer could apply to a string they've never seen, without asking me. Count sentence lengths, check whether contractions appear, check whether exclamation marks appear, check person and address, check whether headings are sentence case or title case. Report what the samples actually do, not what you assume good writing does. Where the samples are inconsistent, say so rather than picking one and presenting it as a rule.

4. Build the vocabulary tables. For "Use," pull words and phrases that recur across samples and carry brand meaning. For "Avoid," pull from the counter-samples — and give the reason, not just the word, so the rule generalises past that exact term. For brand-specific terms, note capitalisation and any term used in a non-obvious way.

5. For the Reference section, quote the single strongest sample verbatim as "This is the voice." Then use a counter-sample, or write generic AI copy for the same context, as "This is not the voice." Add one line naming exactly what's wrong with it.

6. Format the output exactly as FORMAT.md specifies. The output is a single complete voice.md file. Don't wrap it in commentary, apology, or summary.

Two things to be careful about:

- Quote real lines from my samples wherever the format calls for an example. Don't paraphrase them into something smoother. The roughness is the data.
- Where you're inferring rather than observing, mark the line with a Markdown HTML comment saying what you inferred it from, so I can check your reasoning and delete what you got wrong.

If the samples don't support a section, say so instead of filling it. A half-complete voice.md anchored in real writing is more useful than a complete one you made up.
```

## Notes on iteration

The first output will be recognisable but generic. The second will be usable.

Useful re-prompts:

- *"These descriptors would fit any competent B2B brand. What is distinctive about how we write, specifically?"*
- *"The mechanics section is a list of writing best practices. Cut anything that isn't actually observable in my samples."*
- *"You missed the thing I'd describe as [name]. Find it in the samples or tell me it isn't there."*
- *"The avoid list has words, not reasons. Give me the reason for each one."*
- *"Show me the three lines from my samples that most support the descriptor 'calm'."*

That last one is worth running on every descriptor. If the model can't produce three supporting lines, the descriptor is aspirational and should come out.

## Notes on the output

The output is a single `voice.md` file. Save it in your project root alongside `mood.md` and `tokens.md` if you have them. All three are intended to be read together by any agent generating work.

Treat the file as a working document. Voice drifts, and a `voice.md` that hasn't been revised since the brand's early copy will quietly brief agents to write like a company that no longer exists.
