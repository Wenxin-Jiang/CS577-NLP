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
      value: 0.9962546816
    - name: NER Recall
      type: recall
      value: 0.9925373134
    - name: NER F Score
      type: f_score
      value: 0.9943925234
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
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
| **`ner`** | `awarded` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 99.44 |
| `ENTS_P` | 99.63 |
| `ENTS_R` | 99.25 |
| `TOK2VEC_LOSS` | 37454.98 |
| `NER_LOSS` | 9266.72 |