---
tags:
- spacy
- token-classification
language:
- multilingual
model-index:
- name: xx_ner_sport_entities_uncased
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9361702128
    - name: NER Recall
      type: recall
      value: 0.9565217391
    - name: NER F Score
      type: f_score
      value: 0.9462365591
---
| Feature | Description |
| --- | --- |
| **Name** | `xx_ner_sport_entities_uncased` |
| **Version** | `1.9.0` |
| **spaCy** | `>=3.5.1,<3.6.0` |
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
| **`ner`** | `ALIAS_TEAM`, `PLAYER`, `TEAM`, `TOURNAMENT` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 94.62 |
| `ENTS_P` | 93.62 |
| `ENTS_R` | 95.65 |
| `TRANSFORMER_LOSS` | 48370.44 |
| `NER_LOSS` | 165512.78 |