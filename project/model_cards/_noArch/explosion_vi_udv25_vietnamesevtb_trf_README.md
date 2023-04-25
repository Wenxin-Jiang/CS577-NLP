---
tags:
- spacy
- token-classification
language:
- vi
license: cc-by-sa-4.0
model-index:
- name: vi_udv25_vietnamesevtb_trf
  results:
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.8805048216
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9018631331
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9695345305
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.8934519139
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.6807696182
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.6063552526
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.943275972
---
UD v2.5 benchmarking pipeline for UD_Vietnamese-VTB

| Feature | Description |
| --- | --- |
| **Name** | `vi_udv25_vietnamesevtb_trf` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `experimental_char_ner_tokenizer`, `transformer`, `tagger`, `morphologizer`, `parser`, `experimental_edit_tree_lemmatizer` |
| **Components** | `experimental_char_ner_tokenizer`, `transformer`, `senter`, `tagger`, `morphologizer`, `parser`, `experimental_edit_tree_lemmatizer` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [Universal Dependencies v2.5](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3105) (Zeman, Daniel; et al.) |
| **License** | `CC BY-SA 4.0` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (81 labels for 6 components)</summary>

| Component | Labels |
| --- | --- |
| **`experimental_char_ner_tokenizer`** | `TOKEN` |
| **`senter`** | `I`, `S` |
| **`tagger`** | `!`, `"`, `,`, `-`, `.`, `...`, `:`, `;`, `?`, `@`, `A`, `C`, `CC`, `E`, `I`, `L`, `LBKT`, `M`, `N`, `NP`, `Nb`, `Nc`, `Np`, `Nu`, `Ny`, `P`, `R`, `RBKT`, `T`, `V`, `VP`, `X`, `Y`, `Z` |
| **`morphologizer`** | `POS=NOUN`, `POS=ADP`, `POS=X\|Polarity=Neg`, `POS=VERB`, `POS=ADJ`, `POS=PUNCT`, `POS=X`, `POS=SCONJ`, `NumType=Card\|POS=NUM`, `POS=DET`, `POS=CCONJ`, `POS=PROPN`, `POS=AUX`, `POS=PART`, `POS=INTJ` |
| **`parser`** | `ROOT`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `ccomp`, `compound`, `conj`, `cop`, `csubj`, `dep`, `det`, `discourse`, `iobj`, `list`, `mark`, `nmod`, `nsubj`, `nummod`, `obj`, `obl`, `parataxis`, `punct`, `xcomp` |
| **`experimental_edit_tree_lemmatizer`** | `0` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_F` | 87.90 |
| `TOKEN_P` | 86.84 |
| `TOKEN_R` | 89.00 |
| `TOKEN_ACC` | 98.42 |
| `SENTS_F` | 94.33 |
| `SENTS_P` | 96.23 |
| `SENTS_R` | 92.50 |
| `TAG_ACC` | 88.05 |
| `POS_ACC` | 90.19 |
| `MORPH_ACC` | 96.95 |
| `DEP_UAS` | 68.08 |
| `DEP_LAS` | 60.64 |
| `LEMMA_ACC` | 89.35 |