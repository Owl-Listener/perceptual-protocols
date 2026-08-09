# tokens-protocol generation prompt

A prompt for generating a `tokens.md` from a token file you already have. Works with Claude, Gemini, or ChatGPT.

This is the one protocol in the family where the model does the boring half and you do the important half. It can read your values. It cannot read your intent. Expect to rewrite the usage columns — that pass is the protocol working, not failing.

## How to use

1. Gather your token source. Any of these work:
   - `tokens.json` or a style-dictionary output
   - `tailwind.config.ts` / `tailwind.config.js`
   - A CSS custom-property block (`:root { --color-... }`)
   - A Figma variables export
   - A screenshot of your Figma variables panel, if that's genuinely all you have
2. Open Claude, Gemini, or ChatGPT.
3. Upload the token source and the `FORMAT.md` from this folder.
4. Optionally upload your `mood.md` or `vocab.md` — the model will use them to propose usage rules that match the intended feel rather than generic defaults.
5. Paste the prompt below.
6. Save the output as `tokens.md` in your project root, then edit the usage columns.

## The prompt

```
You are helping me generate a tokens.md — a semantic annotation layer over a design system that already exists.

A tokens.md doesn't replace my design tokens. It sits above them and tells an agent what each token means and when to reach for it, so that generated UI makes the right choices instead of merely valid ones.

I've uploaded:
- The format spec for tokens.md files (FORMAT.md)
- My actual token source
- Optionally, a mood.md or vocab.md describing how this product is meant to feel

Your job:

1. Fill in the ## Source section first. Name the format and the path of what I gave you. If theming or dark mode is resolved automatically in my source (CSS variables, Figma modes, a data-theme attribute), say so here in one line and use a single value column throughout. If it isn't, add a Dark column to the color tables.

2. Group my raw tokens into semantic roles. If my source already uses semantic naming, keep my names exactly — do not rename them to your preferred convention. If my source is primitives only (blue-500, gray-100), propose a semantic layer and map each semantic name to the primitive it resolves to. Say explicitly that you are proposing, not reporting.

3. For every row, fill in "Use for" and "Do not use for."
   - Where my source or my other files give you evidence for the rule, use it.
   - Where you are guessing, mark the cell with a trailing (?) so I can find every guess in one pass.
   - "Do not use for" must name a plausible misuse — a mistake someone would actually make. If you can't think of one, leave the cell empty rather than filling it with something true but useless.

4. Add the Rules blocks under ## Spacing and ## Motion. These express relationships the individual rows can't: which part of the scale to use within a component versus between sections, and any accessibility rules (prefers-reduced-motion, never animating layout properties).

5. Omit any section my source has no tokens for. Do not emit a section full of placeholders. Instead, list the omitted sections at the end so I know what's missing.

6. Format the output exactly as FORMAT.md specifies. The output is a single complete tokens.md file. Don't wrap it in commentary.

Two constraints:

- Do not invent values. If a value isn't in what I uploaded, leave it out or write [not in source]. A wrong hex in this file gets propagated into generated UI with total confidence, which is worse than a gap.
- Keep it thin. Where a table would restate a long list of values available at the linked source, summarise the scale and its rules instead of copying every row.

If I gave you a mood.md or vocab.md, use it when proposing usage rules — a product briefed as restrained should not get usage rules that reach for the boldest token by default. Note in a comment where you did this.
```

## After the first pass

Search the output for `(?)` and fix every one. That's the real work, and it usually takes twenty minutes.

Then check the things models reliably get wrong:

- **Semantic collisions.** `warning` and `danger` given the same guidance, `info` and `interactive.primary` given the same hex with no note about why.
- **Invented dark values.** If you didn't supply dark tokens, the dark column should say `[not in source]`, not a plausible slate palette.
- **Elevation in dark mode.** Shadows mostly stop working on dark surfaces. If your system solves it with borders or surface lightening instead, say so — no model will guess it.
- **Motion rules quietly dropped.** `prefers-reduced-motion` should be in the rules block. Add it if it isn't.
- **Spacing rules that restate the scale.** *"Use space.4 for 16px gaps"* is circular. The rule should say what relationship the step expresses.

Useful re-prompts:

- *"Every cell you marked (?) — list them with your reasoning so I can correct them in one pass."*
- *"You renamed my tokens. Restore my original names."*
- *"Collapse the color section. It's restating the source instead of pointing at it."*
- *"Which of these usage rules did you derive from my mood.md, and which are generic defaults?"*

## Notes on the output

The output is a single `tokens.md` file. Save it in your project root — ideally in the same repository as the token source it points at, so the two move through review together.

Re-run the prompt when the system changes materially, not when a single value changes. For single values, edit the file by hand or, better, elide the value and let the source carry it.
