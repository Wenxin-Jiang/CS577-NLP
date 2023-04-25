---
tags:
- spacy
- token-classification
- text-classification
language:
- en
model-index:
- name: en_healthsea
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 80.77
    - name: NER Recall
      type: recall
      value: 79.92
    - name: NER F Score
      type: f_score
      value: 80.34
---

# Welcome to Healthsea ✨
Create better access to health with machine learning and natural language processing. This is the trained healthsea pipeline for analyzing user reviews to supplements by extracting their effects on health. This pipeline features a trained NER model and a custom Text Classification model with Clause Segmentation and Blinding capabilities.

> Read more in the [blog post](https://explosion.ai/blog/healthsea) and visit the [healthsea repository](https://github.com/explosion/healthsea) for all training workflows, custom components and training data.

| Feature | Description |
| --- | --- |
| **Name** | `en_healthsea` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.0,<3.3.0` |
| **Default Pipeline** | `sentencizer`, `tok2vec`, `ner`, `benepar`, `segmentation`, `clausecat`, `aggregation` |
| **Components** | `sentencizer`, `tok2vec`, `ner`, `benepar`, `segmentation`, `clausecat`, `aggregation` |
| **Vectors** | 684830 keys, 684830 unique vectors (300 dimensions) |
| **Sources** | n/a |
| **License** | MIT |
| **Author** | [Explosion](explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (6 labels for 2 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `BENEFIT`, `CONDITION` |
| **`clausecat`** | `POSITIVE`, `NEUTRAL`, `NEGATIVE`, `ANAMNESIS` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 80.34 |
| `ENTS_P` | 80.77 |
| `ENTS_R` | 79.92 |
| `CATS_SCORE` | 74.87 |
| `CATS_MICRO_P` | 82.17 |
| `CATS_MICRO_R` | 80.85 |
| `CATS_MICRO_F` | 81.51 |
| `CATS_MACRO_P` | 78.01 |
| `CATS_MACRO_R` | 72.41 |
| `CATS_MACRO_F` | 74.87 |
| `CATS_MACRO_AUC` | 92.76 |
| `CATS_LOSS` | 297.22 |
