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
      value: 0.6486486486
    - name: NER Recall
      type: recall
      value: 0.6839378238
    - name: NER F Score
      type: f_score
      value: 0.6658259773
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
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
| `ENTS_F` | 66.58 |
| `ENTS_P` | 64.86 |
| `ENTS_R` | 68.39 |
| `TRANSFORMER_LOSS` | 532576.24 |
| `NER_LOSS` | 570559.29 |