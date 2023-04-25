---
tags:
- spacy
- token-classification
language:
- fr
license: lgpl-lr
model-index:
- name: fr_dep_news_trf
  results:
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9579788605
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9870585202
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9784491648
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9167694205
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9441518606
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.9235307728
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9410348977
---
### Details: https://spacy.io/models/fr#fr_dep_news_trf

French transformer pipeline (camembert-base). Components: transformer, morphologizer, parser, attribute_ruler, lemmatizer.

| Feature | Description |
| --- | --- |
| **Name** | `fr_dep_news_trf` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `transformer`, `morphologizer`, `parser`, `attribute_ruler`, `lemmatizer` |
| **Components** | `transformer`, `morphologizer`, `parser`, `attribute_ruler`, `lemmatizer` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [UD French Sequoia v2.8](https://github.com/UniversalDependencies/UD_French-Sequoia) (Candito, Marie; Seddah, Djamé; Perrier, Guy; Guillaume, Bruno)<br />[spaCy lookups data](https://github.com/explosion/spacy-lookups-data) (Explosion)<br />[camembert-base](https://huggingface.co/camembert-base) (Martin, Louis and Muller, Benjamin and Suarez, Pedro Javier Ortiz and Dupont, Yoann and Romary, Laurent and de la Clergerie, Eric Villemonte and Seddah, Djame and Sagot, Benoit}) |
| **License** | `LGPL-LR` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (232 labels for 2 components)</summary>

| Component | Labels |
| --- | --- |
| **`morphologizer`** | `POS=PROPN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=PRON\|Person=1`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `POS=SCONJ`, `POS=ADP`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `NumType=Ord\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=NOUN`, `POS=PUNCT`, `Gender=Masc\|Number=Sing\|POS=PROPN`, `Number=Plur\|POS=ADJ`, `Gender=Masc\|Number=Plur\|POS=NOUN`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Number=Sing\|POS=ADJ`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `POS=ADV`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=PROPN`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Art`, `NumType=Card\|POS=NUM`, `Definite=Def\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Plur\|POS=ADJ`, `POS=CCONJ`, `Gender=Fem\|Number=Plur\|POS=NOUN`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Plur\|POS=ADJ`, `POS=ADJ`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `POS=PRON\|PronType=Rel`, `Number=Sing\|POS=DET\|Poss=Yes`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=ADP\|PronType=Art`, `Definite=Def\|Number=Plur\|POS=ADP\|PronType=Art`, `Definite=Ind\|Number=Plur\|POS=DET\|PronType=Art`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `POS=VERB\|VerbForm=Inf`, `Gender=Fem\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3`, `Number=Plur\|POS=DET`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `POS=ADV\|PronType=Int`, `POS=VERB\|Tense=Pres\|VerbForm=Part`, `Gender=Fem\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|POS=ADJ`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Number=Plur\|POS=DET\|Poss=Yes`, `POS=AUX\|VerbForm=Inf`, `Gender=Masc\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Gender=Masc\|POS=VERB\|Tense=Past\|VerbForm=Part`, `POS=ADV\|Polarity=Neg`, `Definite=Ind\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3`, `POS=PRON\|Person=3\|Reflex=Yes`, `Gender=Masc\|POS=NOUN`, `POS=AUX\|Tense=Past\|VerbForm=Part`, `POS=PRON\|Person=3`, `Number=Plur\|POS=NOUN`, `NumType=Ord\|Number=Sing\|POS=ADJ`, `POS=VERB\|Tense=Past\|VerbForm=Part`, `POS=AUX\|Tense=Pres\|VerbForm=Part`, `Gender=Masc\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Sing\|POS=PRON\|Person=3`, `Number=Sing\|POS=NOUN`, `Gender=Masc\|Number=Plur\|POS=PRON\|Person=3`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|NumType=Ord\|Number=Sing\|POS=ADJ`, `Number=Plur\|POS=PROPN`, `Number=Sing\|POS=PROPN`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET`, `Gender=Fem\|Number=Sing\|POS=DET\|Poss=Yes`, `Gender=Masc\|POS=PRON`, `POS=NOUN`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON`, `Gender=Masc\|NumType=Ord\|Number=Plur\|POS=ADJ`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Number=Sing\|POS=PRON`, `Number=Sing\|POS=PRON\|PronType=Dem`, `Mood=Ind\|POS=VERB\|VerbForm=Fin`, `Number=Plur\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=PRON`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Dem`, `Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Rel`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|NumType=Ord\|Number=Sing\|POS=ADJ`, `POS=PRON`, `POS=NUM`, `Gender=Fem\|POS=NOUN`, `Gender=Fem\|Number=Plur\|POS=PRON`, `Number=Plur\|POS=PRON\|Person=3`, `Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Sing\|POS=PRON\|Person=1`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=PRON`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `POS=INTJ`, `Number=Plur\|POS=PRON\|Person=2`, `NumType=Card\|POS=PRON`, `Definite=Ind\|Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `NumType=Card\|POS=NOUN`, `POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Plur\|POS=PRON\|Person=3`, `Gender=Fem\|Number=Sing\|POS=DET`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=DET`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Definite=Ind\|Gender=Masc\|Number=Plur\|POS=DET\|PronType=Art`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Dem`, `Gender=Masc\|Number=Plur\|POS=PROPN`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Dem`, `Number=Sing\|POS=DET`, `Gender=Masc\|NumType=Card\|Number=Plur\|POS=NOUN`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Dem`, `Mood=Ind\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|POS=PRON`, `Gender=Masc\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Rel`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `POS=X`, `POS=SYM`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Int`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Int`, `POS=DET`, `Gender=Masc\|Number=Plur\|POS=PRON`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|POS=VERB\|Person=3\|VerbForm=Fin`, `Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Int`, `Gender=Masc\|Number=Plur\|POS=DET`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Rel`, `Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Rel`, `POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Gender=Fem\|NumType=Ord\|Number=Plur\|POS=ADJ`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Fut\|VerbForm=Fin`, `Mood=Imp\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=2\|Reflex=Yes`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=1\|Reflex=Yes`, `Gender=Masc\|NumType=Card\|Number=Sing\|POS=NOUN`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Number=Sing\|POS=PRON\|Person=1\|Reflex=Yes`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|POS=PROPN`, `Mood=Cnd\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=2\|Tense=Imp\|VerbForm=Fin`, `Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Plur\|POS=PROPN`, `Gender=Masc\|NumType=Card\|POS=NUM` |
| **`parser`** | `ROOT`, `acl`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux:pass`, `aux:tense`, `case`, `cc`, `ccomp`, `conj`, `cop`, `dep`, `det`, `expl:comp`, `expl:pass`, `expl:subj`, `fixed`, `flat:foreign`, `flat:name`, `iobj`, `mark`, `nmod`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl:agent`, `obl:arg`, `obl:mod`, `parataxis`, `punct`, `vocative`, `xcomp` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_ACC` | 99.80 |
| `TOKEN_P` | 98.44 |
| `TOKEN_R` | 98.96 |
| `TOKEN_F` | 98.70 |
| `POS_ACC` | 98.71 |
| `MORPH_ACC` | 97.84 |
| `MORPH_MICRO_P` | 99.36 |
| `MORPH_MICRO_R` | 99.01 |
| `MORPH_MICRO_F` | 99.19 |
| `SENTS_P` | 93.32 |
| `SENTS_R` | 94.90 |
| `SENTS_F` | 94.10 |
| `DEP_UAS` | 94.42 |
| `DEP_LAS` | 92.35 |
| `TAG_ACC` | 95.80 |
| `LEMMA_ACC` | 91.68 |