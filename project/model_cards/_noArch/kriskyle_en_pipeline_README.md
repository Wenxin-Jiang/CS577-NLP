---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: asc_annotator
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9152868695
    - name: NER Recall
      type: recall
      value: 0.9177606178
    - name: NER F Score
      type: f_score
      value: 0.9165220744
license: cc-by-sa-4.0
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.2,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [Kristopher Kyle, Hakyung Sung]() |

### Label Scheme

<details>

This model identifies and categorizes Argument Structure Constructions (ASCs). ASC types are marked on the main verb of the ASC.

<summary>View label scheme (9 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `ATTR`, `CAUS_MOT`, `DITRAN`, `INTRAN_MOT`, `INTRAN_RES`, `INTRAN_S`, `PASSIVE`, `TRAN_RES`, `TRAN_S` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 91.65 |
| `ENTS_P` | 91.53 |
| `ENTS_R` | 91.78 |
| `TRANSFORMER_LOSS` | 10943.24 |
| `NER_LOSS` | 18950.33 |