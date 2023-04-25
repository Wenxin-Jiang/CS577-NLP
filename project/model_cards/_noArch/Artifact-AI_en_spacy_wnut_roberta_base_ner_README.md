---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_wnut_roberta_base_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.5875776398
    - name: NER Recall
      type: recall
      value: 0.5657894737
    - name: NER F Score
      type: f_score
      value: 0.5764777575
---
| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_wnut_roberta_base_ner` |
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
| `ENTS_F` | 57.65 |
| `ENTS_P` | 58.76 |
| `ENTS_R` | 56.58 |
| `TRANSFORMER_LOSS` | 67607.50 |
| `NER_LOSS` | 89310.00 |