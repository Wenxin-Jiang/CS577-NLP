---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_ner_skills
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.3980582524
    - name: NER Recall
      type: recall
      value: 0.3404507711
    - name: NER F Score
      type: f_score
      value: 0.3670076726
---
| Feature | Description |
| --- | --- |
| **Name** | `en_ner_skills` |
| **Version** | `0.1.0` |
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
| `ENTS_F` | 36.70 |
| `ENTS_P` | 39.81 |
| `ENTS_R` | 34.05 |
| `TOK2VEC_LOSS` | 607659.90 |
| `NER_LOSS` | 491709.76 |