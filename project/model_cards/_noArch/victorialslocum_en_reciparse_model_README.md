---
tags:
- spacy
- token-classification
language:
- en
license: mit
widget:
- text: "Season the chicken inside and out with salt and pepper, really getting into all of the crevices. Let the chicken hang out for at least 1 hour at room temperature, which will help the meat absorb the salt. If you can season a few days in advance and let rest, uncovered, in the fridge, even better."
---
| Feature | Description |
| --- | --- |
| **Name** | `en_reciparse_model` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.3.1,<3.4.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (1 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `INGREDIENT` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 87.97 |
| `ENTS_P` | 88.54 |
| `ENTS_R` | 87.40 |
| `TOK2VEC_LOSS` | 37557.71 |
| `NER_LOSS` | 19408.65 |