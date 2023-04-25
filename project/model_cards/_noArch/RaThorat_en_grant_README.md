---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_grant
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8150708215
    - name: NER Recall
      type: recall
      value: 0.7125309559
    - name: NER F Score
      type: f_score
      value: 0.760359408
---
| Feature | Description |
| --- | --- |
| **Name** | `en_grant` |
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
| **`ner`** | `ACTIVITY`, `DISCIPLINE`, `GPE`, `JOURNAL`, `KEYWORD`, `LICENSE`, `MEDIUM`, `METASTD`, `MONEY`, `ORG`, `PERSON`, `POSITION`, `PRODUCT`, `RECOGNITION`, `REF`, `REPOSITORY`, `WEBSITE`, `YEAR` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 76.04 |
| `ENTS_P` | 81.51 |
| `ENTS_R` | 71.25 |
| `TOK2VEC_LOSS` | 9725604.63 |
| `NER_LOSS` | 930155.13 |