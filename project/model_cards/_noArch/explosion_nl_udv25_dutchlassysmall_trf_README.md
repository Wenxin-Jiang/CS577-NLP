---
tags:
- spacy
- token-classification
language:
- nl
license: cc-by-sa-4.0
model-index:
- name: nl_udv25_dutchlassysmall_trf
  results:
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9592982456
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9636842105
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9772747214
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9670628481
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9022862512
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.8620941643
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9183673469
---
UD v2.5 benchmarking pipeline for UD_Dutch-LassySmall

| Feature | Description |
| --- | --- |
| **Name** | `nl_udv25_dutchlassysmall_trf` |
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

<summary>View label scheme (1070 labels for 6 components)</summary>

| Component | Labels |
| --- | --- |
| **`experimental_char_ner_tokenizer`** | `TOKEN` |
| **`senter`** | `I`, `S` |
| **`tagger`** | `ADJ\|nom\|basis\|met-e\|mv-n`, `ADJ\|nom\|basis\|met-e\|zonder-n\|bijz`, `ADJ\|nom\|basis\|met-e\|zonder-n\|stan`, `ADJ\|nom\|basis\|zonder\|mv-n`, `ADJ\|nom\|basis\|zonder\|zonder-n`, `ADJ\|nom\|comp\|met-e\|mv-n`, `ADJ\|nom\|sup\|met-e\|mv-n`, `ADJ\|nom\|sup\|met-e\|zonder-n\|stan`, `ADJ\|nom\|sup\|zonder\|zonder-n`, `ADJ\|postnom\|basis\|zonder`, `ADJ\|prenom\|basis\|met-e\|bijz`, `ADJ\|prenom\|basis\|met-e\|stan`, `ADJ\|prenom\|basis\|zonder`, `ADJ\|prenom\|comp\|met-e\|stan`, `ADJ\|prenom\|comp\|zonder`, `ADJ\|prenom\|sup\|met-e\|stan`, `ADJ\|vrij\|basis\|zonder`, `ADJ\|vrij\|comp\|zonder`, `ADJ\|vrij\|sup\|zonder`, `BW`, `LET`, `LID\|bep\|gen\|evmo`, `LID\|bep\|gen\|rest3`, `LID\|bep\|stan\|evon`, `LID\|bep\|stan\|rest`, `LID\|onbep\|stan\|agr`, `N\|eigen\|ev\|basis\|gen`, `N\|eigen\|ev\|basis\|genus\|stan`, `N\|eigen\|ev\|basis\|onz\|stan`, `N\|eigen\|ev\|basis\|zijd\|stan`, `N\|eigen\|ev\|dim\|onz\|stan`, `N\|eigen\|mv\|basis`, `N\|soort\|ev\|basis\|dat`, `N\|soort\|ev\|basis\|gen`, `N\|soort\|ev\|basis\|genus\|stan`, `N\|soort\|ev\|basis\|onz\|stan`, `N\|soort\|ev\|basis\|zijd\|stan`, `N\|soort\|ev\|dim\|onz\|stan`, `N\|soort\|mv\|basis`, `N\|soort\|mv\|dim`, `SPEC\|afgebr`, `SPEC\|afk`, `SPEC\|deeleigen`, `SPEC\|enof`, `SPEC\|symb`, `SPEC\|vreemd`, `TSW`, `TW\|hoofd\|nom\|mv-n\|basis`, `TW\|hoofd\|nom\|zonder-n\|basis`, `TW\|hoofd\|nom\|zonder-n\|dim`, `TW\|hoofd\|prenom\|stan`, `TW\|hoofd\|vrij`, `TW\|rang\|nom\|zonder-n`, `TW\|rang\|prenom\|stan`, `VG\|neven`, `VG\|onder`, `VNW\|aanw\|adv-pron\|obl\|vol\|3o\|getal`, `VNW\|aanw\|adv-pron\|stan\|red\|3\|getal`, `VNW\|aanw\|det\|stan\|nom\|met-e\|mv-n`, `VNW\|aanw\|det\|stan\|nom\|met-e\|zonder-n`, `VNW\|aanw\|det\|stan\|prenom\|met-e\|rest`, `VNW\|aanw\|det\|stan\|prenom\|zonder\|agr`, `VNW\|aanw\|det\|stan\|prenom\|zonder\|evon`, `VNW\|aanw\|det\|stan\|prenom\|zonder\|rest`, `VNW\|aanw\|pron\|gen\|vol\|3m\|ev`, `VNW\|aanw\|pron\|stan\|vol\|3o\|ev`, `VNW\|aanw\|pron\|stan\|vol\|3\|getal`, `VNW\|betr\|det\|stan\|nom\|zonder\|zonder-n`, `VNW\|betr\|pron\|stan\|vol\|3\|ev`, `VNW\|betr\|pron\|stan\|vol\|persoon\|getal`, `VNW\|bez\|det\|stan\|red\|3\|ev\|prenom\|zonder\|agr`, `VNW\|bez\|det\|stan\|vol\|1\|ev\|prenom\|zonder\|agr`, `VNW\|bez\|det\|stan\|vol\|1\|mv\|prenom\|met-e\|rest`, `VNW\|bez\|det\|stan\|vol\|1\|mv\|prenom\|zonder\|evon`, `VNW\|bez\|det\|stan\|vol\|2\|getal\|prenom\|zonder\|agr`, `VNW\|bez\|det\|stan\|vol\|3m\|ev\|prenom\|met-e\|rest`, `VNW\|bez\|det\|stan\|vol\|3p\|mv\|prenom\|met-e\|rest`, `VNW\|bez\|det\|stan\|vol\|3v\|ev\|prenom\|met-e\|rest`, `VNW\|bez\|det\|stan\|vol\|3\|ev\|prenom\|zonder\|agr`, `VNW\|bez\|det\|stan\|vol\|3\|mv\|prenom\|zonder\|agr`, `VNW\|onbep\|adv-pron\|obl\|vol\|3o\|getal`, `VNW\|onbep\|det\|stan\|nom\|met-e\|mv-n`, `VNW\|onbep\|det\|stan\|nom\|met-e\|zonder-n`, `VNW\|onbep\|det\|stan\|prenom\|met-e\|agr`, `VNW\|onbep\|det\|stan\|prenom\|met-e\|evz`, `VNW\|onbep\|det\|stan\|prenom\|met-e\|mv`, `VNW\|onbep\|det\|stan\|prenom\|met-e\|rest`, `VNW\|onbep\|det\|stan\|prenom\|zonder\|agr`, `VNW\|onbep\|det\|stan\|prenom\|zonder\|evon`, `VNW\|onbep\|det\|stan\|vrij\|zonder`, `VNW\|onbep\|grad\|gen\|nom\|met-e\|mv-n\|basis`, `VNW\|onbep\|grad\|stan\|nom\|met-e\|mv-n\|basis`, `VNW\|onbep\|grad\|stan\|nom\|met-e\|zonder-n\|basis`, `VNW\|onbep\|grad\|stan\|nom\|met-e\|zonder-n\|sup`, `VNW\|onbep\|grad\|stan\|prenom\|met-e\|agr\|basis`, `VNW\|onbep\|grad\|stan\|prenom\|met-e\|agr\|sup`, `VNW\|onbep\|grad\|stan\|prenom\|met-e\|mv\|basis`, `VNW\|onbep\|grad\|stan\|prenom\|zonder\|agr\|basis`, `VNW\|onbep\|grad\|stan\|prenom\|zonder\|agr\|comp`, `VNW\|onbep\|grad\|stan\|vrij\|zonder\|basis`, `VNW\|onbep\|grad\|stan\|vrij\|zonder\|comp`, `VNW\|onbep\|grad\|stan\|vrij\|zonder\|sup`, `VNW\|onbep\|pron\|stan\|vol\|3o\|ev`, `VNW\|onbep\|pron\|stan\|vol\|3p\|ev`, `VNW\|pers\|pron\|nomin\|nadr\|3v\|ev\|fem`, `VNW\|pers\|pron\|nomin\|red\|1\|mv`, `VNW\|pers\|pron\|nomin\|red\|2v\|ev`, `VNW\|pers\|pron\|nomin\|red\|3p\|ev\|masc`, `VNW\|pers\|pron\|nomin\|vol\|1\|ev`, `VNW\|pers\|pron\|nomin\|vol\|1\|mv`, `VNW\|pers\|pron\|nomin\|vol\|2b\|getal`, `VNW\|pers\|pron\|nomin\|vol\|3p\|mv`, `VNW\|pers\|pron\|nomin\|vol\|3v\|ev\|fem`, `VNW\|pers\|pron\|nomin\|vol\|3\|ev\|masc`, `VNW\|pers\|pron\|obl\|nadr\|3m\|ev\|masc`, `VNW\|pers\|pron\|obl\|vol\|3p\|mv`, `VNW\|pers\|pron\|obl\|vol\|3\|ev\|masc`, `VNW\|pers\|pron\|obl\|vol\|3\|getal\|fem`, `VNW\|pers\|pron\|stan\|red\|3\|ev\|fem`, `VNW\|pers\|pron\|stan\|red\|3\|ev\|onz`, `VNW\|pers\|pron\|stan\|red\|3\|mv`, `VNW\|pr\|pron\|obl\|red\|1\|ev`, `VNW\|pr\|pron\|obl\|red\|2v\|getal`, `VNW\|pr\|pron\|obl\|vol\|1\|ev`, `VNW\|pr\|pron\|obl\|vol\|1\|mv`, `VNW\|recip\|pron\|obl\|vol\|persoon\|mv`, `VNW\|refl\|pron\|obl\|nadr\|3\|getal`, `VNW\|refl\|pron\|obl\|red\|3\|getal`, `VNW\|vb\|adv-pron\|obl\|vol\|3o\|getal`, `VNW\|vb\|pron\|stan\|vol\|3o\|ev`, `VNW\|vb\|pron\|stan\|vol\|3p\|getal`, `VZ\|fin`, `VZ\|init`, `VZ\|versm`, `WW\|inf\|nom\|zonder\|zonder-n`, `WW\|inf\|vrij\|zonder`, `WW\|od\|nom\|met-e\|mv-n`, `WW\|od\|nom\|met-e\|zonder-n`, `WW\|od\|prenom\|met-e`, `WW\|od\|prenom\|zonder`, `WW\|od\|vrij\|zonder`, `WW\|pv\|conj\|ev`, `WW\|pv\|tgw\|ev`, `WW\|pv\|tgw\|met-t`, `WW\|pv\|tgw\|mv`, `WW\|pv\|verl\|ev`, `WW\|pv\|verl\|mv`, `WW\|vd\|nom\|met-e\|mv-n`, `WW\|vd\|nom\|met-e\|zonder-n`, `WW\|vd\|prenom\|met-e`, `WW\|vd\|prenom\|zonder`, `WW\|vd\|vrij\|zonder` |
| **`morphologizer`** | `Definite=Def\|POS=DET`, `Degree=Pos\|POS=ADJ`, `POS=CCONJ`, `Gender=Neut\|Number=Sing\|POS=NOUN`, `POS=PUNCT`, `POS=DET`, `Degree=Sup\|POS=ADJ`, `Number=Sing\|POS=AUX\|Tense=Pres\|VerbForm=Fin`, `Gender=Com\|Number=Sing\|POS=PROPN`, `POS=SYM`, `POS=NUM`, `POS=ADP`, `Definite=Ind\|POS=DET`, `Gender=Com\|Number=Sing\|POS=NOUN`, `Degree=Cmp\|POS=ADJ`, `Gender=Neut\|Number=Sing\|POS=PROPN`, `POS=ADV`, `Number=Sing\|POS=AUX\|Tense=Past\|VerbForm=Fin`, `POS=PROPN`, `Number=Plur\|POS=NOUN`, `POS=VERB\|VerbForm=Inf`, `POS=PRON\|PronType=Rel`, `Number=Sing\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `POS=PRON\|PronType=Ind`, `POS=VERB\|VerbForm=Part`, `POS=ADJ`, `POS=X`, `Gender=Com,Neut\|Number=Sing\|POS=PROPN`, `Foreign=Yes\|POS=X`, `POS=PRON\|Person=3\|PronType=Prs`, `POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `Number=Plur\|POS=PROPN`, `Number=Plur\|POS=AUX\|Tense=Past\|VerbForm=Fin`, `Number=Plur\|POS=VERB\|Tense=Pres\|VerbForm=Fin`, `Number=Sing\|POS=VERB\|Tense=Past\|VerbForm=Fin`, `POS=PRON\|Person=3\|PronType=Rel`, `POS=AUX\|VerbForm=Inf`, `POS=SCONJ`, `Number=Plur\|POS=AUX\|Tense=Pres\|VerbForm=Fin`, `Abbr=Yes\|POS=X`, `Case=Nom\|POS=PRON\|Person=3\|PronType=Prs`, `POS=PRON\|Person=3\|PronType=Dem`, `Number=Plur\|POS=VERB\|Tense=Past\|VerbForm=Fin`, `Case=Acc\|POS=PRON\|Person=3\|PronType=Prs\|Reflex=Yes`, `POS=PRON\|PronType=Dem`, `POS=PRON\|Person=3\|PronType=Int`, `Gender=Com,Neut\|Number=Sing\|POS=NOUN`, `POS=PRON\|Person=3\|PronType=Ind`, `Case=Nom\|POS=PRON\|Person=2\|PronType=Prs`, `Number=Sing\|POS=NOUN`, `Case=Acc\|POS=PRON\|PronType=Rcp`, `POS=AUX\|VerbForm=Part`, `Number=Sing\|POS=PROPN`, `Case=Nom\|POS=PRON\|Person=1\|PronType=Prs`, `Case=Acc\|POS=PRON\|Person=2\|PronType=Prs`, `Case=Acc\|POS=PRON\|Person=3\|PronType=Prs`, `POS=INTJ`, `POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `Case=Acc\|POS=PRON\|Person=1\|PronType=Prs`, `POS=PRON\|Person=2\|Poss=Yes\|PronType=Prs` |
| **`parser`** | `ROOT`, `acl`, `acl:relcl`, `advcl`, `advmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `ccomp`, `compound:prt`, `conj`, `cop`, `csubj`, `dep`, `det`, `expl`, `expl:pv`, `fixed`, `flat`, `iobj`, `mark`, `nmod`, `nmod:poss`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `obl:agent`, `orphan`, `parataxis`, `punct`, `xcomp` |
| **`experimental_edit_tree_lemmatizer`** | `1`, `3`, `4`, `6`, `8`, `10`, `13`, `15`, `17`, `19`, `21`, `22`, `25`, `27`, `29`, `30`, `32`, `36`, `37`, `39`, `41`, `42`, `45`, `47`, `49`, `51`, `53`, `55`, `58`, `59`, `61`, `63`, `65`, `66`, `70`, `72`, `74`, `76`, `78`, `79`, `80`, `82`, `84`, `86`, `89`, `92`, `94`, `96`, `97`, `99`, `101`, `104`, `107`, `109`, `110`, `112`, `114`, `116`, `117`, `118`, `119`, `120`, `121`, `124`, `126`, `127`, `130`, `133`, `134`, `135`, `137`, `139`, `142`, `143`, `145`, `148`, `152`, `154`, `156`, `159`, `160`, `163`, `165`, `167`, `168`, `172`, `175`, `176`, `178`, `182`, `184`, `187`, `189`, `190`, `192`, `194`, `195`, `197`, `199`, `200`, `203`, `205`, `207`, `208`, `209`, `212`, `214`, `215`, `217`, `219`, `220`, `221`, `224`, `227`, `228`, `230`, `232`, `233`, `237`, `238`, `240`, `241`, `242`, `244`, `245`, `248`, `249`, `250`, `251`, `252`, `255`, `258`, `259`, `260`, `262`, `266`, `268`, `270`, `272`, `275`, `278`, `280`, `281`, `282`, `283`, `285`, `287`, `290`, `291`, `293`, `297`, `299`, `300`, `301`, `302`, `306`, `307`, `309`, `310`, `311`, `313`, `314`, `316`, `318`, `319`, `320`, `324`, `329`, `332`, `333`, `335`, `337`, `339`, `343`, `346`, `347`, `348`, `352`, `353`, `357`, `358`, `359`, `360`, `362`, `363`, `366`, `369`, `372`, `374`, `377`, `378`, `379`, `381`, `382`, `386`, `387`, `391`, `395`, `397`, `399`, `400`, `401`, `403`, `406`, `407`, `408`, `409`, `410`, `411`, `412`, `414`, `415`, `417`, `419`, `421`, `423`, `426`, `427`, `428`, `431`, `433`, `435`, `437`, `439`, `441`, `444`, `446`, `448`, `451`, `453`, `455`, `457`, `458`, `460`, `462`, `463`, `465`, `467`, `469`, `470`, `472`, `474`, `475`, `478`, `482`, `483`, `485`, `489`, `491`, `492`, `493`, `495`, `499`, `500`, `502`, `506`, `508`, `511`, `514`, `518`, `520`, `522`, `525`, `527`, `528`, `532`, `534`, `535`, `538`, `540`, `541`, `544`, `546`, `547`, `548`, `551`, `552`, `556`, `558`, `559`, `560`, `563`, `565`, `567`, `569`, `570`, `573`, `577`, `579`, `581`, `584`, `587`, `589`, `591`, `595`, `597`, `599`, `600`, `601`, `602`, `606`, `608`, `610`, `612`, `614`, `615`, `616`, `618`, `619`, `620`, `621`, `622`, `626`, `628`, `629`, `631`, `632`, `634`, `635`, `636`, `637`, `639`, `641`, `644`, `649`, `653`, `654`, `656`, `657`, `658`, `661`, `663`, `664`, `665`, `666`, `667`, `668`, `669`, `670`, `674`, `676`, `678`, `679`, `682`, `685`, `687`, `689`, `692`, `694`, `696`, `699`, `702`, `703`, `704`, `705`, `706`, `708`, `709`, `711`, `712`, `714`, `715`, `717`, `718`, `719`, `722`, `725`, `729`, `730`, `733`, `736`, `738`, `739`, `743`, `745`, `746`, `749`, `750`, `328`, `752`, `754`, `755`, `757`, `760`, `761`, `762`, `764`, `767`, `769`, `770`, `773`, `777`, `778`, `781`, `783`, `784`, `785`, `786`, `789`, `790`, `793`, `794`, `795`, `798`, `800`, `162`, `803`, `806`, `809`, `812`, `813`, `815`, `817`, `818`, `819`, `821`, `823`, `824`, `825`, `827`, `830`, `832`, `834`, `836`, `838`, `648`, `839`, `841`, `843`, `844`, `846`, `848`, `849`, `851`, `852`, `853`, `854`, `855`, `857`, `859`, `860`, `861`, `863`, `865`, `867`, `869`, `872`, `873`, `875`, `877`, `879`, `881`, `883`, `885`, `886`, `887`, `888`, `890`, `893`, `894`, `896`, `899`, `901`, `902`, `904`, `906`, `908`, `911`, `913`, `915`, `918`, `919`, `920`, `921`, `926`, `928`, `930`, `931`, `932`, `933`, `934`, `396`, `935`, `936`, `938`, `939`, `940`, `942`, `945`, `946`, `947`, `948`, `950`, `951`, `954`, `956`, `957`, `960`, `962`, `964`, `967`, `969`, `970`, `971`, `975`, `976`, `977`, `978`, `979`, `980`, `981`, `982`, `983`, `984`, `985`, `988`, `990`, `991`, `995`, `997`, `998`, `840`, `999`, `1000`, `1002`, `1003`, `1004`, `1006`, `1008`, `1009`, `1013`, `1017`, `862`, `1019`, `1020`, `1021`, `1024`, `1025`, `1027`, `1028`, `1029`, `1031`, `1033`, `1036`, `1039`, `1040`, `1041`, `1043`, `1044`, `1047`, `1048`, `1052`, `1055`, `1056`, `1057`, `1061`, `1062`, `1063`, `1066`, `1069`, `507`, `1071`, `1072`, `1074`, `1075`, `1076`, `1078`, `1079`, `1080`, `1081`, `1082`, `1085`, `1086`, `1087`, `1089`, `1090`, `1091`, `1093`, `1094`, `1097`, `1100`, `1102`, `1103`, `1104`, `1106`, `1107`, `1108`, `1109`, `1111`, `1113`, `1115`, `1116`, `1119`, `1121`, `1122`, `1123`, `1125`, `1126`, `1127`, `1128`, `1129`, `1131`, `1132`, `1135`, `1138`, `1140`, `1141`, `1143`, `1144`, `1145`, `1147`, `1150`, `1151`, `1152`, `1154`, `1155`, `1158`, `1159`, `1160`, `1161`, `1162`, `1164`, `1166`, `1167`, `1169`, `1170`, `1172`, `1175`, `1177`, `510`, `1178`, `1181`, `1182`, `1183`, `1185`, `1187`, `1189`, `1190`, `1191`, `1192`, `1194`, `1197`, `1201`, `1202`, `1203`, `1206`, `1208`, `1209`, `1210`, `1213`, `1217`, `1218`, `1220`, `1221`, `1223`, `1225`, `1227`, `1229`, `1231`, `1233`, `1236`, `1238`, `1240`, `1241`, `1244`, `1245`, `1247`, `1249`, `1250`, `1252`, `1253`, `1254`, `1255`, `1257`, `1259`, `1261`, `1262`, `1264`, `1266`, `1268`, `1271`, `1273`, `1274`, `1276`, `1278`, `1279`, `48`, `1280`, `1281`, `1283`, `1248`, `1284`, `1286`, `1287`, `1289`, `1290`, `1292`, `884`, `1293`, `1295`, `1296`, `1298`, `1299`, `1300`, `1302`, `1303`, `1304`, `1305`, `1306`, `1307`, `1309`, `1311`, `1313`, `1316`, `1317`, `1318`, `1319`, `1321`, `206`, `1322`, `1323`, `1328`, `1330`, `1331`, `1332`, `1334`, `1336`, `1338`, `1341`, `1342`, `1343`, `1344`, `1345`, `1346`, `1347`, `1348`, `1350`, `1352`, `1354`, `1356`, `1357`, `1358`, `1359`, `1360`, `1361`, `864`, `1363`, `1364`, `1366`, `1367`, `1368`, `1370`, `1371`, `1372`, `1374`, `1376`, `1377`, `1378`, `1379`, `1381`, `1382`, `1383`, `1384`, `1386`, `1387`, `1389`, `1390`, `1391`, `1393`, `1396`, `1397`, `1398`, `1399`, `1403`, `1404`, `1406`, `1407`, `1410`, `1412`, `1415`, `1416`, `1419`, `1421`, `1422`, `1423`, `1424`, `1425`, `1427`, `1429`, `1432`, `1433`, `1437`, `1440`, `1442`, `1447`, `1450`, `1452`, `1454`, `1457`, `1458`, `1459`, `1460`, `1462`, `1463`, `1464`, `1466`, `1468`, `1469`, `1471`, `1473`, `1475`, `1476`, `1478`, `1479`, `1480`, `1481`, `1482`, `1483`, `1484` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_F` | 99.91 |
| `TOKEN_P` | 99.88 |
| `TOKEN_R` | 99.94 |
| `TOKEN_ACC` | 100.00 |
| `SENTS_F` | 91.84 |
| `SENTS_P` | 90.52 |
| `SENTS_R` | 93.20 |
| `TAG_ACC` | 95.93 |
| `POS_ACC` | 96.37 |
| `MORPH_ACC` | 97.73 |
| `DEP_UAS` | 90.23 |
| `DEP_LAS` | 86.21 |
| `LEMMA_ACC` | 96.71 |