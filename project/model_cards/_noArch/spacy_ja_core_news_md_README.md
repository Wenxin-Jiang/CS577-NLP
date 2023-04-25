---
tags:
- spacy
- token-classification
language:
- ja
license: cc-by-sa-4.0
model-index:
- name: ja_core_news_md
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.7121418827
    - name: NER Recall
      type: recall
      value: 0.6566037736
    - name: NER F Score
      type: f_score
      value: 0.6832460733
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
      value: 0.9721881391
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
      value: 0.9203675345
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.9074140723
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9774730656
---
### Details: https://spacy.io/models/ja#ja_core_news_md

Japanese pipeline optimized for CPU. Components: tok2vec, morphologizer, parser, senter, ner, attribute_ruler.

| Feature | Description |
| --- | --- |
| **Name** | `ja_core_news_md` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `tok2vec`, `morphologizer`, `parser`, `attribute_ruler`, `ner` |
| **Components** | `tok2vec`, `morphologizer`, `parser`, `senter`, `attribute_ruler`, `ner` |
| **Vectors** | 480443 keys, 20000 unique vectors (300 dimensions) |
| **Sources** | [UD Japanese GSD v2.8](https://github.com/UniversalDependencies/UD_Japanese-GSD) (Omura, Mai; Miyao, Yusuke; Kanayama, Hiroshi; Matsuda, Hiroshi; Wakasa, Aya; Yamashita, Kayo; Asahara, Masayuki; Tanaka, Takaaki; Murawaki, Yugo; Matsumoto, Yuji; Mori, Shinsuke; Uematsu, Sumire; McDonald, Ryan; Nivre, Joakim; Zeman, Daniel)<br />[UD Japanese GSD v2.8 NER](https://github.com/megagonlabs/UD_Japanese-GSD) (Megagon Labs Tokyo)<br />[chiVe: Japanese Word Embedding with Sudachi & NWJC (chive-1.1-mc90-500k)](https://github.com/WorksApplications/chiVe) (Works Applications) |
| **License** | `CC BY-SA 4.0` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (65 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`morphologizer`** | `POS=NOUN`, `POS=ADP`, `POS=VERB`, `POS=SCONJ`, `POS=AUX`, `POS=PUNCT`, `POS=PART`, `POS=DET`, `POS=NUM`, `POS=ADV`, `POS=PRON`, `POS=ADJ`, `POS=PROPN`, `POS=CCONJ`, `POS=SYM`, `POS=NOUN\|Polarity=Neg`, `POS=AUX\|Polarity=Neg`, `POS=SPACE`, `POS=INTJ`, `POS=SCONJ\|Polarity=Neg` |
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
| `POS_ACC` | 97.22 |
| `MORPH_ACC` | 0.00 |
| `MORPH_MICRO_P` | 34.01 |
| `MORPH_MICRO_R` | 98.04 |
| `MORPH_MICRO_F` | 50.51 |
| `SENTS_P` | 97.08 |
| `SENTS_R` | 98.42 |
| `SENTS_F` | 97.75 |
| `DEP_UAS` | 92.04 |
| `DEP_LAS` | 90.74 |
| `TAG_ACC` | 97.12 |
| `LEMMA_ACC` | 96.71 |
| `ENTS_P` | 71.21 |
| `ENTS_R` | 65.66 |
| `ENTS_F` | 68.32 |