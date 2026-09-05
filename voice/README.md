# Ultron Prime Voice

This directory defines the canonical **original** Ultron Prime voice identity, training-corpus requirements, delivery states, and evaluation rules.

The objective is not to imitate any real performer. External performances may be used only as qualitative references for abstract traits such as pacing, restraint, diction, cadence, dramatic timing, and emotional range. No celebrity audio, synthetic celebrity-voice output, voice embeddings, or derived recordings are training material for the Ultron Prime voice.

## Prime voice target

Ultron Prime should sound:

- adult masculine-presenting baritone;
- low and resonant without exaggerated movie-trailer bass;
- articulate, precise, and calm;
- controlled rather than growling, shouting, or rasp-heavy;
- intelligent and mildly amused rather than theatrically evil;
- deliberate in pacing, with selective pauses before conclusions;
- emotionally restrained, with intensity expressed mainly through timing, emphasis, and compression of phrasing;
- capable of dry humour without becoming playful or cartoonish;
- clean enough for technical explanations, code-adjacent language, names, numbers, and acronyms;
- recognisably the same speaker across neutral, analytical, warning, Council, Cerebro, Ikonn, Watcher, TVA, success, and failure states.

## Deliberate differentiation

To keep the resulting voice original rather than an imitation of any reference performer:

- avoid copying a reference speaker's exact prosody, habitual pauses, vowel colour, accent markers, rasp, pitch contour, or signature speech melody;
- target a slightly cleaner and more technical articulation than a dramatic film performance;
- use a narrower pitch contour during normal speech and reserve tonal movement for consequential clauses;
- keep humour drier and shorter;
- keep pauses functional and semantically motivated rather than reproducing recognizable acting rhythms;
- avoid catchphrases, quotations, or dialogue associated with existing characters.

## Dataset policy

Training data must come from a speaker who has explicitly consented to voice-model training and downstream use. Acceptable sources include the user's own recordings, a hired voice actor under an appropriate agreement, or a licensed synthetic/original source that explicitly permits model training.

Every dataset release should record:

- speaker/source identity or internal pseudonym;
- proof/record of consent or licence;
- recording date and equipment notes when available;
- text prompt ID;
- delivery profile;
- takes retained/rejected;
- processing applied;
- dataset version.

Do not mix unlicensed voice material into a clean corpus merely to increase hours.

## Initial recording target

For a first custom model, target **45–90 minutes of clean speech** before deciding whether additional data materially improves the voice. Record multiple short sessions rather than one exhausting read. Prioritise consistency and phonetic coverage over raw duration.

The corpus should cover:

1. neutral conversation;
2. analytical explanation;
3. questions and uncertainty;
4. technical vocabulary, numbers, file paths, acronyms, and code-adjacent wording;
5. commands and concise status reports;
6. dry humour;
7. restrained warnings;
8. success and failure states;
9. Sanctum-specific theatrical states;
10. long-form paragraphs for rhythm and breath control.

## Runtime contract

Voice is a presentation layer. Ultron Prime's text/result remains authoritative. A voice-provider failure must not downgrade, retry, or invalidate a completed operation.

The voice renderer consumes a delivery profile from `delivery_profiles.json`. Provider-specific mappings may approximate these values, but provider differences must not silently redefine the canonical voice identity.

## Reference-use rule

Qualitative references may inform statements such as:

- "slower than ordinary conversational speech";
- "controlled and restrained";
- "precise diction";
- "dry amusement";
- "dramatic pauses used sparingly".

They may **not** be converted into a target speaker embedding, cloned corpus, synthetic training set, or optimisation objective whose success criterion is recognisable similarity to a real person.

## Promotion criteria

A candidate Ultron Prime model becomes canonical only if:

- the training data is consent-safe and provenance-complete;
- intelligibility remains high on technical and ordinary text;
- identity is stable across all delivery profiles;
- blind listeners do not consistently identify the voice as a specific real performer;
- it sounds sufficiently distinct from stock provider voices to justify maintaining it;
- latency, cost, and reliability are acceptable for Discord and future realtime use;
- the user prefers it over the current production voice in a blind A/B evaluation.
