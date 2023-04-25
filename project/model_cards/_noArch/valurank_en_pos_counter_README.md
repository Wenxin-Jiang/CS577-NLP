---
tags:
- spacy
- text-classification
language:
- en
---
A Spacy pipeline for counting Part-of-speech articles

| Feature | Description |
| --- | --- |
| **Name** | `en_pos_counter` |
| **Version** | `0.1` |
| **spaCy** | `>=3.4.0,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `tagger`, `attribute_ruler`, `pos_counter` |
| **Components** | `tok2vec`, `tagger`, `attribute_ruler`, `pos_counter` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [Valurank](www.valurank.com) |

### Label Scheme

<details>

<summary>View label scheme (50 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `$`, `''`, `,`, `-LRB-`, `-RRB-`, `.`, `:`, `ADD`, `AFX`, `CC`, `CD`, `DT`, `EX`, `FW`, `HYPH`, `IN`, `JJ`, `JJR`, `JJS`, `LS`, `MD`, `NFP`, `NN`, `NNP`, `NNPS`, `NNS`, `PDT`, `POS`, `PRP`, `PRP$`, `RB`, `RBR`, `RBS`, `RP`, `SYM`, `TO`, `UH`, `VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`, `WDT`, `WP`, `WP$`, `WRB`, `XX`, `_SP`, ```` |

</details>