---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: fashion_brands_patterns
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.0
    - name: NER Recall
      type: recall
      value: 0.0
    - name: NER F Score
      type: f_score
      value: 0.0
---
| Feature | Description |
| --- | --- |
| **Name** | `en_ner_fashion` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.1.0,<3.2.0` |
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
| **`ner`** | `FASHION_BRAND` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 0.00 |
| `ENTS_P` | 0.00 |
| `ENTS_R` | 0.00 |
| `TOK2VEC_LOSS` | 1043.55 |
| `NER_LOSS` | 1414323.43 |
