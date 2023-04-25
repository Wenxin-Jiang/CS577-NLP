---
tags:
- spacy
- text-classification
language:
- en
model-index:
- name: en_tenarch_archetypes
  results: []
---
| Feature | Description |
| --- | --- |
| **Name** | `en_tenarch_archetypes` |
| **Version** | `0.2.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `transformer`, `textcat_multilabel` |
| **Components** | `transformer`, `textcat_multilabel` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (7 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`textcat_multilabel`** | `SoftwareEngineer`, `QAEngineer`, `DataScientist`, `ProductManager`, `EngineeringManager`, `DevopsEngineer`, `Designer` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `CATS_SCORE` | 96.27 |
| `CATS_MICRO_P` | 86.96 |
| `CATS_MICRO_R` | 83.77 |
| `CATS_MICRO_F` | 85.33 |
| `CATS_MACRO_P` | 84.44 |
| `CATS_MACRO_R` | 88.04 |
| `CATS_MACRO_F` | 85.77 |
| `CATS_MACRO_AUC` | 96.27 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TRANSFORMER_LOSS` | 1021.96 |
| `TEXTCAT_MULTILABEL_LOSS` | 52.26 |