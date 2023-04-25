---
tags:
- spacy
- token-classification
- text-classification
language:
- en
model-index:
- name: en_med12_trf_weakly_supervised
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9995091177
    - name: NER Recall
      type: recall
      value: 0.9983655976
    - name: NER F Score
      type: f_score
      value: 0.9989370304
---
| Feature | Description |
| --- | --- |
| **Name** | `en_med12_trf_weakly_supervised` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner`, `textcat` |
| **Components** | `transformer`, `ner`, `textcat` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

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
| `ENTS_F` | 99.89 |
| `ENTS_P` | 99.95 |
| `ENTS_R` | 99.84 |
| `CATS_SCORE` | 100.00 |
| `CATS_MICRO_P` | 100.00 |
| `CATS_MICRO_R` | 100.00 |
| `CATS_MICRO_F` | 100.00 |
| `CATS_MACRO_P` | 100.00 |
| `CATS_MACRO_R` | 100.00 |
| `CATS_MACRO_F` | 100.00 |
| `CATS_MACRO_AUC` | 100.00 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TRANSFORMER_LOSS` | 18547.50 |
| `NER_LOSS` | 153097.22 |
| `TEXTCAT_LOSS` | 0.00 |