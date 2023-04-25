---
tags:
- spacy
- token-classification
language:
- fr
model-index:
- name: fr_pipeline
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9011406844
    - name: NER Recall
      type: recall
      value: 0.92578125
    - name: NER F Score
      type: f_score
      value: 0.9132947977
---
| Feature | Description |
| --- | --- |
| **Name** | `fr_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `FOOD PRODUCT`, `INGREDIENT`, `MEASURE`, `QUANTITY` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 91.33 |
| `ENTS_P` | 90.11 |
| `ENTS_R` | 92.58 |
| `TOK2VEC_LOSS` | 8670.94 |
| `NER_LOSS` | 4165.31 |