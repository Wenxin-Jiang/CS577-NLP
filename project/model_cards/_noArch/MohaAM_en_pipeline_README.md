---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_pipeline
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9946896173
    - name: NER Recall
      type: recall
      value: 0.9916932907
    - name: NER F Score
      type: f_score
      value: 0.9931891941
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
      value: 1.0
    - name: SENTER Recall
      type: recall
      value: 1.0
    - name: SENTER F Score
      type: f_score
      value: 1.0
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Dependencies Accuracy
      type: accuracy
      value: 0.0
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Dependencies Accuracy
      type: accuracy
      value: 0.0
---
| Feature | Description |
| --- | --- |
| **Name** | `en_pipeline` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.1.0,<3.2.0` |
| **Default Pipeline** | `tok2vec`, `tagger`, `parser`, `ner`, `attribute_ruler`, `lemmatizer` |
| **Components** | `tok2vec`, `tagger`, `parser`, `ner`, `attribute_ruler`, `lemmatizer` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (114 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `$`, `''`, `,`, `-LRB-`, `-RRB-`, `.`, `:`, `ADD`, `AFX`, `CC`, `CD`, `DT`, `EX`, `FW`, `HYPH`, `IN`, `JJ`, `JJR`, `JJS`, `LS`, `MD`, `NFP`, `NN`, `NNP`, `NNPS`, `NNS`, `PDT`, `POS`, `PRP`, `PRP$`, `RB`, `RBR`, `RBS`, `RP`, `SYM`, `TO`, `UH`, `VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`, `WDT`, `WP`, `WP$`, `WRB`, `XX`, ```` |
| **`parser`** | `ROOT`, `acl`, `acomp`, `advcl`, `advmod`, `agent`, `amod`, `appos`, `attr`, `aux`, `auxpass`, `case`, `cc`, `ccomp`, `compound`, `conj`, `csubj`, `csubjpass`, `dative`, `dep`, `det`, `dobj`, `expl`, `intj`, `mark`, `meta`, `neg`, `nmod`, `npadvmod`, `nsubj`, `nsubjpass`, `nummod`, `oprd`, `parataxis`, `pcomp`, `pobj`, `poss`, `preconj`, `predet`, `prep`, `prt`, `punct`, `quantmod`, `relcl`, `xcomp` |
| **`ner`** | `ARC`, `AST`, `BOOK`, `CAUSAL`, `COMPARISON`, `DATE`, `HEM`, `HOUR`, `HYPO`, `INSTRUMENT`, `JUDGEMENT`, `LAWS`, `MODEL`, `NAME`, `Observation`, `PAR`, `PLACE`, `QUANTITY`, `REASON`, `ZOD` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TAG_ACC` | 0.00 |
| `DEP_UAS` | 0.00 |
| `DEP_LAS` | 0.00 |
| `DEP_LAS_PER_TYPE` | 0.00 |
| `SENTS_P` | 100.00 |
| `SENTS_R` | 100.00 |
| `SENTS_F` | 100.00 |
| `ENTS_F` | 99.32 |
| `ENTS_P` | 99.47 |
| `ENTS_R` | 99.17 |
| `LEMMA_ACC` | 0.00 |
| `NER_LOSS` | 7790.09 |
