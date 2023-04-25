---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_grantss
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.769098972
    - name: NER Recall
      type: recall
      value: 0.6617812852
    - name: NER F Score
      type: f_score
      value: 0.7114156528
---
| Feature | Description |
| --- | --- |
| **Name** | `en_grantss` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | research grant applications |
| **License** | n/a |
| **Author** | [Rahul Thorat]() |

### Label Scheme

<details>

<summary>View label scheme (18 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `ACTIVITY`, `DISCIPLINE`, `EVENT`, `GPE`, `JOURNAL`, `KEYWORD`, `LICENSE`, `MEDIUM`, `METASTD`, `MONEY`, `ORG`, `PERSON`, `POSITION`, `PRODUCT`, `RECOGNITION`, `REF`, `REPOSITORY`, `WEBSITE` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 71.14 |
| `ENTS_P` | 76.91 |
| `ENTS_R` | 66.18 |
| `TOK2VEC_LOSS` | 1412244.09 |
| `NER_LOSS` | 1039417.96 |