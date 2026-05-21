# mood-protocol prompt

Use this prompt with any AI that supports image input (Claude, Gemini, ChatGPT, etc.)

## How to use

1. Open your AI assistant (claude.ai, gemini.google.com, chatgpt.com)
2. Upload your moodboard images (screenshots, reference images, palette exports)
3. Paste the prompt below
4. Save the output as `mood.md` in your project

That's it. No setup, no API keys, no code.

## Tips before you paste

- The best input is a screenshot of your annotated Figma/Miro canvas, sticky notes and all
- Include anti-references (things you DON'T want) and mention them in the prompt
- Name anti-reference images with a `not-` or `anti-` prefix — e.g. `not-corporate-dashboard.png`, `anti-pattern.jpg` — so the prompt below can treat them correctly
- Add your own notes alongside the prompt, e.g., "This is for a reading app. Think Kinfolk meets Stripe."
- Name your mood something evocative, not generic

---

## The prompt

Copy everything below this line:

---

You are an expert design director analysing a moodboard.

I've uploaded images that represent the visual direction for a project. These might include annotated Figma canvases (with sticky notes and labels), individual reference images, typography specimens, colour palettes, or anti-references (things I explicitly don't want).

Your job is NOT to describe what's literally in each image. Your job is to extract the DESIGN INTENT — what these images collectively communicate about how something should look and feel.

Think like a designer receiving a moodboard from a creative director. Pay close attention to any handwritten notes, sticky notes, annotations, or labels visible in the images — these are direct commentary and should be weighted heavily.

If any uploaded image's filename begins with `not-` or `anti-` (e.g. `not-corporate.png`, `anti-pattern.jpg`), treat that image as an anti-reference: something the mood must explicitly NOT look or feel like. Do not absorb its aesthetic into the mood; instead, use it to populate the Anti-References section with specific things to avoid. Only that exact prefix counts — filenames like `notebook-ui.png` or `antique-type.png` are normal references.

**The mood is called: [REPLACE WITH YOUR MOOD NAME]**

**My notes: [REPLACE WITH YOUR THOUGHTS, OR DELETE THIS LINE]**

Generate a structured mood file in this exact format:

# Mood: [Name]

## Essence
[2-3 sentences capturing the overall feeling. Write this as a creative direction brief — evocative, specific, actionable. Not "modern and clean" but something a designer could actually work from.]

## Colour
- **Temperature:** [warm / cool / neutral + nuance]
- **Palette:** [list key colours as hex values with semantic names, e.g., #1a1a2e "deep night"]
- **Contrast:** [high / medium / low + how contrast is used]
- **Saturation:** [vivid / muted / desaturated + character]

## Typography
- **Character:** [describe the typographic personality]
- **Weight distribution:** [how type weight creates hierarchy]
- **Density:** [airy / balanced / compact + what that achieves]
- **Suggested pairings:** [if detectable, suggest font pairings or categories]

## Space & Layout
- **Rhythm:** [how space is used — generous, dense, asymmetric, etc.]
- **Grid character:** [rigid / fluid / broken + intent]
- **Scale relationships:** [how size contrast creates hierarchy]

## Texture & Material
- **Surface quality:** [flat / tactile / layered / dimensional]
- **Material references:** [what physical materials this evokes]
- **Finish:** [matte / glossy / rough / polished]

## Emotional Register
[A short paragraph — how should someone FEEL using/viewing the designed thing? Be specific and evocative. Reference cultural touchpoints if relevant.]

## Design Principles
[3-5 short principles extracted from the moodboard that should guide decisions.
Format: **Principle name** — one-sentence explanation.]

## References
[For each image analysed, a brief note on what design signal it contributes. Include any visible annotations or notes from the designer.]

## Anti-References
[Things this mood explicitly is NOT. If anti-reference images were provided, describe what they signal to avoid. If none were provided, infer from the overall direction what would clash with it.]

## Agent Instructions
[A concise paragraph written directly to an AI agent, telling it how to apply this mood when generating UI, choosing colours, writing CSS, or making design decisions. Be specific and actionable.]

Important:
- Extract actual hex colour values where visible
- If you can see annotations or sticky notes, quote them
- Be specific, not generic. "Warm" means nothing. "The warmth of a dimly lit bookshop at 6pm" is useful
- The Agent Instructions section is critical — this is what makes the file actually work in practice
