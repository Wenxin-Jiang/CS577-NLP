---
tags:
- spacy
- token-classification
language:
- de
license: cc-by-nc-4.0
model-index:
- name: de_RTA_NER
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8630136986
    - name: NER Recall
      type: recall
      value: 0.8743253662
    - name: NER F Score
      type: f_score
      value: 0.8686327078
---
Regensburger Reichstag von 1576

| Feature | Description |
| --- | --- |
| **Name** | `de_RTA_NER` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.1.0,<3.2.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | `https://creativecommons.org/licenses/by-nc/4.0/` |
| **Author** | [n/a](https://reichstagsakten-1576.uni-graz.at) |

### Label Scheme

<details>

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `DATE`, `LOC`, `PER`, `TIME` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 86.86 |
| `ENTS_P` | 86.30 |
| `ENTS_R` | 87.43 |
| `TOK2VEC_LOSS` | 43588.74 |
| `NER_LOSS` | 95573.96 |
