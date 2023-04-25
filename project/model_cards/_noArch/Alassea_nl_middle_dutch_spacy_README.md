---
tags:
- spacy
- token-classification
language:
- nl
model-index:
- name: nl_middle_dutch_spacy
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9371146732
    - name: NER Recall
      type: recall
      value: 0.9268292683
    - name: NER F Score
      type: f_score
      value: 0.9319435929
---
| Feature | Description |
| --- | --- |
| **Name** | `nl_middle_dutch_spacy` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.4,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (8 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `B-DATE`, `B-LOC`, `B-MONEY`, `B-PERS`, `I-DATE`, `I-LOC`, `I-MONEY`, `I-PERS` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 93.19 |
| `ENTS_P` | 93.71 |
| `ENTS_R` | 92.68 |
| `TRANSFORMER_LOSS` | 10410.86 |
| `NER_LOSS` | 27922.80 |