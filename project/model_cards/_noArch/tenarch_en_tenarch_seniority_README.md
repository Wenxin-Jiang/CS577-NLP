---
tags:
- spacy
- text-classification
language:
- en
model-index:
- name: en_tenarch_seniority
  results: []
---
| Feature | Description |
| --- | --- |
| **Name** | `en_tenarch_seniority` |
| **Version** | `0.2.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `transformer`, `textcat` |
| **Components** | `transformer`, `textcat` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (6 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`textcat`** | `INTERN`, `ENTRY`, `MID`, `SENIOR`, `DIRECTOR`, `EXECUTIVE` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `CATS_SCORE` | 73.59 |
| `CATS_MICRO_P` | 87.50 |
| `CATS_MICRO_R` | 87.50 |
| `CATS_MICRO_F` | 87.50 |
| `CATS_MACRO_P` | 75.90 |
| `CATS_MACRO_R` | 72.14 |
| `CATS_MACRO_F` | 73.59 |
| `CATS_MACRO_AUC` | 78.33 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TRANSFORMER_LOSS` | 0.00 |
| `TEXTCAT_LOSS` | 0.00 |