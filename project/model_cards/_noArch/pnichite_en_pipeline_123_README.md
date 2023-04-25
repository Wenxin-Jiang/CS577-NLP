---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_pipeline_123
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.7661674609
    - name: NER Recall
      type: recall
      value: 0.8052226793
    - name: NER F Score
      type: f_score
      value: 0.7852097323
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline_123` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.1,<3.5.0` |
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
| **`ner`** | `DESCRIPTION`, `TITLE` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 78.52 |
| `ENTS_P` | 76.62 |
| `ENTS_R` | 80.52 |
| `TRANSFORMER_LOSS` | 1811559.14 |
| `NER_LOSS` | 6345113.13 |