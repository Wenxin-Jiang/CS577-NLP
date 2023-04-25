---
tags:
- spacy
- text-classification
language:
- en
model-index:
- name: en_triage_subject
  results: []
---
| Feature | Description |
| --- | --- |
| **Name** | `en_triage_subject` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `textcat` |
| **Components** | `tok2vec`, `textcat` |
| **Vectors** | 514157 keys, 514157 unique vectors (300 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (5 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`textcat`** | `General Correspondence`, `Invoice`, `New Claim Form`, `Assessor Report`, `Complaint` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `CATS_SCORE` | 79.52 |
| `CATS_MICRO_P` | 99.34 |
| `CATS_MICRO_R` | 99.34 |
| `CATS_MICRO_F` | 99.34 |
| `CATS_MACRO_P` | 79.37 |
| `CATS_MACRO_R` | 79.67 |
| `CATS_MACRO_F` | 79.52 |
| `CATS_MACRO_AUC` | 79.99 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TOK2VEC_LOSS` | 25952.93 |
| `TEXTCAT_LOSS` | 58.98 |