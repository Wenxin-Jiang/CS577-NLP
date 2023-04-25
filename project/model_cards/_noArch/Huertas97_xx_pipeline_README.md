---
tags:
- spacy
- token-classification
language:
- multilingual
model-index:
- name: xx_pipeline
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9200034895
    - name: NER Recall
      type: recall
      value: 0.918641115
    - name: NER F Score
      type: f_score
      value: 0.9193217975
---
| Feature | Description |
| --- | --- |
| **Name** | `xx_pipeline` |
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
| `ENTS_F` | 91.93 |
| `ENTS_P` | 92.00 |
| `ENTS_R` | 91.86 |
| `TRANSFORMER_LOSS` | 382037.26 |
| `NER_LOSS` | 320041.67 |