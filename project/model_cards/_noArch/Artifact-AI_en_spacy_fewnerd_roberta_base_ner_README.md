---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_spacy_fewnerd_roberta_base_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8410114129
    - name: NER Recall
      type: recall
      value: 0.8490622178
    - name: NER F Score
      type: f_score
      value: 0.8450176401
---
| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_fewnerd_roberta_base_ner` |
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

<summary>View label scheme (8 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `cation`, `ent`, `ganization`, `her`, `ilding`, `oduct`, `rson`, `t` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 84.50 |
| `ENTS_P` | 84.10 |
| `ENTS_R` | 84.91 |
| `TRANSFORMER_LOSS` | 584087.06 |
| `NER_LOSS` | 1240090.07 |