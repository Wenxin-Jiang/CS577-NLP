---
tags:
- spacy
- token-classification
language:
- is
model-index:
- name: is_ner_mim_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9193318395
    - name: NER Recall
      type: recall
      value: 0.9217728758
    - name: NER F Score
      type: f_score
      value: 0.9205507394
---
| Feature | Description |
| --- | --- |
| **Name** | `is_ner_mim_trf` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.1.1,<3.2.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (8 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Date`, `Location`, `Miscellaneous`, `Money`, `Organization`, `Percent`, `Person`, `Time` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 92.06 |
| `ENTS_P` | 91.93 |
| `ENTS_R` | 92.18 |
| `TRANSFORMER_LOSS` | 248325.98 |
| `NER_LOSS` | 120059.07 |