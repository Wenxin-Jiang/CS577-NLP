---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_tenarch_aspects
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.714922049
    - name: NER Recall
      type: recall
      value: 0.7213483146
    - name: NER F Score
      type: f_score
      value: 0.7181208054
---
| Feature | Description |
| --- | --- |
| **Name** | `en_tenarch_aspects` |
| **Version** | `0.2.1` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `tok2vec`, `ner`, `entity_to_skill` |
| **Components** | `tok2vec`, `ner`, `entity_to_skill` |
| **Vectors** | 86498 keys, 86498 unique vectors (100 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (6 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Database`, `Framework`, `Language`, `Library`, `Platform`, `Tool` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 71.81 |
| `ENTS_P` | 71.49 |
| `ENTS_R` | 72.13 |
| `TOK2VEC_LOSS` | 40403.16 |
| `NER_LOSS` | 11205.88 |