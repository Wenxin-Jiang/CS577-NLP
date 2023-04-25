---
tags:
- spacy
- token-classification
language:
- ja
license: cc-by-sa-3.0
model-index:
- name: ja_core_news_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8298969072
    - name: NER Recall
      type: recall
      value: 0.8100628931
    - name: NER F Score
      type: f_score
      value: 0.8198599618
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9712488769
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9798207196
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.0
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9670526831
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9355666622
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.9241776538
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9755142018
---
### Details: https://spacy.io/models/ja#ja_core_news_trf

Japanese transformer pipeline (cl-tohoku/bert-base-japanese-char-v2). Components: transformer, morphologizer, parser, ner.

| Feature | Description |
| --- | --- |
| **Name** | `ja_core_news_trf` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `transformer`, `morphologizer`, `parser`, `attribute_ruler`, `ner` |
| **Components** | `transformer`, `morphologizer`, `parser`, `attribute_ruler`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [UD Japanese GSD v2.8](https://github.com/UniversalDependencies/UD_Japanese-GSD) (Omura, Mai; Miyao, Yusuke; Kanayama, Hiroshi; Matsuda, Hiroshi; Wakasa, Aya; Yamashita, Kayo; Asahara, Masayuki; Tanaka, Takaaki; Murawaki, Yugo; Matsumoto, Yuji; Mori, Shinsuke; Uematsu, Sumire; McDonald, Ryan; Nivre, Joakim; Zeman, Daniel)<br />[UD Japanese GSD v2.8 NER](https://github.com/megagonlabs/UD_Japanese-GSD) (Megagon Labs Tokyo)<br />[cl-tohoku/bert-base-japanese-char-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v2) (Inui Laboratory, Tohoku University) |
| **License** | `CC BY-SA 3.0` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (64 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`morphologizer`** | `POS=NOUN`, `POS=ADP`, `POS=VERB`, `POS=SCONJ`, `POS=AUX`, `POS=PUNCT`, `POS=PART`, `POS=DET`, `POS=NUM`, `POS=ADV`, `POS=PRON`, `POS=ADJ`, `POS=PROPN`, `POS=CCONJ`, `POS=SYM`, `POS=NOUN\|Polarity=Neg`, `POS=AUX\|Polarity=Neg`, `POS=INTJ`, `POS=SCONJ\|Polarity=Neg` |
| **`parser`** | `ROOT`, `acl`, `advcl`, `advmod`, `amod`, `aux`, `case`, `cc`, `ccomp`, `compound`, `cop`, `csubj`, `dep`, `det`, `dislocated`, `fixed`, `mark`, `nmod`, `nsubj`, `nummod`, `obj`, `obl`, `punct` |
| **`ner`** | `CARDINAL`, `DATE`, `EVENT`, `FAC`, `GPE`, `LANGUAGE`, `LAW`, `LOC`, `MONEY`, `MOVEMENT`, `NORP`, `ORDINAL`, `ORG`, `PERCENT`, `PERSON`, `PET_NAME`, `PHONE`, `PRODUCT`, `QUANTITY`, `TIME`, `TITLE_AFFIX`, `WORK_OF_ART` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_ACC` | 99.37 |
| `TOKEN_P` | 97.65 |
| `TOKEN_R` | 97.90 |
| `TOKEN_F` | 97.77 |
| `POS_ACC` | 97.98 |
| `MORPH_ACC` | 0.00 |
| `MORPH_MICRO_P` | 33.56 |
| `MORPH_MICRO_R` | 96.08 |
| `MORPH_MICRO_F` | 49.75 |
| `SENTS_P` | 96.89 |
| `SENTS_R` | 98.22 |
| `SENTS_F` | 97.55 |
| `DEP_UAS` | 93.56 |
| `DEP_LAS` | 92.42 |
| `TAG_ACC` | 97.12 |
| `LEMMA_ACC` | 96.71 |
| `ENTS_P` | 82.99 |
| `ENTS_R` | 81.01 |
| `ENTS_F` | 81.99 |