---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_ncv
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.7012058955
    - name: NER Recall
      type: recall
      value: 0.626746507
    - name: NER F Score
      type: f_score
      value: 0.6618887015
---
| Feature | Description |
| --- | --- |
| **Name** | `en_ncv` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | narrative CVs |
| **License** | n/a |
| **Author** | [Rahul Thorat]() |

### Label Scheme

<details>

<summary>View label scheme (12 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `ACTIVITY`, `GPE`, `KEYWORD`, `MEDIUM`, `MONEY`, `ORG`, `PERSON`, `POSITION`, `RECOGNITION`, `REPOSITORY`, `WEBSITE`, `YEAR` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 66.19 |
| `ENTS_P` | 70.12 |
| `ENTS_R` | 62.67 |
| `TOK2VEC_LOSS` | 786695.63 |
| `NER_LOSS` | 965558.77 |