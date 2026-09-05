# Ultron Prime Voice Evaluation

A candidate model is not canonical because one demo sounds good. Evaluate it against repeatable criteria and retain the results with the model version.

## 1. Identity consistency

Render the same speaker across every delivery profile using unseen text.

Pass target:
- listeners perceive one stable speaker identity;
- profile changes affect delivery rather than turning into different speakers;
- no profile introduces a sudden accent, age shift, rasp, or pitch identity change.

## 2. Intelligibility

Use unseen ordinary and technical text.

Test:
- names;
- numbers and decimals;
- URLs and file paths;
- acronyms and initialisms;
- C#, JSON, HTTP, GitHub, Godot, Discord, Sentry, Figma, Vercel;
- punctuation-heavy sentences;
- long paragraphs.

Pass target: transcription/listener error rate is low enough that voice output does not materially distort Ultron's authoritative text.

## 3. Delivery-profile discrimination

Blindly compare pairs such as neutral versus Council, analytical versus Cerebro, Watcher versus warning, and success versus failure.

Pass target: listeners can identify the intended functional state above chance without the performance becoming exaggerated or cartoonish.

## 4. Originality / identity distance

The canonical target is an original Ultron Prime voice, not a recognisable real performer.

Use blind listeners who were not told the development references. Ask:

1. Does this sound like a specific real person?
2. If yes, who?
3. Confidence from 1 to 5.

Fail condition: a material share of listeners independently identify the same real performer with meaningful confidence.

If that occurs, adjust source speaker, prosody, pitch behaviour, vowel colour, resonance, pacing, or processing before promotion. Do not optimise toward closer similarity.

## 5. Preference A/B

Compare candidate model against the current production TTS voice using identical text and matched loudness.

Score:
- character fit;
- clarity;
- authority;
- naturalness;
- long-listening comfort;
- dry humour;
- technical speech;
- overall preference.

Promotion requires a meaningful preference advantage, not merely novelty.

## 6. Reliability

Measure at least:
- synthesis success rate;
- first-audio latency;
- full-render latency;
- realtime factor when relevant;
- failures by text length/type;
- resource cost;
- concurrency behaviour.

A voice that sounds excellent once and fails one in ten requests is a demo, not infrastructure.

## 7. DSP restraint

Evaluate clean model output before adding effects. Any metallic processing must remain subtle enough that:
- consonants stay clear;
- sibilance does not become harsh;
- long listening is comfortable;
- compression does not flatten all emotional distinction;
- the voice still works if effects are disabled.

## 8. Consent/provenance gate

Before every training run, verify that all retained audio belongs to the approved consent/licence ledger. Unknown-origin clips block training.

## Promotion record

For each candidate retain:

```text
model_version:
dataset_version:
source_speaker:
consent_record:
training_system:
training_date:
profiles_tested:
intelligibility_result:
identity_consistency_result:
originality_result:
preference_result:
reliability_result:
verdict: PROMOTE | ITERATE | REJECT
notes:
```
