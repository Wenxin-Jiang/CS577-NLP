---
tags:
- spacy
- token-classification
language:
- is
model-index:
- name: is_ner_mim_sm
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8029028187
    - name: NER Recall
      type: recall
      value: 0.7796160131
    - name: NER F Score
      type: f_score
      value: 0.7910880829
---
| Feature | Description |
| --- | --- |
| **Name** | `is_ner_mim_sm` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.1.1,<3.2.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
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
| `ENTS_F` | 79.11 |
| `ENTS_P` | 80.29 |
| `ENTS_R` | 77.96 |
| `TOK2VEC_LOSS` | 1079057.14 |
| `NER_LOSS` | 792494.23 |