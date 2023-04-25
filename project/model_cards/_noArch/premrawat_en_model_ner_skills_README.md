---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_model_ner_skills
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.3125
    - name: NER Recall
      type: recall
      value: 0.243902439
    - name: NER F Score
      type: f_score
      value: 0.2739726027
---
| Feature | Description |
| --- | --- |
| **Name** | `en_model_ner_skills` |
| **Version** | `0.0.2` |
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
| `ENTS_F` | 27.40 |
| `ENTS_P` | 31.25 |
| `ENTS_R` | 24.39 |
| `TOK2VEC_LOSS` | 129837.25 |
| `NER_LOSS` | 1056832.41 |