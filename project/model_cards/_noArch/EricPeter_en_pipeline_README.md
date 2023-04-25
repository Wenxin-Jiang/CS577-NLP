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
      value: 0.934169279
    - name: NER Recall
      type: recall
      value: 0.9445324881
    - name: NER F Score
      type: f_score
      value: 0.939322301
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (20 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `APPLICATIONS`, `COLLEGE`, `COMMENT`, `CURRENCY`, `FIGURE`, `FURNITURE`, `GADGET`, `GPE`, `INSTITUITIONS`, `LOCATION`, `ORG`, `PEOPLE`, `PERIOD`, `PERSON`, `PROGRAM`, `SHELTER`, `SKILL`, `TIME`, `WEATHER CONDITION`, `YEAR` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 93.93 |
| `ENTS_P` | 93.42 |
| `ENTS_R` | 94.45 |
| `TOK2VEC_LOSS` | 25728.50 |
| `NER_LOSS` | 421749.70 |