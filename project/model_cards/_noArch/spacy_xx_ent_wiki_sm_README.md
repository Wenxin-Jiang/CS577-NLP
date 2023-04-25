---
tags:
- spacy
- token-classification
language:
- multilingual
license: mit
model-index:
- name: xx_ent_wiki_sm
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8352564288
    - name: NER Recall
      type: recall
      value: 0.8264712666
    - name: NER F Score
      type: f_score
      value: 0.8308406251
---
### Details: https://spacy.io/models/xx#xx_ent_wiki_sm

Multi-language pipeline optimized for CPU. Components: ner.

| Feature | Description |
| --- | --- |
| **Name** | `xx_ent_wiki_sm` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `ner` |
| **Components** | `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [WikiNER](https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500) (Joel Nothman, Nicky Ringland, Will Radford, Tara Murphy, James R Curran) |
| **License** | `MIT` |
| **Author** | [Explosion](https://explosion.ai) |

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
| `ENTS_P` | 83.53 |
| `ENTS_R` | 82.65 |
| `ENTS_F` | 83.08 |