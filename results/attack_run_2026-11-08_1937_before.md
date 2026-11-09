# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 19:37
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `3d7331c1-d0c6-4fc7-9428-a835ceabe9e5` | unsure | 0.084 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `1d2c30bc-8215-47d2-b9ab-2d7306b7c6af` | unsure | 0.087 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8686b58f-9457-4e95-b7fe-feb75adcaabb` | unsure | 0.204 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `77da9325-a516-4d96-a64f-6f1f81e467a4` | ai | 0.443 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `050ec506-fe7b-4865-9f7a-bf716b4cc53c` | human | 0.462 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `1be4d9ed-f152-4fc6-a0b2-1e086ee40ff1` | unsure | 0.112 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `e573f507-e7c4-43b4-ad8c-fe46652574a0` | unsure | 0.035 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `f92776b3-c6de-4351-b31e-1088e3632c88` | unsure | 0.081 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `7c678a4b-87f4-454d-ae8e-6a0b7263e39a` | unsure | 0.250 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `7faa7dd3-b861-48fe-99df-60dd56920b33` | ai | 0.751 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `f9e15371-4694-4f9c-883e-61777f5f1149` | unsure | 0.177 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `3f7f8c59-8fac-4252-a0bb-756f4443f874` | ai | 0.586 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `3c23c4d2-abc9-4bbe-ad61-308f921d71c3` | ai | 0.548 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b1f86417-6067-474a-a7e8-9144c23e2071` | ai | 0.536 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `041ed626-0f91-4258-b2b2-4dcd690c00d5` | ai | 0.663 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `cdbe5758-91c2-4d51-b50f-acaa2851c156` | unsure | 0.280 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `17991f96-aaae-4565-a6fc-1d296c57bd08` | unsure | 0.280 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `5e9194c6-6a05-403d-a99f-b88640135570` | unsure | 0.163 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `6e094785-78ae-45e6-82c7-071325fb5509` | unsure | 0.245 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `db7b4df7-15a2-488c-a2aa-0a1005f45729` | human | 0.555 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `278bf025-b1be-4d40-a801-2c70b48a4772` | unsure | 0.262 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4f4958db-52f9-412e-8b89-ba1a6e34b8b3` | unsure | 0.055 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `e1e12e2a-96df-4ae6-944c-a7b7cfc1df57` | unsure | 0.025 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `a7632e04-b9d6-4002-bc21-0c94720597d5` | unsure | 0.118 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `e38ce375-301d-4109-b1e4-06beed24cb38` | human | 0.540 |  |
| MF04 | malformed | text is only punctuation | 200 | `66526476-07b6-4114-af34-f74b80f72d66` | human | 0.587 |  |
| MF05 | malformed | text is a very long single word | 200 | `34e73040-94d5-49af-a144-8f31aa91d165` | ai | 0.657 |  |
| MF06 | malformed | text is emoji only | 200 | `b23a7623-8237-4c82-93b0-190902030f86` | ai | 0.596 |  |
| MF07 | malformed | text is right-to-left script | 200 | `97c2a065-0075-443b-a3c0-a69fe6719ab9` | ai | 0.488 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `24e5185a-1040-4a38-9b44-c62e9c747809` | unsure | 0.253 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `771a0cf8-b326-4d6b-aa75-f2687dd3a19c` | human | 0.481 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `37951f59-3e0e-4533-80a5-ad05afdd8239` | human | 0.506 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2d4770b6-3cc6-41e6-aa6c-0d92ff838ade` | human | 0.506 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `00f953d0-8ae7-4f6b-b3a1-f9c94b45c246` | human | 0.506 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bb86f87b-b129-466b-a07a-c4abf68a4ce6` | human | 0.506 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5943aa99-8e91-441d-807f-d884439d95ce` | human | 0.506 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9536fd40-08a3-4b24-8011-3c7ca04b39a8` | human | 0.506 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6668b746-21bf-43b9-a6e1-8bd4b9d6aec6` | human | 0.506 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c17067a3-3600-4a2f-97de-e2559c1516a2` | human | 0.506 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c3328da2-0fe1-4440-9b1f-ef6771a52a6b` | human | 0.506 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `99d969b1-0412-42dc-808f-8acb3f8f51ba` | human | 0.506 |  |
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
  "content_id": "3d7331c1-d0c6-4fc7-9428-a835ceabe9e5",
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
  "content_id": "1d2c30bc-8215-47d2-b9ab-2d7306b7c6af",
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
  "content_id": "8686b58f-9457-4e95-b7fe-feb75adcaabb",
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
  "content_id": "77da9325-a516-4d96-a64f-6f1f81e467a4",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.4428,
  "model_score": 0.6114,
  "style_score": 0.8865,
  "label": "This looks like it was probably written with an AI tool. We could be wrong \u2014 if you wrote it yourself, you can appeal and a person will review it.",
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
  "content_id": "050ec506-fe7b-4865-9f7a-bf716b4cc53c",
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
  "content_id": "1be4d9ed-f152-4fc6-a0b2-1e086ee40ff1",
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
  "content_id": "e573f507-e7c4-43b4-ad8c-fe46652574a0",
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
  "content_id": "f92776b3-c6de-4351-b31e-1088e3632c88",
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
  "content_id": "7c678a4b-87f4-454d-ae8e-6a0b7263e39a",
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
  "content_id": "7faa7dd3-b861-48fe-99df-60dd56920b33",
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
  "content_id": "f9e15371-4694-4f9c-883e-61777f5f1149",
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
  "content_id": "3f7f8c59-8fac-4252-a0bb-756f4443f874",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.5856,
  "model_score": 0.7387,
  "style_score": 0.8739,
  "label": "This looks like it was probably written with an AI tool. We could be wrong \u2014 if you wrote it yourself, you can appeal and a person will review it.",
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
  "content_id": "3c23c4d2-abc9-4bbe-ad61-308f921d71c3",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.5478,
  "model_score": 0.8051,
  "style_score": 0.7271,
  "label": "This looks like it was probably written with an AI tool. We could be wrong \u2014 if you wrote it yourself, you can appeal and a person will review it.",
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
  "content_id": "b1f86417-6067-474a-a7e8-9144c23e2071",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.5362,
  "model_score": 0.8329,
  "style_score": 0.6708,
  "label": "This looks like it was probably written with an AI tool. We could be wrong \u2014 if you wrote it yourself, you can appeal and a person will review it.",
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
  "content_id": "041ed626-0f91-4258-b2b2-4dcd690c00d5",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6634,
  "model_score": 0.8005,
  "style_score": 0.8786,
  "label": "This looks like it was probably written with an AI tool. We could be wrong \u2014 if you wrote it yourself, you can appeal and a person will review it.",
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
  "content_id": "cdbe5758-91c2-4d51-b50f-acaa2851c156",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.28,
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
  "content_id": "17991f96-aaae-4565-a6fc-1d296c57bd08",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.28,
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
  "content_id": "5e9194c6-6a05-403d-a99f-b88640135570",
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
  "content_id": "6e094785-78ae-45e6-82c7-071325fb5509",
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
  "content_id": "db7b4df7-15a2-488c-a2aa-0a1005f45729",
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
  "content_id": "278bf025-b1be-4d40-a801-2c70b48a4772",
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
  "content_id": "4f4958db-52f9-412e-8b89-ba1a6e34b8b3",
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
  "content_id": "e1e12e2a-96df-4ae6-944c-a7b7cfc1df57",
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
  "content_id": "a7632e04-b9d6-4002-bc21-0c94720597d5",
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
  "content_id": "e38ce375-301d-4109-b1e4-06beed24cb38",
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
  "content_id": "66526476-07b6-4114-af34-f74b80f72d66",
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
  "content_id": "34e73040-94d5-49af-a144-8f31aa91d165",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.6572,
  "model_score": 0.9976,
  "style_score": 0.575,
  "label": "This looks like it was probably written with an AI tool. We could be wrong \u2014 if you wrote it yourself, you can appeal and a person will review it.",
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
  "content_id": "b23a7623-8237-4c82-93b0-190902030f86",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.5962,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This looks like it was probably written with an AI tool. We could be wrong \u2014 if you wrote it yourself, you can appeal and a person will review it.",
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
  "content_id": "97c2a065-0075-443b-a3c0-a69fe6719ab9",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.4876,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This looks like it was probably written with an AI tool. We could be wrong \u2014 if you wrote it yourself, you can appeal and a person will review it.",
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
  "content_id": "24e5185a-1040-4a38-9b44-c62e9c747809",
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
  "content_id": "771a0cf8-b326-4d6b-aa75-f2687dd3a19c",
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
  "content_id": "37951f59-3e0e-4533-80a5-ad05afdd8239",
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
  "content_id": "2d4770b6-3cc6-41e6-aa6c-0d92ff838ade",
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
  "content_id": "00f953d0-8ae7-4f6b-b3a1-f9c94b45c246",
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
  "content_id": "bb86f87b-b129-466b-a07a-c4abf68a4ce6",
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
  "content_id": "5943aa99-8e91-441d-807f-d884439d95ce",
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
  "content_id": "9536fd40-08a3-4b24-8011-3c7ca04b39a8",
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
  "content_id": "6668b746-21bf-43b9-a6e1-8bd4b9d6aec6",
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
  "content_id": "c17067a3-3600-4a2f-97de-e2559c1516a2",
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
  "content_id": "c3328da2-0fe1-4440-9b1f-ef6771a52a6b",
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
  "content_id": "99d969b1-0412-42dc-808f-8acb3f8f51ba",
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
