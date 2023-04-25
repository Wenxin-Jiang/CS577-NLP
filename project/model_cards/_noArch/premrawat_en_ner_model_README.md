---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_ner_model
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.3624161074
    - name: NER Recall
      type: recall
      value: 0.384341637
    - name: NER F Score
      type: f_score
      value: 0.3730569948
---
| Feature | Description |
| --- | --- |
| **Name** | `en_ner_model` |
| **Version** | `0.1.1` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (1 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `SKILL` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 37.31 |
| `ENTS_P` | 36.24 |
| `ENTS_R` | 38.43 |
| `TOK2VEC_LOSS` | 305790.85 |
| `NER_LOSS` | 801195.82 |