---
tags:
- spacy
- token-classification
language:
- nb
model-index:
- name: nb_nocy_trf
  results:
  - tasks:
      name: NER
      type: token-classification
      metrics:
      - name: Precision
        type: precision
        value: 0.9021803182
      - name: Recall
        type: recall
        value: 0.9069905213
      - name: F Score
        type: f_score
        value: 0.9045790251
  - tasks:
      name: POS
      type: token-classification
      metrics:
      - name: Accuracy
        type: accuracy
        value: 0.987973053
  - tasks:
      name: SENTER
      type: token-classification
      metrics:
      - name: Precision
        type: precision
        value: 0.9679276316
      - name: Recall
        type: recall
        value: 0.9767634855
      - name: F Score
        type: f_score
        value: 0.9723254853
  - tasks:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
      metrics:
      - name: Accuracy
        type: accuracy
        value: 0.9433838463
  - tasks:
      name: LABELED_DEPENDENCIES
      type: token-classification
      metrics:
      - name: Accuracy
        type: accuracy
        value: 0.9433838463
---


# NoCy transformer model

NoCy is a Norwegian transformer model for SpaCy, based on `ltgoslo/norbert` and trained on the NorNE named entity corpus (`NbAiLab/norne`).

The model is made by and for SpaCy, based on the DaCy blueprint (https://github.com/centre-for-humanities-computing/DaCy). Code for the project can be found on github: https://github.com/radbrt/noCy.

The model performance should be quite similar to `NbAiLab/nb-bert-base`.


| Feature | Description |
| --- | --- |
| **Name** | `nb_nocy_trf` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.1.1,<3.2.0` |
| **Default Pipeline** | `transformer`, `tagger`, `morphologizer`, `parser`, `ner` |
| **Components** | `transformer`, `tagger`, `morphologizer`, `parser`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | ltgoslo/norbert |
| **License** | cc-by 4.0 |
| **Author** | Henning Holgersen |

### Label Scheme

<details>

<summary>View label scheme (265 labels for 4 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `INTJ`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `PUNCT`, `SCONJ`, `SYM`, `VERB`, `X` |
| **`morphologizer`** | `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=CCONJ`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `POS=SCONJ`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `POS=PUNCT`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin`, `POS=ADP`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `POS=PROPN`, `POS=X`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PRON\|PronType=Rel`, `Mood=Ind\|POS=AUX\|Tense=Pres\|VerbForm=Fin`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Gender=Fem\|Number=Plur\|POS=NOUN`, `POS=ADV`, `Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Definite=Ind\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `POS=VERB\|VerbForm=Part`, `Definite=Ind\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Degree=Pos\|Number=Plur\|POS=ADJ`, `NumType=Card\|Number=Plur\|POS=NUM`, `Definite=Def\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Case=Acc\|POS=PRON\|PronType=Prs\|Reflex=Yes`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PART`, `POS=VERB\|VerbForm=Inf`, `Case=Nom\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Ind\|POS=AUX\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|POS=PROPN`, `POS=NOUN`, `Gender=Masc\|POS=PROPN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Gen\|Definite=Def\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Abbr=Yes\|POS=PROPN`, `POS=PART\|Polarity=Neg`, `Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Case=Gen\|POS=PROPN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Degree=Sup\|POS=ADJ`, `Case=Gen\|Gender=Fem\|POS=PROPN`, `Number=Plur\|POS=DET\|PronType=Dem`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Definite=Ind\|Degree=Sup\|POS=ADJ`, `Definite=Def\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Gender=Neut\|POS=PROPN`, `Number=Plur\|POS=DET\|PronType=Int`, `Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Definite=Def\|POS=DET\|PronType=Dem`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Art`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Pass`, `Abbr=Yes\|Case=Gen\|POS=PROPN`, `Animacy=Hum\|Case=Nom\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Degree=Cmp\|POS=ADJ`, `POS=ADJ\|VerbForm=Part`, `Gender=Neut\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Abbr=Yes\|POS=ADP`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `POS=AUX\|VerbForm=Part`, `POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `Number=Plur\|POS=DET\|PronType=Ind`, `Degree=Pos\|POS=ADJ`, `Animacy=Hum\|Case=Nom\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `POS=VERB\|VerbForm=Inf\|Voice=Pass`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Ind`, `Animacy=Hum\|Case=Acc\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Number=Plur\|POS=DET\|Polarity=Neg\|PronType=Neg`, `NumType=Card\|POS=NUM`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Ind`, `POS=DET\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Gen\|Gender=Neut\|POS=PROPN`, `Gender=Masc\|Number=Sing\|POS=DET\|Polarity=Neg\|PronType=Neg`, `Definite=Def\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `POS=AUX\|VerbForm=Inf`, `Case=Acc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Gen\|Degree=Pos\|Number=Plur\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Tot`, `Case=Gen\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=DET\|PronType=Prs`, `POS=SYM`, `Gender=Neut\|NumType=Card\|Number=Sing\|POS=NUM`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|PronType=Prs`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Abbr=Yes\|POS=ADV`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Tot`, `Definite=Def\|POS=DET\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Neut\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Int`, `Definite=Def\|NumType=Card\|POS=NUM`, `Mood=Imp\|POS=VERB\|VerbForm=Fin`, `Definite=Ind\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Tot`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Tot`, `Animacy=Hum\|Case=Acc\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|Polarity=Neg\|PronType=Neg,Prs`, `Number=Plur\|POS=PRON\|Person=3\|Polarity=Neg\|PronType=Neg,Prs`, `Definite=Def\|NumType=Card\|Number=Sing\|POS=NUM`, `Gender=Masc\|NumType=Card\|Number=Sing\|POS=NUM`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Case=Gen\|Definite=Def\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Case=Gen\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Animacy=Hum\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Mood=Imp\|POS=AUX\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs,Tot`, `Number=Plur\|POS=ADJ`, `Gender=Masc\|POS=NOUN`, `Abbr=Yes\|POS=NOUN`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `POS=INTJ`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Animacy=Hum\|Case=Acc\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Masc\|Number=Plur\|POS=NOUN`, `POS=ADJ`, `Animacy=Hum\|Case=Acc\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Animacy=Hum\|Case=Acc\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Sing\|POS=PRON\|Polarity=Neg\|PronType=Neg`, `Case=Gen\|POS=NOUN`, `Definite=Ind\|Number=Sing\|POS=ADJ`, `Case=Gen\|Gender=Masc\|POS=PROPN`, `Animacy=Hum\|Number=Plur\|POS=PRON\|PronType=Rcp`, `Case=Gen\|Definite=Ind\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Gen\|Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Int`, `NumType=Card\|Number=Sing\|POS=NUM`, `Animacy=Hum\|Case=Acc\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Degree=Sup\|POS=ADJ`, `Animacy=Hum\|POS=PRON\|PronType=Int`, `POS=DET\|PronType=Ind`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Fem\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Dem`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs,Tot`, `Case=Gen\|Definite=Ind\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|Polarity=Neg\|PronType=Neg`, `Number=Plur\|POS=NOUN`, `Case=Gen\|Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Definite=Ind\|Number=Sing\|POS=VERB\|VerbForm=Part`, `Case=Gen\|Definite=Def\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Pass`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem,Ind`, `Animacy=Hum\|POS=PRON\|Poss=Yes\|PronType=Int`, `Abbr=Yes\|POS=ADJ`, `Case=Gen\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `POS=PRON\|PronType=Prs`, `Case=Gen\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Rcp`, `Definite=Ind\|Degree=Pos\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Art`, `Case=Gen\|NumType=Card\|Number=Plur\|POS=NUM`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Neut\|Number=Plur,Sing\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Tot`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Masc\|Number=Plur,Sing\|POS=NOUN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Int`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Prs`, `Animacy=Hum\|Case=Gen,Nom\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Definite=Def\|Degree=Pos\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Animacy=Hum\|Case=Gen\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Gender=Fem\|NumType=Card\|Number=Sing\|POS=NUM`, `Definite=Ind\|Gender=Masc\|POS=NOUN`, `Definite=Def\|Number=Plur\|POS=NOUN`, `Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Abbr=Yes\|Gender=Masc\|POS=NOUN`, `Abbr=Yes\|Case=Gen\|POS=NOUN`, `Abbr=Yes\|Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Abbr=Yes\|Degree=Pos\|POS=ADJ`, `Case=Gen\|Gender=Fem\|POS=NOUN`, `Case=Gen\|Degree=Cmp\|POS=ADJ`, `Definite=Ind\|Degree=Pos\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=NOUN` |
| **`parser`** | `ROOT`, `acl`, `acl:cleft`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `ccomp`, `compound`, `compound:prt`, `conj`, `cop`, `csubj`, `dep`, `det`, `discourse`, `expl`, `flat:foreign`, `flat:name`, `iobj`, `mark`, `nmod`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `orphan`, `parataxis`, `punct`, `xcomp` |
| **`ner`** | `DRV`, `EVT`, `GPE_LOC`, `GPE_ORG`, `LOC`, `MISC`, `ORG`, `PER`, `PROD` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TAG_ACC` | 98.80 |
| `POS_ACC` | 98.77 |
| `MORPH_ACC` | 98.01 |
| `DEP_UAS` | 94.34 |
| `DEP_LAS` | 92.52 |
| `SENTS_P` | 96.79 |
| `SENTS_R` | 97.68 |
| `SENTS_F` | 97.23 |
| `ENTS_F` | 90.46 |
| `ENTS_P` | 90.22 |
| `ENTS_R` | 90.70 |
| `TRANSFORMER_LOSS` | 1432675.77 |
| `TAGGER_LOSS` | 87954.00 |
| `MORPHOLOGIZER_LOSS` | 105773.67 |
| `PARSER_LOSS` | 1828631.17 |
| `NER_LOSS` | 81943.89 |