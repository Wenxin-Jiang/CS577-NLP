---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_conll2003_xlm_roberta_base_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.951947395
    - name: NER Recall
      type: recall
      value: 0.9501851229
    - name: NER F Score
      type: f_score
      value: 0.9510654426
---
| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_conll2003_xlm_roberta_base_ner` |
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

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `LOC`, `MISC`, `ORG`, `PER` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 95.11 |
| `ENTS_P` | 95.19 |
| `ENTS_R` | 95.02 |
| `TRANSFORMER_LOSS` | 17326.80 |
| `NER_LOSS` | 25273.70 |