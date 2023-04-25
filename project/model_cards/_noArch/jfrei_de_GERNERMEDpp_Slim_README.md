---
tags:
- spacy
- token-classification
language:
- de
model-index:
- name: de_GERNERMEDpp_Slim
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9020724569
    - name: NER Recall
      type: recall
      value: 0.8881619938
    - name: NER F Score
      type: f_score
      value: 0.8950631819
---
Slim model of the GERNERMED++ German NER model for medical entities.

| Feature | Description |
| --- | --- |
| **Name** | `de_GERNERMEDpp_Slim` |
| **Version** | `1.0.0` |
| **spaCy** | `>=3.2.3,<3.3.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [Johann Frei](https://github.com/frankkramer-lab/GERNERMED-pp) |

### Label Scheme

<details>

<summary>View label scheme (6 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Dosage`, `Drug`, `Duration`, `Form`, `Frequency`, `Strength` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 89.51 |
| `ENTS_P` | 90.21 |
| `ENTS_R` | 88.82 |
| `TOK2VEC_LOSS` | 129329.99 |
| `NER_LOSS` | 603008.42 |