# Prompting from mood.md

A mood.md file contains most of what you need to write a strong image generation prompt. This guide shows how to map each section to prompt elements, with syntax for the major generation tools.

---

## How mood.md maps to a prompt

| mood.md section | Maps to |
|---|---|
| `## Essence` | Opening scene or atmosphere description |
| `## Colour` | Color palette, temperature, contrast modifiers |
| `## Texture & Material` | Surface and material descriptors |
| `## Emotional Register` | Mood and atmosphere qualifiers |
| `## Typography` | Style era and visual character (not type itself) |
| `## Design Principles` | Style constraints and aesthetic direction |
| `## References` | Style reference anchors |
| `## Anti-References` | Negative prompts — what to explicitly exclude |

---

## Prompt structure

Build your prompt in this order. Each layer adds specificity without overloading the front.

[Subject or scene] + [Atmosphere from Essence] + [Material/texture] + [Color palette] + [Style anchors from References] + [Technical parameters]


**Negative prompt / exclusions** (from Anti-References) are handled separately in each tool — see below.

---

## Worked example

Given a mood.md with:

- **Essence:** "The quiet of a library at closing time. Dust and amber. Things that have been touched many times."
- **Colour:** Warm ochre, aged paper (#e8d5a3), deep walnut (#3d2b1f), soft shadow
- **Texture & Material:** Worn linen, foxed paper, cracked leather, patinated brass
- **Emotional Register:** Contemplative, unhurried, slightly melancholic
- **References:** Wes Anderson still life, 1970s Penguin book covers
- **Anti-References:** Minimalism, cold lighting, digital flatness, high contrast

**Assembled prompt:**

> Quiet interior, late afternoon light, amber and ochre palette, worn linen and aged paper textures, cracked leather, patinated brass details, contemplative atmosphere, Wes Anderson still life composition, 1970s Penguin book cover aesthetic, soft shadows, film grain

**Negative prompt:**

> minimalist, cold light, high contrast, digital, flat design, neon, stark white

---

## Tool-specific syntax

### Midjourney

[prompt] --ar 3:2 --v 6.1 --style raw


- Use `--no` for exclusions from your Anti-References: `--no minimalist, cold light, digital`
- Use `--sref [image URL]` to anchor to a visual reference from your References section
- Use `--cref [image URL]` to maintain character/subject consistency across a series
- `--style raw` gives more literal interpretation — good when your mood.md is already specific
- Pull hex values from your Colour section directly into the prompt: `ochre #e8d5a3, deep walnut #3d2b1f`

**Example:**
Quiet interior still life, amber and ochre light, aged paper texture, worn linen, patinated brass, contemplative, Wes Anderson composition, 1970s print aesthetic, film grain --ar 3:2 --v 6.1 --style raw --no minimalist, cold light, high contrast, digital, flat


---

### DALL-E 3

DALL-E 3 responds well to natural language. Write the prompt as a descriptive sentence rather than a keyword list — it handles nuance better than most tools.

- Paste your Essence section almost verbatim as the opening
- Describe colors semantically first, then add hex values in brackets
- State exclusions directly: "avoid minimalism, cold lighting, and digital flatness"
- DALL-E 3 doesn't have a separate negative prompt field — weave exclusions into the prompt

**Example:**
A quiet interior at closing time, amber afternoon light filtering through dust. Warm ochre and aged paper tones (#e8d5a3), deep walnut shadows (#3d2b1f). Worn linen, cracked leather, patinated brass. Contemplative and unhurried atmosphere. Composed like a Wes Anderson still life, with the graphic character of a 1970s Penguin book cover. Avoid minimalism, cold lighting, high contrast, and anything that feels digital or flat.


---

### Adobe Firefly

Firefly works well with mood.md because it's trained on licensed content and handles aesthetic style references reliably.

- Use **Content type** setting to match your medium (Photo, Graphic, Art)
- Use **Style** → **Movements** to anchor to aesthetic references from your References section
- Add colors from your Colour section via the **Color and tone** panel — enter hex values directly
- Use **Effects** → **Lighting** to match the light quality described in your Essence
- Paste Anti-References into the **Avoid** field

**Firefly-specific tip:** Firefly handles material and texture descriptions particularly well — pull directly from your `## Texture & Material` section.

---

### Stable Diffusion (with a UI like Automatic1111 or ComfyUI)

SD separates positive and negative prompts explicitly, which maps cleanly to mood.md's References and Anti-References sections.

**Positive prompt** — combine Essence + Colour + Texture + References:
[scene], [atmosphere from Essence], [colors], [textures and materials], [style references], [lighting], film grain, analog


**Negative prompt** — paste directly from Anti-References:

minimalist, cold light, high contrast, digital art, flat design, neon, oversaturated, modern, CGI


**Useful additions:**
- Add LoRA weights for specific aesthetic styles referenced in your mood.md
- Use the Color correction node in ComfyUI to clamp output to your hex palette
- Use `[style], by [reference artist/era]` rather than named individuals where possible

---

## Maintaining consistency across a series

When generating multiple images from the same mood.md:

1. **Keep the base prompt fixed.** Only change the subject or scene — the atmospheric and stylistic modifiers stay identical across every generation.

2. **Use style references.** In Midjourney, use `--sref` with an approved image from your first generation. In Firefly, use **Reference image**. This anchors subsequent images to the established visual language.

3. **Lock your seed.** In SD and Midjourney (`--seed`), reusing the seed with small prompt variations produces more coherent visual families.

4. **Save your assembled prompt.** Once you have a prompt that feels true to the mood.md, save it alongside the file as `[moodname]-prompt.txt`. Treat it as the verbal equivalent of the moodboard.

---

## Updating mood.md from generated outputs

Generation is iterative. If you produce an image that better captures the mood than your original references, feed it back:

1. Add the generated image to your mood folder prefixed with `ref-` (e.g. `ref-first-pass.jpg`)
2. Re-run `generate_mood.py` — the new image will inform the next version of mood.md
3. Update your assembled prompt to reflect any new language the regenerated mood.md introduces

This keeps mood.md as a living document rather than a one-time brief.




