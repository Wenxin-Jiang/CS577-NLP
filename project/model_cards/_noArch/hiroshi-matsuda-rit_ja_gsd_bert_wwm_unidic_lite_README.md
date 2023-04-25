---
tags:
- spacy
- token-classification
language:
- ja
license: CC-BY-SA-4.0
model-index:
- name: ja_gsd_bert_wwm_unidic_lite
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8496143959
    - name: NER Recall
      type: recall
      value: 0.8314465409
    - name: NER F Score
      type: f_score
      value: 0.840432295
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS Accuracy
      type: accuracy
      value: 0.0
  - task:
      name: SENTER
      type: token-classification
    metrics:
    - name: SENTER Precision
      type: precision
      value: 0.9201520913
    - name: SENTER Recall
      type: recall
      value: 0.9546351085
    - name: SENTER F Score
      type: f_score
      value: 0.9370764763
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Dependencies Accuracy
      type: accuracy
      value: 0.9367795389
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Dependencies Accuracy
      type: accuracy
      value: 0.9367795389
---
Japanese transformer pipeline (bert-base). Components: transformer, parser, ner.

| Feature | Description |
| --- | --- |
| **Name** | `ja_gsd_bert_wwm_unidic_lite` |
| **Version** | `3.1.1` |
| **spaCy** | `>=3.1.0,<3.2.0` |
| **Default Pipeline** | `transformer`, `parser`, `ner` |
| **Components** | `transformer`, `parser`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [UD_Japanese-GSD](https://github.com/UniversalDependencies/UD_Japanese-GSD)<br />[UD_Japanese-GSD r2.8+NE](https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8-NE)<br />[SudachiDict_core](https://github.com/WorksApplications/SudachiDict)<br />[cl-tohoku/bert-base-japanese-whole-word-masking](https://huggingface.co/cl-tohoku/bert-base-japanese-whole-word-masking)<br />[unidic_lite](https://github.com/polm/unidic-lite) |
| **License** | `CC BY-SA 4.0` |
| **Author** | [Megagon Labs Tokyo.](https://github.com/megagonlabs/UD_japanese_GSD) |

### Label Scheme

<details>

<summary>View label scheme (45 labels for 2 components)</summary>

| Component | Labels |
| --- | --- |
| **`parser`** | `ROOT`, `acl`, `advcl`, `advmod`, `amod`, `aux`, `case`, `cc`, `ccomp`, `compound`, `cop`, `csubj`, `dep`, `det`, `dislocated`, `fixed`, `mark`, `nmod`, `nsubj`, `nummod`, `obj`, `obl`, `punct` |
| **`ner`** | `CARDINAL`, `DATE`, `EVENT`, `FAC`, `GPE`, `LANGUAGE`, `LAW`, `LOC`, `MONEY`, `MOVEMENT`, `NORP`, `ORDINAL`, `ORG`, `PERCENT`, `PERSON`, `PET_NAME`, `PHONE`, `PRODUCT`, `QUANTITY`, `TIME`, `TITLE_AFFIX`, `WORK_OF_ART` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `DEP_UAS` | 93.68 |
| `DEP_LAS` | 92.61 |
| `SENTS_P` | 92.02 |
| `SENTS_R` | 95.46 |
| `SENTS_F` | 93.71 |
| `ENTS_F` | 84.04 |
| `ENTS_P` | 84.96 |
| `ENTS_R` | 83.14 |
| `TAG_ACC` | 0.00 |
| `TRANSFORMER_LOSS` | 28861.67 |
| `PARSER_LOSS` | 1306248.63 |
| `NER_LOSS` | 13993.36 |
