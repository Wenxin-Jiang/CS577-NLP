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
      value: 0.987456883
    - name: NER Recall
      type: recall
      value: 0.9707151665
    - name: NER F Score
      type: f_score
      value: 0.9790144567
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.4,<3.3.0` |
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
| `ENTS_F` | 97.90 |
| `ENTS_P` | 98.75 |
| `ENTS_R` | 97.07 |
| `TOK2VEC_LOSS` | 248450.31 |
| `NER_LOSS` | 58657.11 |