# vocab-protocol extraction prompt

A prompt for extracting a project-specific perceptual vocabulary from references you supply. Works with Claude, Gemini, or ChatGPT — any model that can read images and text.

## How to use

1. Gather your references:
   - **3 to 5 examples of work that feels right** for the project — screenshots, photos, links, anything you can upload
   - **2 to 3 anti-references** — work that feels wrong, in ways you can point to
   - **Optional:** a moodboard, an existing brand book, or an existing `mood.md`
2. Open Claude, Gemini, or ChatGPT.
3. Upload the images and any text documents.
4. Also upload (or paste in) the canonical `vocab.md` and the `FORMAT.md` from this folder. The model needs them to know the target format and the starter terms.
5. Paste the prompt below.
6. Save the output as `vocab.md` in your project.

## The prompt

```
You are helping me extract a perceptual vocabulary from the references I've uploaded.

A perceptual vocabulary is a small set of aesthetic qualities — terms like "warmth," "restraint," "density," "intimacy" — that describe how a product should feel. The vocabulary is used to brief AI agents so they can apply the right qualities when generating design work.

I've uploaded:
- A canonical starter vocabulary of 10 terms (vocab.md)
- The format spec for vocab.md files (FORMAT.md)
- 3–5 references that capture how the project should feel
- 2–3 anti-references that capture how it should not feel

Your job:

1. Identify which of the 10 canonical terms apply to my project, based on the references. Don't include canonical terms that aren't supported by the references — half a vocabulary is more useful than a complete-but-vague one.

2. Propose 2–5 new project-specific terms that capture qualities the canonical vocabulary doesn't cover. These should:
   - Show up repeatedly in the references (not just once)
   - Be distinctive to this project's aesthetic
   - Be designer-recognisable (a real word designers would say)
   - Be agent-actionable (the agent could produce a different output when asked for more or less of this quality)

3. For each term in your output (canonical and new), include:
   - A one-sentence definition
   - A "When it applies" paragraph
   - 2–3 references drawn from the work I've uploaded, anchored to specific images or sections
   - 2–3 anti-references, drawn from my anti-reference uploads or specific named categories of work that wouldn't embody the term
   - Optional: which other terms it pairs well with, and which it sits in tension with

4. Format the output exactly as FORMAT.md specifies. The output is a single complete vocab.md file. Don't wrap it in commentary, apology, or summary.

Write in the voice of a careful editor: confident, specific, no filler. The agent reading this file later will only have your words to go on. Make them earn their place.

If you're proposing a new term, briefly justify why in a comment line (Markdown HTML comment) above the term so I can decide whether to keep it.

If you can't anchor a term to the references with confidence, omit it. A smaller, sharper vocabulary is the goal.
```

## Notes on iteration

The first output will be useful. The second will be better.

After reading the first pass, push back on the things that feel generic. Useful re-prompts:

- *"These three terms feel generic. Rework them to be more specific to my references."*
- *"You missed the quality I'd describe as [name]. Add it, with anchors from the references."*
- *"The anti-references for [term] feel weak. Sharpen them."*
- *"Drop any term that doesn't have at least two clear anchors in the references I uploaded."*

The vocabulary is a working document. Treat the model's first draft like a junior copywriter's — full of promise, half-edited, worth your attention.

## Notes on the output

The output is a single `vocab.md` file. Save it in your project alongside `mood.md` if you have one. Both files are intended to be read together by any agent generating design work.

If you find a term in your custom vocabulary that you think belongs in the canonical set, send a pull request to the family root with the entry.
