---
tags:
- spacy
- token-classification

language:
- ca

license: gpl-3.0

model-index:
- name: ca_bsc_demo_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9245591117
    - name: NER Recall
      type: recall
      value: 0.9158848269
    - name: NER F Score
      type: f_score
      value: 0.9202015277
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9634938294
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.963614568
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9570511936
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9758267526
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9515815549
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.9353302085
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9929783499

widget:

- text: "El Futbol Club Barcelona, conegut popularment com a Barça, és una entitat poliesportiva amb seu a Barcelona. "

---


## Table of Contents
<details>
<summary>Click to expand</summary>

- [Model description](#model-description)
   - [Install the model](#install-model)
   - [Label scheme](#label-scheme)
   - [Evaluation results](#evaluation-results)
- [Additional information](#additional-information)
  - [Author](#author)
  - [Contact information](#contact-information)
  - [Copyright](#copyright)
  - [Licensing information](#licensing-information)
  - [Funding](#funding)
  - [Citing information](#citing-information)
  - [Disclaimer](#disclaimer)
  
</details>


## Model description

Catalan transformer (projecte-aina/roberta-large-ca-v2) pipeline by BSC. Components: transformer, morphologizer, parser, ner, attribute_ruler, lemmatizer, text classification.

| Feature | Description |
| --- | --- |
| **Name** | `ca_bsc_demo_trf` |
| **Version** | `3.4.2` |
| **spaCy** | `3.4.1` |
| **Default Pipeline** | `transformer`, `tagger`, `morphologizer`, `lemmatizer`, `parser`, `ner`, `textcat` |
| **Components** | `transformer`, `tagger`, `morphologizer`, `lemmatizer`, `parser`, `ner`, `textcat` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** |[roberta-large-ca-v2] (https://huggingface.co/projecte-aina/roberta-large-ca-v2) <br /> Ancora_UD_10 <br />[WikiCAT_ca] (https://huggingface.co/datasets/projecte-aina/WikiCAT_ca) |
| **License** | `GNU GPL 3.0` |
| **Author** | [AINA project](https://huggingface.co/projecte-aina) |


### Install the model

pip install https://huggingface.co/projecte-aina/ca_bsc_demo_trf/resolve/main/ca_bsc_demo_trf-any-py3-none-any.whl

More extensive demo at https://spacydemo.aina.bsc.es


### Label scheme

<details>

<summary>View label scheme (342 labels for 5 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `INTJ`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `PUNCT`, `SCONJ`, `SYM`, `VERB`, `X` |
| **`morphologizer`** | `Definite=Def\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `POS=PROPN`, `POS=PUNCT\|PunctSide=Ini\|PunctType=Brck`, `POS=PUNCT\|PunctSide=Fin\|PunctType=Brck`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=NOUN`, `POS=ADP`, `NumType=Card\|Number=Plur\|POS=NUM`, `Gender=Masc\|Number=Plur\|POS=NOUN`, `Number=Sing\|POS=ADJ`, `POS=CCONJ`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Ind`, `NumForm=Digit\|NumType=Card\|POS=NUM`, `NumForm=Digit\|POS=NOUN`, `Gender=Masc\|Number=Plur\|POS=ADJ`, `POS=PUNCT\|PunctType=Comm`, `POS=AUX\|VerbForm=Inf`, `Case=Acc,Dat\|POS=PRON\|Person=3\|PrepCase=Npr\|PronType=Prs\|Reflex=Yes`, `Definite=Def\|Gender=Masc\|Number=Plur\|POS=DET\|PronType=Art`, `POS=PRON\|PronType=Rel`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Plur\|POS=NOUN`, `Gender=Fem\|Number=Plur\|POS=ADJ`, `POS=VERB\|VerbForm=Inf`, `Case=Acc,Dat\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Plur\|POS=ADJ`, `POS=PUNCT\|PunctType=Peri`, `Number=Sing\|POS=PRON\|PronType=Rel`, `Gender=Masc\|Number=Sing\|POS=NOUN`, `Mood=Imp\|Number=Sing\|POS=VERB\|Person=2\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=ADJ\|VerbForm=Part`, `POS=SCONJ`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Ind`, `Gender=Fem\|Number=Plur\|POS=ADJ\|VerbForm=Part`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `POS=VERB\|VerbForm=Ger`, `POS=NOUN`, `Gender=Fem\|NumType=Card\|Number=Sing\|POS=NUM`, `Gender=Fem\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Gender=Fem\|NumType=Ord\|Number=Plur\|POS=ADJ`, `POS=SYM`, `Gender=Masc\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `POS=ADV\|Polarity=Neg`, `POS=ADV`, `Number=Sing\|POS=PRON\|PronType=Dem`, `Number=Sing\|POS=NOUN`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=NOUN`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=ADJ`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Tot`, `Case=Loc\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|NumType=Ord\|Number=Sing\|POS=ADJ`, `Degree=Cmp\|POS=ADV`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Plur\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Gender=Masc\|NumType=Ord\|Number=Sing\|POS=ADJ`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `NumType=Card\|POS=NUM`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Number=Sing\|POS=PRON\|PronType=Ind`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Number=Plur\|POS=DET\|PronType=Ind`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Dem`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Gender=Masc\|NumType=Card\|Number=Sing\|POS=NUM`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Case=Acc\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Sing\|POS=DET\|PronType=Ind`, `POS=PUNCT`, `Number=Sing\|POS=DET\|PronType=Rel`, `Case=Gen\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|NumType=Card\|Number=Plur\|POS=NUM`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `POS=DET\|PronType=Ind`, `Case=Acc\|Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Acc,Dat\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Degree=Cmp\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Ind`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Plur\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Case=Acc\|Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Ind`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Ind`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|PronType=Rel`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Int`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `AdvType=Tim\|POS=NOUN`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Ind`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Ind`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Int`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=3\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Case=Acc\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Int`, `POS=PUNCT\|PunctType=Semi`, `Mood=Cnd\|Number=Plur\|POS=AUX\|Person=3\|VerbForm=Fin`, `Case=Dat\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|NumType=Card\|Number=Plur\|POS=NUM`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Ind`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `NumForm=Digit\|POS=SYM`, `Gender=Masc\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Int`, `POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Int`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=3\|VerbForm=Fin`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=3\|VerbForm=Fin`, `POS=PART`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Tot`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Dem`, `POS=ADJ`, `Gender=Masc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Degree=Cmp\|Number=Plur\|POS=ADJ`, `POS=PUNCT\|PunctType=Dash`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Case=Acc\|Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|POS=NOUN`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Int`, `Gender=Masc\|NumType=Ord\|Number=Plur\|POS=ADJ`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Fut\|VerbForm=Fin`, `POS=PUNCT\|PunctType=Colo`, `Gender=Masc\|NumType=Card\|POS=NUM`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Sing\|POS=PRON\|PronType=Int`, `POS=PUNCT\|PunctType=Quot`, `Mood=Imp\|Number=Sing\|POS=VERB\|Person=3\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `POS=AUX\|VerbForm=Ger`, `Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Imp\|Number=Sing\|POS=AUX\|Person=3\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|PronType=Ind`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Dem`, `Case=Acc,Dat\|Number=Sing\|POS=PRON\|Person=2\|Polite=Infm\|PrepCase=Npr\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Int`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `NumForm=Digit\|NumType=Frac\|POS=NUM`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Dem`, `Gender=Fem\|POS=NOUN`, `Case=Acc,Dat\|Number=Sing\|POS=PRON\|Person=1\|PrepCase=Npr\|PronType=Prs`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=2\|Tense=Fut\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Case=Nom\|Number=Sing\|POS=PRON\|Person=2\|Polite=Infm\|PronType=Prs`, `POS=X`, `Mood=Cnd\|Number=Plur\|POS=AUX\|Person=1\|VerbForm=Fin`, `Number=Sing\|POS=DET\|PronType=Dem`, `POS=DET`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `POS=DET\|PronType=Art`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `NumType=Ord\|Number=Sing\|POS=ADJ`, `Gender=Fem\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `Number=Plur\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Gender=Fem\|Number=Plur\|POS=AUX\|Tense=Past\|VerbForm=Part`, `Gender=Masc\|Number=Plur\|POS=AUX\|Tense=Past\|VerbForm=Part`, `Number=Plur\|POS=PRON\|PronType=Dem`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=1\|VerbForm=Fin`, `POS=PRON\|PronType=Ind`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=3\|VerbForm=Fin`, `Case=Nom\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Acc\|Number=Sing\|POS=PRON\|Person=1\|PrepCase=Pre\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `POS=PUNCT\|PunctSide=Fin\|PunctType=Qest`, `NumForm=Digit\|NumType=Ord\|POS=ADJ`, `Case=Acc\|POS=PRON\|Person=3\|PrepCase=Pre\|PronType=Prs\|Reflex=Yes`, `NumForm=Digit\|NumType=Frac\|POS=SYM`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `POS=PUNCT\|PunctSide=Ini\|PunctType=Qest`, `NumType=Card\|Number=Sing\|POS=NUM`, `Foreign=Yes\|POS=PRON\|PronType=Int`, `Foreign=Yes\|Mood=Ind\|POS=VERB\|VerbForm=Fin`, `Foreign=Yes\|POS=ADP`, `Gender=Masc\|Number=Sing\|POS=PROPN`, `POS=PUNCT\|PunctSide=Ini\|PunctType=Excl`, `POS=PUNCT\|PunctSide=Fin\|PunctType=Excl`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=1\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Mood=Sub\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `POS=PUNCT\|PunctSide=Ini\|PunctType=Comm`, `POS=PUNCT\|PunctSide=Fin\|PunctType=Comm`, `Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Case=Acc,Dat\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=1\|VerbForm=Fin`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=1\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Number=Sing\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Gender=Masc\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `POS=VERB\|Tense=Past\|VerbForm=Part`, `Mood=Imp\|Number=Plur\|POS=AUX\|Person=3\|VerbForm=Fin`, `Case=Nom\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Rel`, `Definite=Ind\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Sing\|Number[psor]=Plur\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `Number=Plur\|Number[psor]=Plur\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `POS=AUX\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|NumType=Card\|POS=NUM`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `AdvType=Tim\|Degree=Cmp\|POS=ADV`, `Case=Acc\|Number=Sing\|POS=PRON\|Person=2\|Polite=Infm\|PrepCase=Pre\|PronType=Prs`, `POS=DET\|PronType=Rel`, `Definite=Ind\|Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Fut\|VerbForm=Fin`, `POS=INTJ`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `POS=VERB\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Case=Acc\|POS=PRON\|Person=3\|PronType=Prs\|Reflex=Yes`, `Foreign=Yes\|POS=NOUN`, `Foreign=Yes\|Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Foreign=Yes\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Foreign=Yes\|POS=SCONJ`, `Foreign=Yes\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|POS=SYM`, `Gender=Fem\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Number=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=PROPN`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Definite=Def\|Foreign=Yes\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Foreign=Yes\|POS=VERB`, `Foreign=Yes\|POS=ADJ`, `Foreign=Yes\|POS=DET`, `Foreign=Yes\|POS=ADV`, `Degree=Cmp\|POS=ADJ`, `AdvType=Tim\|POS=SYM`, `Number=Plur\|POS=DET\|PronType=Dem`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=2\|Tense=Fut\|VerbForm=Fin` |
| **`parser`** | `ROOT`, `acl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `case`, `cc`, `ccomp`, `compound`, `conj`, `cop`, `csubj`, `dep`, `det`, `expl:pass`, `fixed`, `flat`, `iobj`, `mark`, `nmod`, `nsubj`, `nummod`, `obj`, `obl`, `parataxis`, `punct`, `xcomp` |
| **`ner`** | `LOC`, `MISC`, `ORG`, `PER` |
| **`textcat`** | `Economia`, `Enginyeria`, `Entreteniment`, `Història`, `Humanitats`, `Dret`, `Matemàtiques`, `Música`, `Filosofia`, `Política`, `Religió`, `Esport`, `Ciència_i_Tecnologia` |

</details>


### Evaluation results

| Type | Score |
| --- | --- |
| `TAG_ACC` | 96.35 |
| `POS_ACC` | 96.36 |
| `MORPH_ACC` | 95.71 |
| `LEMMA_ACC` | 97.58 |
| `DEP_UAS` | 95.16 |
| `DEP_LAS` | 93.53 |
| `SENTS_P` | 99.30 |
| `SENTS_R` | 99.30 |
| `SENTS_F` | 99.30 |
| `ENTS_F` | 92.02 |
| `ENTS_P` | 92.46 |
| `ENTS_R` | 91.59 |
| `TRANSFORMER_LOSS` | 2061930.61 |
| `TAGGER_LOSS` | 462421.82 |
| `MORPHOLOGIZER_LOSS` | 583505.58 |
| `PARSER_LOSS` | 628332.01 |
| `NER_LOSS` | 12427.23 |




## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information
For further information, send an email to aina@bsc.es

### Copyright
Copyright (c) 2022 Text Mining Unit at Barcelona Supercomputing Center 

### Licensing information

### Funding
This work was funded by the [Departament de la Vicepresidència i de Polítiques Digitals i Territori de la Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).

### Citing information

### Disclaimer

<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner and creator of the models (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.

