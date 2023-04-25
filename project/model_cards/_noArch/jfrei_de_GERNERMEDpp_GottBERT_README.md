---
tags:
- spacy
- token-classification
language:
- de
model-index:
- name: de_GERNERMEDpp_GottBERT
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9240268876
    - name: NER Recall
      type: recall
      value: 0.9207165109
    - name: NER F Score
      type: f_score
      value: 0.922368729
---
GermanBERT-based model of the GERNERMED++ German NER model for medical entities.

| Feature | Description |
| --- | --- |
| **Name** | `de_GERNERMEDpp_GottBERT` |
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
| `ENTS_F` | 92.24 |
| `ENTS_P` | 92.40 |
| `ENTS_R` | 92.07 |
| `TRANSFORMER_LOSS` | 353176.15 |
| `NER_LOSS` | 525846.32 |