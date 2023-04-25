---
tags:
- spacy
- token-classification
language:
- nb
license: cc-by-sa-4.0
model-index:
- name: nb_udv25_norwegianbokmaal_trf
  results:
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9916412329
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9913112816
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9842448239
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9882042399
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9563180335
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.9390763849
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9879568106
---
UD v2.5 benchmarking pipeline for UD_Norwegian-Bokmaal

| Feature | Description |
| --- | --- |
| **Name** | `nb_udv25_norwegianbokmaal_trf` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `experimental_char_ner_tokenizer`, `transformer`, `tagger`, `morphologizer`, `parser`, `experimental_edit_tree_lemmatizer` |
| **Components** | `experimental_char_ner_tokenizer`, `transformer`, `senter`, `tagger`, `morphologizer`, `parser`, `experimental_edit_tree_lemmatizer` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [Universal Dependencies v2.5](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3105) (Zeman, Daniel; et al.) |
| **License** | `CC BY-SA 4.0` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (1240 labels for 6 components)</summary>

| Component | Labels |
| --- | --- |
| **`experimental_char_ner_tokenizer`** | `TOKEN` |
| **`senter`** | `I`, `S` |
| **`tagger`** | `ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `INTJ`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `PUNCT`, `SCONJ`, `SYM`, `VERB`, `X` |
| **`morphologizer`** | `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=CCONJ`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `POS=SCONJ`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `POS=PUNCT`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin`, `POS=ADP`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `POS=PROPN`, `POS=X`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PRON\|PronType=Rel`, `Mood=Ind\|POS=AUX\|Tense=Pres\|VerbForm=Fin`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Gender=Fem\|Number=Plur\|POS=NOUN`, `POS=ADV`, `Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Definite=Ind\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `POS=VERB\|VerbForm=Part`, `Definite=Ind\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Degree=Pos\|Number=Plur\|POS=ADJ`, `NumType=Card\|Number=Plur\|POS=NUM`, `Definite=Def\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Case=Acc\|POS=PRON\|PronType=Prs\|Reflex=Yes`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PART`, `POS=VERB\|VerbForm=Inf`, `Case=Nom\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Ind\|POS=AUX\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|POS=PROPN`, `POS=NOUN`, `Gender=Masc\|POS=PROPN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Gen\|Definite=Def\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Abbr=Yes\|POS=PROPN`, `POS=PART\|Polarity=Neg`, `Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Case=Gen\|POS=PROPN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Degree=Sup\|POS=ADJ`, `Case=Gen\|Gender=Fem\|POS=PROPN`, `Number=Plur\|POS=DET\|PronType=Dem`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Definite=Ind\|Degree=Sup\|POS=ADJ`, `Definite=Def\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Gender=Neut\|POS=PROPN`, `Number=Plur\|POS=DET\|PronType=Int`, `Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Definite=Def\|POS=DET\|PronType=Dem`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Art`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Pass`, `Abbr=Yes\|Case=Gen\|POS=PROPN`, `Animacy=Hum\|Case=Nom\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Degree=Cmp\|POS=ADJ`, `POS=ADJ\|VerbForm=Part`, `Gender=Neut\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Abbr=Yes\|POS=ADP`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `POS=AUX\|VerbForm=Part`, `POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `Number=Plur\|POS=DET\|PronType=Ind`, `Degree=Pos\|POS=ADJ`, `Animacy=Hum\|Case=Nom\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `POS=VERB\|VerbForm=Inf\|Voice=Pass`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Ind`, `Animacy=Hum\|Case=Acc\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Number=Plur\|POS=DET\|Polarity=Neg\|PronType=Neg`, `NumType=Card\|POS=NUM`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Ind`, `POS=DET\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Gen\|Gender=Neut\|POS=PROPN`, `Gender=Masc\|Number=Sing\|POS=DET\|Polarity=Neg\|PronType=Neg`, `Definite=Def\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `POS=AUX\|VerbForm=Inf`, `Case=Acc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Gen\|Degree=Pos\|Number=Plur\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Tot`, `Case=Gen\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=DET\|PronType=Prs`, `POS=SYM`, `Gender=Neut\|NumType=Card\|Number=Sing\|POS=NUM`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|PronType=Prs`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Abbr=Yes\|POS=ADV`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Tot`, `Definite=Def\|POS=DET\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Neut\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Int`, `Definite=Def\|NumType=Card\|POS=NUM`, `Mood=Imp\|POS=VERB\|VerbForm=Fin`, `Definite=Ind\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Tot`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Tot`, `Animacy=Hum\|Case=Acc\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|Polarity=Neg\|PronType=Neg,Prs`, `Number=Plur\|POS=PRON\|Person=3\|Polarity=Neg\|PronType=Neg,Prs`, `Definite=Def\|NumType=Card\|Number=Sing\|POS=NUM`, `Gender=Masc\|NumType=Card\|Number=Sing\|POS=NUM`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Case=Gen\|Definite=Def\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Case=Gen\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Animacy=Hum\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Mood=Imp\|POS=AUX\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs,Tot`, `Number=Plur\|POS=ADJ`, `Gender=Masc\|POS=NOUN`, `Abbr=Yes\|POS=NOUN`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `POS=INTJ`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Animacy=Hum\|Case=Acc\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Masc\|Number=Plur\|POS=NOUN`, `POS=ADJ`, `Animacy=Hum\|Case=Acc\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Animacy=Hum\|Case=Acc\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Sing\|POS=PRON\|Polarity=Neg\|PronType=Neg`, `Case=Gen\|POS=NOUN`, `Definite=Ind\|Number=Sing\|POS=ADJ`, `Case=Gen\|Gender=Masc\|POS=PROPN`, `Animacy=Hum\|Number=Plur\|POS=PRON\|PronType=Rcp`, `Case=Gen\|Definite=Ind\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Gen\|Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Int`, `NumType=Card\|Number=Sing\|POS=NUM`, `Animacy=Hum\|Case=Acc\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Degree=Sup\|POS=ADJ`, `Animacy=Hum\|POS=PRON\|PronType=Int`, `POS=DET\|PronType=Ind`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Fem\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Dem`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs,Tot`, `Case=Gen\|Definite=Ind\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|Polarity=Neg\|PronType=Neg`, `Number=Plur\|POS=NOUN`, `POS=PRON\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Definite=Ind\|Number=Sing\|POS=VERB\|VerbForm=Part`, `Case=Gen\|Definite=Def\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Pass`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem,Ind`, `Animacy=Hum\|POS=PRON\|Poss=Yes\|PronType=Int`, `Abbr=Yes\|POS=ADJ`, `Case=Gen\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Case=Gen\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Rcp`, `Definite=Ind\|Degree=Pos\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Art`, `Case=Gen\|NumType=Card\|Number=Plur\|POS=NUM`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Neut\|Number=Plur,Sing\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Tot`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Masc\|Number=Plur,Sing\|POS=NOUN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Int`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Prs`, `Animacy=Hum\|Case=Gen,Nom\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Definite=Def\|Degree=Pos\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Animacy=Hum\|Case=Gen\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Gender=Fem\|NumType=Card\|Number=Sing\|POS=NUM`, `Definite=Ind\|Gender=Masc\|POS=NOUN`, `Definite=Def\|Number=Plur\|POS=NOUN`, `Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Abbr=Yes\|Gender=Masc\|POS=NOUN`, `Abbr=Yes\|Case=Gen\|POS=NOUN`, `Abbr=Yes\|Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Abbr=Yes\|Degree=Pos\|POS=ADJ`, `Case=Gen\|Gender=Fem\|POS=NOUN`, `Case=Gen\|Degree=Cmp\|POS=ADJ`, `Definite=Ind\|Degree=Pos\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=NOUN` |
| **`parser`** | `ROOT`, `acl`, `acl:cleft`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `ccomp`, `compound`, `compound:prt`, `conj`, `cop`, `csubj`, `dep`, `det`, `discourse`, `expl`, `flat:foreign`, `flat:name`, `iobj`, `mark`, `nmod`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `orphan`, `parataxis`, `punct`, `reparandum`, `xcomp` |
| **`experimental_edit_tree_lemmatizer`** | `1`, `2`, `4`, `6`, `8`, `10`, `12`, `14`, `16`, `18`, `20`, `22`, `24`, `26`, `28`, `32`, `34`, `36`, `38`, `40`, `42`, `44`, `47`, `49`, `51`, `52`, `54`, `56`, `58`, `59`, `60`, `62`, `64`, `65`, `67`, `69`, `70`, `71`, `73`, `75`, `78`, `81`, `83`, `87`, `89`, `93`, `96`, `98`, `99`, `100`, `102`, `104`, `106`, `110`, `112`, `115`, `116`, `118`, `120`, `122`, `124`, `128`, `131`, `133`, `135`, `137`, `140`, `142`, `143`, `144`, `145`, `147`, `149`, `151`, `153`, `154`, `156`, `158`, `159`, `162`, `165`, `166`, `168`, `169`, `171`, `173`, `175`, `177`, `179`, `180`, `182`, `184`, `185`, `186`, `187`, `189`, `190`, `192`, `193`, `194`, `195`, `198`, `199`, `201`, `203`, `204`, `207`, `209`, `211`, `214`, `217`, `218`, `219`, `220`, `223`, `225`, `227`, `228`, `229`, `231`, `232`, `233`, `235`, `236`, `239`, `240`, `243`, `246`, `248`, `249`, `250`, `251`, `254`, `257`, `259`, `261`, `263`, `266`, `267`, `270`, `272`, `274`, `275`, `276`, `279`, `282`, `283`, `284`, `285`, `286`, `289`, `290`, `291`, `292`, `294`, `298`, `302`, `304`, `305`, `306`, `309`, `310`, `311`, `314`, `315`, `316`, `317`, `319`, `320`, `322`, `46`, `324`, `326`, `327`, `329`, `330`, `331`, `332`, `334`, `335`, `336`, `337`, `339`, `340`, `341`, `343`, `344`, `346`, `348`, `349`, `352`, `353`, `354`, `356`, `357`, `358`, `359`, `361`, `363`, `364`, `365`, `367`, `369`, `372`, `374`, `375`, `376`, `377`, `378`, `380`, `381`, `384`, `385`, `387`, `389`, `391`, `394`, `396`, `397`, `400`, `403`, `405`, `406`, `408`, `409`, `410`, `411`, `413`, `415`, `416`, `418`, `420`, `422`, `423`, `424`, `426`, `428`, `429`, `431`, `432`, `433`, `434`, `435`, `437`, `438`, `440`, `442`, `445`, `446`, `448`, `449`, `450`, `451`, `452`, `453`, `456`, `458`, `459`, `460`, `461`, `462`, `465`, `466`, `468`, `469`, `471`, `474`, `475`, `476`, `477`, `479`, `480`, `482`, `485`, `486`, `488`, `489`, `491`, `492`, `493`, `494`, `495`, `497`, `498`, `499`, `500`, `502`, `503`, `504`, `505`, `506`, `507`, `509`, `510`, `511`, `513`, `517`, `518`, `519`, `521`, `522`, `525`, `526`, `528`, `529`, `533`, `537`, `539`, `541`, `543`, `545`, `546`, `547`, `549`, `550`, `552`, `553`, `554`, `555`, `557`, `558`, `559`, `560`, `561`, `562`, `563`, `564`, `566`, `568`, `570`, `574`, `575`, `576`, `577`, `579`, `581`, `582`, `583`, `585`, `586`, `587`, `589`, `590`, `591`, `593`, `595`, `597`, `599`, `602`, `603`, `604`, `605`, `607`, `608`, `610`, `611`, `612`, `614`, `616`, `617`, `619`, `620`, `621`, `624`, `626`, `628`, `630`, `632`, `635`, `636`, `639`, `640`, `642`, `645`, `647`, `650`, `651`, `652`, `655`, `657`, `658`, `659`, `661`, `662`, `663`, `664`, `665`, `666`, `667`, `668`, `669`, `670`, `672`, `673`, `676`, `677`, `678`, `681`, `682`, `683`, `684`, `686`, `687`, `688`, `690`, `692`, `693`, `694`, `695`, `697`, `698`, `699`, `700`, `701`, `702`, `704`, `705`, `707`, `709`, `710`, `711`, `712`, `713`, `714`, `715`, `716`, `717`, `719`, `721`, `723`, `726`, `728`, `729`, `730`, `731`, `732`, `733`, `734`, `736`, `737`, `738`, `739`, `741`, `742`, `743`, `745`, `746`, `747`, `748`, `749`, `750`, `751`, `753`, `754`, `757`, `759`, `760`, `761`, `762`, `763`, `765`, `767`, `768`, `770`, `771`, `772`, `773`, `775`, `777`, `778`, `779`, `780`, `781`, `783`, `784`, `785`, `786`, `787`, `788`, `789`, `790`, `791`, `792`, `795`, `798`, `799`, `801`, `802`, `803`, `805`, `806`, `809`, `811`, `812`, `814`, `815`, `816`, `817`, `818`, `820`, `822`, `823`, `824`, `825`, `826`, `827`, `828`, `829`, `830`, `832`, `833`, `836`, `838`, `839`, `840`, `841`, `843`, `844`, `845`, `846`, `847`, `848`, `850`, `851`, `852`, `853`, `854`, `855`, `857`, `858`, `859`, `860`, `862`, `864`, `865`, `868`, `869`, `870`, `871`, `872`, `873`, `874`, `876`, `877`, `878`, `881`, `883`, `884`, `885`, `886`, `887`, `888`, `889`, `890`, `892`, `893`, `894`, `896`, `897`, `898`, `899`, `901`, `902`, `905`, `908`, `911`, `912`, `913`, `915`, `916`, `917`, `918`, `919`, `920`, `921`, `925`, `927`, `928`, `929`, `930`, `932`, `936`, `937`, `938`, `940`, `941`, `943`, `944`, `947`, `948`, `950`, `952`, `953`, `955`, `957`, `959`, `962`, `964`, `966`, `967`, `968`, `969`, `971`, `972`, `973`, `974`, `977`, `978`, `117`, `41`, `979`, `980`, `981`, `982`, `983`, `985`, `988`, `989`, `990`, `992`, `994`, `995`, `996`, `998`, `999`, `1000`, `1001`, `1002`, `1003`, `1004`, `1007`, `1009`, `1010`, `1011`, `1012`, `1013`, `1014`, `1015`, `1016`, `1017`, `1018`, `1019`, `1020`, `1021`, `1022`, `1023`, `1024`, `1025`, `1026`, `1029`, `1031`, `1035`, `1037`, `1039`, `1040`, `1041`, `1043`, `1044`, `1045`, `1048`, `1049`, `1050`, `1051`, `1053`, `1056`, `1058`, `1059`, `1060`, `1061`, `1064`, `1066`, `1068`, `1070`, `1071`, `1072`, `1075`, `1078`, `1079`, `1080`, `1081`, `1084`, `1085`, `1088`, `1090`, `1093`, `1095`, `1099`, `1102`, `1103`, `1105`, `1106`, `1107`, `1109`, `1110`, `1111`, `1113`, `1115`, `1116`, `1121`, `1123`, `1124`, `1126`, `1128`, `1129`, `1130`, `1131`, `1133`, `1134`, `1136`, `1137`, `1138`, `1139`, `1141`, `1143`, `1144`, `1145`, `1147`, `1148`, `1149`, `1150`, `1151`, `1153`, `1154`, `1156`, `1157`, `1158`, `1162`, `1163`, `1165`, `1166`, `1167`, `1168`, `1169`, `1170`, `1171`, `1172`, `1173`, `1174`, `1175`, `1176`, `1030`, `1179`, `1180`, `1182`, `1184`, `1185`, `1186`, `1187`, `1188`, `1189`, `1190`, `1191`, `1192`, `1193`, `1195`, `1198`, `1199`, `1201`, `1202`, `1204`, `1205`, `1206`, `1207`, `1211`, `1213`, `1214`, `1216`, `1219`, `1220`, `1221`, `1222`, `1223`, `1224`, `1225`, `1226`, `1228`, `1230`, `1232`, `1234`, `1235`, `1238`, `1239`, `1240`, `1241`, `1242`, `1244`, `1247`, `1248`, `1249`, `1250`, `1251`, `1253`, `1254`, `1255`, `1256`, `1257`, `1258`, `1259`, `1262`, `1263`, `1265`, `1267`, `515`, `1268`, `1269`, `1271`, `1273`, `1274`, `1275`, `1276`, `1277`, `1279`, `1280`, `1282`, `1283`, `1284`, `1285`, `1287`, `1289`, `1291`, `1292`, `1294`, `1297`, `1298`, `1299`, `1302`, `1303`, `1305`, `1307`, `1308`, `1309`, `1311`, `1312`, `1313`, `1314`, `1315`, `1316`, `1317`, `1318`, `1320`, `1321`, `1322`, `1324`, `1325`, `1326`, `1329`, `1331`, `1334`, `1336`, `1337`, `1340`, `1341`, `1342`, `1343`, `1346`, `1348`, `1349`, `1350`, `1352`, `1353`, `1355`, `1357`, `1358`, `1359`, `1361`, `965`, `1362`, `1363`, `1364`, `1366`, `1369`, `1370`, `1371`, `1372`, `1373`, `1375`, `1376`, `1377`, `1379`, `1381`, `1382`, `1383`, `1385`, `1387`, `1388`, `1390`, `1392`, `1393`, `1394`, `1395`, `1396`, `1397`, `1398`, `1399`, `1400`, `1402`, `1403`, `1405`, `1406`, `1407`, `1409`, `1411`, `1412`, `1413`, `1414`, `1418`, `1419`, `1420`, `1421`, `1423`, `1424`, `1425`, `1427`, `1428`, `1429`, `1430`, `1432`, `1433`, `1435`, `1437`, `1438`, `1441`, `1442`, `1444`, `1446`, `1447`, `1449`, `1453`, `1455`, `1457`, `1458`, `1460`, `1462`, `1463`, `1464`, `1466`, `1469`, `1470`, `1471`, `1473`, `1475`, `1476`, `1477`, `1478`, `1479`, `1482`, `1483`, `1484`, `1486`, `1487`, `1489`, `1491`, `1493`, `1494`, `1495`, `1496`, `1497`, `1498`, `1499`, `1500`, `1501`, `1502`, `1503`, `1504`, `1506`, `1507`, `1508`, `1510`, `1511`, `1512`, `1513`, `1516`, `1517`, `1518`, `1519`, `1520`, `1521`, `1522`, `1523`, `849` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_F` | 100.00 |
| `TOKEN_P` | 100.00 |
| `TOKEN_R` | 100.00 |
| `TOKEN_ACC` | 100.00 |
| `SENTS_F` | 98.80 |
| `SENTS_P` | 98.84 |
| `SENTS_R` | 98.75 |
| `TAG_ACC` | 99.16 |
| `POS_ACC` | 99.13 |
| `MORPH_ACC` | 98.42 |
| `DEP_UAS` | 95.63 |
| `DEP_LAS` | 93.91 |
| `LEMMA_ACC` | 98.82 |