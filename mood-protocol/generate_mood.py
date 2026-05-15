#!/usr/bin/env python3
"""
mood-protocol: Generate a mood.md from a folder of visual references.

Drop images into a /mood/ folder — screenshots of Figma moodboards,
colour palettes, typography samples, spatial references, annotated canvases —
and this script will read them through a vision model and generate a
structured mood.md that any AI agent can use for design direction.

Usage:
    python generate_mood.py                           # scans ./mood/ → generates ./mood.md
    python generate_mood.py --model gemini            # use Gemini instead of Claude
    python generate_mood.py --input ./my-refs         # custom input folder
    python generate_mood.py --output ./project        # custom output location
    python generate_mood.py --name "Brand V2"         # give the mood a name
    python generate_mood.py --claude-model <id>       # pin a specific Claude snapshot
    python generate_mood.py --gemini-model <id>       # pin a specific Gemini model
    python generate_mood.py --max-tokens 16384        # raise the output cap for dense moods
    python generate_mood.py --dry-run                 # preview the prompt; no API call, no tokens

Requires (install only what you need):
    For Claude:   python -m pip install -r requirements-claude.txt  + set ANTHROPIC_API_KEY
    For Gemini:   python -m pip install -r requirements-gemini.txt  + set GEMINI_API_KEY

    (Bare 'pip install anthropic' / 'pip install google-genai' also works.)
"""

import base64
import argparse
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Image handling
# ---------------------------------------------------------------------------
# These are the image types both Claude and Gemini vision can process.
# We ignore everything else (PDFs, .ai files, etc.)

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

# Spec version stamped into the footer of every generated mood.md, per SPEC.md.
SPEC_VERSION = "0.1.0"

# Default model strings. Override on the CLI with --claude-model / --gemini-model
# when a newer snapshot is out, so the script doesn't rot as models are retired.
DEFAULT_CLAUDE_MODEL = "claude-sonnet-4-20250514"
DEFAULT_GEMINI_MODEL = "gemini-2.5-flash"

# A dense mood.md with many images, references, and anti-references can run
# long. 8192 gives comfortable headroom; override with --max-tokens if needed.
DEFAULT_MAX_TOKENS = 8192


def get_image_media_type(filepath: Path) -> str:
    """
    Maps a file extension to the MIME type the API expects.
    Think of this as telling the API "this is a JPEG" vs "this is a PNG"
    so it knows how to decode the image data.
    """
    extension_to_mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    return extension_to_mime[filepath.suffix.lower()]


def encode_image_to_base64(filepath: Path) -> str:
    """
    Reads an image file and converts it to base64 text.

    Why base64? The API can't receive a file directly — it needs the image
    data embedded in the JSON request. Base64 is a way of encoding binary
    data (the image) as plain text characters. It's like putting a painting
    in an envelope by describing every pixel as a letter.
    """
    with open(filepath, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def read_image_bytes(filepath: Path) -> bytes:
    """
    Reads the raw bytes of an image file.
    Gemini's SDK can work with raw bytes directly, so we don't always
    need the base64 step.
    """
    with open(filepath, "rb") as f:
        return f.read()


ANTI_REFERENCE_PREFIXES = ("not-", "anti-")


def is_anti_reference(image_path: Path) -> bool:
    """
    An image is treated as an anti-reference ("what to avoid") when its
    filename starts with `not-` or `anti-`, per SPEC.md. Using a prefix —
    not a substring — avoids false-positives on filenames like
    `notebook-ui.png` or `antique-type.png`.
    """
    return image_path.stem.lower().startswith(ANTI_REFERENCE_PREFIXES)


def collect_images(folder: Path) -> list[Path]:
    """
    Scans the mood folder and returns all supported image files,
    sorted alphabetically so the output is deterministic
    (same input → same order every time).
    """
    images = [
        f for f in folder.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
    images.sort(key=lambda f: f.name.lower())
    return images


# ---------------------------------------------------------------------------
# Notes handling
# ---------------------------------------------------------------------------

def read_notes(folder: Path) -> str | None:
    """
    Checks if the designer left a notes.md in the mood folder.
    This is optional — it lets you add freeform thoughts like
    "I want this to feel like a Sunday morning magazine" or
    "NOT corporate, NOT glassmorphic."
    """
    notes_path = folder / "notes.md"
    if notes_path.exists():
        return notes_path.read_text(encoding="utf-8").strip()
    return None


# ---------------------------------------------------------------------------
# The vision prompt — this is the core craft of the whole tool
# ---------------------------------------------------------------------------
# IMPORTANT: This prompt is IDENTICAL for both Claude and Gemini.
# That's the whole point of a protocol — the design intelligence
# lives in the prompt, not in the API plumbing.

SYSTEM_PROMPT = """You are an expert design director analysing a moodboard.

You are looking at images that a designer has curated to communicate the visual 
direction for a project. These might be:
- Screenshots of annotated Figma moodboard canvases (with sticky notes, labels, groupings)
- Individual reference images (photography, UI screenshots, textures, palettes)
- Typography specimens or colour palette exports
- Anti-references (things the designer explicitly does NOT want)

Your job is NOT to describe what's literally in each image. Your job is to 
extract the DESIGN INTENT — what these images collectively communicate about 
how something should look and feel.

Think like a designer receiving a moodboard from a creative director. Ask yourself:
- What's the emotional register here?
- What colour temperature and palette is being established?
- What typographic character is being signalled?
- How dense or spacious should the result feel?
- What material/surface qualities are being referenced?
- What era, movement, or cultural references are present?
- What is being explicitly rejected (anti-references)?

Pay close attention to any handwritten notes, sticky notes, annotations, or 
labels visible in the images — these are the designer's direct commentary and 
should be weighted heavily.

If a filename begins with the prefix "not-" or "anti-" (e.g. not-corporate.png,
anti-pattern.jpg), treat that image as an anti-reference (what to avoid).
Only the documented prefixes count — filenames like "notebook-ui.png" or
"antique-type.png" are normal references, not anti-references."""


def build_user_prompt(images: list[Path], notes: str | None, mood_name: str) -> str:
    """
    Builds the prompt that tells the vision model what we want back.
    The structure here mirrors the mood.md format we want generated.
    This prompt is shared by ALL backends — the protocol is model-agnostic.

    Positive references and anti-references are listed in two clearly
    labelled blocks so the model doesn't have to infer the distinction
    from filename heuristics. The classification uses is_anti_reference,
    matching the convention in SPEC.md.
    """
    references = [img.name for img in images if not is_anti_reference(img)]
    anti_references = [img.name for img in images if is_anti_reference(img)]

    prompt = f"""Analyse this moodboard and generate a structured mood file called "{mood_name}".

The attached images fall into two groups:

References — absorb these into the mood:
"""
    prompt += "\n".join(f"- {name}" for name in references) if references else "- (none)"
    prompt += "\n\nAnti-references — the mood must explicitly NOT look or feel like these. Do not absorb their aesthetic; instead, use them to populate the Anti-References section with specific things to avoid:\n"
    prompt += "\n".join(f"- {name}" for name in anti_references) if anti_references else "- (none provided)"
    prompt += "\n\n"

    if notes:
        prompt += f"""The designer also left these notes:

---
{notes}
---

Weight these notes heavily — they represent direct intent.

"""

    prompt += """Generate the mood file in this exact markdown structure:

# Mood: [Name]

## Essence
[2-3 sentences capturing the overall feeling. Write this as a creative direction 
brief — evocative, specific, actionable. Not "modern and clean" but something a 
designer could actually work from.]

## Colour
- **Temperature:** [warm / cool / neutral + nuance]
- **Palette:** [list key colours as hex values with semantic names, e.g., #1a1a2e "deep night"]
- **Contrast:** [high / medium / low + how contrast is used]
- **Saturation:** [vivid / muted / desaturated + character]

## Typography
- **Character:** [describe the typographic personality — e.g., "editorial serif with quiet authority"]
- **Weight distribution:** [how type weight creates hierarchy]
- **Density:** [airy / balanced / compact + what that achieves]
- **Suggested pairings:** [if detectable, suggest font pairings or categories]

## Space & Layout
- **Rhythm:** [how space is used — generous, dense, asymmetric, etc.]
- **Grid character:** [rigid / fluid / broken + intent]
- **Scale relationships:** [how size contrast creates hierarchy]

## Texture & Material
- **Surface quality:** [flat / tactile / layered / dimensional]
- **Material references:** [what physical materials this evokes — paper, glass, stone, fabric]
- **Finish:** [matte / glossy / rough / polished]

## Emotional Register
[A short paragraph — how should someone FEEL using/viewing the designed thing? 
Be specific and evocative. Reference cultural touchpoints if relevant.]

## Design Principles
[3-5 short principles extracted from the moodboard that should guide decisions.
Format: **Principle name** — one-sentence explanation.]

## References
[For each image analysed, a brief note on what design signal it contributes.
Include any visible annotations or notes from the designer.]

## Anti-References
[Things this mood explicitly is NOT. If anti-reference images were provided, 
describe what they signal to avoid. If none were provided, infer from the 
overall direction what would clash with it.]

## Agent Instructions
[A concise paragraph written directly to an AI agent, telling it how to apply 
this mood when generating UI, choosing colours, writing CSS, or making design 
decisions. Be specific and actionable.]

Important:
- Extract actual hex colour values where visible in palette images
- If you can see annotations or sticky notes, quote them
- Be specific, not generic. "Warm" means nothing. "The warmth of a dimly lit 
  bookshop at 6pm" is useful.
- The Agent Instructions section is critical — this is what makes the file 
  actually work in practice."""

    return prompt


# ---------------------------------------------------------------------------
# Backend: Claude (Anthropic)
# ---------------------------------------------------------------------------

def analyse_with_claude(
    images: list[Path],
    notes: str | None,
    mood_name: str,
    model: str,
    max_tokens: int,
) -> str:
    """
    Sends all the moodboard images to Claude's vision API.

    We import anthropic HERE rather than at the top of the file.
    Why? So people who only use Gemini don't need to install the
    anthropic package, and vice versa. The import only happens
    when you actually choose this backend.
    """
    try:
        import anthropic
    except ImportError:
        print("\n  ✗ anthropic package not installed.")
        print("    Run: pip install anthropic")
        print("    And set ANTHROPIC_API_KEY in your environment.\n")
        sys.exit(1)

    client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY from environment

    # Build the message content: alternating images and their filenames
    # so the model knows which image is which
    content = []
    for image_path in images:
        content.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": get_image_media_type(image_path),
                "data": encode_image_to_base64(image_path),
            },
        })
        content.append({
            "type": "text",
            "text": f"[Image: {image_path.name}]",
        })

    # Add the main analysis prompt at the end
    content.append({
        "type": "text",
        "text": build_user_prompt(images, notes, mood_name),
    })

    print(f"  Sending {len(images)} images to Claude ({model}) for analysis...")
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": content}],
    )

    stop_reason = getattr(response, "stop_reason", None)

    # A refusal comes back with stop_reason="refusal" in newer Claude models.
    if stop_reason == "refusal":
        print("\n  ✗ Claude declined to generate a mood from these images.")
        print("    Try removing any images that may have triggered a refusal,")
        print("    or switch backends with --model gemini.\n")
        sys.exit(1)

    # The API can return non-text blocks (e.g. thinking, tool_use) mixed in;
    # pull out only the text blocks and concatenate.
    text_parts = [
        getattr(block, "text", "")
        for block in (response.content or [])
        if getattr(block, "type", None) == "text"
    ]
    text = "".join(text_parts).strip()

    if not text:
        block_types = [getattr(b, "type", "?") for b in (response.content or [])]
        print("\n  ✗ Claude returned no text content.")
        print(f"    stop_reason: {stop_reason}")
        print(f"    content blocks: {block_types}\n")
        sys.exit(1)

    if stop_reason == "max_tokens":
        print(f"\n  ⚠ Output hit the max_tokens cap ({max_tokens}); the mood may be truncated.")
        print("    Re-run with --max-tokens <larger> if the file looks cut off.\n")

    return text


# ---------------------------------------------------------------------------
# Backend: Gemini (Google)
# ---------------------------------------------------------------------------

def analyse_with_gemini(
    images: list[Path],
    notes: str | None,
    mood_name: str,
    model: str,
    max_tokens: int,
) -> str:
    """
    Sends all the moodboard images to Gemini's vision API.

    Gemini's SDK works a bit differently from Claude's:
    - Instead of a system prompt parameter, we pass it when configuring
    - Images are sent as Part objects with inline_data (raw bytes + mime type)
    - The response structure is simpler — just .text on the response

    But the PROMPT is identical. Same design intelligence, different plumbing.
    """
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("\n  ✗ google-genai package not installed.")
        print("    Run: pip install google-genai")
        print("    And set GEMINI_API_KEY in your environment.\n")
        sys.exit(1)

    import os

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("\n  ✗ GEMINI_API_KEY environment variable not set.")
        print("    Get an API key at https://aistudio.google.com/apikey\n")
        sys.exit(1)

    # Create the Gemini client
    # The system_instruction is Gemini's equivalent of Claude's system prompt
    client = genai.Client(api_key=api_key)

    # Build the content parts: images interleaved with their filenames,
    # just like we do for Claude — same pattern, different format
    parts = []
    for image_path in images:
        # Gemini takes raw bytes wrapped in a Part object
        parts.append(
            types.Part.from_bytes(
                data=read_image_bytes(image_path),
                mime_type=get_image_media_type(image_path),
            )
        )
        parts.append(
            types.Part.from_text(text=f"[Image: {image_path.name}]")
        )

    # Add the main analysis prompt
    parts.append(
        types.Part.from_text(
            text=build_user_prompt(images, notes, mood_name)
        )
    )

    print(f"  Sending {len(images)} images to Gemini ({model}) for analysis...")
    response = client.models.generate_content(
        model=model,
        contents=types.Content(
            role="user",
            parts=parts,
        ),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            max_output_tokens=max_tokens,
        ),
    )

    # Prompt-level block (safety filter rejected the input entirely).
    prompt_feedback = getattr(response, "prompt_feedback", None)
    block_reason = getattr(prompt_feedback, "block_reason", None) if prompt_feedback else None
    if block_reason:
        print(f"\n  ✗ Gemini blocked the request: {block_reason}")
        print("    Try removing any images that may have triggered a safety filter,")
        print("    or switch backends with --model claude.\n")
        sys.exit(1)

    text = (getattr(response, "text", None) or "").strip()
    candidates = getattr(response, "candidates", None) or []
    finish_reason = getattr(candidates[0], "finish_reason", None) if candidates else None

    if not text:
        print("\n  ✗ Gemini returned no text content.")
        if finish_reason is not None:
            print(f"    finish_reason: {finish_reason}")
        print("    This usually means the response was blocked or empty. Try")
        print("    different images, or switch backends with --model claude.\n")
        sys.exit(1)

    # finish_reason is an enum in google-genai; its string form ends in MAX_TOKENS.
    if finish_reason is not None and str(finish_reason).endswith("MAX_TOKENS"):
        print(f"\n  ⚠ Output hit the max_output_tokens cap ({max_tokens}); the mood may be truncated.")
        print("    Re-run with --max-tokens <larger> if the file looks cut off.\n")

    return text


# ---------------------------------------------------------------------------
# Backend router
# ---------------------------------------------------------------------------
# This maps the --model flag to the right function.
# Adding a new backend (GPT, Llama, etc.) is as simple as writing
# a new analyse_with_X function and adding it here.

BACKENDS = {
    "claude": analyse_with_claude,
    "gemini": analyse_with_gemini,
}


# ---------------------------------------------------------------------------
# Main flow
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate a mood.md from a folder of visual references.",
        epilog="Example: python generate_mood.py --model gemini --name 'Editorial Warmth'",
    )
    parser.add_argument(
        "--input", "-i",
        type=Path,
        default=Path("./mood"),
        help="Path to folder containing moodboard images (default: ./mood)",
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("."),
        help="Directory where mood.md will be written (default: current directory)",
    )
    parser.add_argument(
        "--name", "-n",
        type=str,
        default="Untitled Mood",
        help="Name for this mood (default: 'Untitled Mood')",
    )
    parser.add_argument(
        "--model", "-m",
        type=str,
        choices=list(BACKENDS.keys()),
        default="claude",
        help="Which vision model to use (default: claude)",
    )
    parser.add_argument(
        "--claude-model",
        type=str,
        default=DEFAULT_CLAUDE_MODEL,
        help=f"Claude model snapshot to use (default: {DEFAULT_CLAUDE_MODEL})",
    )
    parser.add_argument(
        "--gemini-model",
        type=str,
        default=DEFAULT_GEMINI_MODEL,
        help=f"Gemini model to use (default: {DEFAULT_GEMINI_MODEL})",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=DEFAULT_MAX_TOKENS,
        help=f"Max tokens in the generated mood (default: {DEFAULT_MAX_TOKENS})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the prompt and image list without calling the API (no tokens spent)",
    )
    args = parser.parse_args()

    model_string = args.claude_model if args.model == "claude" else args.gemini_model

    # ---- Validate input ----
    if not args.input.exists():
        print(f"\n  ✗ Mood folder not found: {args.input}")
        print(f"    Create it and add some images, then run again.\n")
        sys.exit(1)

    images = collect_images(args.input)
    if not images:
        print(f"\n  ✗ No images found in {args.input}")
        print(f"    Supported formats: {', '.join(SUPPORTED_EXTENSIONS)}\n")
        sys.exit(1)

    notes = read_notes(args.input)

    # ---- Show what we found ----
    print(f"\n  ◉ mood-protocol")
    print(f"  ─────────────────────────────")
    print(f"  Mood name:  {args.name}")
    print(f"  Model:      {args.model} ({model_string})")
    print(f"  Source:     {args.input.resolve()}")
    print(f"  Images:     {len(images)}")
    for img in images:
        # Mark anti-references with a different symbol so the designer
        # can see at a glance which images are "avoid this" signals
        prefix = "  ⊘" if is_anti_reference(img) else "  ◦"
        print(f"    {prefix} {img.name}")
    if notes:
        print(f"  Notes:      ✓ found notes.md")
    print(f"  ─────────────────────────────")

    # ---- Dry run: preview the prompt without spending any tokens ----
    if args.dry_run:
        print("\n  ◉ DRY RUN — no API call will be made, no mood.md will be written.\n")
        print("  ── System prompt ─────────────")
        print(SYSTEM_PROMPT)
        print("\n  ── User prompt ───────────────")
        print(build_user_prompt(images, notes, args.name))
        print("\n  ── Images that would be sent ─")
        for img in images:
            marker = "anti-reference" if is_anti_reference(img) else "reference"
            print(f"    {img.name}  ({marker})")
        print("\n  Re-run without --dry-run to actually generate the mood.\n")
        return

    # ---- Analyse using the chosen backend ----
    analyse_fn = BACKENDS[args.model]
    mood_content = analyse_fn(images, notes, args.name, model_string, args.max_tokens)

    # ---- Sanity-check the response before writing ----
    # The prompt asks for a document that starts with '# Mood: <name>'. If
    # that heading is missing we very likely got a refusal, an apology, or
    # some other non-mood text. Refuse to write it rather than clobber the
    # user's mood.md with junk.
    if "# Mood" not in mood_content:
        print("\n  ✗ The model returned a response that doesn't look like a mood file.")
        print("    Expected a markdown document starting with '# Mood: ...'")
        print(f"    First 200 chars of what came back:\n")
        print(f"    {mood_content[:200]!r}\n")
        print("    Nothing was written. Try a different model, adjust your notes,")
        print("    or remove images that may have been refused.\n")
        sys.exit(1)

    # ---- Write output ----
    output_path = args.output / "mood.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    mood_content = mood_content.rstrip() + f"\n\n<!-- mood-protocol v{SPEC_VERSION} -->\n"
    output_path.write_text(mood_content, encoding="utf-8")

    print(f"  ✓ Generated {output_path.resolve()}")
    print(f"  ─────────────────────────────\n")


if __name__ == "__main__":
    main()
