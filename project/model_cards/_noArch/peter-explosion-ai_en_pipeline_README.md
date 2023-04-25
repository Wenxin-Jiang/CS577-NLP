---
tags:
- spacy
- text-classification
language:
- en
model-index:
- name: en_pipeline
  results: []
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `textcat` |
| **Components** | `textcat` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (2 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`textcat`** | `POSITIVE`, `NEGATIVE` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `CATS_SCORE` | 55.70 |
| `CATS_MICRO_P` | 58.65 |
| `CATS_MICRO_R` | 58.65 |
| `CATS_MICRO_F` | 58.65 |
| `CATS_MACRO_P` | 61.88 |
| `CATS_MACRO_R` | 58.69 |
| `CATS_MACRO_F` | 55.70 |
| `CATS_MACRO_AUC` | 63.53 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TEXTCAT_LOSS` | 3.74 |