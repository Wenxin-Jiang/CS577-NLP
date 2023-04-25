---
tags:
- spacy
- token-classification
language:
- de
model-index:
- name: de_fnhd_nerdh
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9629324547
    - name: NER Recall
      type: recall
      value: 0.9504065041
    - name: NER F Score
      type: f_score
      value: 0.9566284779
---
Deutsche NER-Pipeline für frühneuhochdeutsche Texte (2.Version)

| Feature | Description |
| --- | --- |
| **Name** | `de_fnhd_nerdh` |
| **Version** | `0.0.2` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 500000 keys, 500000 unique vectors (300 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [ih]() |

### Label Scheme

<details>

<summary>View label scheme (5 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `OBJEKT`, `ORGANISATION`, `ORT`, `PERSON`, `ZEIT` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 95.66 |
| `ENTS_P` | 96.29 |
| `ENTS_R` | 95.04 |
| `TOK2VEC_LOSS` | 25311.59 |
| `NER_LOSS` | 15478.32 |