---
tags:
- spacy
- token-classification
language:
- da
license: cc-by-sa-4.0
model-index:
- name: da_udv25_danishddt_trf
  results:
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9848998161
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.98480302
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9819959346
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9755129694
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.8966826762
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.8728917681
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9688888889
---
UD v2.5 benchmarking pipeline for UD_Danish-DDT

| Feature | Description |
| --- | --- |
| **Name** | `da_udv25_danishddt_trf` |
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

<summary>View label scheme (1316 labels for 6 components)</summary>

| Component | Labels |
| --- | --- |
| **`experimental_char_ner_tokenizer`** | `TOKEN` |
| **`senter`** | `I`, `S` |
| **`tagger`** | `ADJ`, `ADP`, `ADV`, `AUX`, `CCONJ`, `DET`, `INTJ`, `NOUN`, `NUM`, `PART`, `PRON`, `PROPN`, `PUNCT`, `SCONJ`, `SYM`, `VERB`, `X` |
| **`morphologizer`** | `AdpType=Prep\|POS=ADP`, `Definite=Ind\|Gender=Com\|Number=Sing\|POS=NOUN`, `Mood=Ind\|POS=AUX\|Tense=Pres\|VerbForm=Fin\|Voice=Act`, `POS=PROPN`, `Definite=Ind\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=SCONJ`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=NOUN`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Act`, `POS=ADV`, `Number=Plur\|POS=DET\|PronType=Dem`, `Degree=Pos\|Number=Plur\|POS=ADJ`, `Definite=Ind\|Gender=Com\|Number=Plur\|POS=NOUN`, `POS=PUNCT`, `POS=CCONJ`, `Definite=Ind\|Degree=Cmp\|Number=Sing\|POS=ADJ`, `Degree=Cmp\|POS=ADJ`, `POS=PRON\|PartType=Inf`, `Gender=Com\|Number=Sing\|POS=DET\|PronType=Ind`, `Definite=Ind\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Case=Acc\|Gender=Neut\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Dem`, `Degree=Pos\|POS=ADV`, `Definite=Def\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PRON\|PronType=Dem`, `NumType=Card\|POS=NUM`, `Definite=Ind\|Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Case=Acc\|Gender=Com\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Degree=Pos\|Gender=Com\|Number=Sing\|POS=ADJ`, `Case=Nom\|Gender=Com\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `NumType=Ord\|POS=ADJ`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Mood=Ind\|POS=AUX\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `POS=VERB\|VerbForm=Inf\|Voice=Act`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Act`, `POS=NOUN`, `Mood=Ind\|POS=VERB\|Tense=Pres\|VerbForm=Fin\|Voice=Pass`, `POS=ADP\|PartType=Inf`, `Degree=Pos\|POS=ADJ`, `Definite=Def\|Gender=Com\|Number=Plur\|POS=NOUN`, `Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Com\|Number=Sing\|POS=NOUN`, `POS=AUX\|VerbForm=Inf\|Voice=Act`, `Definite=Ind\|Degree=Pos\|Gender=Com\|Number=Sing\|POS=ADJ`, `Gender=Com\|Number=Sing\|POS=DET\|PronType=Dem`, `Number=Plur\|POS=DET\|PronType=Ind`, `Gender=Com\|Number=Sing\|POS=PRON\|PronType=Ind`, `Case=Acc\|POS=PRON\|Person=3\|PronType=Prs\|Reflex=Yes`, `POS=PART\|PartType=Inf`, `Gender=Neut\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Acc\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Case=Nom\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Nom\|Gender=Com\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Nom\|Gender=Com\|POS=PRON\|PronType=Ind`, `Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Ind`, `Mood=Imp\|POS=VERB`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Definite=Ind\|Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Part`, `POS=X`, `Case=Nom\|Gender=Com\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Def\|Gender=Com\|Number=Plur\|POS=NOUN`, `POS=VERB\|Tense=Pres\|VerbForm=Part`, `Number=Plur\|POS=PRON\|PronType=Int,Rel`, `POS=VERB\|VerbForm=Inf\|Voice=Pass`, `Case=Gen\|Definite=Ind\|Gender=Com\|Number=Sing\|POS=NOUN`, `Degree=Cmp\|POS=ADV`, `POS=ADV\|PartType=Inf`, `Degree=Sup\|POS=ADV`, `Number=Plur\|POS=PRON\|PronType=Dem`, `Number=Plur\|POS=PRON\|PronType=Ind`, `Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Case=Acc\|Gender=Com\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|POS=PROPN`, `POS=ADP`, `Degree=Cmp\|Number=Plur\|POS=ADJ`, `Definite=Def\|Degree=Sup\|POS=ADJ`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Degree=Pos\|Number=Sing\|POS=ADJ`, `Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Gender=Com\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Number=Plur\|POS=PRON\|PronType=Rcp`, `Case=Gen\|Degree=Cmp\|POS=ADJ`, `Case=Gen\|Definite=Def\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Number[psor]=Plur\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs`, `POS=INTJ`, `Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Degree=Pos\|Gender=Neut\|Number=Sing\|POS=ADJ`, `Gender=Neut\|Number=Sing\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Case=Acc\|Gender=Com\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Plur\|POS=NOUN`, `Number=Sing\|POS=PRON\|PronType=Int,Rel`, `Number=Plur\|Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Int,Rel`, `Definite=Def\|Degree=Sup\|Number=Plur\|POS=ADJ`, `Case=Nom\|Gender=Com\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Definite=Ind\|Number=Sing\|POS=NOUN`, `Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Plur\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `POS=SYM`, `Case=Nom\|Gender=Com\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Degree=Sup\|POS=ADJ`, `Number=Plur\|POS=DET\|PronType=Ind\|Style=Arch`, `Case=Gen\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Dem`, `Foreign=Yes\|POS=X`, `POS=DET\|Person=2\|Polite=Form\|Poss=Yes\|PronType=Prs`, `Gender=Neut\|Number=Sing\|POS=PRON\|PronType=Dem`, `Case=Acc\|Gender=Com\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Gen\|Definite=Ind\|Gender=Neut\|Number=Sing\|POS=NOUN`, `Case=Gen\|POS=PRON\|PronType=Int,Rel`, `Gender=Com\|Number=Sing\|POS=PRON\|PronType=Dem`, `Abbr=Yes\|POS=X`, `Case=Gen\|Definite=Ind\|Gender=Com\|Number=Plur\|POS=NOUN`, `Definite=Def\|Degree=Abs\|POS=ADJ`, `Definite=Ind\|Degree=Sup\|Number=Sing\|POS=ADJ`, `Definite=Ind\|POS=NOUN`, `Gender=Com\|Number=Plur\|POS=NOUN`, `Number[psor]=Plur\|POS=DET\|Person=1\|Poss=Yes\|PronType=Prs`, `Gender=Com\|POS=PRON\|PronType=Int,Rel`, `Case=Nom\|Gender=Com\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Degree=Abs\|POS=ADV`, `POS=VERB\|VerbForm=Ger`, `POS=VERB\|Tense=Past\|VerbForm=Part`, `Definite=Def\|Degree=Sup\|Number=Sing\|POS=ADJ`, `Number=Plur\|Number[psor]=Plur\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs\|Style=Form`, `Case=Gen\|Definite=Def\|Degree=Pos\|Number=Sing\|POS=ADJ`, `Case=Gen\|Degree=Pos\|Number=Plur\|POS=ADJ`, `Case=Acc\|Gender=Com\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Gender=Com\|Number=Sing\|POS=PRON\|PronType=Int,Rel`, `POS=VERB\|Tense=Pres`, `Case=Gen\|Number=Plur\|POS=DET\|PronType=Ind`, `Number[psor]=Plur\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `POS=PRON\|Person=2\|Polite=Form\|Poss=Yes\|PronType=Prs`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `POS=AUX\|Tense=Pres\|VerbForm=Part`, `Mood=Ind\|POS=VERB\|Tense=Past\|VerbForm=Fin\|Voice=Pass`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Degree=Sup\|Number=Plur\|POS=ADJ`, `Case=Acc\|Gender=Com\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Neut\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs\|Reflex=Yes`, `Definite=Ind\|Number=Plur\|POS=NOUN`, `Case=Gen\|Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Mood=Imp\|POS=AUX`, `Gender=Com\|Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `Number[psor]=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Definite=Def\|Gender=Com\|Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Part`, `Number=Plur\|Number[psor]=Sing\|POS=DET\|Person=2\|Poss=Yes\|PronType=Prs`, `Case=Gen\|Gender=Com\|Number=Sing\|POS=DET\|PronType=Ind`, `Case=Gen\|POS=NOUN`, `Number[psor]=Plur\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `POS=DET\|PronType=Dem`, `Definite=Def\|Number=Plur\|POS=NOUN` |
| **`parser`** | `ROOT`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `case`, `cc`, `ccomp`, `compound:prt`, `conj`, `cop`, `dep`, `det`, `discourse`, `expl`, `fixed`, `flat`, `goeswith`, `iobj`, `list`, `mark`, `nmod`, `nmod:poss`, `nsubj`, `nummod`, `obj`, `obl`, `obl:loc`, `obl:tmod`, `punct`, `vocative`, `xcomp` |
| **`experimental_edit_tree_lemmatizer`** | `1`, `2`, `4`, `7`, `9`, `11`, `13`, `15`, `17`, `19`, `21`, `23`, `27`, `31`, `33`, `35`, `37`, `39`, `42`, `44`, `45`, `5`, `47`, `49`, `51`, `53`, `55`, `57`, `59`, `63`, `67`, `69`, `73`, `75`, `77`, `79`, `81`, `83`, `85`, `87`, `89`, `91`, `93`, `95`, `97`, `101`, `103`, `104`, `106`, `109`, `113`, `115`, `116`, `117`, `118`, `119`, `122`, `124`, `127`, `130`, `133`, `134`, `135`, `138`, `140`, `141`, `144`, `146`, `148`, `149`, `151`, `153`, `154`, `156`, `157`, `158`, `159`, `160`, `164`, `166`, `169`, `172`, `175`, `177`, `179`, `181`, `183`, `185`, `188`, `6`, `190`, `192`, `195`, `197`, `199`, `201`, `203`, `205`, `207`, `209`, `212`, `214`, `216`, `217`, `220`, `221`, `222`, `224`, `227`, `228`, `229`, `230`, `232`, `234`, `236`, `238`, `239`, `241`, `243`, `244`, `247`, `248`, `249`, `250`, `252`, `253`, `254`, `255`, `257`, `258`, `262`, `264`, `270`, `274`, `277`, `278`, `280`, `282`, `284`, `286`, `289`, `290`, `292`, `293`, `294`, `295`, `296`, `297`, `298`, `301`, `302`, `304`, `305`, `306`, `308`, `310`, `312`, `314`, `315`, `317`, `319`, `323`, `324`, `326`, `328`, `330`, `332`, `334`, `336`, `339`, `341`, `342`, `344`, `345`, `346`, `348`, `350`, `353`, `356`, `357`, `359`, `362`, `363`, `365`, `366`, `368`, `369`, `370`, `372`, `374`, `375`, `376`, `378`, `380`, `381`, `385`, `387`, `388`, `392`, `394`, `398`, `401`, `402`, `403`, `405`, `406`, `407`, `408`, `409`, `410`, `411`, `414`, `415`, `416`, `419`, `422`, `423`, `426`, `430`, `431`, `432`, `433`, `436`, `437`, `438`, `439`, `440`, `441`, `442`, `443`, `445`, `446`, `448`, `449`, `450`, `451`, `452`, `453`, `456`, `457`, `460`, `462`, `468`, `469`, `471`, `472`, `473`, `474`, `476`, `478`, `480`, `481`, `484`, `485`, `486`, `488`, `489`, `491`, `492`, `493`, `494`, `495`, `496`, `498`, `500`, `502`, `505`, `507`, `508`, `510`, `511`, `512`, `514`, `515`, `517`, `519`, `521`, `522`, `524`, `525`, `528`, `530`, `532`, `533`, `535`, `536`, `537`, `539`, `542`, `543`, `546`, `547`, `550`, `551`, `553`, `554`, `556`, `557`, `558`, `561`, `562`, `563`, `564`, `567`, `569`, `570`, `573`, `575`, `576`, `577`, `578`, `579`, `580`, `582`, `583`, `584`, `585`, `587`, `588`, `590`, `591`, `593`, `597`, `598`, `600`, `601`, `602`, `603`, `605`, `606`, `607`, `608`, `609`, `610`, `612`, `614`, `617`, `618`, `621`, `623`, `625`, `626`, `627`, `628`, `629`, `630`, `631`, `633`, `634`, `635`, `636`, `638`, `639`, `640`, `641`, `642`, `643`, `645`, `646`, `647`, `649`, `650`, `651`, `653`, `656`, `657`, `659`, `660`, `661`, `662`, `664`, `665`, `667`, `670`, `671`, `672`, `674`, `675`, `676`, `677`, `678`, `679`, `680`, `681`, `683`, `685`, `686`, `688`, `689`, `690`, `691`, `692`, `693`, `694`, `696`, `697`, `698`, `699`, `701`, `702`, `703`, `704`, `705`, `706`, `707`, `709`, `711`, `714`, `715`, `717`, `720`, `721`, `722`, `723`, `725`, `728`, `730`, `731`, `732`, `734`, `736`, `738`, `740`, `742`, `746`, `747`, `748`, `750`, `752`, `753`, `754`, `758`, `759`, `763`, `764`, `766`, `768`, `769`, `773`, `775`, `776`, `778`, `779`, `780`, `781`, `782`, `785`, `788`, `789`, `790`, `791`, `795`, `796`, `797`, `798`, `800`, `801`, `803`, `805`, `806`, `807`, `808`, `810`, `812`, `813`, `815`, `816`, `818`, `821`, `822`, `823`, `825`, `827`, `830`, `832`, `836`, `837`, `838`, `840`, `841`, `844`, `846`, `848`, `850`, `851`, `852`, `854`, `856`, `858`, `860`, `861`, `863`, `864`, `865`, `866`, `867`, `868`, `870`, `872`, `873`, `874`, `875`, `880`, `882`, `884`, `885`, `886`, `887`, `889`, `891`, `892`, `893`, `894`, `895`, `896`, `898`, `902`, `903`, `905`, `907`, `908`, `909`, `911`, `912`, `913`, `914`, `915`, `917`, `918`, `919`, `920`, `922`, `923`, `924`, `926`, `927`, `928`, `929`, `931`, `934`, `935`, `936`, `938`, `939`, `940`, `941`, `942`, `944`, `945`, `947`, `949`, `951`, `952`, `954`, `955`, `956`, `958`, `960`, `961`, `962`, `969`, `970`, `974`, `975`, `977`, `978`, `979`, `980`, `981`, `983`, `984`, `987`, `988`, `989`, `993`, `995`, `998`, `1000`, `1001`, `1002`, `1004`, `1007`, `1011`, `1012`, `1014`, `1017`, `1018`, `1020`, `1021`, `1022`, `1023`, `1025`, `1026`, `1027`, `1029`, `1030`, `1031`, `1032`, `1033`, `1034`, `1036`, `1037`, `1038`, `1040`, `1042`, `1044`, `1045`, `1048`, `1050`, `1051`, `1053`, `1054`, `1056`, `1057`, `1058`, `1059`, `1060`, `1061`, `1062`, `1064`, `1066`, `1067`, `1069`, `1070`, `1072`, `1073`, `1076`, `1078`, `1080`, `1081`, `1085`, `1086`, `1087`, `1088`, `1089`, `1090`, `1092`, `1093`, `1094`, `1096`, `1097`, `1098`, `1100`, `1101`, `1102`, `1106`, `1109`, `1110`, `1111`, `1113`, `1114`, `1116`, `1117`, `1119`, `1120`, `1122`, `1123`, `1125`, `1127`, `1128`, `1131`, `1132`, `1133`, `1134`, `1135`, `1136`, `1137`, `1138`, `1141`, `831`, `1142`, `1143`, `1144`, `1146`, `1148`, `1150`, `1152`, `1153`, `1155`, `1157`, `1158`, `1160`, `1161`, `1162`, `1163`, `1168`, `1170`, `1171`, `1174`, `1175`, `1176`, `1178`, `1181`, `1182`, `1183`, `1185`, `1186`, `1189`, `1191`, `1192`, `1193`, `1194`, `1195`, `1196`, `1198`, `1199`, `1201`, `1203`, `1204`, `1205`, `1206`, `1207`, `1208`, `1209`, `1210`, `1211`, `1212`, `1213`, `1214`, `1215`, `1218`, `1219`, `1220`, `1222`, `1223`, `1224`, `1225`, `1226`, `1227`, `1229`, `1231`, `1232`, `1235`, `1236`, `1238`, `1239`, `1242`, `1244`, `1247`, `1248`, `1249`, `1250`, `1251`, `1253`, `1255`, `1257`, `1258`, `1259`, `1261`, `1263`, `1265`, `1266`, `1267`, `1269`, `1271`, `1272`, `1273`, `1274`, `1276`, `1277`, `1278`, `1280`, `1281`, `1282`, `1283`, `1285`, `1286`, `1287`, `1288`, `1289`, `1291`, `1293`, `1294`, `1295`, `1297`, `1298`, `1299`, `1300`, `1303`, `1305`, `1307`, `1309`, `1310`, `1311`, `1312`, `1315`, `1316`, `1318`, `1321`, `1322`, `1323`, `1324`, `1325`, `1326`, `1327`, `1329`, `1330`, `1331`, `1332`, `1333`, `1334`, `1335`, `1336`, `1337`, `1338`, `1339`, `1341`, `1342`, `1343`, `1344`, `1345`, `1346`, `1347`, `1348`, `1349`, `1351`, `1352`, `1353`, `1354`, `1355`, `1357`, `1358`, `1359`, `1360`, `1362`, `1364`, `1365`, `1367`, `1368`, `1369`, `1370`, `1371`, `1372`, `1374`, `1376`, `1377`, `1379`, `1380`, `1382`, `1383`, `1384`, `1386`, `1387`, `1389`, `1390`, `1391`, `1392`, `1394`, `1396`, `1398`, `1399`, `1400`, `1401`, `1403`, `1404`, `1405`, `1406`, `1407`, `1408`, `1409`, `1410`, `1147`, `1411`, `1413`, `1414`, `1415`, `1418`, `1420`, `1421`, `1422`, `1423`, `1426`, `1427`, `1428`, `1430`, `1431`, `1433`, `1438`, `1439`, `1440`, `1441`, `1442`, `1444`, `1446`, `1448`, `1449`, `1453`, `1454`, `1456`, `1457`, `1459`, `1463`, `1465`, `1466`, `1468`, `1469`, `1470`, `1472`, `1476`, `1478`, `1479`, `1480`, `1481`, `1482`, `1483`, `1485`, `1486`, `1487`, `1488`, `1490`, `1491`, `1493`, `1494`, `1496`, `1498`, `1500`, `1502`, `1503`, `1504`, `1505`, `1506`, `1508`, `1509`, `1511`, `1512`, `1513`, `1514`, `1516`, `1518`, `1519`, `1521`, `1522`, `1524`, `1525`, `1527`, `1533`, `1534`, `1535`, `1536`, `1538`, `1540`, `1541`, `1544`, `1545`, `1547`, `1548`, `1549`, `1550`, `1551`, `1552`, `1556`, `1557`, `1559`, `1560`, `1561`, `1562`, `1563`, `1564`, `1568`, `1569`, `1571`, `1572`, `1574`, `1577`, `1578`, `1579`, `1580`, `1581`, `1583`, `1585`, `1586`, `1587`, `1588`, `1589`, `1590`, `1591`, `1594`, `1595`, `1596`, `1597`, `1598`, `1599`, `1602`, `1603`, `1605`, `1606`, `1608`, `1610`, `1612`, `1613`, `1614`, `1616`, `1618`, `1619`, `1620`, `1621`, `1622`, `1623`, `1626`, `1627`, `1629`, `1630`, `1631`, `1632`, `1634`, `1636`, `1637`, `1638`, `1639`, `1640`, `1641`, `1642`, `1644`, `1645`, `1647`, `1649`, `1651`, `1653`, `1656`, `1657`, `1658`, `1659`, `1660`, `1661`, `1663`, `1665`, `1666`, `1667`, `1668`, `1670`, `1673`, `1674`, `1676`, `1677`, `1678`, `1679`, `1680`, `1681`, `1684`, `1685`, `1687`, `1688`, `1689`, `1690`, `1692`, `1693`, `1643`, `1694`, `1695`, `1696`, `1697`, `1699`, `1701`, `1702`, `1704`, `1706`, `1708`, `1710`, `1711`, `1712`, `1714`, `1715`, `1717`, `1719`, `1720`, `1721`, `1722`, `1723`, `1724`, `1725`, `1726`, `1727`, `1728`, `1729`, `1730`, `1732`, `1734`, `1735`, `1737`, `1739`, `1741`, `1742`, `1743`, `1745`, `1747`, `1749`, `1750`, `1751`, `1753`, `1754`, `1756`, `1758`, `1759`, `1760`, `1761`, `1762`, `1764`, `1766`, `1768`, `1769`, `1770`, `1771`, `1772`, `1773`, `1774` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_F` | 99.96 |
| `TOKEN_P` | 99.95 |
| `TOKEN_R` | 99.96 |
| `TOKEN_ACC` | 100.00 |
| `SENTS_F` | 96.89 |
| `SENTS_P` | 97.15 |
| `SENTS_R` | 96.63 |
| `TAG_ACC` | 98.49 |
| `POS_ACC` | 98.48 |
| `MORPH_ACC` | 98.20 |
| `DEP_UAS` | 89.67 |
| `DEP_LAS` | 87.29 |
| `LEMMA_ACC` | 97.55 |