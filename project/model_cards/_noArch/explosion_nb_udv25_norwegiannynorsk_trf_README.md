---
tags:
- spacy
- token-classification
language:
- nb
license: cc-by-sa-4.0
model-index:
- name: nb_udv25_norwegiannynorsk_trf
  results:
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9833263993
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9833584024
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9790699907
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9828149002
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9411235308
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.9214320428
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9910005294
---
UD v2.5 benchmarking pipeline for UD_Norwegian-Nynorsk

| Feature | Description |
| --- | --- |
| **Name** | `nb_udv25_norwegiannynorsk_trf` |
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

<summary>View label scheme (1400 labels for 6 components)</summary>

| Component | Labels |
| --- | --- |
| **`experimental_char_ner_tokenizer`** | `TOKEN` |
| **`senter`** | `I`, `S` |
| **`tagger`** | `ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `INTJ`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `PUNCT`, `SCONJ`, `SYM`, `VERB`, `X` |
| **`morphologizer`** | `Number=Plur\|POS=DET\|PronType=Ind`, `Definite=Ind\|Gender=Masc\|Number=Plur\|POS=NOUN`, `POS=ADP`, `Definite=Def\|Gender=Masc\|Number=Sing\|POS=NOUN`, `POS=PUNCT`, `Gender=Masc\|POS=NOUN`, `POS=CCONJ`, `Definite=Ind\|Number=Plur\|POS=NOUN`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `POS=NOUN`, `POS=PROPN`, `Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Mood=Ind\|POS=AUX\|Tense=Past\|VerbForm=Fin`, `Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Animacy=Hum\|Case=Nom\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `POS=ADV`, `Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Gender=Masc\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=SCONJ`, `Gender=Neut\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Mood=Ind\|POS=AUX\|Tense=Pres\|VerbForm=Fin`, `POS=PART`, `POS=VERB\|VerbForm=Inf`, `POS=PRON\|PronType=Rel`, `POS=VERB\|VerbForm=Part`, `Animacy=Hum\|Case=Acc\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Degree=Pos\|Number=Plur\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Dem`, `Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Abbr=Yes\|POS=NOUN`, `Definite=Ind\|Degree=Pos\|Gender=Masc\|Number=Sing\|POS=ADJ`, `Abbr=Yes\|POS=ADV`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Degree=Cmp\|POS=ADJ`, `POS=ADJ\|VerbForm=Part`, `Case=Nom\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `POS=DET\|PronType=Int`, `POS=AUX\|VerbForm=Inf`, `Definite=Def\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Definite=Def\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Case=Acc\|Number=Sing\|POS=PRON\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Definite=Def\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Gender=Fem\|Number=Sing\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Abbr=Yes\|POS=ADJ`, `POS=PART\|Polarity=Neg`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Art`, `POS=INTJ`, `Animacy=Hum\|Number=Sing\|POS=PRON\|PronType=Art,Prs`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Gen\|POS=PROPN`, `Animacy=Hum\|Case=Nom\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=DET\|Polarity=Neg\|PronType=Neg`, `Animacy=Hum\|Case=Acc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Animacy=Hum\|Case=Acc\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Animacy=Hum\|Case=Nom\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Art`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PRON\|PronType=Int`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `NumType=Card\|POS=NUM`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=DET\|PronType=Tot`, `Definite=Ind\|Degree=Sup\|POS=ADJ`, `NumType=Card\|Number=Plur\|POS=NUM`, `Definite=Def\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Mood=Imp\|POS=VERB\|VerbForm=Fin`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Ind`, `Definite=Def\|POS=DET\|PronType=Dem`, `POS=X`, `Case=Gen\|Gender=Masc\|POS=NOUN`, `POS=AUX\|VerbForm=Part`, `Number=Plur\|POS=ADJ\|VerbForm=Part`, `Case=Acc\|Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Number=Sing\|POS=DET\|PronType=Tot`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Animacy=Hum\|Number=Plur\|POS=PRON\|PronType=Rcp`, `Definite=Def\|Degree=Sup\|POS=ADJ`, `Gender=Masc\|NumType=Card\|Number=Sing\|POS=NUM`, `POS=DET\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Ind`, `Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `Definite=Ind\|Degree=Pos\|POS=ADJ`, `Number=Plur\|POS=PRON\|Poss=Yes\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=DET\|PronType=Tot`, `POS=SYM`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Tot`, `Number=Plur\|POS=NOUN`, `Definite=Ind\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Masc\|Number=Sing\|POS=NOUN`, `Gender=Fem,Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Abbr=Yes\|POS=PRON\|PronType=Prs`, `Abbr=Yes\|Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `POS=ADJ`, `Gender=Neut\|POS=NOUN`, `Animacy=Hum\|Case=Acc\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Prs`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Dem`, `Gender=Fem\|POS=NOUN`, `Degree=Pos\|POS=ADJ`, `Definite=Def\|NumType=Card\|Number=Sing\|POS=NUM`, `Animacy=Hum\|Case=Nom\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Animacy=Hum\|Case=Acc\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Definite=Def\|NumType=Card\|POS=NUM`, `Case=Nom\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Tot`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs,Tot`, `Case=Acc\|Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Gender=Fem\|Number=Sing\|POS=DET\|Polarity=Neg\|PronType=Neg`, `Gender=Fem\|NumType=Card\|Number=Sing\|POS=NUM`, `Definite=Def\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Degree=Pos\|Gender=Fem\|Number=Sing\|POS=ADJ`, `Animacy=Hum\|POS=PRON\|PronType=Int`, `Mood=Imp\|POS=AUX\|VerbForm=Fin`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Number=Plur\|POS=DET\|PronType=Prs`, `Case=Gen\|Gender=Masc\|Number=Sing\|POS=DET\|PronType=Dem`, `Abbr=Yes\|POS=CCONJ`, `Number=Plur\|POS=PRON\|Person=3\|Polarity=Neg\|PronType=Neg,Prs`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `Definite=Def\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=ADJ`, `Gender=Masc\|Number=Sing\|POS=DET\|Polarity=Neg\|PronType=Neg`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=DET\|PronType=Prs`, `Gender=Masc\|Number=Sing\|POS=PRON\|Person=3\|Polarity=Neg\|PronType=Neg,Prs`, `Abbr=Yes\|Case=Gen\|POS=NOUN`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Dem`, `Definite=Def\|POS=ADV`, `Number=Sing\|POS=PRON\|Polarity=Neg\|PronType=Neg`, `Case=Gen\|Definite=Ind\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Abbr=Yes\|Definite=Def,Ind\|Gender=Neut\|Number=Plur,Sing\|POS=NOUN`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Prs`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Ind,Prs`, `Case=Gen\|Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Abbr=Yes\|POS=ADP`, `Gender=Fem\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Gen\|Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Animacy=Hum\|Case=Nom\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Masc\|Number=Plur\|POS=NOUN`, `Gender=Neut\|NumType=Card\|Number=Sing\|POS=NUM`, `Gender=Fem\|Number=Sing\|POS=PRON\|Person=3\|PronType=Art,Prs`, `Definite=Def\|Number=Plur\|POS=NOUN`, `Abbr=Yes\|Gender=Masc\|POS=NOUN`, `Case=Gen\|POS=NOUN`, `Definite=Ind\|Gender=Fem\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Case=Gen\|Definite=Ind\|Gender=Fem\|Number=Sing\|POS=NOUN`, `Case=Gen\|Degree=Pos\|Number=Plur\|POS=ADJ`, `POS=PRON\|PronType=Prs`, `POS=ADV\|VerbForm=Inf`, `Degree=Sup\|POS=ADJ`, `Definite=Ind\|Degree=Pos\|Gender=Neut\|POS=ADJ`, `Definite=Ind\|Gender=Masc\|POS=NOUN`, `Animacy=Hum\|Case=Nom\|Gender=Masc\|POS=PRON\|Person=3\|PronType=Prs`, `Abbr=Yes\|POS=PROPN`, `Case=Gen\|Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=VERB\|VerbForm=Part`, `Gender=Neut\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Gen\|Gender=Fem\|POS=NOUN`, `Case=Gen\|Gender=Neut\|POS=NOUN`, `Definite=Def\|POS=ADJ\|VerbForm=Part`, `POS=DET\|PronType=Dem`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Case=Gen\|Definite=Ind\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ\|VerbForm=Part`, `Case=Gen\|Definite=Def\|Gender=Fem\|Number=Plur\|POS=NOUN`, `Definite=Ind\|Number=Plur\|POS=ADJ\|VerbForm=Part`, `NumType=Card\|POS=NUM\|PronType=Dem`, `Definite=Ind\|Number=Sing\|POS=VERB\|VerbForm=Part` |
| **`parser`** | `ROOT`, `acl`, `acl:cleft`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `ccomp`, `compound`, `compound:prt`, `conj`, `cop`, `csubj`, `dep`, `det`, `discourse`, `expl`, `flat:foreign`, `flat:name`, `iobj`, `mark`, `nmod`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `orphan`, `parataxis`, `punct`, `reparandum`, `xcomp` |
| **`experimental_edit_tree_lemmatizer`** | `2`, `4`, `5`, `7`, `9`, `11`, `13`, `17`, `19`, `21`, `23`, `25`, `29`, `31`, `35`, `38`, `40`, `42`, `44`, `45`, `47`, `49`, `51`, `53`, `55`, `56`, `58`, `62`, `65`, `67`, `70`, `72`, `75`, `77`, `79`, `80`, `82`, `84`, `86`, `88`, `90`, `92`, `95`, `98`, `100`, `102`, `104`, `106`, `107`, `108`, `110`, `112`, `114`, `119`, `121`, `123`, `126`, `128`, `130`, `132`, `134`, `136`, `138`, `141`, `143`, `145`, `146`, `148`, `150`, `152`, `154`, `156`, `158`, `160`, `162`, `164`, `165`, `167`, `170`, `171`, `172`, `174`, `175`, `177`, `178`, `180`, `182`, `185`, `186`, `189`, `191`, `193`, `196`, `198`, `202`, `203`, `207`, `209`, `212`, `214`, `217`, `220`, `222`, `224`, `225`, `227`, `228`, `231`, `233`, `235`, `238`, `239`, `241`, `245`, `247`, `248`, `250`, `253`, `255`, `256`, `259`, `262`, `263`, `265`, `266`, `268`, `270`, `271`, `274`, `275`, `277`, `279`, `280`, `282`, `285`, `288`, `290`, `292`, `294`, `296`, `298`, `299`, `302`, `306`, `309`, `310`, `313`, `316`, `318`, `320`, `321`, `322`, `323`, `324`, `327`, `329`, `330`, `332`, `334`, `335`, `337`, `340`, `341`, `342`, `343`, `345`, `346`, `347`, `349`, `350`, `352`, `354`, `355`, `356`, `357`, `358`, `360`, `362`, `363`, `365`, `366`, `368`, `370`, `371`, `373`, `375`, `378`, `379`, `380`, `383`, `384`, `385`, `386`, `388`, `389`, `392`, `393`, `394`, `395`, `397`, `398`, `399`, `400`, `401`, `403`, `405`, `407`, `408`, `410`, `412`, `413`, `415`, `417`, `419`, `420`, `423`, `424`, `425`, `426`, `427`, `429`, `431`, `432`, `433`, `435`, `438`, `440`, `442`, `444`, `446`, `447`, `448`, `449`, `451`, `452`, `454`, `456`, `458`, `459`, `462`, `465`, `466`, `468`, `469`, `470`, `471`, `473`, `475`, `476`, `478`, `479`, `481`, `482`, `484`, `485`, `488`, `489`, `490`, `492`, `495`, `497`, `501`, `503`, `505`, `507`, `508`, `510`, `512`, `513`, `515`, `517`, `518`, `520`, `521`, `523`, `524`, `526`, `527`, `529`, `530`, `531`, `534`, `536`, `537`, `538`, `539`, `541`, `543`, `544`, `545`, `547`, `548`, `549`, `551`, `552`, `553`, `556`, `557`, `558`, `559`, `561`, `562`, `564`, `565`, `567`, `568`, `569`, `571`, `573`, `574`, `577`, `578`, `580`, `581`, `582`, `583`, `584`, `585`, `589`, `591`, `593`, `594`, `596`, `598`, `599`, `602`, `603`, `604`, `605`, `607`, `609`, `611`, `613`, `615`, `616`, `617`, `619`, `621`, `622`, `623`, `625`, `627`, `629`, `630`, `631`, `632`, `633`, `635`, `636`, `637`, `639`, `640`, `641`, `642`, `644`, `645`, `647`, `648`, `649`, `651`, `652`, `653`, `655`, `659`, `660`, `661`, `662`, `663`, `664`, `665`, `666`, `668`, `671`, `672`, `673`, `675`, `676`, `677`, `678`, `679`, `680`, `684`, `687`, `688`, `689`, `184`, `690`, `692`, `261`, `694`, `695`, `696`, `698`, `701`, `702`, `705`, `707`, `709`, `710`, `711`, `714`, `715`, `716`, `718`, `720`, `721`, `723`, `725`, `727`, `729`, `731`, `732`, `735`, `737`, `738`, `739`, `740`, `743`, `744`, `746`, `747`, `749`, `750`, `751`, `752`, `753`, `754`, `755`, `756`, `758`, `760`, `761`, `762`, `765`, `768`, `769`, `770`, `772`, `773`, `775`, `777`, `778`, `780`, `781`, `784`, `785`, `787`, `789`, `791`, `792`, `793`, `795`, `796`, `798`, `799`, `801`, `803`, `805`, `806`, `808`, `810`, `811`, `815`, `816`, `817`, `818`, `819`, `820`, `821`, `822`, `825`, `827`, `828`, `829`, `830`, `832`, `833`, `834`, `835`, `836`, `837`, `839`, `840`, `842`, `843`, `845`, `846`, `847`, `849`, `850`, `851`, `852`, `854`, `855`, `857`, `860`, `861`, `862`, `863`, `865`, `867`, `868`, `870`, `872`, `874`, `875`, `876`, `877`, `878`, `879`, `881`, `883`, `884`, `885`, `887`, `889`, `890`, `891`, `894`, `895`, `897`, `898`, `900`, `902`, `905`, `907`, `909`, `910`, `911`, `912`, `913`, `914`, `915`, `917`, `919`, `921`, `922`, `926`, `928`, `929`, `930`, `931`, `932`, `933`, `935`, `936`, `939`, `940`, `941`, `943`, `944`, `946`, `948`, `949`, `950`, `951`, `952`, `953`, `955`, `957`, `958`, `960`, `961`, `962`, `963`, `964`, `965`, `966`, `967`, `968`, `970`, `971`, `973`, `974`, `976`, `977`, `978`, `979`, `980`, `982`, `983`, `984`, `986`, `988`, `989`, `990`, `992`, `993`, `995`, `997`, `999`, `1000`, `1001`, `1003`, `1006`, `1007`, `1009`, `1010`, `1011`, `1012`, `1014`, `1015`, `1016`, `1019`, `1020`, `1021`, `1023`, `1024`, `1025`, `1027`, `1028`, `1030`, `1032`, `1033`, `1034`, `1036`, `1037`, `1040`, `1043`, `1044`, `1046`, `1048`, `1050`, `1051`, `1053`, `1055`, `1056`, `1057`, `1058`, `1059`, `1060`, `1061`, `1062`, `1064`, `1065`, `1067`, `1068`, `1069`, `1071`, `1072`, `1073`, `1077`, `1078`, `1079`, `1080`, `1082`, `1083`, `1084`, `1085`, `1087`, `1088`, `1090`, `1092`, `1096`, `1098`, `1100`, `1102`, `1104`, `1106`, `1107`, `1110`, `1112`, `1114`, `1116`, `1118`, `1120`, `1121`, `1124`, `1127`, `1128`, `1130`, `1131`, `1133`, `1134`, `1135`, `1138`, `1139`, `1141`, `1142`, `1143`, `1146`, `1147`, `1150`, `1151`, `1154`, `1156`, `1157`, `1158`, `1160`, `1161`, `1162`, `1163`, `1165`, `1166`, `1168`, `1170`, `1172`, `1173`, `1174`, `1175`, `1176`, `1177`, `1180`, `1183`, `1186`, `1187`, `1190`, `1192`, `1193`, `1194`, `1195`, `1198`, `1199`, `1200`, `1202`, `1205`, `1207`, `1208`, `1209`, `1210`, `1212`, `1213`, `1214`, `1215`, `1216`, `1217`, `1219`, `1220`, `1221`, `1222`, `1224`, `1225`, `1226`, `1227`, `1229`, `1231`, `1232`, `1235`, `1236`, `1239`, `1240`, `1241`, `1243`, `1244`, `1245`, `1248`, `1250`, `1251`, `1252`, `1253`, `1254`, `1255`, `1258`, `1259`, `1260`, `1261`, `1263`, `1265`, `1266`, `1267`, `1268`, `1269`, `1270`, `1271`, `1272`, `1273`, `1274`, `1275`, `1278`, `1279`, `1280`, `1281`, `1282`, `1283`, `1285`, `1286`, `1287`, `1289`, `1291`, `1293`, `1294`, `1295`, `1296`, `1298`, `1299`, `1300`, `1301`, `1302`, `1303`, `1304`, `1307`, `1308`, `1309`, `1311`, `1312`, `1315`, `1317`, `1319`, `1320`, `1322`, `1324`, `1325`, `1326`, `1327`, `1329`, `1330`, `1331`, `1332`, `1333`, `1334`, `1335`, `1337`, `1338`, `1340`, `1341`, `1342`, `1343`, `1345`, `1347`, `1348`, `1349`, `1350`, `1351`, `1353`, `1354`, `1356`, `1359`, `1360`, `1362`, `1363`, `1364`, `1365`, `1366`, `1367`, `1369`, `1370`, `1372`, `1374`, `1376`, `1377`, `1378`, `1379`, `1380`, `1382`, `1383`, `1385`, `1386`, `1390`, `1391`, `1257`, `1392`, `1393`, `1394`, `1395`, `1396`, `1397`, `1398`, `1399`, `1400`, `1402`, `1403`, `1404`, `1405`, `1408`, `1409`, `1411`, `576`, `1413`, `1414`, `1416`, `1417`, `1419`, `1420`, `1421`, `1422`, `1423`, `1426`, `1429`, `1430`, `1433`, `1435`, `1436`, `1437`, `1439`, `1441`, `1442`, `1443`, `1444`, `1445`, `1447`, `1448`, `1449`, `1451`, `1452`, `1453`, `1454`, `1456`, `1457`, `1460`, `1462`, `1463`, `1465`, `1467`, `1468`, `1469`, `1470`, `1471`, `1472`, `1474`, `1476`, `1477`, `1478`, `1479`, `1481`, `1484`, `1486`, `1489`, `1492`, `1494`, `1496`, `1498`, `1499`, `1501`, `1504`, `1505`, `1506`, `1508`, `1510`, `1511`, `1512`, `1513`, `1514`, `1517`, `1518`, `1520`, `1521`, `1522`, `1524`, `1525`, `1526`, `1528`, `1531`, `1533`, `1535`, `1536`, `1537`, `1538`, `1540`, `1543`, `1544`, `1546`, `1547`, `1549`, `1550`, `1552`, `1555`, `1558`, `1559`, `1560`, `1561`, `1563`, `1565`, `1566`, `1567`, `1570`, `1572`, `1574`, `1576`, `1578`, `1579`, `1580`, `1582`, `1585`, `1587`, `1589`, `1590`, `1591`, `1593`, `1595`, `1596`, `1597`, `1598`, `1599`, `1600`, `1601`, `1604`, `1608`, `1610`, `1611`, `1612`, `1613`, `1614`, `1616`, `1617`, `1618`, `1620`, `1621`, `1623`, `1624`, `1625`, `1626`, `1627`, `1628`, `1631`, `1632`, `1635`, `1636`, `1638`, `1639`, `1641`, `1642`, `1643`, `1644`, `1645`, `1647`, `1648`, `1651`, `1653`, `1654`, `1655`, `1657`, `1658`, `1659`, `1660`, `1661`, `1662`, `1664`, `1666`, `1669`, `1673`, `1676`, `1677`, `1679`, `1682`, `1684`, `1686`, `1689`, `1690`, `1691`, `1692`, `1694`, `1696`, `1697`, `1699`, `1701`, `1702`, `1703`, `1705`, `1706`, `1708`, `1709`, `1711`, `1712`, `1713`, `1715`, `1717`, `1718`, `1720`, `1722`, `1724`, `1725`, `1726`, `1728`, `1730`, `1732`, `1734`, `1736`, `1738`, `1741`, `1743`, `1745`, `1747`, `1748`, `1749`, `1750`, `1751`, `1753`, `1754`, `1755`, `1756`, `1757`, `1758`, `1761`, `1763`, `1765`, `1767`, `1771`, `1774`, `1777`, `1779`, `1781`, `1783`, `1785`, `1786`, `1789`, `1791`, `1792`, `1793`, `1794`, `1795`, `1797`, `1800`, `1803`, `1806`, `1808`, `1810`, `1811`, `1812`, `1813`, `1816`, `1818`, `1820`, `1821`, `1823`, `1827`, `1829`, `1831`, `1832`, `1833`, `1835`, `1837`, `1838`, `1840`, `1842`, `1843`, `1844`, `1845`, `1848`, `1849`, `1851`, `1852`, `1854`, `1855`, `1857`, `1858`, `1859`, `1861`, `1862`, `1863`, `1866`, `1868`, `1871`, `1873`, `1874`, `1875`, `1876`, `1877`, `1879`, `1882`, `1884`, `1885`, `1887`, `1889`, `1890`, `1891`, `1892`, `1894`, `1896` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_F` | 99.96 |
| `TOKEN_P` | 99.96 |
| `TOKEN_R` | 99.96 |
| `TOKEN_ACC` | 99.99 |
| `SENTS_F` | 99.10 |
| `SENTS_P` | 99.15 |
| `SENTS_R` | 99.05 |
| `TAG_ACC` | 98.33 |
| `POS_ACC` | 98.34 |
| `MORPH_ACC` | 97.91 |
| `DEP_UAS` | 94.11 |
| `DEP_LAS` | 92.14 |
| `LEMMA_ACC` | 98.28 |