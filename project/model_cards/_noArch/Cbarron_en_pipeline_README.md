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
      value: 1.0
    - name: NER Recall
      type: recall
      value: 1.0
    - name: NER F Score
      type: f_score
      value: 1.0
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
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

<summary>View label scheme (3 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `FOOD`, `QUANTITY`, `SERVING` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 100.00 |
| `ENTS_P` | 100.00 |
| `ENTS_R` | 100.00 |
| `TRANSFORMER_LOSS` | 62.83 |
| `NER_LOSS` | 84.62 |