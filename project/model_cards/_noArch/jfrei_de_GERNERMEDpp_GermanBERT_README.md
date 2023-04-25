---
tags:
- spacy
- token-classification
language:
- de
model-index:
- name: de_GERNERMEDpp_GermanBERT
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9088501091
    - name: NER Recall
      type: recall
      value: 0.9085669782
    - name: NER F Score
      type: f_score
      value: 0.9087085216
---
GottBERT-based model of the GERNERMED++ German NER model for medical entities.

| Feature | Description |
| --- | --- |
| **Name** | `de_GERNERMEDpp_GermanBERT` |
| **Version** | `1.0.0` |
| **spaCy** | `>=3.2.3,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
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
| `ENTS_F` | 90.87 |
| `ENTS_P` | 90.89 |
| `ENTS_R` | 90.86 |
| `TRANSFORMER_LOSS` | 193600.80 |
| `NER_LOSS` | 255416.71 |