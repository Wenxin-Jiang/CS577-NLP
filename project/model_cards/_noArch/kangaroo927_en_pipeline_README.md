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
| **spaCy** | `>=3.1.4,<3.2.0` |
| **Default Pipeline** | `transformer`, `textcat` |
| **Components** | `transformer`, `textcat` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (22 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`textcat`** | `Acute Bleed/Mesenteric Ischemia`, `Adrenal Mass Abdomen/Pelvis`, `Aortic Aneurysm Post EVT`, `Aortic Aneurysm Pre EVT`, `Aortic Dissection`, `Cystogram`, `Dual Phase Abdomen/Pelvis`, `Enterography IBD`, `NON Contrast Abdomen/Pelvis`, `Oral & IV Abdomen Pelvis`, `Oral Contrast Abdomen/Pelvis`, `Pancreas Mass Abdomen/Pelvis`, `Pelvis Only`, `Rectal Contrast Abdomen/Pelvis`, `Renal Donor`, `Renal Mass Abdomen/Pelvis`, `Renal Stone Abdomen/Pelvis`, `Routine Abdomen/Pelvis`, `Trauma Abdomen/Pelvis`, `Urogram Post Treatment/Follow Up`, `Urogram Pre Treatment Initial`, `Venogram` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `CATS_SCORE` | 76.67 |
| `CATS_MICRO_P` | 85.89 |
| `CATS_MICRO_R` | 85.19 |
| `CATS_MICRO_F` | 85.54 |
| `CATS_MACRO_P` | 74.35 |
| `CATS_MACRO_R` | 80.69 |
| `CATS_MACRO_F` | 76.67 |
| `CATS_MACRO_AUC` | 97.57 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TRANSFORMER_LOSS` | 19.80 |
| `TEXTCAT_LOSS` | 504.30 |