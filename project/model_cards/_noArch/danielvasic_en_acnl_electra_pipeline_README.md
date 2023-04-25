---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_acnl_electra_pipeline
  results:
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS Accuracy
      type: accuracy
      value: 0.9769257272
  - task:
      name: SENTER
      type: token-classification
    metrics:
    - name: SENTER Precision
      type: precision
      value: 0.9508884151
    - name: SENTER Recall
      type: recall
      value: 0.94805839
    - name: SENTER F Score
      type: f_score
      value: 0.9494712937
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Dependencies Accuracy
      type: accuracy
      value: 0.9577103137
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Dependencies Accuracy
      type: accuracy
      value: 0.9577103137
---
| Feature | Description |
| --- | --- |
| **Name** | `en_acnl_electra_pipeline` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.1.3,<3.2.0` |
| **Default Pipeline** | `transformer`, `tagger`, `parser` |
| **Components** | `transformer`, `tagger`, `parser` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | GPL |
| **Author** | Daniel Vasić() |

### Label Scheme

<details>

<summary>View label scheme (87 labels for 2 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `$`, `''`, `,`, `-LRB-`, `-RRB-`, `.`, `:`, `ADD`, `AFX`, `CC`, `CD`, `DT`, `EX`, `FW`, `HYPH`, `IN`, `JJ`, `JJR`, `JJS`, `LS`, `MD`, `NFP`, `NN`, `NNP`, `NNPS`, `NNS`, `PDT`, `POS`, `PRP`, `PRP$`, `RB`, `RBR`, `RBS`, `RP`, `SYM`, `TO`, `UH`, `VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`, `VERB`, `WDT`, `WP`, `WP$`, `WRB`, `XX`, ```` |
| **`parser`** | `ROOT`, `acl`, `acomp`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `auxpass`, `case`, `cc`, `ccomp`, `compound`, `conj`, `dative`, `dep`, `det`, `dobj`, `intj`, `mark`, `meta`, `neg`, `nmod`, `npadvmod`, `nummod`, `parataxis`, `pcomp`, `pobj`, `poss`, `preconj`, `predet`, `prep`, `prt`, `punct`, `quantmod`, `relcl`, `xcomp` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TAG_ACC` | 97.69 |
| `DEP_UAS` | 95.77 |
| `DEP_LAS` | 94.52 |
| `SENTS_P` | 95.09 |
| `SENTS_R` | 94.81 |
| `SENTS_F` | 94.95 |
| `TRANSFORMER_LOSS` | 6123357.72 |
| `TAGGER_LOSS` | 338995.26 |
| `PARSER_LOSS` | 4101825.66 |