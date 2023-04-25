---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_conll2003_distilroberta_base_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9569910609
    - name: NER Recall
      type: recall
      value: 0.954897341
    - name: NER F Score
      type: f_score
      value: 0.9559430545
---
| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_conll2003_distilroberta_base_ner` |
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
| `ENTS_F` | 95.59 |
| `ENTS_P` | 95.70 |
| `ENTS_R` | 95.49 |
| `TRANSFORMER_LOSS` | 84212.33 |
| `NER_LOSS` | 104250.60 |