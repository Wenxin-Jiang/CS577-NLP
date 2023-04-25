---
tags:
- spacy
- token-classification
language:
- fr
model-index:
- name: fr_ner_ingredients
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8990228013
    - name: NER Recall
      type: recall
      value: 0.9019607843
    - name: NER F Score
      type: f_score
      value: 0.9004893964
---
| Feature | Description |
| --- | --- |
| **Name** | `fr_ner_ingredients` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (5 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `BRAND`, `FOOD PRODUCT`, `INGREDIENT`, `MEASURE`, `QUANTITY` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 90.05 |
| `ENTS_P` | 89.90 |
| `ENTS_R` | 90.20 |
| `TOK2VEC_LOSS` | 65769.53 |
| `NER_LOSS` | 7865.95 |