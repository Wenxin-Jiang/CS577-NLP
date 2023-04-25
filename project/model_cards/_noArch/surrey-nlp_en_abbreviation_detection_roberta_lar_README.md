---
tags:
- spacy
- token-classification
language:
- en
widget:
- text: "Light dissolved inorganic carbon (DIC) resulting from the oxidation of hydrocarbons."
- text: "RAFs are plotted for a selection of neurons in the dorsal zone (DZ) of auditory cortex in Figure 1."
- text: "Images were acquired using a GE 3.0T MRI scanner with an upgrade for echo-planar imaging (EPI)."
model-index:
- name: en_abbreviation_detection_roberta_lar
  results:
  - task:
      name: AbbreviationDetection
      type: token-classification
    metrics:
    - name: Precision
      type: precision
      value: 0.9611772641
    - name: Recall
      type: recall
      value: 0.9446958783
    - name: F Score
      type: f_score
      value: 0.9528653083
---
| Feature | Description |
| --- | --- |
| **Name** | `en_abbreviation_detection_roberta_lar` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `transformer`, `abbreviationDetection` |
| **Components** | `transformer`, `abbreviationDetection` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | PLOSDataset-LREC22-Submitted |
| **License** | cc-by-sa-4.0 |
| **Author** | [Diptesh Kanojia](https://dipteshkanojia.github.io) |

### Label Scheme

<details>

<summary>View label scheme (3 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`abbreviationDetection`** | `AC`, `LF`, `O` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 95.29 |
| `ENTS_P` | 96.12 |
| `ENTS_R` | 94.47 |
| `TRANSFORMER_LOSS` | 287952.16 |
| `NER_LOSS` | 608954.79 |
