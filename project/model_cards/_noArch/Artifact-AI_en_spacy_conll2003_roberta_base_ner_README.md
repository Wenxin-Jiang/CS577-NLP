---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_conll2003_roberta_base_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9572935857
    - name: NER Recall
      type: recall
      value: 0.9619656681
    - name: NER F Score
      type: f_score
      value: 0.9596239402
---
| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_conll2003_roberta_base_ner` |
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
| `ENTS_F` | 95.96 |
| `ENTS_P` | 95.73 |
| `ENTS_R` | 96.20 |
| `TRANSFORMER_LOSS` | 10078.40 |
| `NER_LOSS` | 13928.28 |