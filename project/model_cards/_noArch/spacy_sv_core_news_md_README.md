---
tags:
- spacy
- token-classification
language:
- sv
license: cc-by-sa-4.0
model-index:
- name: sv_core_news_md
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8516666667
    - name: NER Recall
      type: recall
      value: 0.7459854015
    - name: NER F Score
      type: f_score
      value: 0.7953307393
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9482494641
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9606001837
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9541696438
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9557007247
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.8339750849
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.7849377123
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9126213592
---
### Details: https://spacy.io/models/sv#sv_core_news_md

Swedish pipeline optimized for CPU. Components: tok2vec, tagger, morphologizer, parser, lemmatizer (trainable_lemmatizer), senter, ner.

| Feature | Description |
| --- | --- |
| **Name** | `sv_core_news_md` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `tok2vec`, `tagger`, `morphologizer`, `parser`, `lemmatizer`, `attribute_ruler`, `ner` |
| **Components** | `tok2vec`, `tagger`, `morphologizer`, `parser`, `lemmatizer`, `senter`, `attribute_ruler`, `ner` |
| **Vectors** | floret (50000, 300) |
| **Sources** | [UD Swedish Talbanken v2.8](https://github.com/UniversalDependencies/UD_Swedish-Talbanken) (Nivre, Joakim; Smith, Aaron)<br />[Stockholm-Umeå Corpus (SUC) v3.0](https://huggingface.co/datasets/KBLab/sucx3_ner) (Språkbanken)<br />[Explosion Vectors (OSCAR 2109 + Wikipedia + OpenSubtitles + WMT News Crawl)](https://github.com/explosion/spacy-vectors-builder) (Explosion) |
| **License** | `CC BY-SA 4.0` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (381 labels for 4 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `AB`, `AB\|AN`, `AB\|KOM`, `AB\|POS`, `AB\|SMS`, `AB\|SUV`, `DT\|NEU\|SIN\|DEF`, `DT\|NEU\|SIN\|IND`, `DT\|NEU\|SIN\|IND/DEF`, `DT\|UTR/NEU\|PLU\|DEF`, `DT\|UTR/NEU\|PLU\|IND`, `DT\|UTR/NEU\|PLU\|IND/DEF`, `DT\|UTR/NEU\|SIN/PLU\|IND`, `DT\|UTR/NEU\|SIN\|DEF`, `DT\|UTR/NEU\|SIN\|IND`, `DT\|UTR\|SIN\|DEF`, `DT\|UTR\|SIN\|IND`, `DT\|UTR\|SIN\|IND/DEF`, `HA`, `HD\|NEU\|SIN\|IND`, `HD\|UTR/NEU\|PLU\|IND`, `HD\|UTR\|SIN\|IND`, `HP\|-\|-\|-`, `HP\|NEU\|SIN\|IND`, `HP\|UTR/NEU\|PLU\|IND`, `HP\|UTR\|SIN\|IND`, `HS\|DEF`, `IE`, `IN`, `JJ`, `JJ\|AN`, `JJ\|KOM\|UTR/NEU\|SIN/PLU\|IND/DEF\|NOM`, `JJ\|POS\|MAS\|SIN\|DEF\|GEN`, `JJ\|POS\|MAS\|SIN\|DEF\|NOM`, `JJ\|POS\|NEU\|SIN\|IND/DEF\|NOM`, `JJ\|POS\|NEU\|SIN\|IND\|NOM`, `JJ\|POS\|UTR/NEU\|PLU\|IND/DEF\|GEN`, `JJ\|POS\|UTR/NEU\|PLU\|IND/DEF\|NOM`, `JJ\|POS\|UTR/NEU\|PLU\|IND\|NOM`, `JJ\|POS\|UTR/NEU\|SIN/PLU\|IND/DEF\|NOM`, `JJ\|POS\|UTR/NEU\|SIN\|DEF\|NOM`, `JJ\|POS\|UTR\|-\|-\|SMS`, `JJ\|POS\|UTR\|SIN\|IND/DEF\|NOM`, `JJ\|POS\|UTR\|SIN\|IND\|GEN`, `JJ\|POS\|UTR\|SIN\|IND\|NOM`, `JJ\|SUV\|MAS\|SIN\|DEF\|NOM`, `JJ\|SUV\|UTR/NEU\|PLU\|DEF\|NOM`, `JJ\|SUV\|UTR/NEU\|SIN/PLU\|DEF\|NOM`, `JJ\|SUV\|UTR/NEU\|SIN/PLU\|IND\|NOM`, `KN`, `MAD`, `MID`, `NN`, `NN\|-\|-\|-\|-`, `NN\|AN`, `NN\|NEU\|-\|-\|SMS`, `NN\|NEU\|PLU\|DEF\|GEN`, `NN\|NEU\|PLU\|DEF\|NOM`, `NN\|NEU\|PLU\|IND\|GEN`, `NN\|NEU\|PLU\|IND\|NOM`, `NN\|NEU\|SIN\|DEF\|GEN`, `NN\|NEU\|SIN\|DEF\|NOM`, `NN\|NEU\|SIN\|IND`, `NN\|NEU\|SIN\|IND\|GEN`, `NN\|NEU\|SIN\|IND\|NOM`, `NN\|SMS`, `NN\|UTR\|-\|-\|-`, `NN\|UTR\|-\|-\|SMS`, `NN\|UTR\|PLU\|DEF\|GEN`, `NN\|UTR\|PLU\|DEF\|NOM`, `NN\|UTR\|PLU\|IND\|GEN`, `NN\|UTR\|PLU\|IND\|NOM`, `NN\|UTR\|SIN\|DEF\|GEN`, `NN\|UTR\|SIN\|DEF\|NOM`, `NN\|UTR\|SIN\|IND\|GEN`, `NN\|UTR\|SIN\|IND\|NOM`, `PAD`, `PC\|PRF\|NEU\|SIN\|IND\|NOM`, `PC\|PRF\|UTR/NEU\|PLU\|IND/DEF\|GEN`, `PC\|PRF\|UTR/NEU\|PLU\|IND/DEF\|NOM`, `PC\|PRF\|UTR/NEU\|SIN\|DEF\|NOM`, `PC\|PRF\|UTR\|SIN\|IND\|NOM`, `PC\|PRS\|UTR/NEU\|SIN/PLU\|IND/DEF\|NOM`, `PL`, `PM`, `PM\|GEN`, `PM\|NOM`, `PM\|SMS`, `PN\|MAS\|SIN\|DEF\|SUB/OBJ`, `PN\|NEU\|SIN\|DEF`, `PN\|NEU\|SIN\|DEF\|SUB/OBJ`, `PN\|NEU\|SIN\|IND\|SUB/OBJ`, `PN\|UTR/NEU\|PLU\|DEF\|OBJ`, `PN\|UTR/NEU\|PLU\|DEF\|SUB`, `PN\|UTR/NEU\|PLU\|DEF\|SUB/OBJ`, `PN\|UTR/NEU\|PLU\|IND\|SUB/OBJ`, `PN\|UTR/NEU\|SIN/PLU\|DEF\|OBJ`, `PN\|UTR\|PLU\|DEF\|OBJ`, `PN\|UTR\|PLU\|DEF\|SUB`, `PN\|UTR\|SIN\|DEF\|NOM`, `PN\|UTR\|SIN\|DEF\|OBJ`, `PN\|UTR\|SIN\|DEF\|SUB`, `PN\|UTR\|SIN\|DEF\|SUB/OBJ`, `PN\|UTR\|SIN\|IND\|NOM`, `PN\|UTR\|SIN\|IND\|SUB`, `PN\|UTR\|SIN\|IND\|SUB/OBJ`, `PP`, `PS\|NEU\|SIN\|DEF`, `PS\|UTR/NEU\|PLU\|DEF`, `PS\|UTR/NEU\|SIN/PLU\|DEF`, `PS\|UTR\|SIN\|DEF`, `RG\|NEU\|SIN\|IND\|NOM`, `RG\|NOM`, `RG\|SMS`, `RG\|UTR\|SIN\|IND\|NOM`, `RO\|MAS\|SIN\|IND/DEF\|NOM`, `RO\|NOM`, `SN`, `UO`, `VB\|AN`, `VB\|IMP\|AKT`, `VB\|IMP\|SFO`, `VB\|INF\|AKT`, `VB\|INF\|SFO`, `VB\|KON\|PRS\|AKT`, `VB\|KON\|PRT\|AKT`, `VB\|PRS\|AKT`, `VB\|PRS\|SFO`, `VB\|PRT\|AKT`, `VB\|PRT\|SFO`, `VB\|SUP\|AKT`, `VB\|SUP\|SFO`, `_SP` |
| **`morphologizer`** | `Case=Nom\|Definite=Ind\|Degree=Pos\|Gender=Com\|Number=Sing\|POS=ADJ`, `Case=Nom\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=NOUN`, `POS=ADP`, `Case=Nom\|Definite=Ind\|Gender=Com\|Number=Plur\|POS=NOUN`, `Case=Nom\|Definite=Def\|Gender=Com\|Number=Sing\|POS=NOUN`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Pass`, `POS=PUNCT`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Prs`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Act`, `Abbr=Yes\|POS=ADV`, `POS=SCONJ`, `POS=ADV`, `Case=Nom\|Definite=Ind\|Gender=Com\|NumType=Card\|Number=Sing\|POS=NUM`, `Mood=Ind\|POS=AUX\|Tense=Pres\|VerbForm=Fin\|Voice=Act`, `POS=PART`, `POS=VERB\|VerbForm=Inf`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Prs`, `Number=Plur\|POS=DET\|PronType=Tot`, `Case=Nom\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Case=Nom\|Degree=Pos\|Number=Plur\|POS=ADJ`, `Case=Nom\|Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `POS=CCONJ`, `Definite=Def\|Number=Plur\|POS=DET\|PronType=Art`, `POS=PRON\|PronType=Rel`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Degree=Pos\|POS=ADV`, `Definite=Def\|Number=Plur\|POS=DET\|PronType=Dem`, `Case=Nom\|Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Nom\|Definite=Def\|Degree=Pos\|Gender=Masc\|Number=Sing\|POS=ADJ`, `POS=VERB\|VerbForm=Sup\|Voice=Act`, `Case=Nom\|Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PART\|Polarity=Neg`, `Case=Nom\|Degree=Pos\|POS=ADJ`, `Case=Gen\|Definite=Ind\|Gender=Com\|Number=Plur\|POS=NOUN`, `Degree=Cmp\|POS=ADV`, `POS=VERB\|VerbForm=Inf\|Voice=Pass`, `Case=Nom\|Definite=Ind\|Degree=Pos\|Number=Plur\|POS=ADJ`, `Case=Nom\|Definite=Def\|Gender=Com\|Number=Plur\|POS=NOUN`, `Degree=Sup\|POS=ADV`, `Case=Nom\|NumType=Card\|POS=NUM`, `Abbr=Yes\|POS=NOUN`, `Case=Nom\|Definite=Def\|Degree=Sup\|POS=ADJ`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Mood=Imp\|POS=VERB\|VerbForm=Fin\|Voice=Act`, `POS=VERB\|VerbForm=Inf\|Voice=Act`, `Case=Nom\|Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `POS=AUX\|VerbForm=Inf\|Voice=Act`, `Case=Nom\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=ADJ\|Tense=Past\|VerbForm=Part`, `Case=Nom\|Definite=Def\|Number=Plur\|POS=PRON\|PronType=Prs`, `Case=Nom\|Number=Plur\|POS=ADJ\|Tense=Past\|VerbForm=Part`, `POS=AUX\|VerbForm=Sup\|Voice=Act`, `Case=Acc\|Definite=Def\|Number=Plur\|POS=PRON\|PronType=Rcp`, `POS=SPACE`, `POS=VERB\|VerbForm=Sup\|Voice=Pass`, `Mood=Ind\|POS=AUX\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Nom\|Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Case=Nom\|Degree=Cmp\|POS=ADJ`, `Definite=Ind\|Number=Sing\|POS=DET\|PronType=Tot`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Nom\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=ADJ\|Tense=Past\|VerbForm=Part`, `Definite=Ind\|POS=DET\|PronType=Ind`, `Case=Nom\|Definite=Def\|Number=Sing\|POS=ADJ\|Tense=Past\|VerbForm=Part`, `Case=Nom\|POS=ADJ\|Tense=Pres\|VerbForm=Part`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Ind`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Dem`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Art`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `Case=Acc\|Definite=Def\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Prs`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Int`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Case=Nom\|Definite=Def\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Prs`, `Definite=Def\|Number=Plur\|POS=PRON\|PronType=Dem`, `Definite=Def\|Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Case=Acc\|Definite=Def\|Number=Plur\|POS=PRON\|PronType=Prs`, `Case=Nom\|Definite=Def\|Degree=Sup\|Number=Plur\|POS=ADJ`, `Case=Nom\|Degree=Pos\|Gender=Com\|Number=Sing\|POS=ADJ`, `Gender=Com\|Number=Sing\|POS=DET\|PronType=Tot`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Dem`, `Case=Gen\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=NOUN`, `POS=NOUN`, `Case=Nom\|POS=ADJ`, `Case=Nom\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Ind`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Ind`, `Definite=Ind\|Number=Plur\|POS=PRON\|PronType=Tot`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Ind`, `Definite=Ind\|Number=Plur\|POS=PRON\|PronType=Ind`, `Definite=Def\|POS=PRON\|Poss=Yes\|PronType=Ind`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Gender=Com\|POS=NOUN`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Tot`, `Case=Gen\|Definite=Def\|Gender=Com\|Number=Sing\|POS=NOUN`, `Case=Acc\|Definite=Def\|POS=PRON\|PronType=Prs`, `Definite=Def\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Case=Nom\|POS=PROPN`, `Case=Nom\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Case=Nom\|Definite=Def\|Gender=Com\|Number=Plur\|POS=PRON\|PronType=Prs`, `Definite=Def\|Number=Plur\|POS=DET\|PronType=Prs`, `Case=Gen\|Number=Plur\|POS=ADJ\|Tense=Past\|VerbForm=Part`, `Case=Acc\|Definite=Def\|Gender=Com\|Number=Plur\|POS=PRON\|PronType=Prs`, `Definite=Ind\|Number=Plur\|POS=PRON\|PronType=Rel`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin`, `Definite=Ind\|Number=Plur\|POS=PRON\|PronType=Int`, `Number=Plur\|POS=DET\|PronType=Ind`, `Case=Gen\|POS=PROPN`, `POS=PROPN`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Int`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Tot`, `Gender=Neut\|POS=NOUN`, `Case=Gen\|Definite=Def\|Gender=Com\|Number=Plur\|POS=NOUN`, `Definite=Ind\|Number=Plur\|POS=DET\|PronType=Int`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Neg`, `POS=VERB\|VerbForm=Sup`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Pass`, `Case=Nom\|Definite=Ind\|Gender=Neut\|NumType=Card\|Number=Sing\|POS=NUM`, `Foreign=Yes\|POS=NOUN`, `Foreign=Yes\|POS=ADJ`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Ind`, `Definite=Ind\|Number=Plur\|POS=DET\|PronType=Ind`, `POS=SYM`, `Case=Nom\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Tot`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Ind`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Int`, `Case=Nom\|Definite=Ind\|Degree=Sup\|POS=ADJ`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Dem`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Neg`, `Mood=Sub\|POS=AUX\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `Degree=Pos\|Gender=Com\|POS=ADJ`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Ind`, `Case=Nom\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Case=Nom\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Number=Plur\|POS=PRON\|PronType=Ind`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Prs`, `Definite=Ind\|POS=DET\|PronType=Prs`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Prs`, `Definite=Def\|POS=PRON\|Poss=Yes\|PronType=Rel`, `Case=Gen\|Degree=Pos\|Number=Plur\|POS=ADJ`, `Definite=Def\|Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Ind`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Prs`, `Abbr=Yes\|POS=ADJ`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Rel`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Rel`, `NumType=Card\|POS=NUM`, `POS=INTJ`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Int`, `Degree=Sup\|POS=ADV\|Polarity=Neg`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Tot`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Prs`, `Definite=Def\|POS=PRON\|Poss=Yes\|PronType=Int`, `POS=ADV\|Polarity=Neg`, `Definite=Ind\|Number=Sing\|POS=DET\|PronType=Ind`, `POS=ADJ`, `Case=Nom\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Prs`, `Case=Gen\|Definite=Def\|Degree=Pos\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Case=Nom\|Definite=Def\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Tot`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Tot`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Neg`, `Case=Nom\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Definite=Ind\|Number=Plur\|POS=DET\|PronType=Neg`, `Case=Nom\|Definite=Def\|Degree=Sup\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Dem`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Tot`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Neg`, `Gender=Com\|Number=Sing\|POS=DET\|PronType=Prs`, `Mood=Imp\|POS=VERB\|VerbForm=Fin\|Voice=Pass`, `Case=Nom\|Definite=Def\|Number=Plur\|POS=PRON\|PronType=Ind`, `Case=Acc\|Definite=Def\|POS=PRON\|PronType=Ind`, `Foreign=Yes\|POS=ADP`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Prs`, `Definite=Def\|POS=PRON\|Poss=Yes\|PronType=Dem`, `Abbr=Yes\|Mood=Imp\|POS=VERB\|VerbForm=Fin\|Voice=Act`, `Mood=Sub\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Act`, `Case=Nom\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Rel`, `Foreign=Yes\|POS=CCONJ`, `POS=DET\|PronType=Art`, `Definite=Ind\|Number=Sing\|POS=DET\|PronType=Prs`, `Definite=Ind\|Number=Plur\|POS=DET\|PronType=Tot`, `Case=Nom\|Definite=Def\|Gender=Com\|Number=Sing\|POS=PRON\|PronType=Ind`, `Case=Nom\|Definite=Def\|Number=Plur\|POS=PRON\|PronType=Rel`, `Case=Acc\|Definite=Def\|Number=Plur\|POS=PRON\|PronType=Tot`, `Definite=Def\|Number=Plur\|POS=PRON\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Degree=Pos\|Gender=Com\|Number=Sing\|POS=ADJ`, `Definite=Def\|Number=Plur\|POS=PRON\|PronType=Tot`, `Degree=Pos\|POS=ADV\|Polarity=Neg`, `Mood=Sub\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `POS=PRON\|PronType=Ind`, `Definite=Ind\|POS=DET\|PronType=Neg`, `Definite=Ind\|Number=Plur\|POS=PRON\|PronType=Neg`, `POS=CCONJ\|Polarity=Neg`, `Case=Nom\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Case=Acc\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Case=Nom\|Definite=Def\|Number=Plur\|POS=PRON\|PronType=Tot`, `Definite=Def\|Number=Plur\|POS=DET\|PronType=Tot`, `Mood=Imp\|POS=AUX\|VerbForm=Fin\|Voice=Act`, `Foreign=Yes\|POS=ADV`, `Definite=Def\|POS=PRON\|Poss=Yes\|PronType=Rcp`, `Case=Acc\|Definite=Def\|POS=PRON\|Polarity=Neg\|PronType=Ind` |
| **`parser`** | `ROOT`, `acl`, `acl:cleft`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `ccomp`, `compound:prt`, `conj`, `cop`, `csubj`, `dep`, `det`, `dislocated`, `expl`, `fixed`, `flat:name`, `iobj`, `mark`, `nmod`, `nmod:poss`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `obl:agent`, `parataxis`, `punct`, `xcomp` |
| **`ner`** | `EVN`, `LOC`, `MSR`, `OBJ`, `ORG`, `PRS`, `TME`, `WRK` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_ACC` | 99.99 |
| `TOKEN_P` | 99.95 |
| `TOKEN_R` | 99.96 |
| `TOKEN_F` | 99.95 |
| `TAG_ACC` | 94.82 |
| `POS_ACC` | 96.06 |
| `MORPH_ACC` | 95.42 |
| `MORPH_MICRO_P` | 97.28 |
| `MORPH_MICRO_R` | 97.17 |
| `MORPH_MICRO_F` | 97.23 |
| `SENTS_P` | 89.35 |
| `SENTS_R` | 93.25 |
| `SENTS_F` | 91.26 |
| `DEP_UAS` | 83.40 |
| `DEP_LAS` | 78.49 |
| `LEMMA_ACC` | 95.57 |
| `ENTS_P` | 85.17 |
| `ENTS_R` | 74.60 |
| `ENTS_F` | 79.53 |