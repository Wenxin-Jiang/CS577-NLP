---
tags:
- spacy
- token-classification
language:
- ca
model-index:
- name: ca_bsc_ud11_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9021669853
    - name: NER Recall
      type: recall
      value: 0.8953194181
    - name: NER F Score
      type: f_score
      value: 0.8987301587
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9759922789
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9920799759
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9892617681
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9632267319
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9524239398
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.9346149783
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9947337624
---
| Feature | Description |
| --- | --- |
| **Name** | `ca_bsc_ud11_trf` |
| **Version** | `3.4.4` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `transformer`, `tagger`, `morphologizer`, `lemmatizer`, `parser`, `ner` |
| **Components** | `transformer`, `tagger`, `morphologizer`, `lemmatizer`, `parser`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (600 labels for 4 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `INTJ`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `PUNCT`, `SCONJ`, `SYM`, `VERB`, `ao0cs0`, `ao0fp0`, `ao0fs0`, `ao0mp0`, `ao0ms0`, `aq0cn0`, `aq0cp0`, `aq0cp00`, `aq0cs0`, `aq0fp0`, `aq0fpp`, `aq0fs0`, `aq0fsp`, `aq0mp0`, `aq0mpp`, `aq0ms0`, `aq0msp`, `cc`, `cs`, `da0cs0`, `da0fp0`, `da0fs0`, `da0mp0`, `da0ms0`, `dd0cp0`, `dd0cs0`, `dd0fp0`, `dd0fs0`, `dd0mp0`, `dd0ms0`, `de0cn0`, `di0cn0`, `di0cp0`, `di0cs0`, `di0fp0`, `di0fs0`, `di0mp0`, `di0ms0`, `dn0cp0`, `dn0cs0`, `dn0fp0`, `dn0fs0`, `dn0mp0`, `dn0ms0`, `dp1cpp`, `dp1fpp`, `dp1fps`, `dp1fsp`, `dp1fss`, `dp1mpp`, `dp1mps`, `dp1msp`, `dp1mss`, `dp2fss`, `dp2mps`, `dp2mss`, `dp3fp0`, `dp3fs0`, `dp3mp0`, `dp3ms0`, `dr0cs0`, `dt0fp0`, `dt0fs0`, `dt0mp0`, `dt0ms0`, `faa`, `fat`, `fc`, `fca`, `fct`, `fd`, `fe`, `fg`, `fh`, `fia`, `fit`, `fp`, `fpa`, `fpt`, `fs`, `fx`, `fz`, `nc00000`, `nccn000`, `nccp000`, `nccs000`, `ncfn000`, `ncfp000`, `ncfs000`, `ncmn000`, `ncmp000`, `ncms000`, `np00000`, `np0000a`, `np0000d`, `np0000l`, `np0000o`, `np0000p`, `p0000000`, `p010p000`, `p010s000`, `p020p000`, `p020s000`, `p0300000`, `pd0cp000`, `pd0cs000`, `pd0fp000`, `pd0fs000`, `pd0mp000`, `pd0ms000`, `pd0ns000`, `pi0cn000`, `pi0cp000`, `pi0cs000`, `pi0fp000`, `pi0fs000`, `pi0mp0`, `pi0mp000`, `pi0ms000`, `pn0cp000`, `pn0cs000`, `pn0fp000`, `pn0fs000`, `pn0mp000`, `pn0ms000`, `pp1cp000`, `pp1cs000`, `pp1csn00`, `pp1cso00`, `pp2cp000`, `pp2cp00p`, `pp2cs000`, `pp2cs00p`, `pp3cn000`, `pp3cno00`, `pp3cp000`, `pp3csa00`, `pp3csd00`, `pp3fp000`, `pp3fpa00`, `pp3fs000`, `pp3fsa00`, `pp3mp000`, `pp3mpa00`, `pp3ms000`, `pp3msa00`, `pp3nn000`, `pr000000`, `pr0cn000`, `pr0cp000`, `pr0cs0`, `pr0cs000`, `pr0ms000`, `pt000000`, `pt0cs000`, `pt0fp000`, `pt0fs000`, `pt0mp000`, `pt0ms000`, `px1fp0p0`, `px1fs0p0`, `px1ms0p0`, `px3cp0p0`, `px3cs0p0`, `px3fp0s0`, `px3fs000`, `px3fs0s0`, `px3mp000`, `px3ms000`, `rg`, `rn`, `spcmp`, `spcms`, `sps00`, `vag0000`, `vaic1p0`, `vaic3p0`, `vaic3s0`, `vaif1p0`, `vaif1s0`, `vaif2p0`, `vaif3p0`, `vaif3s0`, `vaii1p0`, `vaii1s0`, `vaii3p0`, `vaii3s0`, `vaip1p0`, `vaip1s0`, `vaip2p0`, `vaip2s0`, `vaip3p0`, `vaip3s0`, `van0000`, `vap00sm`, `vasi100`, `vasi1p0`, `vasi3p0`, `vasi3s0`, `vasp1p0`, `vasp3p0`, `vasp3s0`, `vm00000`, `vmg0000`, `vmic1p0`, `vmic1s0`, `vmic3p0`, `vmic3s0`, `vmif1p0`, `vmif1s0`, `vmif2p0`, `vmif3p0`, `vmif3s0`, `vmii1p0`, `vmii1s0`, `vmii3p0`, `vmii3s0`, `vmip1p0`, `vmip1s0`, `vmip2p0`, `vmip2s0`, `vmip3p0`, `vmip3s0`, `vmis3p0`, `vmis3s0`, `vmm01p0`, `vmm02s0`, `vmm03p0`, `vmm03s0`, `vmn0000`, `vmp0000`, `vmp00fs`, `vmp00mp`, `vmp00ms`, `vmp00pf`, `vmp00pm`, `vmp00sf`, `vmp00sm`, `vmsi1p0`, `vmsi1s0`, `vmsi3p0`, `vmsi3s0`, `vmsp1p0`, `vmsp1s0`, `vmsp2p0`, `vmsp2s0`, `vmsp3p0`, `vmsp3s0`, `vsg0000`, `vsic3p0`, `vsic3s0`, `vsif3p0`, `vsif3s0`, `vsii1p0`, `vsii1s0`, `vsii3p0`, `vsii3s0`, `vsip1p0`, `vsip1s0`, `vsip2s0`, `vsip3p0`, `vsip3s0`, `vsis3p0`, `vsis3s0`, `vsm03p0`, `vsm03s0`, `vsn0000`, `vsp00sm`, `vssi3p0`, `vssi3s0`, `vssp1p0`, `vssp3p0`, `vssp3s0`, `zm`, `zp` |
| **`morphologizer`** | `Definite=Def\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `POS=PROPN`, `POS=PUNCT\|PunctSide=Ini\|PunctType=Brck`, `POS=PUNCT\|PunctSide=Fin\|PunctType=Brck`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=NOUN`, `POS=ADP`, `NumType=Card\|Number=Plur\|POS=NUM`, `Gender=Masc\|Number=Plur\|POS=NOUN`, `Number=Sing\|POS=ADJ`, `POS=CCONJ`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Ind`, `NumForm=Digit\|NumType=Card\|POS=NUM`, `NumForm=Digit\|POS=NOUN`, `Gender=Masc\|Number=Plur\|POS=ADJ`, `POS=PUNCT\|PunctType=Comm`, `POS=AUX\|VerbForm=Inf`, `Case=Acc,Dat\|POS=PRON\|Person=3\|PrepCase=Npr\|PronType=Prs\|Reflex=Yes`, `Definite=Def\|Gender=Masc\|Number=Plur\|POS=DET\|PronType=Art`, `POS=PRON\|PronType=Rel`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Plur\|POS=NOUN`, `Gender=Fem\|Number=Plur\|POS=ADJ`, `POS=VERB\|VerbForm=Inf`, `Case=Acc,Dat\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Plur\|POS=ADJ`, `POS=PUNCT\|PunctType=Peri`, `Number=Sing\|POS=PRON\|PronType=Rel`, `Gender=Masc\|Number=Sing\|POS=NOUN`, `Mood=Imp\|Number=Sing\|POS=VERB\|Person=2\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=ADJ\|VerbForm=Part`, `POS=SCONJ`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Ind`, `Gender=Fem\|Number=Plur\|POS=ADJ\|VerbForm=Part`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `POS=VERB\|VerbForm=Ger`, `POS=NOUN`, `Gender=Fem\|NumType=Card\|Number=Sing\|POS=NUM`, `Gender=Fem\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Gender=Fem\|NumType=Ord\|Number=Plur\|POS=ADJ`, `POS=PUNCT\|PunctType=Quot`, `Gender=Masc\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `POS=ADV\|Polarity=Neg`, `POS=ADV`, `Number=Sing\|POS=PRON\|PronType=Dem`, `Number=Sing\|POS=NOUN`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=NOUN`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=ADJ`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Tot`, `Case=Loc\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|NumType=Ord\|Number=Sing\|POS=ADJ`, `Degree=Cmp\|POS=ADV`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Plur\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Gender=Masc\|NumType=Ord\|Number=Sing\|POS=ADJ`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `NumType=Card\|POS=NUM`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Number=Sing\|POS=PRON\|PronType=Ind`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Number=Plur\|POS=DET\|PronType=Ind`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Dem`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Gender=Masc\|NumType=Card\|Number=Sing\|POS=NUM`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Case=Acc\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Sing\|POS=DET\|PronType=Ind`, `POS=PUNCT`, `Number=Sing\|POS=DET\|PronType=Rel`, `Case=Gen\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|NumType=Card\|Number=Plur\|POS=NUM`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `POS=DET\|PronType=Ind`, `Case=Acc\|Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Acc,Dat\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Degree=Cmp\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Ind`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Plur\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Case=Acc\|Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Ind`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Ind`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|PronType=Rel`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Int`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `AdvType=Tim\|POS=NOUN`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Ind`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Ind`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Int`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=3\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Case=Acc\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Int`, `POS=PUNCT\|PunctType=Semi`, `Mood=Cnd\|Number=Plur\|POS=AUX\|Person=3\|VerbForm=Fin`, `Case=Dat\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|NumType=Card\|Number=Plur\|POS=NUM`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Ind`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `NumForm=Digit\|POS=SYM`, `Gender=Masc\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Int`, `POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Int`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=3\|VerbForm=Fin`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=3\|VerbForm=Fin`, `POS=PART`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Tot`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Dem`, `POS=ADJ`, `Gender=Masc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Degree=Cmp\|Number=Plur\|POS=ADJ`, `POS=PUNCT\|PunctType=Dash`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Case=Acc\|Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|POS=NOUN`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Int`, `Gender=Masc\|NumType=Ord\|Number=Plur\|POS=ADJ`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `POS=PUNCT\|PunctType=Colo`, `Gender=Masc\|NumType=Card\|POS=NUM`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Sing\|POS=PRON\|PronType=Int`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Mood=Imp\|Number=Sing\|POS=VERB\|Person=3\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `POS=AUX\|VerbForm=Ger`, `Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Imp\|Number=Sing\|POS=AUX\|Person=3\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|PronType=Ind`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Dem`, `Case=Acc,Dat\|Number=Sing\|POS=PRON\|Person=2\|Polite=Infm\|PrepCase=Npr\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Int`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `NumForm=Digit\|NumType=Frac\|POS=NUM`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Dem`, `Gender=Fem\|POS=NOUN`, `Case=Acc,Dat\|Number=Sing\|POS=PRON\|Person=1\|PrepCase=Npr\|PronType=Prs`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=2\|Tense=Fut\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Case=Nom\|Number=Sing\|POS=PRON\|Person=2\|Polite=Infm\|PronType=Prs`, `POS=X`, `Mood=Cnd\|Number=Plur\|POS=AUX\|Person=1\|VerbForm=Fin`, `Number=Sing\|POS=DET\|PronType=Dem`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `POS=DET\|PronType=Art`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `NumType=Ord\|Number=Sing\|POS=ADJ`, `Number=Plur\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Number=Plur\|POS=PRON\|PronType=Dem`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=1\|VerbForm=Fin`, `POS=PRON\|PronType=Ind`, `POS=SYM`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=3\|VerbForm=Fin`, `POS=VERB\|VerbForm=Fin`, `Case=Nom\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Acc\|Number=Sing\|POS=PRON\|Person=1\|PrepCase=Pre\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `NumForm=Digit\|NumType=Frac\|POS=SYM`, `NumType=Card\|Number=Sing\|POS=NUM`, `POS=PUNCT\|PunctSide=Ini\|PunctType=Qest`, `POS=PUNCT\|PunctSide=Fin\|PunctType=Qest`, `NumForm=Digit\|NumType=Ord\|POS=ADJ`, `Foreign=Yes\|POS=PRON\|PronType=Int`, `Foreign=Yes\|Mood=Ind\|POS=VERB\|VerbForm=Fin`, `Foreign=Yes\|POS=ADP`, `Gender=Masc\|Number=Sing\|POS=PROPN`, `Case=Acc\|POS=PRON\|Person=3\|PrepCase=Pre\|PronType=Prs\|Reflex=Yes`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `POS=PUNCT\|PunctSide=Ini\|PunctType=Excl`, `POS=PUNCT\|PunctSide=Fin\|PunctType=Excl`, `Gender=Masc\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=1\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `POS=NUM`, `Mood=Imp\|Number=Plur\|POS=AUX\|Person=3\|VerbForm=Fin`, `Case=Nom\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=1\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Mood=Sub\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `POS=PUNCT\|PunctSide=Ini\|PunctType=Comm`, `POS=PUNCT\|PunctSide=Fin\|PunctType=Comm`, `Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Case=Acc,Dat\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=1\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Number=Sing\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Gender=Masc\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `POS=VERB\|Tense=Past\|VerbForm=Part`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `Foreign=Yes\|POS=NOUN`, `Definite=Def\|Foreign=Yes\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Foreign=Yes\|POS=VERB`, `Foreign=Yes\|POS=ADJ`, `Foreign=Yes\|POS=DET`, `Foreign=Yes\|POS=ADV`, `Definite=Ind\|Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `POS=INTJ`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Case=Acc\|POS=PRON\|Person=3\|PronType=Prs\|Reflex=Yes`, `AdvType=Tim\|POS=SYM`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `AdvType=Tim\|Degree=Cmp\|POS=ADV`, `Case=Acc\|Number=Sing\|POS=PRON\|Person=2\|Polite=Infm\|PrepCase=Pre\|PronType=Prs`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Degree=Cmp\|POS=ADJ`, `POS=DET`, `Gender=Masc\|Number=Sing\|Number[psor]=Plur\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `Number=Plur\|Number[psor]=Plur\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Fut\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|POS=SYM`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `POS=DET\|PronType=Rel`, `Gender=Fem\|NumType=Card\|POS=NUM`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `POS=AUX\|Tense=Past\|VerbForm=Part`, `Foreign=Yes\|Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Foreign=Yes\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Foreign=Yes\|POS=SCONJ`, `Foreign=Yes\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Number=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Gender=Fem\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Gender=Fem\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Definite=Ind\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=PROPN`, `Number=Plur\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Rel` |
| **`parser`** | `ROOT`, `acl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `case`, `cc`, `ccomp`, `compound`, `conj`, `cop`, `csubj`, `dep`, `det`, `expl:pass`, `fixed`, `flat`, `iobj`, `mark`, `nmod`, `nsubj`, `nummod`, `obj`, `obl`, `parataxis`, `punct`, `xcomp` |
| **`ner`** | `LOC`, `MISC`, `ORG`, `PER` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TAG_ACC` | 97.60 |
| `POS_ACC` | 99.21 |
| `MORPH_ACC` | 98.93 |
| `LEMMA_ACC` | 96.32 |
| `DEP_UAS` | 95.24 |
| `DEP_LAS` | 93.46 |
| `SENTS_P` | 99.47 |
| `SENTS_R` | 99.47 |
| `SENTS_F` | 99.47 |
| `ENTS_F` | 89.87 |
| `ENTS_P` | 90.22 |
| `ENTS_R` | 89.53 |
| `TRANSFORMER_LOSS` | 9797954.44 |
| `TAGGER_LOSS` | 445221.52 |
| `MORPHOLOGIZER_LOSS` | 250027.62 |
| `PARSER_LOSS` | 2268999.48 |
| `NER_LOSS` | 65976.59 |