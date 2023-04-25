---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_scibert_ScienceIE
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9891304348
    - name: NER Recall
      type: recall
      value: 0.9923664122
    - name: NER F Score
      type: f_score
      value: 0.9907457812
---
| Feature | Description |
| --- | --- |
| **Name** | `en_scibert_ScienceIE` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.1.1,<3.2.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | UBIAI (https://ubiai.tools) |

### Label Scheme

<details>

<summary>View label scheme (3 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `MATERIAL`, `PROCESS`, `TASK` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 99.07 |
| `ENTS_P` | 98.91 |
| `ENTS_R` | 99.24 |
| `TRANSFORMER_LOSS` | 370249.46 |
| `NER_LOSS` | 216581.66 |