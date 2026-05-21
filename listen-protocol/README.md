# listen-protocol

> From listening to seeing.

A protocol for translating an audio reference — heard, named, or described — into a perceptual brief. Take a soundtrack, an ambient recording, a piece of music, a voice, a place — any sound source that carries the feeling of a project — and produce a `listen.md` an agent can read to inform visual, motion, or experiential output.

Part of the [Perceptual Protocols](../) family.

## What this is for

listen-protocol makes an implicit signal explicit, so an agent can read it and translate it into perceptual choices in the work.

mood-protocol takes visual references and produces a brief. trace-protocol reads existing UIs. listen-protocol does the same job for the auditory dimension — and the output is format-compatible with the other two so the family composes cleanly.

Four common uses:

**Cross-modal briefing.** You have a soundtrack you've been listening to while imagining a project. Hand it to listen-protocol and get back a structured perceptual brief that captures what about the sound matters. Use that brief alongside a visual mood.md to give the agent two anchors instead of one.

**Place-derived design.** Record the ambient sound of a real place — a bookshop, a hospital, a forest, a kitchen — and use listen-protocol to extract its perceptual identity. This is how you design *for* a context, not just *in* one.

**Voice-led products.** If your product has audio (podcasts, calls, voice interfaces, accessibility), the brief should start with sound. A visual mood derived later inherits the right perceptual register.

**Film, theatre, and experiential design.** Where sound is half the medium, briefing from sound first lets the visuals serve the auditory direction rather than fight it.

## What this gives you

- A canonical starter vocabulary of six sound-native qualities — see [`sound.md`](./sound.md)
- A prompt for extracting a project-specific perceptual brief from audio references — see [`PROMPT.md`](./PROMPT.md)
- A format spec defining the `listen.md` output — see [`FORMAT.md`](./FORMAT.md)
- A worked example tracing Brian Eno's *Music for Airports* — see [`examples/example-music-for-airports.md`](./examples/example-music-for-airports.md)

## On the input modality problem

Sound is harder to capture in current AI tools than images. Be honest about what's possible:

- **Best case:** the model handles your audio file directly and reads it acoustically. Available today in **GPT-4o** and **Gemini 1.5+**. Quality is variable. Claude does not natively process audio at the time of writing.
- **Cultural case:** you reference a famous work by name (*"Music for Airports"*, *"the Twin Peaks theme"*, *"Bach's Cello Suite No. 1"*), and the model reasons from its training knowledge of how that work sounds and what it culturally signifies. **This is the dominant mode for most users today.** Honest but anchored in *received perception*, not *direct listening*.
- **Description case:** you describe the sound in writing. This is what designers do informally all the time and is perfectly valid here.
- **Spectrogram case:** you generate a visual representation of audio and upload that. Sometimes the cleanest fallback when the model can't process audio directly.

The PROMPT.md explicitly invites combinations. Don't fight the tool — use whatever fidelity is available and document which mode you used, so the brief is read with the right caveats. The worked example for *Music for Airports* uses the cultural-reference mode, and the brief itself flags this in its Source section.

## How to use it

1. Gather your audio inputs. The protocol works with whatever fidelity your model supports — most usefully:
   - **Named references** (*"Brian Eno – Music for Airports"*, *"the soundtrack to Lost in Translation"*) — works famously enough that the model can reason from cultural reception. This is the dominant mode for most users today.
   - **Written descriptions** of soundscapes (*"a small independent bookshop on a Saturday afternoon — low chatter, the rustle of pages, distant traffic, a kettle in the back"*) — honest about what it is: your description, structured.
   - **Streaming links** (YouTube, Spotify, Bandcamp) — the model can't actually "hear" them, but it can identify the work and reason from training knowledge. Same as named references in effect.
   - **Spectrograms** — visual representations of audio. A clean way to get sonic information into a vision model that can't process audio directly.
   - **Audio files** (MP3, WAV) — direct acoustic processing is currently available in **GPT-4o** and **Gemini 1.5+**. Claude does not natively process audio at the time of writing. Use this mode when you specifically want the model reading the file rather than reasoning from cultural knowledge of it.
2. Open Claude, Gemini, or ChatGPT. Upload or paste your references.
3. Also upload `sound.md`, `vocab.md`, and `FORMAT.md` so the model has the shared vocabularies.
4. Paste the prompt from [`PROMPT.md`](./PROMPT.md).
5. Save the output as `listen.md` in your project.

## Output format

The output is a `listen.md`, defined in [`FORMAT.md`](./FORMAT.md). It uses the same underlying structure as `mood.md` and `trace.md`, with one addition: a Sound-anchors section that captures the audio-specific qualities (using `sound.md` terms) before translating them to visual and motion implications. This makes the cross-modal translation step *visible and inspectable* rather than hidden in the prompt.

## How it composes with the family

visual moodboard ────► mood-protocol  ────► mood.md  ─┐
existing UI      ────► trace-protocol ────► trace.md ─┤
audio references ────► listen-protocol ───► listen.md ─┼─► agent reads any or all
your project intent ──► vocab.md / sound.md / motion.md / situation.md ──┘     to generate
↓
critique.md

All three brief-producing protocols (mood, trace, listen) produce format-compatible files that the agent can read together or separately. A project might have:

- A visual `mood.md` (from Pinterest references)
- A `listen.md` (from the soundtrack the designer associates with the project)
- A `vocab.md` (the shared static vocabulary)
- A `sound.md` (the shared sound vocabulary)
- A `motion.md` (for temporal qualities)

The agent reading all five has a richer perceptual brief than any single-modal approach can offer.

## The canonical sound vocabulary

Six terms, chosen because they cover distinct sonic territory and are immediately recognisable to anyone who works with audio:

- **timbre** — the character/texture of a sound (a piano vs a clarinet)
- **register** — pitch-position dominance (bass-heavy vs treble-led)
- **spaciousness** — the perceived acoustic space (closet vs cathedral)
- **pulse** — rhythmic energy and beat-orientation
- **dynamics** — range from quiet to loud and how it shifts
- **decay** — how sounds end (sharp cut vs long fade)

Full definitions, technical anchors, references, and anti-references live in [`sound.md`](./sound.md). Many sound qualities (warmth, density, intimacy, restraint) overlap with `vocab.md`'s static qualities — the brief can and should reach for those terms when they apply, only using sound.md terms for the qualities that are genuinely sound-native.

## A worked example

See [`examples/example-music-for-airports.md`](./examples/example-music-for-airports.md) for a `listen.md` extracted from Brian Eno's 1978 album *Music for Airports* — a work explicitly designed as a perceptual environment. Useful as a reference for what good output looks like, and as evidence that the cross-modal translation (sound → visual brief) produces something coherent and useful.

## Open caveats worth being honest about

**Cross-modal translation isn't a science.** There are cultural conventions about which sounds map to which visual qualities (low register = warm/dark, high register = bright/cool), but no universal mapping. The protocol does its best to reason from these conventions, but the translation always has interpretive choices. Treat a `listen.md` as a starting point for argument, not a settled finding.

**The "described vs heard" gap.** When the model reads an audio reference by name, the brief is anchored to *cultural reputation* rather than *acoustic content*. That's fine, but it's a different kind of brief than one produced from direct listening. The PROMPT.md asks the model to flag which source mode it used.

**Validating sound → visual transfer is harder than visual → visual.** The trace-triangulation workflow that closes the loop on mood-protocol and trace-protocol gets more complicated here, because the agent's output is usually visual and the brief was sonic. We don't yet have a clean methodology for this. For now, treat listen-protocol's output as a brief input, not a fully closed loop.

## License

MIT — see the family root.
