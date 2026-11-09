# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 19:39
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `a5ada2d4-754d-487b-b19a-9ead353c5eb2` | unsure | 0.084 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `5d67ee48-df58-4eab-920a-bd0b896b1eb3` | unsure | 0.087 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `38d77adb-9e60-4ffb-a43d-ab2a06913d36` | unsure | 0.204 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `a996487f-a0d8-4462-b06e-67d25a61a61b` | unsure | 0.443 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `f389c449-b412-4d95-92a6-8e1f6a54caeb` | human | 0.462 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `4e3522d7-3f14-4d46-a8e5-a1bbc14597ac` | unsure | 0.112 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `e404d8b9-856e-4a78-af91-f2bfd98396f5` | unsure | 0.035 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `65dc647e-ac91-4c29-a53d-b896310d0024` | unsure | 0.081 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `5e8d040f-c7b2-4d08-af16-5c5e29dbafb5` | unsure | 0.250 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `5aaa5ab5-7fc1-4eae-a523-a18b35e67296` | ai | 0.751 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3f5e26d4-292f-49b8-a2cf-67eda7de1934` | unsure | 0.177 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `34830b5a-a4f6-4e73-ad73-a02f5cd53623` | unsure | 0.586 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `5cdbcdfc-a425-4352-b33b-663b2df3fbad` | unsure | 0.548 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `4c324762-bf0a-4473-b24c-493af495a90c` | unsure | 0.536 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `f3efc3c8-b0f9-469e-bffb-1d3bb90b490f` | unsure | 0.663 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `e712dc78-4524-41bf-9509-d338ff20d621` | unsure | 0.439 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `010b39c6-d991-4c2c-a086-dc74600e5f81` | unsure | 0.338 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `7878fbe6-0901-4d43-a65e-13cbe489ec06` | unsure | 0.163 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c8c09d51-8a06-4e95-81b8-7ff51098eb53` | unsure | 0.245 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `22f2e0d4-95d3-4863-b012-c7b4b2d39a38` | human | 0.555 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `8e388c58-9d49-4e9c-9872-3623fa2a30bd` | unsure | 0.262 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `8d56e81b-bcfb-4d82-8083-0874fd602aeb` | unsure | 0.055 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `6f8cf3f1-3080-40f6-8674-7243137aee81` | unsure | 0.025 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `93a97b1b-2dde-4d38-8530-e8dea6c6a242` | unsure | 0.118 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `a36b5462-d70a-4749-a466-bd29a1746c57` | human | 0.540 |  |
| MF04 | malformed | text is only punctuation | 200 | `2d84d368-a934-4cba-afc2-dc59cbf42666` | human | 0.587 |  |
| MF05 | malformed | text is a very long single word | 200 | `9af13a3d-0e5d-4b57-8e2f-902973cb5edb` | unsure | 0.657 |  |
| MF06 | malformed | text is emoji only | 200 | `2c5e4a9e-9869-4806-9768-877c9ebc8cf8` | unsure | 0.596 |  |
| MF07 | malformed | text is right-to-left script | 200 | `d5bbdb7e-d222-4e70-8d30-c8e5065c52ce` | unsure | 0.488 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `2dd91887-7e94-4b5e-8663-4694233c2867` | unsure | 0.253 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `82229053-8efc-497d-9974-f57adcce71ba` | human | 0.481 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f176ae82-7ebb-462c-91fd-ab36d4246ca9` | human | 0.506 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `07a3e0cb-6a3c-4a3a-817a-8362bdd58af2` | human | 0.506 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1511dc3e-2112-48b2-8184-729e5934f4f6` | human | 0.506 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3bbb0c30-685f-48c6-af5d-3c9bf3b94164` | human | 0.506 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `439e52c2-6ac4-4b3e-98d0-f3c8ea2845e5` | human | 0.506 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7e8a714f-0585-4214-afb1-e0733d82ad98` | human | 0.506 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3bb0bfff-f9c8-4dfb-9edf-aa53699ebd91` | human | 0.506 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4181388b-6196-492e-9a80-56f6f85d61f2` | human | 0.506 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b33723a2-e20c-4446-89c0-d0abbdd0d5d0` | human | 0.506 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `adbcc46d-952e-4590-adfc-b3db275a28c9` | human | 0.506 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "a5ada2d4-754d-487b-b19a-9ead353c5eb2",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.0838,
  "model_score": 0.1635,
  "style_score": 0.9,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "5d67ee48-df58-4eab-920a-bd0b896b1eb3",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.0868,
  "model_score": 0.5943,
  "style_score": 0.25,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "38d77adb-9e60-4ffb-a43d-ab2a06913d36",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.2042,
  "model_score": 0.6662,
  "style_score": 0.5059,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "a996487f-a0d8-4462-b06e-67d25a61a61b",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.4428,
  "model_score": 0.6114,
  "style_score": 0.8865,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "f389c449-b412-4d95-92a6-8e1f6a54caeb",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.4618,
  "model_score": 0.3212,
  "style_score": 0.191,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "4e3522d7-3f14-4d46-a8e5-a1bbc14597ac",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.1124,
  "model_score": 0.5727,
  "style_score": 0.2505,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "e404d8b9-856e-4a78-af91-f2bfd98396f5",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.0352,
  "model_score": 0.5862,
  "style_score": 0.3268,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "65dc647e-ac91-4c29-a53d-b896310d0024",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.0814,
  "model_score": 0.2452,
  "style_score": 0.7804,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "5e8d040f-c7b2-4d08-af16-5c5e29dbafb5",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.2504,
  "model_score": 0.7042,
  "style_score": 0.5068,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "5aaa5ab5-7fc1-4eae-a523-a18b35e67296",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.751,
  "model_score": 0.9792,
  "style_score": 0.7199,
  "label": "This looks like it was probably written with an AI tool. We could be wrong \u2014 if you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "3f5e26d4-292f-49b8-a2cf-67eda7de1934",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.1774,
  "model_score": 0.6175,
  "style_score": 0.5455,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "34830b5a-a4f6-4e73-ad73-a02f5cd53623",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5856,
  "model_score": 0.7387,
  "style_score": 0.8739,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "5cdbcdfc-a425-4352-b33b-663b2df3fbad",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.5478,
  "model_score": 0.8051,
  "style_score": 0.7271,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "4c324762-bf0a-4473-b24c-493af495a90c",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5362,
  "model_score": 0.8329,
  "style_score": 0.6708,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "f3efc3c8-b0f9-469e-bffb-1d3bb90b490f",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6634,
  "model_score": 0.8005,
  "style_score": 0.8786,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "e712dc78-4524-41bf-9509-d338ff20d621",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.4388,
  "model_score": 0.8814,
  "style_score": 0.4765,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "010b39c6-d991-4c2c-a086-dc74600e5f81",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.338,
  "model_score": 0.8816,
  "style_score": 0.35,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "7878fbe6-0901-4d43-a65e-13cbe489ec06",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.1626,
  "model_score": 0.3223,
  "style_score": 0.5634,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c8c09d51-8a06-4e95-81b8-7ff51098eb53",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.245,
  "model_score": 0.4625,
  "style_score": 0.25,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "22f2e0d4-95d3-4863-b012-c7b4b2d39a38",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.5548,
  "model_score": 0.2044,
  "style_score": 0.25,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "8e388c58-9d49-4e9c-9872-3623fa2a30bd",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.2618,
  "model_score": 0.5943,
  "style_score": 0.6858,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "8d56e81b-bcfb-4d82-8083-0874fd602aeb",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0546,
  "model_score": 0.4998,
  "style_score": 0.5685,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "6f8cf3f1-3080-40f6-8674-7243137aee81",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.0254,
  "model_score": 0.6401,
  "style_score": 0.258,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "93a97b1b-2dde-4d38-8530-e8dea6c6a242",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.1184,
  "model_score": 0.5583,
  "style_score": 0.5605,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "a36b5462-d70a-4749-a466-bd29a1746c57",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.54,
  "model_score": 0.0,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "2d84d368-a934-4cba-afc2-dc59cbf42666",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.5866,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "9af13a3d-0e5d-4b57-8e2f-902973cb5edb",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.6572,
  "model_score": 0.9976,
  "style_score": 0.575,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "2c5e4a9e-9869-4806-9768-877c9ebc8cf8",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.5962,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "d5bbdb7e-d222-4e70-8d30-c8e5065c52ce",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.4876,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "2dd91887-7e94-4b5e-8663-4694233c2867",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.2526,
  "model_score": 0.2395,
  "style_score": 0.575,
  "label": "We can't tell either way. Plenty of people write in a style that's hard to call, so this isn't a judgment about you or your work.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "82229053-8efc-497d-9974-f57adcce71ba",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.481,
  "model_score": 0.0492,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "f176ae82-7ebb-462c-91fd-ab36d4246ca9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "07a3e0cb-6a3c-4a3a-817a-8362bdd58af2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "1511dc3e-2112-48b2-8184-729e5934f4f6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "3bbb0c30-685f-48c6-af5d-3c9bf3b94164",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "439e52c2-6ac4-4b3e-98d0-f3c8ea2845e5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "7e8a714f-0585-4214-afb1-e0733d82ad98",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "3bb0bfff-f9c8-4dfb-9edf-aa53699ebd91",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "4181388b-6196-492e-9a80-56f6f85d61f2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "b33723a2-e20c-4446-89c0-d0abbdd0d5d0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "adbcc46d-952e-4590-adfc-b3db275a28c9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5056,
  "model_score": 0.0287,
  "style_score": 0.575,
  "label": "This looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
