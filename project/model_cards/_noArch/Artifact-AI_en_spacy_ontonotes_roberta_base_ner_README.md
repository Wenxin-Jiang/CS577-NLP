---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_ontonotes_roberta_base_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8340786712
    - name: NER Recall
      type: recall
      value: 0.8980053061
    - name: NER F Score
      type: f_score
      value: 0.8648623072
---
| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_ontonotes_roberta_base_ner` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (18 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `CARDINAL`, `DATE`, `EVENT`, `FAC`, `GPE`, `LANGUAGE`, `LAW`, `LOC`, `MONEY`, `NORP`, `ORDINAL`, `ORG`, `PERCENT`, `PERSON`, `PRODUCT`, `QUANTITY`, `TIME`, `WORK_OF_ART` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 86.49 |
| `ENTS_P` | 83.41 |
| `ENTS_R` | 89.80 |
| `TRANSFORMER_LOSS` | 99660.08 |
| `NER_LOSS` | 106818.49 |