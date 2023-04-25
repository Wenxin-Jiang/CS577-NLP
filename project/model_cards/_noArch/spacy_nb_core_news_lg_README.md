---
tags:
- spacy
- token-classification
language:
- nb
license: mit
model-index:
- name: nb_core_news_lg
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.848358209
    - name: NER Recall
      type: recall
      value: 0.8418246445
    - name: NER F Score
      type: f_score
      value: 0.8450787987
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9738284801
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9738284801
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9628456102
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9728940554
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.894563298
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.8641570172
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9414451827
---
### Details: https://spacy.io/models/nb#nb_core_news_lg

Norwegian (Bokmål) pipeline optimized for CPU. Components: tok2vec, morphologizer, parser, lemmatizer (trainable_lemmatizer), senter, ner, attribute_ruler.

| Feature | Description |
| --- | --- |
| **Name** | `nb_core_news_lg` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `tok2vec`, `morphologizer`, `parser`, `lemmatizer`, `attribute_ruler`, `ner` |
| **Components** | `tok2vec`, `morphologizer`, `parser`, `lemmatizer`, `senter`, `attribute_ruler`, `ner` |
| **Vectors** | 500000 keys, 500000 unique vectors (300 dimensions) |
| **Sources** | [UD Norwegian Bokmaal v2.8](https://github.com/UniversalDependencies/UD_Norwegian-Bokmaal) (Øvrelid, Lilja; Jørgensen, Fredrik; Hohle, Petter)<br />[NorNE: Norwegian Named Entities (commit: bd311de5)](https://github.com/ltgoslo/norne) (Language Technology Group (University of Oslo))<br />[Explosion fastText Vectors (cbow, OSCAR Common Crawl + Wikipedia)](https://spacy.io) (Explosion) |
| **License** | `MIT` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (249 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`morphologizer`** | `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=CCONJ`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `POS=SCONJ`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `POS=PUNCT`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin`, `POS=ADP`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `POS=PROPN`, `POS=X`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PRON\|PronType=Rel`, `Mood=Ind\|POS=AUX\|Tense=Pres\|VerbForm=Fin`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Gender=Fem\|Number=Plur\|POS=NOUN`, `POS=ADV`, `Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Definite=Ind\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `POS=VERB\|VerbForm=Part`, `Definite=Ind\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Degree=Pos\|Number=Plur\|POS=ADJ`, `NumType=Card\|Number=Plur\|POS=NUM`, `Definite=Def\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Case=Acc\|POS=PRON\|PronType=Prs\|Reflex=Yes`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PART`, `POS=VERB\|VerbForm=Inf`, `Case=Nom\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Ind\|POS=AUX\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|POS=PROPN`, `POS=NOUN`, `Gender=Masc\|POS=PROPN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Gen\|Definite=Def\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Abbr=Yes\|POS=PROPN`, `POS=PART\|Polarity=Neg`, `Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Case=Gen\|POS=PROPN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Degree=Sup\|POS=ADJ`, `Case=Gen\|Gender=Fem\|POS=PROPN`, `Number=Plur\|POS=DET\|PronType=Dem`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Definite=Ind\|Degree=Sup\|POS=ADJ`, `Definite=Def\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Gender=Neut\|POS=PROPN`, `Number=Plur\|POS=DET\|PronType=Int`, `Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Definite=Def\|POS=DET\|PronType=Dem`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Art`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Pass`, `Abbr=Yes\|Case=Gen\|POS=PROPN`, `Animacy=Hum\|Case=Nom\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Degree=Cmp\|POS=ADJ`, `POS=ADJ\|VerbForm=Part`, `Gender=Neut\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Abbr=Yes\|POS=ADP`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `POS=AUX\|VerbForm=Part`, `POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `Number=Plur\|POS=DET\|PronType=Ind`, `Degree=Pos\|POS=ADJ`, `Animacy=Hum\|Case=Nom\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `POS=VERB\|VerbForm=Inf\|Voice=Pass`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Ind`, `Animacy=Hum\|Case=Acc\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Number=Plur\|POS=DET\|Polarity=Neg\|PronType=Neg`, `NumType=Card\|POS=NUM`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Ind`, `POS=DET\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Gen\|Gender=Neut\|POS=PROPN`, `Gender=Masc\|Number=Sing\|POS=DET\|Polarity=Neg\|PronType=Neg`, `Definite=Def\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `POS=AUX\|VerbForm=Inf`, `Case=Acc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Gen\|Degree=Pos\|Number=Plur\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Tot`, `Case=Gen\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=DET\|PronType=Prs`, `POS=SYM`, `Gender=Neut\|NumType=Card\|Number=Sing\|POS=NUM`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|PronType=Prs`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Abbr=Yes\|POS=ADV`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Tot`, `Definite=Def\|POS=DET\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Neut\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Int`, `Definite=Def\|NumType=Card\|POS=NUM`, `Mood=Imp\|POS=VERB\|VerbForm=Fin`, `Definite=Ind\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Tot`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Tot`, `Animacy=Hum\|Case=Acc\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|Polarity=Neg\|PronType=Neg,Prs`, `Number=Plur\|POS=PRON\|Person=3\|Polarity=Neg\|PronType=Neg,Prs`, `Definite=Def\|NumType=Card\|Number=Sing\|POS=NUM`, `Gender=Masc\|NumType=Card\|Number=Sing\|POS=NUM`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Case=Gen\|Definite=Def\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Case=Gen\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `POS=SPACE`, `Animacy=Hum\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Mood=Imp\|POS=AUX\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs,Tot`, `Number=Plur\|POS=ADJ`, `Gender=Masc\|POS=NOUN`, `Abbr=Yes\|POS=NOUN`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `POS=INTJ`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Animacy=Hum\|Case=Acc\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Masc\|Number=Plur\|POS=NOUN`, `POS=ADJ`, `Animacy=Hum\|Case=Acc\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Animacy=Hum\|Case=Acc\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Sing\|POS=PRON\|Polarity=Neg\|PronType=Neg`, `Case=Gen\|POS=NOUN`, `Definite=Ind\|Number=Sing\|POS=ADJ`, `Case=Gen\|Gender=Masc\|POS=PROPN`, `Animacy=Hum\|Number=Plur\|POS=PRON\|PronType=Rcp`, `Case=Gen\|Definite=Ind\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Gen\|Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Int`, `NumType=Card\|Number=Sing\|POS=NUM`, `Animacy=Hum\|Case=Acc\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Degree=Sup\|POS=ADJ`, `Animacy=Hum\|POS=PRON\|PronType=Int`, `POS=DET\|PronType=Ind`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Fem\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Dem`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs,Tot`, `Case=Gen\|Definite=Ind\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|Polarity=Neg\|PronType=Neg`, `Number=Plur\|POS=NOUN`, `POS=PRON\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Definite=Ind\|Number=Sing\|POS=VERB\|VerbForm=Part`, `Case=Gen\|Definite=Def\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Pass`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem,Ind`, `Animacy=Hum\|POS=PRON\|Poss=Yes\|PronType=Int`, `Abbr=Yes\|POS=ADJ`, `Case=Gen\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Case=Gen\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Rcp`, `Definite=Ind\|Degree=Pos\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Art`, `Case=Gen\|NumType=Card\|Number=Plur\|POS=NUM`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Neut\|Number=Plur,Sing\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Tot`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Masc\|Number=Plur,Sing\|POS=NOUN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Int`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Prs`, `Animacy=Hum\|Case=Gen,Nom\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Definite=Def\|Degree=Pos\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Animacy=Hum\|Case=Gen\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Gender=Fem\|NumType=Card\|Number=Sing\|POS=NUM`, `Definite=Ind\|Gender=Masc\|POS=NOUN`, `Definite=Def\|Number=Plur\|POS=NOUN`, `Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Abbr=Yes\|Gender=Masc\|POS=NOUN`, `Abbr=Yes\|Case=Gen\|POS=NOUN`, `Abbr=Yes\|Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Abbr=Yes\|Degree=Pos\|POS=ADJ`, `Case=Gen\|Gender=Fem\|POS=NOUN`, `Case=Gen\|Degree=Cmp\|POS=ADJ`, `Definite=Ind\|Degree=Pos\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=NOUN` |
| **`parser`** | `ROOT`, `acl`, `acl:cleft`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `ccomp`, `compound`, `compound:prt`, `conj`, `cop`, `csubj`, `dep`, `det`, `discourse`, `expl`, `flat:foreign`, `flat:name`, `iobj`, `mark`, `nmod`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `orphan`, `parataxis`, `punct`, `xcomp` |
| **`ner`** | `DRV`, `EVT`, `GPE_LOC`, `GPE_ORG`, `LOC`, `MISC`, `ORG`, `PER`, `PROD` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_ACC` | 99.81 |
| `TOKEN_P` | 99.71 |
| `TOKEN_R` | 99.53 |
| `TOKEN_F` | 99.62 |
| `POS_ACC` | 97.38 |
| `MORPH_ACC` | 96.28 |
| `MORPH_MICRO_P` | 97.90 |
| `MORPH_MICRO_R` | 97.07 |
| `MORPH_MICRO_F` | 97.48 |
| `SENTS_P` | 94.18 |
| `SENTS_R` | 94.11 |
| `SENTS_F` | 94.14 |
| `DEP_UAS` | 89.46 |
| `DEP_LAS` | 86.42 |
| `LEMMA_ACC` | 97.29 |
| `TAG_ACC` | 97.38 |
| `ENTS_P` | 84.84 |
| `ENTS_R` | 84.18 |
| `ENTS_F` | 84.51 |