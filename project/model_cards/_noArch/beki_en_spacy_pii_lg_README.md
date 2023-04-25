---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_pii_lg
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9099727257
    - name: NER Recall
      type: recall
      value: 0.8798970607
    - name: NER F Score
      type: f_score
      value: 0.8946822084
widget:
- text: "SELECT shipping FROM users WHERE shipping = '201 Thayer St Providence RI 02912'"
---

| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_pii` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 514157 keys, 514157 unique vectors (300 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (5 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `DATE_TIME`, `LOC`, `NRP`, `ORG`, `PER` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 89.47 |
| `ENTS_P` | 91.00 |
| `ENTS_R` | 87.99 |
| `TOK2VEC_LOSS` | 82522.55 |
| `NER_LOSS` | 106026.29 |