---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_ontonotes_distilroberta_base_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8317391704
    - name: NER Recall
      type: recall
      value: 0.8886214012
    - name: NER F Score
      type: f_score
      value: 0.859239905
---
| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_ontonotes_distilroberta_base_ner` |
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
| `ENTS_F` | 85.92 |
| `ENTS_P` | 83.17 |
| `ENTS_R` | 88.86 |
| `TRANSFORMER_LOSS` | 296718.63 |
| `NER_LOSS` | 211595.82 |