---
tags:
- spacy
- token-classification
- text-classification
language:
- en
model-index:
- name: en_tenarchexp3
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.95
    - name: NER Recall
      type: recall
      value: 0.8507462687
    - name: NER F Score
      type: f_score
      value: 0.8976377953
---
| Feature | Description |
| --- | --- |
| **Name** | `en_tenarchexp3` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.4,<3.3.0` |
| **Default Pipeline** | `tok2vec`, `ner`, `textcat_multilabel` |
| **Components** | `tok2vec`, `ner`, `textcat_multilabel` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (7 labels for 2 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Seniority`, `TechSkill` |
| **`textcat_multilabel`** | `SoftwareEngineer`, `SiteReliabitliyEngineer`, `ProductManager`, `DataScientist`, `Designer` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 89.76 |
| `ENTS_P` | 95.00 |
| `ENTS_R` | 85.07 |
| `CATS_SCORE` | 71.89 |
| `CATS_MICRO_P` | 47.92 |
| `CATS_MICRO_R` | 86.79 |
| `CATS_MICRO_F` | 61.74 |
| `CATS_MACRO_P` | 39.21 |
| `CATS_MACRO_R` | 55.42 |
| `CATS_MACRO_F` | 44.90 |
| `CATS_MACRO_AUC` | 71.89 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TOK2VEC_LOSS` | 31131.44 |
| `NER_LOSS` | 5486.16 |
| `TEXTCAT_MULTILABEL_LOSS` | 5.73 |