---
tags:
- spacy
- token-classification
language:
- en
model-index:
- name: en_engagement_RoBERTa_combined
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
      value: 0.9764065336
---
| Feature | Description |
| --- | --- |
| **Name** | `en_engagement_RoBERTa_combined` |
| **Version** | `AtoI_0.1.85` |
| **spaCy** | `>=3.3.0,<3.4.0` |
| **Default Pipeline** | `transformer`, `tagger`, `parser`, `ner`, `trainable_transformer`, `span_finder`, `spancat` |
| **Components** | `transformer`, `tagger`, `parser`, `ner`, `trainable_transformer`, `span_finder`, `spancat` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (124 labels for 4 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `$`, `''`, `,`, `-LRB-`, `-RRB-`, `.`, `:`, `ADD`, `AFX`, `CC`, `CD`, `DT`, `EX`, `FW`, `HYPH`, `IN`, `JJ`, `JJR`, `JJS`, `LS`, `MD`, `NFP`, `NN`, `NNP`, `NNPS`, `NNS`, `PDT`, `POS`, `PRP`, `PRP$`, `RB`, `RBR`, `RBS`, `RP`, `SYM`, `TO`, `UH`, `VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`, `WDT`, `WP`, `WP$`, `WRB`, `XX`, ```` |
| **`parser`** | `ROOT`, `acl`, `acomp`, `advcl`, `advmod`, `agent`, `amod`, `appos`, `attr`, `aux`, `auxpass`, `case`, `cc`, `ccomp`, `compound`, `conj`, `csubj`, `csubjpass`, `dative`, `dep`, `det`, `dobj`, `expl`, `intj`, `mark`, `meta`, `neg`, `nmod`, `npadvmod`, `nsubj`, `nsubjpass`, `nummod`, `oprd`, `parataxis`, `pcomp`, `pobj`, `poss`, `preconj`, `predet`, `prep`, `prt`, `punct`, `quantmod`, `relcl`, `xcomp` |
| **`ner`** | `CARDINAL`, `DATE`, `EVENT`, `FAC`, `GPE`, `LANGUAGE`, `LAW`, `LOC`, `MONEY`, `NORP`, `ORDINAL`, `ORG`, `PERCENT`, `PERSON`, `PRODUCT`, `QUANTITY`, `TIME`, `WORK_OF_ART` |
| **`spancat`** | `MONOGLOSS`, `ATTRIBUTE`, `JUSTIFY`, `COUNTER`, `CITATION`, `ENTERTAIN`, `ENDORSE`, `DENY`, `CONCUR`, `PRONOUNCE`, `TEMPORAL`, `CONTRAST` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TAG_ACC` | 0.00 |
| `DEP_UAS` | 0.00 |
| `DEP_LAS` | 0.00 |
| `DEP_LAS_PER_TYPE` | 0.00 |
| `SENTS_P` | 96.76 |
| `SENTS_R` | 98.53 |
| `SENTS_F` | 97.64 |
| `ENTS_F` | 0.00 |
| `ENTS_P` | 0.00 |
| `ENTS_R` | 0.00 |
| `SPAN_FINDER_SPAN_CANDIDATES_F` | 50.09 |
| `SPAN_FINDER_SPAN_CANDIDATES_P` | 35.70 |
| `SPAN_FINDER_SPAN_CANDIDATES_R` | 83.94 |
| `SPANS_SC_F` | 76.49 |
| `SPANS_SC_P` | 75.89 |
| `SPANS_SC_R` | 77.11 |
| `LEMMA_ACC` | 0.00 |
| `TRAINABLE_TRANSFORMER_LOSS` | 1535.39 |
| `SPAN_FINDER_LOSS` | 20411.83 |
| `SPANCAT_LOSS` | 24075.13 |