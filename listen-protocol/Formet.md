# listen.md format spec

A `listen.md` is a structured perceptual brief produced from audio references. It follows the same overall structure as `mood.md`, with one addition: an explicit **Sound anchors** section that captures the sonic qualities before they're translated into cross-modal implications. This makes the cross-modal translation step visible and inspectable.

## Top-level structure

```markdown
# Listen: [project or reference name]

## Source

[Brief description of the audio input(s): named works, recordings,
descriptions. Include whether the model read the audio directly,
referenced it culturally, or worked from description. This caveat
matters for interpretation.]

## Mood summary

[A single paragraph capturing the perceptual identity the audio
suggests for the project. Same style as mood.md's Essence section.]

## Sound anchors

### [sound-vocabulary term from sound.md]
- **In the source:** [what specifically in the audio carries this quality]
- **Why it matters:** [what perceptual signal it carries]

[Repeat for each sound-vocab term that genuinely applies. Don't
include terms the source doesn't support.]

## Cross-modal translation

[For each sound anchor above, what it implies for the project's
visual / motion / experiential output. Be explicit about the
mapping. This is where the cross-modal logic lives, visible to
review rather than hidden in the prompt.]

### Visual implications (anchored to vocab.md terms)
- [Sound quality] → [visual quality]: [reasoning]

### Motion implications (anchored to motion.md terms)
- [Sound quality] → [motion quality]: [reasoning]

### Project-specific implications
[Anything that doesn't fit cleanly into vocab/motion but matters
for this project.]

## Implied vocabulary (cross-references)

[Same structure as mood.md's vocab section. Which canonical terms
from vocab.md does this brief imply, anchored to the cross-modal
translation above.]

## Anti-references

[What this listen explicitly is NOT — sound categories that would
contradict the brief. Specific is better than abstract. Categories,
not punching down.]

## Choices that produce this listen

[The specific sonic decisions, named, that constitute the
perceptual identity. Same role as mood.md's "design principles."]

## Cultural or temporal context

[Where this sound sits — a genre, era, region, sonic lineage.
Optional but anchors the brief in something locatable.]

## Confidence and uncertainty

[Crucial section for listen-protocol specifically. Flag:
- Whether the model read audio directly or worked from cultural reference / description
- Which cross-modal translations are well-established conventions vs interpretive choices
- What can't be verified from the available source materials]
```

## Rules

**Every brief identifies its source mode.** Was the audio actually heard, referenced culturally by name, or described in writing? This determines how the brief should be read. The Source section is not optional.

**Sound anchors come before cross-modal translation.** Always. The order matters because it makes the translation step inspectable: a reader can see *what the audio is doing* before they see *what the brief proposes the design should do*. Hiding the translation inside cross-modal claims makes the brief impossible to audit.

**Cross-modal claims are explicit, not assumed.** When the brief says "low register implies warm/dark visual treatment," say so directly. The cultural convention is real, but it's still a convention — making it visible lets the designer override it where appropriate.

**Use shared vocabularies where they fit.** `vocab.md` terms for static qualities the sound implies. `motion.md` terms for temporal qualities. Only reach for `sound.md` terms when the quality is genuinely sound-native (timbre, register, spaciousness, pulse, dynamics, decay).

**Anti-references describe categories.** Same rule as elsewhere in the family. *"A loudness-war mastered pop track"* is fair; naming a specific artist as bad isn't.

**Confidence section is required, not optional.** listen-protocol has more interpretive risk than the visual protocols. Honest grading of confidence is what makes the brief trustworthy.

## What makes a good listen.md

A useful brief has six properties:

1. **Names its source mode** so the reader knows whether to trust the brief as acoustically anchored or culturally received
2. **Anchors sound qualities to specific sonic features** (not just "warm" but "the bass-heavy register and woody piano timbre")
3. **Makes cross-modal translation visible** so the design choices can be audited rather than just accepted
4. **Reaches for existing vocabularies** (vocab, motion) before inventing new sound-specific terms
5. **Flags interpretive choices honestly** in the confidence section
6. **Anti-references are specific and category-level**

## Composing with the family

A `listen.md` is most useful alongside `mood.md` (if you have a visual mood for the same project) and `vocab.md` (for the cross-modal terms). The agent reading both has multi-modal coverage of the brief.

A `listen.md` can also stand alone for projects where sound is the primary or only modality — voice interfaces, podcasts, audio experiences. In those cases, the visual implications section becomes secondary and the sound anchors and motion implications carry the brief.

## When listen-protocol isn't the right tool

If your project has no audio dimension and no audio reference informs your design intent, you don't need this protocol. mood-protocol from visual references is sufficient.

If you have an audio reference but it's used purely as "background while working" with no intent to inform the design, you don't need this protocol either. listen-protocol is for cases where the sound is *part of the brief*, not just present during the work.
