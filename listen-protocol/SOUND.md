# Sound Vocabulary

A starter perceptual vocabulary for sound. Six qualities, chosen because they cover distinct sonic territory, are immediately recognisable to anyone who works with audio, and are genuinely sound-native — they don't already exist in `vocab.md` (static qualities) or `motion.md` (temporal qualities).

This file is intended to be included in a project alongside `mood.md`, `vocab.md`, and (optionally) `motion.md`. Each entry includes perceptual descriptions, technical anchors where they apply, and cross-references to the other vocabularies where a sound quality has a clear visual or motion analogue.

Format spec: see `FORMAT.md`. To extend the vocabulary for your project, see `PROMPT.md`.

---

## timbre

**One line:** The character or texture of a sound, distinct from pitch and loudness.

**When it applies:** When the brief depends on *what the sound is made of* — wooden, metallic, vocal, synthetic, breathy, granular. Timbre is the "material" of sound the way `materiality` is the "stuff" of a visual surface. A piano and a clarinet playing the same note at the same volume are different in timbre; the difference is the whole story.

**References:**
- An upright piano in a small room — wooden, slightly detuned, with hammer felt audible
- A spoken-word podcast recorded in a treated booth — warm, present, no room
- A vinyl record played on a quality turntable — natural decay, audible surface texture, no digital hardness

**Technical anchors:**
- Spectral content (harmonic richness, overtone structure)
- Attack envelope shape
- Presence or absence of digital processing (compression, EQ, reverb tail character)
- Often described in adjectives: woody, brassy, glassy, papery, granular, smooth, sharp, smoky

**Anti-references:**
- A generic synthesizer pad with no character — timbreless, "professional" but anonymous
- Heavily auto-tuned voice — timbral signal sanded away
- A YouTube ad voiceover at peak compression — flattened beyond timbral interest

**Pairs well with:** materiality (visual analogue), warmth, intimacy
**Tensions with:** highly processed/synthesized sound, sterile-mix aesthetics

**Cross-references:** Closely adjacent to `materiality` in `vocab.md`. If a brief calls for high materiality visually, it almost always calls for rich timbre sonically. The two should usually be specified together.

---

## register

**One line:** The pitch-position dominance of a sound — bass-heavy, treble-led, mid-rich, or full-range.

**When it applies:** When the brief depends on *where in the spectrum the sound lives*. Register carries enormous perceptual weight: a deep voice signals different things from a high one, and a bass-heavy mix feels physically different from a treble-led one.

**References:**
- A male baritone narrator (NPR's *This American Life*) — register signals authority and confidence
- A boy soprano in a choir — register signals fragility and aspiration
- Sub-bass in dub reggae — register felt in the body, not just heard
- A piccolo or whistle — register signals brightness, alertness, sometimes shrillness

**Technical anchors:**
- Dominant frequency range:
  - Sub-bass <60Hz (felt in the chest)
  - Bass 60–250Hz (warmth, weight, body)
  - Low-mid 250–500Hz (fullness, sometimes mud)
  - Mid 500Hz–2kHz (presence, vocal range)
  - High-mid 2k–4kHz (definition, edge)
  - Presence 4k–6kHz (clarity, intimacy)
  - Brilliance 6k–20kHz (air, sparkle)

**Anti-references:**
- A loudness-war mastered pop track with everything at 0dB across all frequencies — registerless, no breathing room
- A laptop-speaker mix that's been "corrected" to sound bass-heavy through phase tricks — implied register, not real one

**Pairs well with:** authority (low register), intimacy (close presence range), warmth (low-mid)
**Tensions with:** none inherent — registers compose freely, though extremes (sub-bass + brilliance with no mid) can feel hollow

**Cross-references:** Maps to colour temperature in some traditions — low register feels warm/dark; high register feels cool/bright. Use this carefully; it's a cultural mapping, not a universal law.

---

## spaciousness

**One line:** The perceived acoustic space a sound implies — small and dry to large and reverberant.

**When it applies:** When the brief depends on *what kind of room the sound lives in*. Spaciousness signals enclosure, scale, and emotional distance. The same voice in a closet vs a cathedral is two different perceptual experiences.

**References:**
- ASMR whispered close to the microphone — extreme proximity, almost no space; intimacy through nearness
- A Gregorian chant recorded in the actual abbey it was composed for — vast natural reverb; the space *is* the music
- Brian Eno's *Music for Airports* — designed for a specific imagined large quiet hall
- A field recording from a forest — natural ambient space, not artificial reverb

**Technical anchors:**
- Reverberation time (RT60) — short (<0.5s) feels close; long (>2s) feels vast
- Early reflection pattern (small room vs hall vs outdoor)
- Stereo width and depth
- Direct-to-reverberant ratio (high = close; low = distant)

**Anti-references:**
- A pop vocal drenched in plate reverb to sound "professional" — spaciousness as effect, not as architecture
- A modern phone-call recording — flat, spaceless, all direct sound
- A dry-mixed podcast — present but airless

**Pairs well with:** refuge (small enclosure), authority (cathedral-scale), restraint (clean dry mixes)
**Tensions with:** intimacy (when space becomes vast enough to feel impersonal)

**Cross-references:** Maps to whitespace / spatial generosity in visual `vocab.md`. A spacious sound brief usually wants a spacious visual brief — but the inverse isn't always true (you can have a dense visual layout with intimate dry sound).

---

## pulse

**One line:** Rhythmic energy and beat-orientation — from absent to mechanical to driving.

**When it applies:** When the brief depends on *whether time is felt as drift or as beat*. Pulse is the temporal heartbeat of sound; its presence or absence shapes everything else.

**References:**
- A metronome at 120 BPM — pure pulse, no other content
- Techno or house music — pulse as the entire compositional foundation
- A jazz brush drummer keeping time on a ride cymbal — pulse present but soft, conversational
- Ambient drone (Stars of the Lid, etc.) — pulse deliberately absent; time as drift
- A clock ticking in a quiet room — pulse as environmental presence

**Technical anchors:**
- BPM (beats per minute) — 60–80 reflective, 100–120 walking, 120–140 energetic, 140+ driving
- Pulse regularity — strict mechanical, swung, organic-loose, or absent
- Transient density per second
- Presence or absence of beat-defining elements (kick, snare, percussion)

**Anti-references:**
- A piece marketed as "rhythmic" but with no real pulse — bad EDM with confused programming
- A jazz piece played without time — beautiful but failing the pulse brief
- A typewriter on screen as "rhythm" — rhythm-as-aesthetic, not real pulse

**Pairs well with:** motion's snappy, motion's mechanical (the visual analogues)
**Tensions with:** calm, glassy, contemplative briefs; pulse and slowness are usually opposed (though slow pulse exists)

**Cross-references:** Maps directly to motion qualities. A pulse-led sound brief almost always wants snappy or mechanical motion; a pulseless sound brief almost always wants calm or glassy motion. This is one of the cleanest cross-modal mappings in the family.

---

## dynamics

**One line:** The range from quietest to loudest, and how much it shifts over time.

**When it applies:** When the brief depends on *whether sound stays even or whether it breathes between extremes*. Dynamics signal emotional honesty (whisper-to-shout vs flat-compressed), drama (theatrical builds and drops), and trust (a recording that doesn't need to be loud to be heard).

**References:**
- Beethoven's 9th Symphony — extreme dynamic range, quiet-to-thunder shifts that carry the emotional architecture
- A live jazz recording with audible audience and breath — high dynamics, low compression
- An audiobook professionally narrated — even modulation, deliberate dynamics control
- A FM radio talk show — flatly compressed, all peaks at the same level
- Whispered conversation rising to argument — emotional dynamics in voice, the same principle as music

**Technical anchors:**
- Dynamic range in dB (DR) — DR15+ is very high, DR8–10 is moderate, DR3–6 is heavy compression
- Crest factor (peak-to-RMS ratio)
- Presence or absence of compression and limiting
- Loudness normalisation (LUFS) practices

**Anti-references:**
- A loudness-war mastered pop track — dynamics flattened to fit perceived loudness norms
- A YouTube creator's "always at peak" voice processing — same problem in spoken content
- A film mix where the dialogue is quiet and the explosions are unbearable — high dynamics misused (this is broken dynamics, not absent)

**Pairs well with:** theatrical motion, irreverence (when dynamic shifts surprise), authority (when dynamics earn their range)
**Tensions with:** invisibility, restraint when dynamics are *unearned* dramatic

**Cross-references:** Maps loosely to visual contrast. High dynamics often want high visual contrast. Compressed sound often wants flat visual treatment. But the analogy isn't tight; some compressed-sound briefs (radio talk, news) want clear, even-contrast visuals.

---

## decay

**One line:** How sounds end — sharp cut, natural fade, or extended ring.

**When it applies:** When the brief depends on *the texture of endings*. Decay signals materiality (natural fade implies a real instrument in a real space), pacing (long decay slows the listener), and honesty (digital silence-cuts are almost always wrong for emotional content).

**References:**
- A grand piano note in a small wooden room — full natural decay, audible until inaudible
- A church organ — extended decay through architecture
- A synth patch with no release stage — instant silence, often jarring
- Vinyl crackle fading after the music ends — texture of decay, not just sound
- A drum hit with a long natural cymbal wash vs the same drum hit gated tight

**Technical anchors:**
- Release time in milliseconds — short (<100ms) snaps off; medium (100ms–1s) fades naturally; long (>1s) lingers
- Decay curve — exponential, linear, or shaped
- Natural (instrument + room) vs imposed (gate, automation, fade)

**Anti-references:**
- A podcast that cuts to silence with no breath room — decayless, mechanical, often uncomfortable
- A jingle with hard digital cutoff — efficient but charmless
- A music streaming compression that fades the tail to save bandwidth — decay erased by convenience

**Pairs well with:** glassy motion, calm, spaciousness, materiality
**Tensions with:** snappy motion, mechanical, invisibility when decay is the point

**Cross-references:** Maps to how visual transitions end — soft fades vs hard cuts. A long-decay sound brief usually wants long visual transitions; a hard-cut sound brief usually wants snappy visual transitions. Closely related to motion-protocol's `glassy` and `snappy`.
