---
tags:
- spacy
- token-classification
language:
- da
license: cc-by-sa-4.0
model-index:
- name: da_core_news_sm
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.7359307359
    - name: NER Recall
      type: recall
      value: 0.7083333333
    - name: NER F Score
      type: f_score
      value: 0.7218683652
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9510387912
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9510387912
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9373819555
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.945472155
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.8102850755
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.7631770164
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.8890860692
---
### Details: https://spacy.io/models/da#da_core_news_sm

Danish pipeline optimized for CPU. Components: tok2vec, morphologizer, parser, lemmatizer (trainable_lemmatizer), senter, ner, attribute_ruler.

| Feature | Description |
| --- | --- |
| **Name** | `da_core_news_sm` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `tok2vec`, `morphologizer`, `parser`, `lemmatizer`, `attribute_ruler`, `ner` |
| **Components** | `tok2vec`, `morphologizer`, `parser`, `lemmatizer`, `senter`, `attribute_ruler`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [UD Danish DDT v2.8](https://github.com/UniversalDependencies/UD_Danish-DDT) (Johannsen, Anders; Martínez Alonso, Héctor; Plank, Barbara)<br />[DaNE](https://github.com/alexandrainst/danlp/blob/master/docs/datasets.md#danish-dependency-treebank-dane) (Rasmus Hvingelby, Amalie B. Pauli, Maria Barrett, Christina Rosted, Lasse M. Lidegaard, Anders Søgaard) |
| **License** | `CC BY-SA 4.0` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (194 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`morphologizer`** | `AdpType=Prep\|POS=ADP`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=NOUN`, `Mood=Ind\|POS=AUX\|Tense=Pres\|VerbForm=Fin\|Voice=Act`, `POS=PROPN`, `Definite=Ind\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=SCONJ`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=NOUN`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Act`, `POS=ADV`, `Number=Plur\|POS=DET\|PronType=Dem`, `Degree=Pos\|Number=Plur\|POS=ADJ`, `Definite=Ind\|Gender=Com\|Number=Plur\|POS=NOUN`, `POS=PUNCT`, `POS=CCONJ`, `Definite=Ind\|Degree=Cmp\|Number=Sing\|POS=ADJ`, `Degree=Cmp\|POS=ADJ`, `POS=PRON\|PartType=Inf`, `Gender=Com\|Number=Sing\|POS=DET\|PronType=Ind`, `Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Case=Acc\|Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Degree=Pos\|POS=ADV`, `Definite=Def\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PRON\|PronType=Dem`, `NumType=Card\|POS=NUM`, `Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Case=Acc\|Gender=Com\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Degree=Pos\|Gender=Com\|Number=Sing\|POS=ADJ`, `Case=Nom\|Gender=Com\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `NumType=Ord\|POS=ADJ`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Mood=Ind\|POS=AUX\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `POS=VERB\|VerbForm=Inf\|Voice=Act`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `POS=NOUN`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Pass`, `POS=ADP\|PartType=Inf`, `Degree=Pos\|POS=ADJ`, `Definite=Def\|Gender=Com\|Number=Plur\|POS=NOUN`, `Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Com\|Number=Sing\|POS=NOUN`, `POS=AUX\|VerbForm=Inf\|Voice=Act`, `Definite=Ind\|Degree=Pos\|Gender=Com\|Number=Sing\|POS=ADJ`, `Gender=Com\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=DET\|PronType=Ind`, `Gender=Com\|Number=Sing\|POS=PRON\|PronType=Ind`, `Case=Acc\|POS=PRON\|Person=3\|PronType=Prs\|Reflex=Yes`, `POS=PART\|PartType=Inf`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Acc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Case=Nom\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Nom\|Gender=Com\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Nom\|Gender=Com\|POS=PRON\|PronType=Ind`, `Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Ind`, `Mood=Imp\|POS=VERB`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Definite=Ind\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `POS=X`, `Case=Nom\|Gender=Com\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Com\|Number=Plur\|POS=NOUN`, `POS=VERB\|Tense=Pres\|VerbForm=Part`, `Number=Plur\|POS=PRON\|PronType=Int,Rel`, `POS=VERB\|VerbForm=Inf\|Voice=Pass`, `Case=Gen\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=NOUN`, `Degree=Cmp\|POS=ADV`, `POS=ADV\|PartType=Inf`, `Degree=Sup\|POS=ADV`, `Number=Plur\|POS=PRON\|PronType=Dem`, `Number=Plur\|POS=PRON\|PronType=Ind`, `Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Case=Acc\|Gender=Com\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|POS=PROPN`, `POS=ADP`, `Degree=Cmp\|Number=Plur\|POS=ADJ`, `Definite=Def\|Degree=Sup\|POS=ADJ`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Degree=Pos\|Number=Sing\|POS=ADJ`, `Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Gender=Com\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Number=Plur\|POS=PRON\|PronType=Rcp`, `Case=Gen\|Degree=Cmp\|POS=ADJ`, `POS=SPACE`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Number[psor]=Plur\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `POS=INTJ`, `Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Gender=Neut\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Case=Acc\|Gender=Com\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Number=Sing\|POS=PRON\|PronType=Int,Rel`, `Number=Plur\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Int,Rel`, `Definite=Def\|Degree=Sup\|Number=Plur\|POS=ADJ`, `Case=Nom\|Gender=Com\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Definite=Ind\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Plur\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `POS=SYM`, `Case=Nom\|Gender=Com\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Degree=Sup\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Ind\|Style=Arch`, `Case=Gen\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Dem`, `Foreign=Yes\|POS=X`, `POS=DET\|Person=2\|Polite=Form\|Poss=Yes\|PronType=Prs`, `Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Dem`, `Case=Acc\|Gender=Com\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Case=Gen\|POS=PRON\|PronType=Int,Rel`, `Gender=Com\|Number=Sing\|POS=PRON\|PronType=Dem`, `Abbr=Yes\|POS=X`, `Case=Gen\|Definite=Ind\|Gender=Com\|Number=Plur\|POS=NOUN`, `Definite=Def\|Degree=Abs\|POS=ADJ`, `Definite=Ind\|Degree=Sup\|Number=Sing\|POS=ADJ`, `Definite=Ind\|POS=NOUN`, `Gender=Com\|Number=Plur\|POS=NOUN`, `Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Gender=Com\|POS=PRON\|PronType=Int,Rel`, `Case=Nom\|Gender=Com\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Degree=Abs\|POS=ADV`, `POS=VERB\|VerbForm=Ger`, `POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Degree=Sup\|Number=Sing\|POS=ADJ`, `Number=Plur\|Number[psor]=Plur\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Case=Gen\|Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Case=Gen\|Degree=Pos\|Number=Plur\|POS=ADJ`, `Case=Acc\|Gender=Com\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Gender=Com\|Number=Sing\|POS=PRON\|PronType=Int,Rel`, `POS=VERB\|Tense=Pres`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Ind`, `Number[psor]=Plur\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `POS=PRON\|Person=2\|Polite=Form\|Poss=Yes\|PronType=Prs`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `POS=AUX\|Tense=Pres\|VerbForm=Part`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Pass`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Degree=Sup\|Number=Plur\|POS=ADJ`, `Case=Acc\|Gender=Com\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Definite=Ind\|Number=Plur\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Mood=Imp\|POS=AUX`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Gen\|POS=NOUN`, `Number[psor]=Plur\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `POS=DET\|PronType=Dem`, `Definite=Def\|Number=Plur\|POS=NOUN` |
| **`parser`** | `ROOT`, `acl:relcl`, `advcl`, `advmod`, `advmod:lmod`, `amod`, `appos`, `aux`, `case`, `cc`, `ccomp`, `compound:prt`, `conj`, `cop`, `dep`, `det`, `expl`, `fixed`, `flat`, `iobj`, `list`, `mark`, `nmod`, `nmod:poss`, `nsubj`, `nummod`, `obj`, `obl`, `obl:lmod`, `obl:tmod`, `punct`, `xcomp` |
| **`ner`** | `LOC`, `MISC`, `ORG`, `PER` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_ACC` | 99.89 |
| `TOKEN_P` | 99.78 |
| `TOKEN_R` | 99.75 |
| `TOKEN_F` | 99.76 |
| `POS_ACC` | 95.10 |
| `MORPH_ACC` | 93.74 |
| `MORPH_MICRO_P` | 95.81 |
| `MORPH_MICRO_R` | 94.92 |
| `MORPH_MICRO_F` | 95.36 |
| `SENTS_P` | 88.99 |
| `SENTS_R` | 88.83 |
| `SENTS_F` | 88.91 |
| `DEP_UAS` | 81.03 |
| `DEP_LAS` | 76.32 |
| `LEMMA_ACC` | 94.55 |
| `TAG_ACC` | 95.10 |
| `ENTS_P` | 73.59 |
| `ENTS_R` | 70.83 |
| `ENTS_F` | 72.19 |