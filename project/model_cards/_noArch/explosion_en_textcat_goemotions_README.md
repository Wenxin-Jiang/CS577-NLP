---
tags:
- spacy
- text-classification
language:
- en
license: mit
model-index:
- name: en_textcat_goemotions
  results: []
---
# 🪐 spaCy Project: Categorization of emotions in Reddit posts (Text Classification) This project uses spaCy to train a text classifier on the [GoEmotions dataset](https://github.com/google-research/google-research/tree/master/goemotions)

| Feature | Description |
| --- | --- |
| **Name** | `en_textcat_goemotions` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.1.1,<3.2.0` |
| **Default Pipeline** | `transformer`, `textcat_multilabel` |
| **Components** | `transformer`, `textcat_multilabel` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [GoEmotions dataset](https://github.com/google-research/google-research/tree/master/goemotions) |
| **License** | `MIT` |
| **Author** | [Explosion](explosion.ai) |


> The dataset that this model is trained on has known flaws described [here](https://github.com/google-research/google-research/tree/master/goemotions#disclaimer) as well as label errors resulting from [annotator disagreement](https://www.youtube.com/watch?v=khZ5-AN-n2Y). Anyone using this model should be aware of these limitations of the dataset.

### Label Scheme

<details>

<summary>View label scheme (28 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`textcat_multilabel`** | `admiration`, `amusement`, `anger`, `annoyance`, `approval`, `caring`, `confusion`, `curiosity`, `desire`, `disappointment`, `disapproval`, `disgust`, `embarrassment`, `excitement`, `fear`, `gratitude`, `grief`, `joy`, `love`, `nervousness`, `optimism`, `pride`, `realization`, `relief`, `remorse`, `sadness`, `surprise`, `neutral` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `CATS_SCORE` | 90.22 |
| `CATS_MICRO_P` | 66.67 |
| `CATS_MICRO_R` | 47.81 |
| `CATS_MICRO_F` | 55.68 |
| `CATS_MACRO_P` | 55.00 |
| `CATS_MACRO_R` | 41.93 |
| `CATS_MACRO_F` | 46.29 |
| `CATS_MACRO_AUC` | 90.22 |
| `CATS_MACRO_AUC_PER_TYPE` | 0.00 |
| `TRANSFORMER_LOSS` | 83.51 |
| `TEXTCAT_MULTILABEL_LOSS` | 4549.84 |
