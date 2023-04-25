---
tags:
- spacy
- token-classification
language:
- en
license: mit
model-index:
- name: en_docusco_spacy_fc_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.889028963
    - name: NER Recall
      type: recall
      value: 0.8833963688
    - name: NER F Score
      type: f_score
      value: 0.886203716
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9838746739
---
English pipeline for part-of-speech and rhetorical tagging.

| Feature | Description |
| --- | --- |
| **Name** | `en_docusco_spacy_fc_trf` |
| **Version** | `1.1` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `transformer`, `tagger`, `ner` |
| **Components** | `transformer`, `tagger`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | `MIT` |
| **Author** | [David Brown](https://browndw.github.io/docuscope-docs/) |

### Label Scheme

<details>

<summary>View label scheme (269 labels for 2 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `APPGE`, `AT`, `AT1`, `BCL21`, `BCL22`, `CC`, `CCB`, `CS`, `CS21`, `CS22`, `CS31`, `CS32`, `CS33`, `CS41`, `CS42`, `CS43`, `CS44`, `CSA`, `CSN`, `CST`, `CSW`, `CSW31`, `CSW32`, `CSW33`, `DA`, `DA1`, `DA2`, `DAR`, `DAT`, `DB`, `DB2`, `DD`, `DD1`, `DD2`, `DDQ`, `DDQGE`, `DDQV`, `DDQV31`, `DDQV32`, `DDQV33`, `EX`, `FO`, `FU`, `FW`, `GE`, `IF`, `II`, `II21`, `II22`, `II31`, `II32`, `II33`, `II41`, `II42`, `II43`, `II44`, `IO`, `IW`, `JJ`, `JJ21`, `JJ22`, `JJ31`, `JJ32`, `JJ33`, `JJR`, `JJT`, `JK`, `MC`, `MC1`, `MC2`, `MC221`, `MC222`, `MCMC`, `MD`, `MF`, `ND1`, `NN`, `NN1`, `NN121`, `NN122`, `NN131`, `NN132`, `NN133`, `NN141`, `NN142`, `NN143`, `NN144`, `NN2`, `NN21`, `NN22`, `NN221`, `NN222`, `NN231`, `NN232`, `NN233`, `NN31`, `NN33`, `NNA`, `NNB`, `NNL1`, `NNL2`, `NNO`, `NNO2`, `NNT1`, `NNT2`, `NNU`, `NNU1`, `NNU2`, `NNU21`, `NNU22`, `NP`, `NP1`, `NP2`, `NPD1`, `NPD2`, `NPM1`, `NPM2`, `PN`, `PN1`, `PN121`, `PN122`, `PN21`, `PN22`, `PNQO`, `PNQS`, `PNQS31`, `PNQS32`, `PNQS33`, `PNQV`, `PNX1`, `PPGE`, `PPH1`, `PPHO1`, `PPHO2`, `PPHS1`, `PPHS2`, `PPIO1`, `PPIO2`, `PPIS1`, `PPIS2`, `PPX1`, `PPX121`, `PPX122`, `PPX2`, `PPX221`, `PPX222`, `PPY`, `RA`, `RA21`, `RA22`, `REX`, `REX21`, `REX22`, `REX41`, `REX42`, `REX43`, `REX44`, `RG`, `RG21`, `RG22`, `RGQ`, `RGQV`, `RGQV31`, `RGQV32`, `RGQV33`, `RGR`, `RGT`, `RL`, `RL21`, `RL22`, `RP`, `RPK`, `RR`, `RR21`, `RR22`, `RR31`, `RR32`, `RR33`, `RR41`, `RR42`, `RR43`, `RR44`, `RR51`, `RR52`, `RR53`, `RR54`, `RR55`, `RRQ`, `RRQV`, `RRQV31`, `RRQV32`, `RRQV33`, `RRR`, `RRT`, `RT`, `RT21`, `RT22`, `RT31`, `RT32`, `RT33`, `RT41`, `RT42`, `RT43`, `RT44`, `TO`, `UH`, `UH21`, `UH22`, `UH31`, `UH32`, `UH33`, `VB0`, `VBDR`, `VBDZ`, `VBG`, `VBI`, `VBM`, `VBN`, `VBR`, `VBZ`, `VD0`, `VDD`, `VDG`, `VDI`, `VDN`, `VDZ`, `VH0`, `VHD`, `VHG`, `VHI`, `VHN`, `VHZ`, `VM`, `VM21`, `VM22`, `VMK`, `VV0`, `VVD`, `VVG`, `VVGK`, `VVI`, `VVN`, `VVNK`, `VVZ`, `XX`, `Y`, `ZZ1`, `ZZ2`, `ZZ221`, `ZZ222` |
| **`ner`** | `ActorsAbstractions`, `ActorsFirstPerson`, `ActorsPeople`, `ActorsPublicEntities`, `CitationAuthority`, `CitationControversy`, `CitationNeutral`, `ConfidenceHedged`, `ConfidenceHigh`, `OrganizationNarrative`, `OrganizationReasoning`, `PlanningFuture`, `PlanningStrategy`, `SentimentNegative`, `SentimentPositive`, `SignpostingAcademicWritingMoves`, `SignpostingMetadiscourse`, `StanceEmphatic`, `StanceModerated` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TAG_ACC` | 98.39 |
| `ENTS_F` | 88.62 |
| `ENTS_P` | 88.90 |
| `ENTS_R` | 88.34 |
| `TRANSFORMER_LOSS` | 2319800.36 |
| `TAGGER_LOSS` | 669777.78 |
| `NER_LOSS` | 2048423.35 |