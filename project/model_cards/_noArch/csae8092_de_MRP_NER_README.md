---
tags:
- spacy
- token-classification
language:
- de
license: cc-by-4.0
model-index:
- name: de_MRP_NER
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.905255631
    - name: NER Recall
      type: recall
      value: 0.8568527919
    - name: NER F Score
      type: f_score
      value: 0.8803894298
---
NER Model for 'Ministerratsprotokolle'

| Feature | Description |
| --- | --- |
| **Name** | `de_MRP_NER` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.1.0,<3.2.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | `cc-by` |
| **Author** | [Peter Andorfer]() |

### Label Scheme

<details>

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `GPE`, `LOC`, `ORG`, `PER` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 88.04 |
| `ENTS_P` | 90.53 |
| `ENTS_R` | 85.69 |
| `TOK2VEC_LOSS` | 40077.56 |
| `NER_LOSS` | 77727.57 |
