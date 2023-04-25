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
      value: 0.6478873239
    - name: NER Recall
      type: recall
      value: 0.7150259067
    - name: NER F Score
      type: f_score
      value: 0.6798029557
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.3.0,<3.4.0` |
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
| **`ner`** | `DIPLOMA`, `DIPLOMA_MAJOR`, `EXPERIENCE`, `SKILLS` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 67.98 |
| `ENTS_P` | 64.79 |
| `ENTS_R` | 71.50 |
| `TRANSFORMER_LOSS` | 20684785.56 |
| `NER_LOSS` | 8672497.87 |