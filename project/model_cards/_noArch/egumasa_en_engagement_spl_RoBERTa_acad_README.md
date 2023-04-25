---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_engagement_spl_RoBERTa_acad
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.0
    - name: NER Recall
      type: recall
      value: 0.0
    - name: NER F Score
      type: f_score
      value: 0.0
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.0
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.0
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.0
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.0
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.8508399109
---
| Feature | Description |
| --- | --- |
| **Name** | `en_engagement_spl_RoBERTa_acad` |
| **Version** | `0.6.0` |
| **spaCy** | `>=3.4.4,<3.5.0` |
| **Default Pipeline** | `transformer`, `parser`, `tagger`, `ner`, `attribute_ruler`, `lemmatizer`, `trainable_transformer`, `spancat` |
| **Components** | `transformer`, `parser`, `tagger`, `ner`, `attribute_ruler`, `lemmatizer`, `trainable_transformer`, `spancat` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (124 labels for 4 components)</summary>

| Component | Labels |
| --- | --- |
| **`parser`** | `ROOT`, `acl`, `acomp`, `advcl`, `advmod`, `agent`, `amod`, `appos`, `attr`, `aux`, `auxpass`, `case`, `cc`, `ccomp`, `compound`, `conj`, `csubj`, `csubjpass`, `dative`, `dep`, `det`, `dobj`, `expl`, `intj`, `mark`, `meta`, `neg`, `nmod`, `npadvmod`, `nsubj`, `nsubjpass`, `nummod`, `oprd`, `parataxis`, `pcomp`, `pobj`, `poss`, `preconj`, `predet`, `prep`, `prt`, `punct`, `quantmod`, `relcl`, `xcomp` |
| **`tagger`** | `$`, `''`, `,`, `-LRB-`, `-RRB-`, `.`, `:`, `ADD`, `AFX`, `CC`, `CD`, `DT`, `EX`, `FW`, `HYPH`, `IN`, `JJ`, `JJR`, `JJS`, `LS`, `MD`, `NFP`, `NN`, `NNP`, `NNPS`, `NNS`, `PDT`, `POS`, `PRP`, `PRP$`, `RB`, `RBR`, `RBS`, `RP`, `SYM`, `TO`, `UH`, `VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`, `WDT`, `WP`, `WP$`, `WRB`, `XX`, ```` |
| **`ner`** | `CARDINAL`, `DATE`, `EVENT`, `FAC`, `GPE`, `LANGUAGE`, `LAW`, `LOC`, `MONEY`, `NORP`, `ORDINAL`, `ORG`, `PERCENT`, `PERSON`, `PRODUCT`, `QUANTITY`, `TIME`, `WORK_OF_ART` |
| **`spancat`** | `MONOGLOSS`, `ENDORSE`, `ENDOPHORIC`, `ENTERTAIN`, `PRONOUNCE`, `DENY`, `COUNTER`, `JUSTIFYING`, `ATTRIBUTE`, `SOURCES`, `CITATION`, `CONCUR` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `DEP_UAS` | 0.00 |
| `DEP_LAS` | 0.00 |
| `DEP_LAS_PER_TYPE` | 0.00 |
| `SENTS_P` | 82.24 |
| `SENTS_R` | 88.13 |
| `SENTS_F` | 85.08 |
| `TAG_ACC` | 0.00 |
| `ENTS_F` | 0.00 |
| `ENTS_P` | 0.00 |
| `ENTS_R` | 0.00 |
| `LEMMA_ACC` | 0.00 |
| `SPANS_SC_F` | 72.96 |
| `SPANS_SC_P` | 75.47 |
| `SPANS_SC_R` | 70.61 |
| `TRAINABLE_TRANSFORMER_LOSS` | 651.38 |
| `SPANCAT_LOSS` | 93570.83 |