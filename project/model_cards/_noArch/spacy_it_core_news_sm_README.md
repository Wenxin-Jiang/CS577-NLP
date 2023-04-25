---
tags:
- spacy
- token-classification
language:
- it
license: cc-by-nc-sa-3.0
model-index:
- name: it_core_news_sm
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8600824654
    - name: NER Recall
      type: recall
      value: 0.8579197692
    - name: NER F Score
      type: f_score
      value: 0.858999756
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9650368506
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9701163888
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9701573034
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.969356578
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.8969952665
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.8575397438
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9796640141
---
### Details: https://spacy.io/models/it#it_core_news_sm

Italian pipeline optimized for CPU. Components: tok2vec, morphologizer, tagger, parser, lemmatizer (trainable_lemmatizer), senter, ner.

| Feature | Description |
| --- | --- |
| **Name** | `it_core_news_sm` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `tok2vec`, `morphologizer`, `tagger`, `parser`, `lemmatizer`, `attribute_ruler`, `ner` |
| **Components** | `tok2vec`, `morphologizer`, `tagger`, `parser`, `lemmatizer`, `senter`, `attribute_ruler`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [UD Italian ISDT v2.8](https://github.com/UniversalDependencies/UD_Italian-ISDT) (Bosco, Cristina; Lenci, Alessandro; Montemagni, Simonetta; Simi, Maria)<br />[WikiNER](https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500) (Joel Nothman, Nicky Ringland, Will Radford, Tara Murphy, James R Curran) |
| **License** | `CC BY-NC-SA 3.0` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (443 labels for 4 components)</summary>

| Component | Labels |
| --- | --- |
| **`morphologizer`** | `POS=PROPN`, `POS=PUNCT`, `Gender=Masc\|POS=NOUN`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=ADP\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=NOUN`, `Gender=Masc\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=NOUN`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `POS=AUX\|VerbForm=Inf`, `Gender=Fem\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `POS=ADP`, `Gender=Fem\|Number=Sing\|POS=ADJ`, `POS=PRON\|PronType=Rel`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Definite=Def\|Gender=Masc\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Plur\|POS=NOUN`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Ind`, `Definite=Def\|Gender=Masc\|Number=Plur\|POS=ADP\|PronType=Art`, `Number=Plur\|POS=ADJ`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Art`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `POS=VERB\|VerbForm=Inf`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Number=Sing\|POS=ADJ`, `POS=CCONJ`, `NumType=Card\|POS=NUM`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=ADP\|PronType=Art`, `Definite=Def\|Gender=Fem\|Number=Plur\|POS=ADP\|PronType=Art`, `Gender=Fem\|Number=Plur\|POS=NOUN`, `Clitic=Yes\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|Number=Plur\|POS=ADJ`, `Gender=Fem\|Number=Plur\|POS=DET\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=ADJ`, `POS=SPACE`, `Definite=Def\|Number=Sing\|POS=ADP\|PronType=Art`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|NumType=Ord\|Number=Sing\|POS=ADJ`, `POS=ADV`, `POS=NOUN`, `Number=Sing\|POS=NOUN`, `POS=VERB\|VerbForm=Ger`, `Gender=Masc\|Number=Sing\|POS=DET\|Poss=Yes\|PronType=Prs`, `POS=INTJ`, `Clitic=Yes\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|POS=NOUN`, `Gender=Fem\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Tot`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Mood=Cnd\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Ind`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Plur\|POS=NOUN`, `POS=SCONJ`, `Number=Sing\|POS=DET\|PronType=Ind`, `POS=ADV\|PronType=Neg`, `Clitic=Yes\|POS=VERB\|PronType=Prs\|VerbForm=Inf`, `Gender=Fem\|Number=Plur\|POS=AUX\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Ind`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Ind`, `POS=ADJ`, `Number=Sing\|POS=PRON\|PronType=Rel`, `Gender=Fem\|NumType=Ord\|Number=Sing\|POS=ADJ`, `Number=Sing\|POS=PRON\|PronType=Ind`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=AUX\|Tense=Past\|VerbForm=Part`, `Clitic=Yes\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Ger`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `POS=DET\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=DET\|Poss=Yes\|PronType=Prs`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Ind`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Dem`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Clitic=Yes\|Gender=Masc\|Number=Plur\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Ger`, `Gender=Fem\|Number=Sing\|POS=DET\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Clitic=Yes\|Gender=Masc\|Number=Sing\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Clitic=Yes\|POS=PRON\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Tot`, `Clitic=Yes\|Gender=Masc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Clitic=Yes\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Degree=Cmp\|Number=Plur\|POS=ADJ`, `Clitic=Yes\|Gender=Masc\|Number=Plur\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Degree=Cmp\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Dem`, `Degree=Abs\|POS=ADV`, `Clitic=Yes\|Gender=Fem\|Number=Sing\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Gender=Masc\|Number=Sing\|POS=AUX\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `POS=DET\|PronType=Exc`, `Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Past\|VerbForm=Fin`, `Number=Sing\|POS=DET\|PronType=Dem`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Gender=Fem\|NumType=Ord\|Number=Plur\|POS=ADJ`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `Number=Sing\|POS=DET\|PronType=Int`, `POS=PRON\|PronType=Int`, `Clitic=Yes\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Past\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Ind`, `Number=Sing\|POS=ADP`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Foreign=Yes\|POS=X`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Clitic=Yes\|POS=AUX\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Clitic=Yes\|Gender=Masc\|Mood=Imp\|Number=Plur,Sing\|POS=VERB\|Person=1,3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Number=Plur\|POS=VERB\|Tense=Pres\|VerbForm=Part`, `POS=INTJ\|Polarity=Neg`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|PronType=Rel`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Ind`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Dem`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Rel`, `Clitic=Yes\|Number=Plur\|POS=VERB\|Person=1\|PronType=Prs\|VerbForm=Ger`, `POS=INTJ\|Polarity=Pos`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Int`, `POS=DET\|PronType=Int`, `Gender=Masc\|NumType=Ord\|Number=Plur\|POS=ADJ`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Int`, `Mood=Cnd\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `POS=PRON\|Person=3\|PronType=Prs`, `Degree=Abs\|Gender=Masc\|Number=Plur\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Ind`, `Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Dem`, `Clitic=Yes\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Clitic=Yes\|Gender=Fem\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Clitic=Yes\|Gender=Fem\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Degree=Abs\|Gender=Fem\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Tot`, `Clitic=Yes\|POS=AUX\|PronType=Prs\|VerbForm=Inf`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Tot`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Dem`, `Degree=Abs\|Gender=Masc\|Number=Sing\|POS=ADJ`, `NumType=Ord\|POS=ADJ`, `POS=DET\|PronType=Rel`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Rel`, `Gender=Masc\|Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Clitic=Yes\|Number=Sing\|POS=VERB\|Person=1\|PronType=Prs\|VerbForm=Inf`, `Mood=Imp\|Number=Sing\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|POS=VERB\|PronType=Prs\|VerbForm=Ger`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Gender=Masc\|Number=Plur\|POS=VERB\|Person=3\|PronType=Prs\|Tense=Past\|VerbForm=Part`, `Number=Sing\|POS=PRON\|PronType=Int`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=2\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Clitic=Yes\|Number=Plur\|POS=VERB\|Person=2\|PronType=Prs\|VerbForm=Inf`, `Clitic=Yes\|Number=Plur\|POS=VERB\|Person=1\|PronType=Prs\|VerbForm=Inf`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=2\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Definite=Def\|POS=DET\|PronType=Art`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `POS=SYM`, `Clitic=Yes\|Mood=Imp\|Number=Sing\|POS=VERB\|Person=2\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Gender=Masc\|Mood=Imp\|Number=Sing\|POS=VERB\|Person=2,3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=2\|Tense=Fut\|VerbForm=Fin`, `Clitic=Yes\|Gender=Fem\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Ger`, `Degree=Abs\|Gender=Fem\|Number=Plur\|POS=ADJ`, `Number=Sing\|POS=PRON\|PronType=Dem`, `POS=AUX\|VerbForm=Ger`, `Gender=Masc\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Clitic=Yes\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs\|VerbForm=Inf`, `POS=PRON\|PronType=Ind`, `Clitic=Yes\|Mood=Imp\|Number=Plur\|POS=VERB\|Person=1\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `POS=X`, `Gender=Masc\|POS=ADJ`, `Clitic=Yes\|Gender=Fem\|Number=Sing\|POS=AUX\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Number=Sing\|POS=VERB\|Person=2\|PronType=Prs\|VerbForm=Inf`, `Clitic=Yes\|Gender=Fem\|Number=Sing\|POS=VERB\|Person=3\|PronType=Prs\|Tense=Past\|VerbForm=Part`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=2\|Tense=Imp\|VerbForm=Fin`, `POS=PART`, `Number=Sing\|POS=VERB\|Tense=Pres\|VerbForm=Part`, `NumType=Ord\|Number=Sing\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Int`, `Clitic=Yes\|Mood=Sub\|Number=Plur\|POS=VERB\|Person=1\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=DET\|PronType=Rel`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Clitic=Yes\|Gender=Fem\|Number=Sing\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Ger`, `Clitic=Yes\|Gender=Masc\|Number=Sing\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Ger`, `Clitic=Yes\|Number=Sing\|POS=VERB\|Person=1\|PronType=Prs\|VerbForm=Ger`, `Clitic=Yes\|Number=Sing\|POS=AUX\|Person=1\|PronType=Prs\|VerbForm=Ger`, `Clitic=Yes\|Gender=Masc\|Number=Plur\|POS=AUX\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Clitic=Yes\|Mood=Imp\|Number=Plur,Sing\|POS=VERB\|Person=1,2\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Mood=Imp\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `NumType=Range\|POS=NUM`, `Number=Plur\|POS=PRON\|PronType=Dem`, `POS=VERB\|Tense=Past\|VerbForm=Part`, `Clitic=Yes\|POS=ADV\|PronType=Prs`, `Clitic=Yes\|Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|POS=PRON\|PronType=Rel`, `Clitic=Yes\|Gender=Masc\|Mood=Imp\|Number=Plur,Sing\|POS=VERB\|Person=2,3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Number=Sing\|POS=AUX\|Person=2\|PronType=Prs\|VerbForm=Inf`, `Clitic=Yes\|Number=Sing\|POS=VERB\|Person=2\|PronType=Prs\|VerbForm=Ger`, `Mood=Imp\|Number=Sing\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Gender=Fem\|Mood=Imp\|Number=Sing\|POS=VERB\|Person=2,3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Past\|VerbForm=Fin`, `Clitic=Yes\|Gender=Masc\|Number=Sing\|POS=VERB\|Person=3\|PronType=Prs\|Tense=Past\|VerbForm=Part`, `Clitic=Yes\|Gender=Masc\|Number=Plur,Sing\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Inf`, `Definite=Ind\|POS=DET\|PronType=Art`, `Clitic=Yes\|Gender=Fem,Masc\|Number=Sing\|POS=VERB\|Person=3\|PronType=Prs\|Tense=Past\|VerbForm=Part`, `Definite=Ind\|Gender=Masc\|Number=Plur\|POS=DET\|PronType=Art`, `Definite=Def\|Number=Plur\|POS=ADP\|PronType=Art`, `Clitic=Yes\|Gender=Fem\|Number=Plur\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Inf`, `POS=DET\|PronType=Ind`, `Number=Plur\|POS=DET\|PronType=Dem`, `Clitic=Yes\|Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Plur\|POS=DET\|PronType=Tot`, `Clitic=Yes\|POS=AUX\|Person=3\|PronType=Prs\|VerbForm=Ger`, `Number=Plur\|POS=PRON\|PronType=Ind`, `Clitic=Yes\|Gender=Fem,Masc\|Number=Plur,Sing\|POS=VERB\|Person=3\|PronType=Prs\|Tense=Past\|VerbForm=Part`, `Clitic=Yes\|Number=Plur\|POS=VERB\|PronType=Prs\|VerbForm=Inf`, `Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Number=Plur\|POS=ADP`, `Clitic=Yes\|Gender=Masc\|Number=Sing\|POS=ADV\|Person=3\|PronType=Prs`, `Clitic=Yes\|Mood=Imp\|Number=Plur\|POS=VERB\|Person=1,2\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Gender=Fem\|Number=Plur\|POS=VERB\|Person=3\|PronType=Prs\|Tense=Past\|VerbForm=Part`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Cnd\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Gender=Fem\|Number=Plur\|POS=ADV\|Person=3\|PronType=Prs`, `POS=DET\|PronType=Tot`, `POS=PRON\|PronType=Dem`, `Clitic=Yes\|Gender=Masc\|Mood=Imp\|Number=Plur\|POS=VERB\|Person=2,3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Definite=Ind\|Number=Sing\|POS=DET\|PronType=Art`, `NumType=Ord\|POS=NUM`, `Clitic=Yes\|Gender=Fem\|Number=Plur\|POS=VERB\|Person=3\|PronType=Prs\|VerbForm=Ger`, `Gender=Masc\|POS=DET\|PronType=Dem`, `Clitic=Yes\|Gender=Masc\|Number=Plur,Sing\|POS=VERB\|Person=3\|PronType=Prs\|Tense=Past\|VerbForm=Part`, `Gender=Masc\|Number=Sing\|POS=NOUN\|Tense=Past\|VerbForm=Part`, `Gender=Masc\|Number=Plur\|POS=DET\|PronType=Int`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Int`, `Mood=Imp\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Int`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Int`, `Number=Plur\|POS=PRON\|PronType=Int`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Int`, `Clitic=Yes\|Number=Plur\|POS=PRON\|PronType=Prs`, `Foreign=Yes\|Number=Sing\|POS=X`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Fut\|VerbForm=Fin`, `POS=PRON\|PronType=Prs`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=2\|Tense=Imp\|VerbForm=Fin`, `POS=SCONJ\|PronType=Rel`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `POS=PRON\|Person=3\|PronType=Rel`, `Clitic=Yes\|Number=Plur\|POS=VERB\|Person=2\|PronType=Prs\|VerbForm=Ger`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|VerbForm=Fin`, `Clitic=Yes\|Mood=Ind\|Number=Sing\|POS=VERB\|Person=1,3\|PronType=Prs\|Tense=Past\|VerbForm=Fin`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Degree=Cmp\|POS=ADJ`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=2\|Tense=Fut\|VerbForm=Fin`, `Definite=Def\|Number=Plur\|POS=DET\|PronType=Art`, `Number=Sing\|POS=DET\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=ADP`, `Gender=Fem\|POS=ADJ`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Gender=Fem\|Mood=Imp\|Number=Plur\|POS=VERB\|Person=2,3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|POS=DET\|Poss=Yes\|PronType=Prs`, `Gender=Fem\|Number=Plur\|POS=PROPN`, `Definite=Ind\|Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=ADJ\|Poss=Yes\|PronType=Prs`, `Foreign=Yes\|POS=NOUN`, `Clitic=Yes\|Gender=Fem\|Mood=Imp\|Number=Plur\|POS=VERB\|Person=1,3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Clitic=Yes\|Gender=Masc\|Mood=Imp\|Number=Plur\|POS=VERB\|Person=1,3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=DET`, `Clitic=Yes\|Gender=Fem\|Mood=Imp\|Number=Plur,Sing\|POS=VERB\|Person=1,3\|PronType=Prs\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=DET`, `Number=Sing\|POS=X`, `Foreign=Yes\|Gender=Masc\|POS=X`, `Clitic=Yes\|Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Prs`, `Clitic=Yes\|Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Prs`, `Clitic=Yes\|Definite=Def\|Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Art`, `Gender=Masc\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Fin`, `Definite=Def\|Gender=Fem\|POS=DET`, `Definite=Def\|POS=DET`, `Foreign=Yes\|POS=PROPN`, `NumType=Card\|POS=PROPN`, `Gender=Fem\|Number=Sing\|POS=DET`, `Degree=Abs\|Gender=Masc\|Number=Sing\|POS=ADV`, `Gender=Masc\|Number=Plur\|POS=NOUN\|Tense=Past\|VerbForm=Part`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=2`, `Clitic=Yes\|Number=Plur\|POS=AUX\|Person=1\|PronType=Prs\|VerbForm=Inf`, `Gender=Masc\|Number=Sing\|POS=DET`, `Number=Sing\|POS=DET`, `Gender=Masc\|Number=Sing\|POS=PRON`, `POS=DET` |
| **`tagger`** | `A`, `AP`, `B`, `BN`, `B_PC`, `CC`, `CS`, `DD`, `DE`, `DI`, `DQ`, `DR`, `E`, `E_RD`, `FB`, `FC`, `FF`, `FS`, `I`, `N`, `NO`, `PART`, `PC`, `PC_PC`, `PD`, `PE`, `PI`, `PP`, `PQ`, `PR`, `RD`, `RI`, `S`, `SP`, `SW`, `SYM`, `T`, `V`, `VA`, `VA_PC`, `VM`, `VM_PC`, `VM_PC_PC`, `V_B`, `V_PC`, `V_PC_PC`, `X`, `_SP` |
| **`parser`** | `ROOT`, `acl`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `ccomp`, `compound`, `conj`, `cop`, `csubj`, `dep`, `det`, `det:poss`, `det:predet`, `discourse`, `expl`, `expl:impers`, `expl:pass`, `fixed`, `flat`, `flat:foreign`, `flat:name`, `iobj`, `mark`, `nmod`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `obl:agent`, `parataxis`, `punct`, `vocative`, `xcomp` |
| **`ner`** | `LOC`, `MISC`, `ORG`, `PER` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_ACC` | 99.93 |
| `TOKEN_P` | 99.80 |
| `TOKEN_R` | 99.78 |
| `TOKEN_F` | 99.79 |
| `POS_ACC` | 97.01 |
| `MORPH_ACC` | 97.02 |
| `MORPH_MICRO_P` | 98.53 |
| `MORPH_MICRO_R` | 97.73 |
| `MORPH_MICRO_F` | 98.12 |
| `TAG_ACC` | 96.50 |
| `SENTS_P` | 97.71 |
| `SENTS_R` | 98.23 |
| `SENTS_F` | 97.97 |
| `DEP_UAS` | 89.70 |
| `DEP_LAS` | 85.75 |
| `LEMMA_ACC` | 96.94 |
| `ENTS_P` | 86.01 |
| `ENTS_R` | 85.79 |
| `ENTS_F` | 85.90 |