---
tags:
- spacy
- token-classification
language:
- multilingual
model-index:
- name: xx_LeetSpeakNER_mstsb_mpnet
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.912373549
    - name: NER Recall
      type: recall
      value: 0.9160452962
    - name: NER F Score
      type: f_score
      value: 0.9142057358
---
| Feature | Description |
| --- | --- |
| **Name** | `xx_LeetSpeakNER_mstsb_mpnet` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `INV_CAMO`, `LEETSPEAK`, `MIX`, `PUNCT_CAMO` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 91.42 |
| `ENTS_P` | 91.24 |
| `ENTS_R` | 91.60 |
| `TRANSFORMER_LOSS` | 396910.59 |
| `NER_LOSS` | 373097.06 |