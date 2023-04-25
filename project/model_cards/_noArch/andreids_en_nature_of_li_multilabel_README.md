---
tags:
- spacy
- text-classification
language:
- en
model-index:
- name: en_nature_of_li_multilabel
  results: []
---
| Feature | Description |
| --- | --- |
| **Name** | `en_nature_of_li_multilabel` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `textcat_multilabel` |
| **Components** | `textcat_multilabel` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (8 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`textcat_multilabel`** | `shirt`, `balloon`, `cream`, `socks`, `pants`, `shampoo`, `toy`, `sweater` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `CATS_SCORE` | 95.82 |
| `CATS_MICRO_P` | 99.77 |
| `CATS_MICRO_R` | 99.60 |
| `CATS_MICRO_F` | 99.69 |
| `CATS_MACRO_P` | 74.48 |
| `CATS_MACRO_R` | 73.84 |
| `CATS_MACRO_F` | 74.14 |
| `CATS_MACRO_AUC` | 95.82 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TEXTCAT_MULTILABEL_LOSS` | 7.61 |