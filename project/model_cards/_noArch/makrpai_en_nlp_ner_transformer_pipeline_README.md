---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_nlp_ner_transformer_pipeline
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9959297344
    - name: NER Recall
      type: recall
      value: 0.9981392686
    - name: NER F Score
      type: f_score
      value: 0.9970332773
---
| Feature | Description |
| --- | --- |
| **Name** | `en_nlp_ner_transformer_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.4,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [mak]() |

### Label Scheme

<details>

<summary>View label scheme (7 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `BI Tools`, `Financial`, `HCM`, `Hybris`, `Netweaver`, `SAP`, `Supply Chain` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 99.70 |
| `ENTS_P` | 99.59 |
| `ENTS_R` | 99.81 |
| `TRANSFORMER_LOSS` | 5936.42 |
| `NER_LOSS` | 13605.26 |