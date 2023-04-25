---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_wnut_distilroberta_base_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.5612366231
    - name: NER Recall
      type: recall
      value: 0.5645933014
    - name: NER F Score
      type: f_score
      value: 0.5629099583
---
| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_wnut_distilroberta_base_ner` |
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
| `ENTS_F` | 56.29 |
| `ENTS_P` | 56.12 |
| `ENTS_R` | 56.46 |
| `TRANSFORMER_LOSS` | 148295.07 |
| `NER_LOSS` | 193452.51 |