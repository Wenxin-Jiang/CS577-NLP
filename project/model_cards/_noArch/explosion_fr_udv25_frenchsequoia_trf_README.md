---
tags:
- spacy
- token-classification
language:
- fr
license: lgpl-lr
model-index:
- name: fr_udv25_frenchsequoia_trf
  results:
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9864663202
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9856429784
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9755018013
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9741188577
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9467530964
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.9260331057
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9441747573
---
UD v2.5 benchmarking pipeline for UD_French-Sequoia

| Feature | Description |
| --- | --- |
| **Name** | `fr_udv25_frenchsequoia_trf` |
| **Version** | `0.0.1` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `experimental_char_ner_tokenizer`, `transformer`, `tagger`, `morphologizer`, `parser`, `experimental_edit_tree_lemmatizer` |
| **Components** | `experimental_char_ner_tokenizer`, `transformer`, `senter`, `tagger`, `morphologizer`, `parser`, `experimental_edit_tree_lemmatizer` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [Universal Dependencies v2.5](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3105) (Zeman, Daniel; et al.) |
| **License** | `LGPL-LR` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (916 labels for 6 components)</summary>

| Component | Labels |
| --- | --- |
| **`experimental_char_ner_tokenizer`** | `TOKEN` |
| **`senter`** | `I`, `S` |
| **`tagger`** | `ADJ`, `ADP`, `ADP_DET`, `ADP_PRON`, `ADV`, `AUX`, `CCONJ`, `DET`, `INTJ`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `PUNCT`, `SCONJ`, `SYM`, `VERB`, `X` |
| **`morphologizer`** | `POS=PROPN`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=PRON\|Person=1`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `POS=SCONJ`, `POS=ADP`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `NumType=Ord\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=NOUN`, `POS=PUNCT`, `Gender=Masc\|Number=Sing\|POS=PROPN`, `Number=Plur\|POS=ADJ`, `Gender=Masc\|Number=Plur\|POS=NOUN`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Number=Sing\|POS=ADJ`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `POS=ADV`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=PROPN`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Art`, `NumType=Card\|POS=NUM`, `Definite=Def\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Masc\|Number=Plur\|POS=ADJ`, `POS=CCONJ`, `Gender=Fem\|Number=Plur\|POS=NOUN`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Plur\|POS=ADJ`, `POS=ADJ`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `POS=PRON\|PronType=Rel`, `Number=Sing\|POS=DET\|Poss=Yes`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=ADP\|PronType=Art`, `Definite=Def\|Number=Plur\|POS=ADP\|PronType=Art`, `Definite=Ind\|Number=Plur\|POS=DET\|PronType=Art`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `POS=VERB\|VerbForm=Inf`, `Gender=Fem\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3`, `Number=Plur\|POS=DET`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `POS=ADV\|PronType=Int`, `POS=VERB\|Tense=Pres\|VerbForm=Part`, `Gender=Fem\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Masc\|POS=ADJ`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Number=Plur\|POS=DET\|Poss=Yes`, `POS=AUX\|VerbForm=Inf`, `Gender=Masc\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Gender=Masc\|POS=VERB\|Tense=Past\|VerbForm=Part`, `POS=ADV\|Polarity=Neg`, `Definite=Ind\|Number=Sing\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3`, `POS=PRON\|Person=3\|Reflex=Yes`, `Gender=Masc\|POS=NOUN`, `POS=AUX\|Tense=Past\|VerbForm=Part`, `POS=PRON\|Person=3`, `Number=Plur\|POS=NOUN`, `NumType=Ord\|Number=Sing\|POS=ADJ`, `POS=VERB\|Tense=Past\|VerbForm=Part`, `POS=AUX\|Tense=Pres\|VerbForm=Part`, `Gender=Masc\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Sing\|POS=PRON\|Person=3`, `Number=Sing\|POS=NOUN`, `Gender=Masc\|Number=Plur\|POS=PRON\|Person=3`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|NumType=Ord\|Number=Sing\|POS=ADJ`, `Number=Plur\|POS=PROPN`, `Number=Sing\|POS=PROPN`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=DET`, `Gender=Fem\|Number=Sing\|POS=DET\|Poss=Yes`, `Gender=Masc\|POS=PRON`, `POS=NOUN`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON`, `Gender=Masc\|NumType=Ord\|Number=Plur\|POS=ADJ`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Fut\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Number=Sing\|POS=PRON`, `Number=Sing\|POS=PRON\|PronType=Dem`, `Mood=Ind\|POS=VERB\|VerbForm=Fin`, `Number=Plur\|POS=DET\|PronType=Dem`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=PRON`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Dem`, `Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Rel`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=3\|Tense=Imp\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|NumType=Ord\|Number=Sing\|POS=ADJ`, `POS=PRON`, `POS=NUM`, `Gender=Fem\|POS=NOUN`, `Gender=Fem\|Number=Plur\|POS=PRON`, `Number=Plur\|POS=PRON\|Person=3`, `Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Sing\|POS=PRON\|Person=1`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Past\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=PRON`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `POS=INTJ`, `Number=Plur\|POS=PRON\|Person=2`, `NumType=Card\|POS=PRON`, `Definite=Ind\|Gender=Fem\|Number=Plur\|POS=DET\|PronType=Art`, `Gender=Fem\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `NumType=Card\|POS=NOUN`, `POS=PRON\|PronType=Int`, `Gender=Fem\|Number=Plur\|POS=PRON\|Person=3`, `Gender=Fem\|Number=Sing\|POS=DET`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=DET`, `Mood=Sub\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Definite=Ind\|Gender=Masc\|Number=Plur\|POS=DET\|PronType=Art`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=PRON\|PronType=Dem`, `Gender=Masc\|Number=Plur\|POS=PROPN`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Dem`, `Number=Sing\|POS=DET`, `Gender=Masc\|NumType=Card\|Number=Plur\|POS=NOUN`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Dem`, `Mood=Ind\|POS=VERB\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|POS=PRON`, `Gender=Masc\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Gender=Fem\|Number=Sing\|POS=PRON\|PronType=Rel`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `POS=X`, `POS=SYM`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Int`, `Gender=Fem\|Number=Plur\|POS=DET\|PronType=Int`, `POS=DET`, `Gender=Masc\|Number=Plur\|POS=PRON`, `POS=PART`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|POS=VERB\|Person=3\|VerbForm=Fin`, `Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Mood=Cnd\|Number=Plur\|POS=VERB\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Int`, `Gender=Masc\|Number=Plur\|POS=DET`, `Gender=Fem\|Number=Plur\|POS=PRON\|PronType=Rel`, `Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Gender=Masc\|Number=Plur\|POS=PRON\|PronType=Rel`, `POS=VERB\|Tense=Past\|VerbForm=Part\|Voice=Pass`, `Gender=Fem\|NumType=Ord\|Number=Plur\|POS=ADJ`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Fut\|VerbForm=Fin`, `Mood=Imp\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=2\|Reflex=Yes`, `Mood=Cnd\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=1\|Reflex=Yes`, `Gender=Masc\|NumType=Card\|Number=Sing\|POS=NOUN`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Number=Sing\|POS=PRON\|Person=1\|Reflex=Yes`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=AUX\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Imp\|VerbForm=Fin`, `Mood=Sub\|Number=Sing\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Gender=Masc\|POS=PROPN`, `Mood=Cnd\|Number=Plur\|POS=AUX\|Person=3\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Mood=Sub\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Mood=Ind\|Number=Sing\|POS=VERB\|Person=1\|Tense=Fut\|VerbForm=Fin`, `Gender=Fem\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Mood=Cnd\|Number=Sing\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Imp\|Number=Plur\|POS=VERB\|Person=1\|Tense=Pres\|VerbForm=Fin`, `Mood=Sub\|Number=Plur\|POS=AUX\|Person=2\|Tense=Pres\|VerbForm=Fin`, `Mood=Ind\|Number=Plur\|POS=VERB\|Person=2\|Tense=Imp\|VerbForm=Fin`, `Gender=Fem\|POS=ADV`, `Mood=Ind\|Number=Sing\|POS=AUX\|Person=2\|Tense=Imp\|VerbForm=Fin`, `Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Gender=Fem\|Number=Plur\|POS=PROPN`, `Gender=Masc\|NumType=Card\|POS=NUM` |
| **`parser`** | `ROOT`, `acl`, `acl:relcl`, `advcl`, `advcl:cleft`, `advmod`, `amod`, `appos`, `aux:caus`, `aux:pass`, `aux:tense`, `case`, `cc`, `ccomp`, `conj`, `cop`, `csubj`, `dep`, `det`, `dislocated`, `expl:comp`, `expl:pass`, `expl:subj`, `fixed`, `flat:foreign`, `flat:name`, `iobj`, `mark`, `nmod`, `nsubj`, `nsubj:caus`, `nsubj:pass`, `nummod`, `obj`, `obl:agent`, `obl:arg`, `obl:mod`, `orphan`, `parataxis`, `punct`, `vocative`, `xcomp` |
| **`experimental_edit_tree_lemmatizer`** | `0`, `3`, `4`, `6`, `8`, `10`, `12`, `14`, `16`, `20`, `22`, `24`, `26`, `30`, `32`, `34`, `36`, `39`, `40`, `42`, `44`, `45`, `48`, `50`, `52`, `54`, `56`, `58`, `61`, `63`, `66`, `70`, `72`, `74`, `77`, `79`, `81`, `82`, `84`, `86`, `88`, `89`, `91`, `95`, `97`, `99`, `102`, `103`, `106`, `110`, `111`, `113`, `114`, `115`, `118`, `119`, `123`, `125`, `126`, `128`, `130`, `132`, `133`, `134`, `136`, `138`, `139`, `140`, `142`, `143`, `144`, `146`, `148`, `150`, `152`, `155`, `157`, `160`, `161`, `163`, `165`, `167`, `171`, `173`, `174`, `176`, `177`, `179`, `181`, `183`, `185`, `187`, `189`, `191`, `192`, `195`, `197`, `198`, `200`, `202`, `203`, `205`, `208`, `210`, `211`, `212`, `214`, `217`, `218`, `221`, `225`, `227`, `229`, `230`, `232`, `234`, `236`, `238`, `240`, `242`, `243`, `245`, `247`, `248`, `251`, `253`, `255`, `257`, `258`, `260`, `261`, `264`, `267`, `268`, `269`, `272`, `273`, `276`, `277`, `278`, `279`, `284`, `287`, `288`, `291`, `293`, `295`, `298`, `299`, `301`, `304`, `306`, `307`, `309`, `310`, `313`, `315`, `318`, `319`, `322`, `324`, `325`, `327`, `329`, `330`, `332`, `333`, `336`, `339`, `341`, `342`, `344`, `346`, `347`, `350`, `351`, `353`, `356`, `358`, `359`, `361`, `363`, `365`, `367`, `369`, `373`, `376`, `378`, `379`, `380`, `382`, `384`, `386`, `389`, `390`, `391`, `394`, `396`, `398`, `399`, `401`, `404`, `406`, `409`, `412`, `414`, `418`, `421`, `423`, `424`, `426`, `428`, `429`, `430`, `434`, `436`, `438`, `440`, `441`, `443`, `446`, `447`, `448`, `451`, `453`, `456`, `457`, `458`, `460`, `462`, `463`, `465`, `468`, `470`, `472`, `474`, `480`, `482`, `483`, `485`, `486`, `490`, `493`, `494`, `497`, `499`, `500`, `501`, `503`, `506`, `509`, `511`, `512`, `514`, `516`, `518`, `522`, `523`, `526`, `530`, `532`, `534`, `537`, `539`, `540`, `541`, `543`, `545`, `546`, `548`, `550`, `551`, `552`, `554`, `556`, `557`, `558`, `561`, `563`, `565`, `567`, `570`, `571`, `573`, `574`, `575`, `576`, `578`, `579`, `581`, `582`, `583`, `584`, `586`, `587`, `588`, `589`, `590`, `592`, `595`, `600`, `603`, `604`, `606`, `608`, `611`, `612`, `614`, `615`, `616`, `618`, `619`, `620`, `621`, `622`, `623`, `624`, `625`, `626`, `627`, `628`, `629`, `630`, `631`, `632`, `633`, `634`, `635`, `636`, `638`, `640`, `644`, `646`, `647`, `648`, `650`, `652`, `654`, `657`, `659`, `660`, `661`, `662`, `663`, `664`, `665`, `666`, `668`, `672`, `674`, `675`, `677`, `678`, `679`, `680`, `681`, `682`, `683`, `684`, `685`, `686`, `687`, `688`, `689`, `690`, `691`, `692`, `693`, `694`, `695`, `696`, `697`, `698`, `699`, `700`, `701`, `702`, `704`, `705`, `706`, `707`, `708`, `709`, `710`, `711`, `712`, `713`, `714`, `715`, `716`, `717`, `718`, `719`, `720`, `721`, `722`, `723`, `724`, `725`, `726`, `727`, `728`, `729`, `730`, `731`, `732`, `733`, `734`, `735`, `736`, `737`, `738`, `739`, `740`, `741`, `743`, `744`, `747`, `748`, `749`, `750`, `751`, `752`, `753`, `754`, `755`, `756`, `758`, `760`, `762`, `763`, `766`, `767`, `768`, `770`, `772`, `773`, `774`, `775`, `776`, `777`, `778`, `779`, `781`, `783`, `784`, `786`, `787`, `789`, `790`, `791`, `794`, `795`, `796`, `797`, `798`, `799`, `800`, `801`, `802`, `803`, `807`, `809`, `812`, `813`, `815`, `817`, `819`, `821`, `825`, `828`, `829`, `832`, `833`, `834`, `837`, `838`, `839`, `841`, `842`, `844`, `846`, `849`, `851`, `853`, `854`, `855`, `858`, `861`, `862`, `866`, `868`, `869`, `871`, `872`, `874`, `876`, `879`, `880`, `882`, `885`, `887`, `891`, `893`, `895`, `898`, `899`, `902`, `903`, `905`, `906`, `908`, `910`, `911`, `912`, `914`, `917`, `920`, `923`, `925`, `927`, `929`, `932`, `933`, `934`, `936`, `938`, `939`, `943`, `944`, `945`, `946`, `947`, `950`, `952`, `954`, `956`, `958`, `959`, `961`, `963`, `965`, `967`, `969`, `971`, `973`, `976`, `978`, `979`, `980`, `981`, `984`, `986`, `987`, `990`, `993`, `994`, `996`, `998`, `999`, `1000`, `1001`, `1002`, `1004`, `1006`, `1007`, `1009`, `1010`, `1012`, `1014`, `1016`, `1018`, `1021`, `1023`, `1026`, `1027`, `1029`, `1031`, `1033`, `1034`, `1036`, `1037`, `1039`, `1041`, `1043`, `1044`, `1045`, `1046`, `1049`, `1051`, `1053`, `1054`, `1055`, `1056`, `1057`, `1058`, `1059`, `1061`, `1063`, `1065`, `1067`, `1068`, `1070`, `1072`, `1073`, `1075`, `1077`, `1078`, `1080`, `1081`, `1082`, `1084`, `1085`, `1087`, `1088`, `1089`, `1090`, `1091`, `1092`, `1094`, `1095`, `1097`, `1098`, `1100`, `1103`, `1106`, `1108`, `1110`, `1111`, `1113`, `1116`, `1117`, `1119`, `1121`, `1124`, `1127`, `1129`, `1131`, `1132`, `1133`, `1135`, `1136`, `1138`, `1139`, `1141`, `1142`, `1145`, `1148`, `1153`, `1154`, `1156`, `1157`, `1159`, `1161` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_F` | 99.70 |
| `TOKEN_P` | 99.69 |
| `TOKEN_R` | 99.71 |
| `TOKEN_ACC` | 99.96 |
| `SENTS_F` | 94.42 |
| `SENTS_P` | 94.42 |
| `SENTS_R` | 94.42 |
| `TAG_ACC` | 98.65 |
| `POS_ACC` | 98.56 |
| `MORPH_ACC` | 97.55 |
| `DEP_UAS` | 94.68 |
| `DEP_LAS` | 92.60 |
| `LEMMA_ACC` | 97.41 |