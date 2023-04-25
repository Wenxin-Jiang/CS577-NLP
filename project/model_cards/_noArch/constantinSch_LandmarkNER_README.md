---
tags:
- spacy
- token-classification
language:
- de
model-index:
- name: de_pipeline
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8379052369
    - name: NER Recall
      type: recall
      value: 0.8704663212
    - name: NER F Score
      type: f_score
      value: 0.8538754765
---
### Introduction
German Named Entity Recognition model for recognizing Bavarian landmarks. Fine-tuned "bert-base-german-cased" with 6450 annotated sentences of which 1467 contained landmarks, from subtitles of videos from Bayerischer Rundfunk.

| Feature | Description |
| --- | --- |
| **Name** | `de_pipeline` |
| **Version** | `0.1.0` |
| **spaCy** | `>=3.3.0,<3.4.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | Constantin Förster |

### Label Scheme

<details>

<summary>View label scheme (1 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `LM` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 85.39 |
| `ENTS_P` | 83.79 |
| `ENTS_R` | 87.05 |
| `TRANSFORMER_LOSS` | 4216.96 |
| `NER_LOSS` | 78511.31 |