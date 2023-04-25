---
tags:
- spacy
- token-classification
- text-classification
language:
- en
model-index:
- name: en_med12_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8398220245
    - name: NER Recall
      type: recall
      value: 0.8445190157
    - name: NER F Score
      type: f_score
      value: 0.842163971
---
| Feature | Description |
| --- | --- |
| **Name** | `en_med12_trf` |
| **Version** | `1` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner`, `textcat` |
| **Components** | `transformer`, `ner`, `textcat` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | Apache License, Version 2.0 |
| **Author** | Karl Renius |

### Label Scheme

<details>

<summary>View label scheme (14 labels for 2 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Denominator_Unit`, `Denominator_Value`, `Dose_Form`, `Medication_Name`, `NDC`, `Numerator_Unit`, `Numerator_Value`, `Product_Package_Type`, `Product_Package_Type_Value`, `Quantity_Factor_Unit`, `Quantity_Factor_Unit_Value`, `Quantity_Factor_Value` |
| **`textcat`** | `OTHER`, `MEDICATION` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 84.22 |
| `ENTS_P` | 83.98 |
| `ENTS_R` | 84.45 |
| `CATS_SCORE` | 93.88 |
| `CATS_MICRO_P` | 89.78 |
| `CATS_MICRO_R` | 97.98 |
| `CATS_MICRO_F` | 93.70 |
| `CATS_MACRO_P` | 90.29 |
| `CATS_MACRO_R` | 97.93 |
| `CATS_MACRO_F` | 93.88 |
| `CATS_MACRO_AUC` | 98.53 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TRANSFORMER_LOSS` | 152780.09 |
| `NER_LOSS` | 69513.43 |
| `TEXTCAT_LOSS` | 1868.30 |