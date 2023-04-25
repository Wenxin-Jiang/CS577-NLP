---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_wnut_xlm_roberta_base_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.6577540107
    - name: NER Recall
      type: recall
      value: 0.5885167464
    - name: NER F Score
      type: f_score
      value: 0.6212121212
---
| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_wnut_xlm_roberta_base_ner` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (6 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `corporation`, `creative-work`, `group`, `location`, `person`, `product` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 62.12 |
| `ENTS_P` | 65.78 |
| `ENTS_R` | 58.85 |
| `TRANSFORMER_LOSS` | 26744.67 |
| `NER_LOSS` | 38227.81 |