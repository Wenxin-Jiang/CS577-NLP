---
tags:
- spacy
- token-classification
language:
- en
license: mit
model-index:
- name: en_stylecheck
  results: []
---
Check style on English text (currently passive text).

| Feature | Description |
| --- | --- |
| **Name** | `en_stylecheck` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.1.1,<3.2.0` |
| **Default Pipeline** | `tok2vec`, `tagger`, `parser`, `attribute_ruler`, `lemmatizer`, `ner`, `stylecheck` |
| **Components** | `tok2vec`, `tagger`, `parser`, `senter`, `attribute_ruler`, `lemmatizer`, `ner`, `stylecheck` |
| **Vectors** | 684830 keys, 20000 unique vectors (300 dimensions) |
| **Sources** | n/a |
| **License** | `MIT` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (115 labels for 5 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `$`, `''`, `,`, `-LRB-`, `-RRB-`, `.`, `:`, `ADD`, `AFX`, `CC`, `CD`, `DT`, `EX`, `FW`, `HYPH`, `IN`, `JJ`, `JJR`, `JJS`, `LS`, `MD`, `NFP`, `NN`, `NNP`, `NNPS`, `NNS`, `PDT`, `POS`, `PRP`, `PRP$`, `RB`, `RBR`, `RBS`, `RP`, `SYM`, `TO`, `UH`, `VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`, `WDT`, `WP`, `WP$`, `WRB`, `XX`, ```` |
| **`parser`** | `ROOT`, `acl`, `acomp`, `advcl`, `advmod`, `agent`, `amod`, `appos`, `attr`, `aux`, `auxpass`, `case`, `cc`, `ccomp`, `compound`, `conj`, `csubj`, `csubjpass`, `dative`, `dep`, `det`, `dobj`, `expl`, `intj`, `mark`, `meta`, `neg`, `nmod`, `npadvmod`, `nsubj`, `nsubjpass`, `nummod`, `oprd`, `parataxis`, `pcomp`, `pobj`, `poss`, `preconj`, `predet`, `prep`, `prt`, `punct`, `quantmod`, `relcl`, `xcomp` |
| **`senter`** | `I`, `S` |
| **`ner`** | `CARDINAL`, `DATE`, `EVENT`, `FAC`, `GPE`, `LANGUAGE`, `LAW`, `LOC`, `MONEY`, `NORP`, `ORDINAL`, `ORG`, `PERCENT`, `PERSON`, `PRODUCT`, `QUANTITY`, `TIME`, `WORK_OF_ART` |
| **`entity_ruler`** | `PASSIVE` |

</details>