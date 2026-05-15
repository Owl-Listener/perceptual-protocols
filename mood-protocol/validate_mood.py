#!/usr/bin/env python3
"""
mood-protocol: Validate a mood.md against the mood-protocol spec.

Reads a mood.md file, checks it for spec conformance, and reports issues.

  - Errors are hard spec violations (missing required section, missing
    required subfield, malformed top heading, etc.). They make the file
    non-conformant.

  - Warnings are convention violations or quality nudges (uppercase hex,
    missing version footer, suspiciously short Essence). The file is
    still technically valid; you might want to fix them anyway.

Usage:
    python validate_mood.py                   # validates ./mood.md
    python validate_mood.py path/to/mood.md   # validates a specific file
    python validate_mood.py --quiet           # only print issues, not the summary header
    python validate_mood.py --strict          # treat warnings as errors

Exit codes:
    0 — no errors (warnings may still exist unless --strict)
    1 — at least one error (or, with --strict, at least one warning)
    2 — file not found, unreadable, or other I/O problem

No external dependencies. Pure stdlib so this works anywhere Python runs.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# ---------------------------------------------------------------------------
# Spec definitions
# ---------------------------------------------------------------------------
# Everything the validator knows about the spec lives in this block.
# When SPEC.md changes, this is the only place we have to update.
# Keeping it as a single block (rather than scattered through the checks)
# makes it easy to compare side-by-side with SPEC.md.

SPEC_VERSION = "0.1.0"

# Top-level heading. The spec says: `# Mood: [Name]`.
# We require a non-empty name after the colon — `# Mood:` with nothing after
# is a draft, not a conformant mood.
TOP_HEADING_PATTERN = re.compile(r"^#\s+Mood:\s*(\S.*)$", re.MULTILINE)

# Required `##` sections, in the order the spec lists them. Order isn't
# enforced (people may reorganise for their own reading), but presence is.
REQUIRED_SECTIONS = [
    "Essence",
    "Colour",
    "Typography",
    "Space & Layout",
    "Emotional Register",
    "Agent Instructions",
]

# Optional `##` sections. We don't error if they're missing, but we DO error
# if a section appears that isn't in either list — that catches typos like
# `## Colours` (note the s) or `## Typograhy`.
OPTIONAL_SECTIONS = [
    "Texture & Material",
    "Design Principles",
    "References",
    "Anti-References",
    "Motion",
    "Sound",
]

# Required bolded subfields within specific sections.
# Format: section_name -> list of subfield labels that must appear as
# `- **Label:**` bullets. Matches the format generate_mood.py emits.
REQUIRED_SUBFIELDS = {
    "Colour": ["Temperature", "Palette", "Contrast", "Saturation"],
    "Typography": ["Character", "Weight distribution", "Density"],
    "Space & Layout": ["Rhythm", "Scale relationships"],
}

# Pattern for a bolded subfield bullet, e.g. `- **Temperature:** warm`.
# Captures the label so we can compare it against REQUIRED_SUBFIELDS.
SUBFIELD_PATTERN = re.compile(r"^\s*-\s+\*\*([^*]+?):\*\*", re.MULTILINE)

# Hex colour pattern. Matches #abc, #abcd, #abcdef, #abcdef00.
# We use this to spot uppercase hex (convention violation, warning).
HEX_PATTERN = re.compile(r"#[0-9a-fA-F]{3,8}\b")

# Version footer the generator stamps in. Missing is a warning, not an error,
# because hand-written moods may not have one.
VERSION_FOOTER_PATTERN = re.compile(r"<!--\s*mood-protocol\s+v([\d.]+)\s*-->")


# ---------------------------------------------------------------------------
# Issue model
# ---------------------------------------------------------------------------

@dataclass
class Issue:
    """
    A single problem found during validation.

    severity is either "error" or "warning". section is the `##` heading
    the issue belongs to, or None for file-level issues (missing top
    heading, missing version footer).
    """
    severity: str
    message: str
    section: str | None = None


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------
# We don't need a real markdown library. The mood.md format is simple
# enough that we can split it into sections with a regex on `## ` lines.

def parse_sections(text: str) -> dict[str, str]:
    """
    Split a mood.md document into a dict of {section_name: section_body}.

    `## Colour` and everything until the next `## ` (or end of file) becomes
    sections["Colour"] = "the body text...".

    The top `# Mood: ...` heading is NOT included — that's parsed separately
    by check_top_heading.

    Why regex instead of a markdown parser? mood.md has one heading depth
    (##), no nested headings, no fenced sections we care about. Pulling
    in a markdown library would be a dependency for a 6-line job.
    """
    sections: dict[str, str] = {}

    # Find every line that starts with `## ` and capture position + name.
    # We need the positions so we can slice the body out between them.
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))

    for i, match in enumerate(matches):
        section_name = match.group(1).strip()
        body_start = match.end()
        # The body runs until the next `## ` heading, or end of file.
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[section_name] = text[body_start:body_end].strip()

    return sections


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------
# Each check is a small function that returns a list of Issues. Composable,
# testable, and easy to disable one if it gets noisy without untangling
# the rest of the code.

def check_top_heading(text: str) -> list[Issue]:
    """
    The first non-empty line should match `# Mood: <name>`. We check the
    full document (not just the first line) because the generator's
    sanity-check uses `if "# Mood" not in text` — a stricter check here
    catches files where the top heading is malformed or buried.
    """
    issues: list[Issue] = []

    match = TOP_HEADING_PATTERN.search(text)
    if not match:
        issues.append(Issue(
            severity="error",
            message=(
                "Missing or malformed top heading. The file must contain "
                "`# Mood: <name>` (with a non-empty name)."
            ),
        ))
        return issues

    # Bonus: if the heading exists but isn't on the first non-empty line,
    # that's a soft warning. Some agents may skim only the first heading
    # to identify the file.
    first_nonempty_line = next(
        (line for line in text.splitlines() if line.strip()),
        "",
    )
    if not first_nonempty_line.startswith("# Mood:"):
        issues.append(Issue(
            severity="warning",
            message=(
                "The `# Mood: <name>` heading exists but isn't the first "
                "non-empty line. Some agents skim only the start of the "
                "file to identify it."
            ),
        ))

    return issues


def check_required_sections(sections: dict[str, str]) -> list[Issue]:
    """
    Every section in REQUIRED_SECTIONS must be present. Missing → error.
    """
    issues: list[Issue] = []
    for name in REQUIRED_SECTIONS:
        if name not in sections:
            issues.append(Issue(
                severity="error",
                message=f"Missing required section `## {name}`.",
                section=name,
            ))
    return issues


def check_unknown_sections(sections: dict[str, str]) -> list[Issue]:
    """
    Any `##` section that isn't required or optional is suspicious — usually
    a typo (`## Colours` instead of `## Colour`). We surface those as
    warnings, not errors, because someone may have deliberately added a
    project-specific section.
    """
    issues: list[Issue] = []
    known = set(REQUIRED_SECTIONS) | set(OPTIONAL_SECTIONS)
    for name in sections:
        if name not in known:
            issues.append(Issue(
                severity="warning",
                message=(
                    f"Unknown section `## {name}` is not in the spec. "
                    f"Typo? Or a project-specific extension?"
                ),
                section=name,
            ))
    return issues


def check_required_subfields(sections: dict[str, str]) -> list[Issue]:
    """
    Some sections have required bolded subfields (Colour must have
    Temperature, Palette, Contrast, Saturation; etc.). Missing → error.
    """
    issues: list[Issue] = []

    for section_name, required_labels in REQUIRED_SUBFIELDS.items():
        body = sections.get(section_name)
        if body is None:
            # Already reported by check_required_sections; skip silently.
            continue

        present_labels = {m.group(1).strip() for m in SUBFIELD_PATTERN.finditer(body)}
        for label in required_labels:
            if label not in present_labels:
                issues.append(Issue(
                    severity="error",
                    message=(
                        f"Section `## {section_name}` is missing required "
                        f"subfield `**{label}:**`."
                    ),
                    section=section_name,
                ))

    return issues


def check_hex_lowercase(sections: dict[str, str]) -> list[Issue]:
    """
    SPEC.md says hex values should be lowercase. Uppercase is a convention
    violation, not a spec violation, so this is a warning.
    """
    issues: list[Issue] = []
    body = sections.get("Colour")
    if not body:
        return issues

    uppercase_hex = [h for h in HEX_PATTERN.findall(body) if any(c.isupper() for c in h)]
    # De-duplicate while preserving order so the message reads naturally.
    seen: set[str] = set()
    uniq = [h for h in uppercase_hex if not (h in seen or seen.add(h))]

    if uniq:
        examples = ", ".join(f"`{h}`" for h in uniq[:5])
        more = "" if len(uniq) <= 5 else f" (+{len(uniq) - 5} more)"
        issues.append(Issue(
            severity="warning",
            message=(
                f"Hex values should be lowercase per SPEC.md conventions. "
                f"Found uppercase: {examples}{more}."
            ),
            section="Colour",
        ))

    return issues


def check_palette_has_hex(sections: dict[str, str]) -> list[Issue]:
    """
    The Palette subfield should contain at least one hex value. If the
    palette is described entirely in words ("warm beige, deep navy") with
    no hex, agents can't act on it precisely.
    """
    issues: list[Issue] = []
    body = sections.get("Colour")
    if not body:
        return issues

    # Find the Palette line(s) — the bullet plus everything until the next
    # bullet or end of section. A simple way: grab a window after `**Palette:**`.
    palette_match = re.search(
        r"\*\*Palette:\*\*(.*?)(?=^\s*-\s+\*\*|\Z)",
        body,
        re.DOTALL | re.MULTILINE,
    )
    if not palette_match:
        return issues  # check_required_subfields will already error on this

    palette_body = palette_match.group(1)
    if not HEX_PATTERN.search(palette_body):
        issues.append(Issue(
            severity="warning",
            message=(
                "Palette has no hex values. Agents work best from concrete "
                "hex codes; consider adding them alongside the semantic names."
            ),
            section="Colour",
        ))

    return issues


def check_essence_quality(sections: dict[str, str]) -> list[Issue]:
    """
    Essence should be 2-3 sentences, specific and evocative. We can't judge
    "evocative" programmatically, but we can flag two failure modes:
      - far too short (one short sentence — probably a placeholder)
      - generic descriptors that the prompt explicitly warns against
    """
    issues: list[Issue] = []
    body = sections.get("Essence", "").strip()
    if not body:
        return issues

    # Roughly count sentences. Not perfect (abbreviations etc.) but good
    # enough to catch a one-liner that's clearly a placeholder.
    sentence_count = len(re.findall(r"[.!?](?:\s|$)", body))
    if sentence_count < 2:
        issues.append(Issue(
            severity="warning",
            message=(
                "Essence looks very short. The spec asks for 2-3 sentences "
                "of specific, evocative direction."
            ),
            section="Essence",
        ))

    # The prompt explicitly warns: "'Warm' means nothing." If Essence is
    # mostly generic adjectives, flag it.
    generic_words = {"modern", "clean", "sleek", "minimal", "fresh", "premium"}
    words = re.findall(r"[a-zA-Z]+", body.lower())
    if words:
        generic_ratio = sum(1 for w in words if w in generic_words) / len(words)
        if generic_ratio > 0.05:  # >5% of words are generic descriptors
            issues.append(Issue(
                severity="warning",
                message=(
                    "Essence leans on generic descriptors (modern, clean, "
                    "minimal, etc.). The prompt asks for specifics — "
                    "\"the warmth of a dimly lit bookshop at 6pm\" type "
                    "language, not adjectives."
                ),
                section="Essence",
            ))

    return issues


def check_version_footer(text: str) -> list[Issue]:
    """
    The generator stamps `<!-- mood-protocol v0.1.0 -->` at the end. Missing
    is a warning — hand-written moods may not have one. Version mismatch is
    also a warning, because the spec might have moved on.
    """
    issues: list[Issue] = []
    match = VERSION_FOOTER_PATTERN.search(text)
    if not match:
        issues.append(Issue(
            severity="warning",
            message=(
                f"Missing `<!-- mood-protocol v{SPEC_VERSION} -->` footer. "
                f"The generator adds this automatically; hand-written moods "
                f"benefit from it too — it lets tools know which spec version "
                f"to validate against."
            ),
        ))
        return issues

    found_version = match.group(1)
    if found_version != SPEC_VERSION:
        issues.append(Issue(
            severity="warning",
            message=(
                f"Footer reports spec v{found_version}, but this validator "
                f"checks against v{SPEC_VERSION}. Results may be misleading."
            ),
        ))

    return issues


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def validate(text: str) -> list[Issue]:
    """
    Run every check against the document and return the combined list of
    issues. Order matters for readability — file-level checks first, then
    section-level, then subfield-level, then style/quality.
    """
    sections = parse_sections(text)

    issues: list[Issue] = []
    issues += check_top_heading(text)
    issues += check_required_sections(sections)
    issues += check_unknown_sections(sections)
    issues += check_required_subfields(sections)
    issues += check_palette_has_hex(sections)
    issues += check_hex_lowercase(sections)
    issues += check_essence_quality(sections)
    issues += check_version_footer(text)
    return issues


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------
# Matches the visual style of generate_mood.py so the two tools feel like
# one toolkit: leading whitespace, ◉/✓/✗/⚠ symbols, divider rules.

def format_issue(issue: Issue) -> str:
    symbol = "✗" if issue.severity == "error" else "⚠"
    prefix = f"  {symbol} "
    if issue.section:
        return f"{prefix}[{issue.section}] {issue.message}"
    return f"{prefix}{issue.message}"


def print_report(path: Path, issues: list[Issue], quiet: bool) -> None:
    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]

    if not quiet:
        print(f"\n ◉ mood-protocol validator")
        print(f" ─────────────────────────────")
        print(f" File:     {path.resolve()}")
        print(f" Spec:     v{SPEC_VERSION}")
        print(f" Errors:   {len(errors)}")
        print(f" Warnings: {len(warnings)}")
        print(f" ─────────────────────────────")

    if errors:
        print()
        for issue in errors:
            print(format_issue(issue))

    if warnings:
        print()
        for issue in warnings:
            print(format_issue(issue))

    if not quiet:
        print()
        if not errors and not warnings:
            print("  ✓ Conformant. Nothing to fix.\n")
        elif not errors:
            print("  ✓ Conformant (warnings only — file is technically valid).\n")
        else:
            print("  ✗ Non-conformant. See errors above.\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a mood.md file against the mood-protocol spec.",
        epilog="Exit codes: 0 = no errors, 1 = errors, 2 = I/O problem.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path("./mood.md"),
        help="Path to the mood.md file (default: ./mood.md)",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress the summary header and trailing status line.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (useful in CI).",
    )
    args = parser.parse_args()

    if not args.path.exists():
        print(f"\n  ✗ File not found: {args.path}\n", file=sys.stderr)
        return 2

    try:
        text = args.path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"\n  ✗ Could not read {args.path}: {e}\n", file=sys.stderr)
        return 2

    issues = validate(text)
    print_report(args.path, issues, quiet=args.quiet)

    has_errors = any(i.severity == "error" for i in issues)
    has_warnings = any(i.severity == "warning" for i in issues)

    if has_errors or (args.strict and has_warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
