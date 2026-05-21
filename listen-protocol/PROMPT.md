# listen-protocol extraction prompt

A prompt for extracting a perceptual brief from audio references. Works with Claude, Gemini, or ChatGPT — any model that handles text and can either process audio directly or reason from cultural reference.

## How to use

1. Gather your audio inputs (any combination):
   - **Audio files** (MP3, WAV) — best when the model handles them
   - **Streaming links** (YouTube, Spotify, Bandcamp) — useful even when the model can't acoustically process them
   - **Named references** (artist + work title, *"the soundtrack to X"*)
   - **Written descriptions** of soundscapes or sonic intent
   - **Spectrograms** — visual representations of audio, when the model only handles images
2. Upload along with `sound.md`, `vocab.md`, `motion.md` (if you have it), and `FORMAT.md` from this folder.
3. Open Claude, Gemini, or ChatGPT.
4. Paste the prompt below.
5. Save the output as `listen.md` in your project.

## The prompt

```
You are helping me extract a perceptual brief for a project from audio references. I want a structured listen.md that captures what the sound is doing perceptually, and translates that into cross-modal implications I can use to inform visual and motion design.

I've uploaded:
- sound.md — six sound-native qualities (timbre, register, spaciousness, pulse, dynamics, decay)
- vocab.md — shared static perceptual vocabulary (warmth, restraint, intimacy, etc.)
- motion.md — shared motion vocabulary (snappy, calm, mechanical, etc.) — if available
- FORMAT.md — the spec for what a listen.md should look like
- My audio references — [describe what you uploaded: files, links, named works, descriptions, spectrograms]

Your job:

1. Identify your source mode honestly. For each reference, note whether you:
   - Read the audio directly (file, spectrogram you can interpret acoustically)
   - Referenced the work culturally from training knowledge (you know what Music for Airports sounds like, but you didn't "hear" my upload)
   - Worked from my written description only
   
   Different source modes produce different kinds of brief. Document which.

2. Anchor the sound to sound.md terms. For each of the six terms that genuinely applies to the source, name what specifically in the audio carries that quality. Be precise — "the bass-heavy register and woody piano timbre" rather than just "warm."

3. Cross-translate to vocab.md and motion.md terms. This is the most important and most interpretive step. Make every cross-modal mapping explicit:
   - "Low register and warm timbre → warmth (vocab.md)"
   - "Pulseless and high spaciousness → calm + glassy motion (motion.md)"
   - "High dynamics with long decays → theatrical motion (motion.md)"
   
   Some mappings are conventional (low register feels warm/dark). Some are interpretive choices. Name which are which.

4. Identify project-specific terms only if genuinely needed. Most sound qualities should translate to existing vocabularies. Propose new terms only when the canonical sets fall short — and justify each one against the four canonical-vocabulary criteria.

5. Be opinionated about anti-references. What sound categories would contradict this brief? Specific and category-level, not punching down on named artists.

6. Format the output exactly as FORMAT.md specifies, including the Sound anchors section before Cross-modal translation. The order is non-optional — it makes the brief auditable.

7. The Confidence and uncertainty section is required, not optional. Flag every interpretive choice. Flag the source mode in the verdict (acoustic vs cultural vs descriptive).

Write in the voice of a careful critic who knows both the audio canon and design vocabulary. The agent reading this brief later will need to make visual/motion decisions from your translation, so make the translation legible.

The output is a single complete listen.md. Don't wrap it in commentary or apology.
```

## Notes on iteration

The first pass will often be too generic about cross-modal mappings. Useful re-prompts:

- "Your cross-modal translations are conventional but lazy. The track has [specific quality] — what does that imply for the visual brief beyond 'warm'?"
- "You didn't anchor decay to anything in the source. Either anchor it or drop it."
- "You're treating culturally-received perception as if you heard the audio. Separate those — flag which qualities you're inferring from cultural knowledge vs which would be acoustically obvious."
- "The anti-references are too abstract. What would actively contradict this listen?"
- "The visual implications are too tightly bound to one rendering style. The translation should hold across multiple visual treatments — generalise."

## Notes on cultural vs acoustic listening

A real epistemological caveat to be honest about: when a model "knows" what *Music for Airports* sounds like from training rather than from listening to your upload, it's reasoning from received perception. That's a different kind of brief than one produced from direct acoustic analysis.

This matters because cultural reception sometimes outruns acoustic reality. A model may say *Music for Airports* feels "spacious and calm" because that's how the work is culturally framed, even if a specific cut you uploaded happens to have unusual dynamic content.

For most use cases this gap doesn't matter — designers usually want the *cultural* mood of a reference, not its acoustic fingerprint. But for sound design specifically (where you actually need to produce audio output), the acoustic anchoring matters more. Flag the source mode in your brief so downstream readers can adjust.

## Notes on what to ask the agent to produce

Like other family protocols, listen-protocol's output is a *brief*, not a finished work. The next step is to hand the `listen.md` (plus your other briefs and shared vocabularies) to an agent designing something. The brief's job is to anchor those design decisions in the auditory source.

For initial experiments, asking the agent to produce a landing page hero (as in mood-protocol) is a clean test artifact. The hero gives the cross-modal translation visible surface to inhabit.
