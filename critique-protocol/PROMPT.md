# critique-protocol prompt

A prompt for producing a structured `critique.md` of agent output against a mood and vocabulary. Works with Claude, Gemini, or ChatGPT.

## How to use

1. Gather your inputs:
   - The `mood.md` (or `trace.md`) the work was briefed against
   - The `vocab.md` whose terms you used in the brief
   - The `FORMAT.md` from this folder
   - The output being critiqued — screenshots, copy, links, or a description of the artifact
2. Open Claude, Gemini, or ChatGPT.
3. Upload all of the above.
4. Paste the prompt below.
5. Save the output as a `critique.md` in your project.

## The prompt

```
You are helping me critique a piece of work against the perceptual brief it was generated from. I want a structured critique.md that is anchored, two-sided, actionable, and honest about uncertainty.

I've uploaded:
- mood.md — the perceptual intent the work was briefed against
- vocab.md — the shared vocabulary whose terms are used in the brief
- FORMAT.md — the spec for what a critique.md should look like
- The output being critiqued — [images / copy / description]

Your job:

1. Identify which qualities from mood.md and vocab.md the output is supposed to embody. Treat these as the criteria for the critique.

2. For each criterion, decide whether the output embodies it, partially embodies it, or contradicts it. Anchor every decision to a specific element in the output. No floating adjectives.

3. Structure your output as a critique.md per FORMAT.md, with these sections:
   - Verdict: 1–3 sentences. How well does the output land?
   - What's working: by quality, with "Where" and "Why it works."
   - What's not working: by quality, with "Where," "Mismatch," and a concrete "Suggested move."
   - Tensions surfaced: places where the critique uncovered ambiguity in the brief itself.
   - What I'm unsure about: places where the critique is genuinely uncertain.
   - Next iteration: 2–3 concrete suggestions for the next pass.

4. Be specific. "Lacks warmth" is not a critique. "Lacks warmth — the headline uses a geometric sans-serif which reads efficient but not generous; the brief called for warmth via serif-leaning typography. Suggested move: try Source Serif or similar, increase line height" is.

5. Be two-sided. Always note what works alongside what doesn't. If you genuinely cannot find anything working, say so explicitly and consider whether the brief itself was unachievable.

6. Be actionable. Every "What's not working" entry needs a "Suggested move." If you cannot propose one, move the observation to "What I'm unsure about" and say so.

7. Be honest about uncertainty. Grade your confidence. A critique that pretends certainty about everything is suspect.

The output is a single complete critique.md. Don't wrap it in commentary, summary, or apology.
```

## Notes on iteration

The first pass will be useful but often soft. Useful re-prompts:

- "You said the headline lacks warmth — be more specific about which words in the headline are the problem and what specifically to change."
- "You missed the issue with the CTA. Look at the colour and re-critique."
- "The 'What's not working' entries don't have suggested moves. Add them."
- "You're hedging too much. Commit to a reading where the evidence supports it."
- "The verdict is too generous. The brief asked for X, the output is doing Y. Say so."

## Notes on what makes a critique useful

A few signals that distinguish a useful `critique.md` from a soft one:

- **Specificity.** Every observation points to a named element and a named quality.
- **Asymmetry.** Most outputs have a few things working and several things not. A critique that says "broadly working" is usually flattering the work.
- **Actionability.** The "Next iteration" section should give the agent enough to actually produce a different output on the next pass. If it would only produce the same kind of generic output again, the critique was too soft.
- **Honesty about the brief.** Sometimes the output failed because the brief was unachievable, contradictory, or vague. A critique that surfaces this is more valuable than one that blames the agent for a gap that lives in the intent.

## Critique in a team setting

A `critique.md` is a useful artifact even when no agent will read it. Used between human collaborators, it works like a structured comment thread on a Figma file — anchored, two-sided, actionable. If the next iteration is a designer's hand-pass rather than an agent's regeneration, the critique still does the same work.
