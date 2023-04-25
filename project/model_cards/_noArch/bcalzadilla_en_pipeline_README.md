---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_pipeline
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9840425532
    - name: NER Recall
      type: recall
      value: 0.9788359788
    - name: NER F Score
      type: f_score
      value: 0.9814323607
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (11 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `AMOUNT`, `BILLED TO`, `INVOICE DATE`, `INVOICE NUMBER`, `PROVIDER`, `TABLEROW 1`, `TABLEROW 2`, `TABLEROW 3`, `TABLEROW 4`, `TABLEROW 5`, `TABLEROW 6` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 99.17 |
| `ENTS_P` | 99.17 |
| `ENTS_R` | 99.17 |
| `TOK2VEC_LOSS` | 3632.16 |
| `NER_LOSS` | 11047.27 |