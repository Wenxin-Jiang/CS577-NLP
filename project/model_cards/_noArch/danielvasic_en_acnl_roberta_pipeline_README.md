---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_acnl_roberta_pipeline
  results:
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS Accuracy
      type: accuracy
      value: 0.9805220696
  - task:
      name: SENTER
      type: token-classification
    metrics:
    - name: SENTER Precision
      type: precision
      value: 0.9380376859
    - name: SENTER Recall
      type: recall
      value: 0.954223356
    - name: SENTER F Score
      type: f_score
      value: 0.946061298
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Dependencies Accuracy
      type: accuracy
      value: 0.9597776646
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Dependencies Accuracy
      type: accuracy
      value: 0.9597776646
license: cc-by-4.0
datasets:
- conll2012_ontonotesv5
metrics:
- f1
library_name: spacy
pipeline_tag: text-classification
---
| Feature | Description |
| --- | --- |
| **Name** | `en_acnl_roberta_pipeline` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.1.3,<3.2.0` |
| **Default Pipeline** | `transformer`, `tagger`, `parser` |
| **Components** | `transformer`, `tagger`, `parser` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | OntoNotes |
| **License** | CC BY-SA 4.0 |
| **Author** | Daniel Vasić |

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
| `TAG_ACC` | 98.05 |
| `DEP_UAS` | 95.98 |
| `DEP_LAS` | 94.83 |
| `SENTS_P` | 93.80 |
| `SENTS_R` | 95.42 |
| `SENTS_F` | 94.61 |
| `TRANSFORMER_LOSS` | 3784861.59 |
| `TAGGER_LOSS` | 698704.80 |
| `PARSER_LOSS` | 5540167.00 |