---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_pipeline
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9641899655
    - name: NER Recall
      type: recall
      value: 0.9736053369
    - name: NER F Score
      type: f_score
      value: 0.9688747775
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.3,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (2 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Score`, `Team` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 96.89 |
| `ENTS_P` | 96.42 |
| `ENTS_R` | 97.36 |
| `TRANSFORMER_LOSS` | 4064.10 |
| `NER_LOSS` | 4512.84 |