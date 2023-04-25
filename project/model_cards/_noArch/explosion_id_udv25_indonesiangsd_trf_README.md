---
tags:
- spacy
- token-classification
language:
- id
license: cc-by-sa-4.0
model-index:
- name: id_udv25_indonesiangsd_trf
  results:
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9479067555
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9316523945
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9590072946
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9804947669
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.8615977082
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.7838256704
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.9297777778
---
UD v2.5 benchmarking pipeline for UD_Indonesian-GSD

| Feature | Description |
| --- | --- |
| **Name** | `id_udv25_indonesiangsd_trf` |
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

<summary>View label scheme (1325 labels for 6 components)</summary>

| Component | Labels |
| --- | --- |
| **`experimental_char_ner_tokenizer`** | `TOKEN` |
| **`senter`** | `I`, `S` |
| **`tagger`** | `APP`, `ASP`, `ASP+PS2`, `ASP+PS3`, `ASP+T--`, `ASS`, `ASS+PS3`, `B--`, `B--+PS3`, `B--+T--`, `CC-`, `CC-+PS3`, `CC-+T--`, `CD-`, `CD-+PS3`, `CO-`, `CO-+PS3`, `D--`, `D--+PS2`, `D--+PS3`, `D--+T--`, `F--`, `F--+PS1`, `F--+PS2`, `F--+PS3`, `F--+T--`, `G--`, `G--+PS3`, `G--+T--`, `H--`, `H--+T--`, `I--`, `M--`, `M--+PS3`, `M--+T--`, `NOUN`, `NPD`, `NPD+PS2`, `NPD+PS3`, `NSD`, `NSD+PS1`, `NSD+PS2`, `NSD+PS3`, `NSD+T--`, `NSF`, `NSM`, `NSM+PS3`, `NUM`, `O--`, `PP1`, `PP1+T--`, `PP2`, `PP3`, `PP3+T--`, `PROPN`, `PS1`, `PS1+VSA`, `PS1+VSA+T--`, `PS2`, `PS2+VSA`, `PS3`, `PUNCT`, `R--`, `R--+PS1`, `R--+PS2`, `R--+PS3`, `S--`, `S--+PS3`, `T--`, `VERB`, `VPA`, `VSA`, `VSA+PS1`, `VSA+PS2`, `VSA+PS3`, `VSA+T--`, `VSP`, `VSP+PS3`, `VSP+T--`, `W--`, `W--+T--`, `X`, `X--`, `Z--` |
| **`morphologizer`** | `POS=PROPN`, `POS=AUX`, `POS=DET\|PronType=Ind`, `Number=Sing\|POS=NOUN`, `POS=PRON\|PronType=Rel`, `Number=Sing\|POS=VERB\|Voice=Pass`, `POS=ADP`, `POS=PUNCT`, `Number=Sing\|POS=PROPN`, `POS=NOUN`, `POS=ADV`, `POS=CCONJ`, `Number=Sing\|POS=VERB\|Voice=Act`, `POS=VERB`, `POS=DET\|PronType=Tot`, `Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=3`, `POS=SCONJ`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `POS=DET\|PronType=Dem`, `NumType=Card\|POS=NUM`, `Degree=Pos\|Number=Sing\|POS=NOUN`, `Degree=Pos\|Number=Sing\|POS=ADJ`, `NumType=Card\|POS=DET\|PronType=Ind`, `Degree=Pos\|Number=Sing\|POS=ADP`, `Number[psor]=Sing\|POS=NOUN\|Person[psor]=3`, `Number=Sing\|POS=VERB`, `POS=PRON\|PronType=Int`, `Number=Sing\|POS=ADV\|Voice=Act`, `Number=Sing\|Number[psor]=Sing\|POS=VERB\|Person[psor]=3\|Voice=Act`, `Number=Sing\|POS=ADP\|Voice=Act`, `POS=ADJ`, `Number[psor]=Sing\|POS=ADP\|Person[psor]=3`, `Degree=Pos\|Number=Sing\|POS=DET`, `Degree=Pos\|Number=Sing\|POS=VERB`, `POS=PRON\|PronType=Dem`, `POS=PART\|Polarity=Neg`, `Degree=Pos\|Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=3`, `Number=Sing\|POS=PRON\|Person=1\|Polite=Form\|PronType=Prs`, `Number=Sing\|POS=ADJ`, `Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `POS=SYM`, `POS=ADV\|PronType=Int`, `Clusivity=In\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Number=Sing\|POS=ADJ\|Voice=Act`, `Degree=Pos\|Number=Sing\|POS=PROPN`, `Degree=Pos\|Number=Sing\|POS=ADV`, `Number=Sing\|Number[psor]=Sing\|POS=VERB\|Person[psor]=3\|Voice=Pass`, `Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=3\|Voice=Act`, `Number=Sing\|POS=PROPN\|Voice=Act`, `Number=Sing\|POS=NOUN\|Voice=Act`, `POS=DET`, `Number=Sing\|POS=DET\|Voice=Act`, `NumType=Card\|POS=PRON\|PronType=Ind`, `Number=Sing\|Number[psor]=Sing\|POS=ADV\|Person[psor]=3`, `Number=Sing\|POS=DET`, `Number=Sing\|POS=ADJ\|Voice=Pass`, `POS=CCONJ\|PronType=Dem`, `Number=Sing\|POS=ADP`, `Number=Sing\|POS=ADV`, `Number=Sing\|POS=PRON\|Person=2\|Polite=Infm\|PronType=Prs`, `Number[psor]=Sing\|POS=NOUN\|Person[psor]=2`, `Number=Plur\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=2`, `Number=Sing\|POS=PRON`, `POS=PRON`, `NumType=Card\|POS=ADV\|PronType=Ind`, `NumType=Card\|Number[psor]=Sing\|POS=NUM\|Person[psor]=3`, `Number=Sing\|POS=PRON\|Person=3\|Polite=Form\|PronType=Prs`, `POS=DET\|PronType=Int`, `Number=Sing\|Number[psor]=Sing\|POS=PROPN\|Person[psor]=3`, `Number=Sing\|Number[psor]=Sing\|POS=PROPN\|Person[psor]=1`, `Degree=Pos\|Number=Sing\|POS=SCONJ`, `POS=PRON\|PronType=Ind`, `Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=3\|Voice=Pass`, `POS=VERB\|PronType=Ind`, `Degree=Pos\|Number=Sing\|Number[psor]=Sing\|POS=ADJ\|Person[psor]=3`, `Number=Sing\|POS=SCONJ`, `Degree=Sup\|Number=Sing\|Number[psor]=Sing\|POS=ADJ\|Person[psor]=3`, `Degree=Pos\|Number=Sing\|Number[psor]=Sing\|POS=ADP\|Person[psor]=3`, `Number=Plur\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=3`, `Number=Plur\|POS=NOUN`, `POS=ADV\|PronType=Dem`, `Number=Sing\|POS=VERB\|Person=1\|Voice=Act`, `Degree=Sup\|Number=Sing\|POS=ADJ`, `Number=Sing\|POS=ADP\|Voice=Pass`, `Number[psor]=Sing\|POS=PART\|Person[psor]=3`, `Number=Sing\|POS=NOUN\|Voice=Pass`, `Degree=Pos\|Number=Sing\|Number[psor]=Sing\|POS=CCONJ\|Person[psor]=3`, `POS=PART`, `Number=Sing\|Number[psor]=Sing\|POS=PART\|Person[psor]=3\|Voice=Pass`, `Degree=Sup\|Number=Sing\|POS=ADV`, `Number=Sing\|POS=PRON\|Voice=Act`, `Number=Sing\|Number[psor]=Sing\|POS=PROPN\|Person[psor]=3\|Voice=Act`, `Gender=Masc\|Number=Sing\|POS=PROPN`, `Number[psor]=Sing\|POS=PRON\|Person[psor]=3\|PronType=Tot`, `Degree=Pos\|Number=Sing\|POS=X`, `POS=PRON\|PronType=Tot`, `Degree=Pos\|Number=Sing\|Number[psor]=Sing\|POS=ADV\|Person[psor]=3`, `Degree=Pos\|Number=Sing\|Number[psor]=Sing\|POS=VERB\|Person[psor]=3`, `Number=Sing\|Number[psor]=Sing\|POS=ADP\|Person[psor]=3`, `Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=2`, `POS=SCONJ\|PronType=Int`, `Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Number=Sing\|Number[psor]=Sing\|POS=VERB\|Person[psor]=1\|Voice=Act`, `Number[psor]=Sing\|POS=DET\|Person[psor]=3`, `Number=Sing\|Number[psor]=Sing\|POS=PRON\|Person[psor]=3`, `Clusivity=Ex\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `Number=Plur\|POS=VERB\|Voice=Act`, `Number=Sing\|Number[psor]=Sing\|POS=ADV\|Person[psor]=3\|Voice=Act`, `Degree=Pos\|Number=Sing\|POS=NOUN\|Polarity=Neg`, `POS=X`, `Number[psor]=Sing\|POS=ADJ\|Person[psor]=3`, `Number=Sing\|Number[psor]=Sing\|POS=VERB\|Person[psor]=3`, `Number=Sing\|POS=PRON\|Person=2\|Polite=Form\|PronType=Prs`, `Number=Sing\|POS=PRON\|Person=1\|Polite=Infm\|PronType=Prs`, `Number=Sing\|POS=PROPN\|Voice=Pass`, `POS=ADV\|Polarity=Neg`, `NumType=Card\|Number=Sing\|POS=NUM`, `Number[psor]=Sing\|POS=ADV\|Person[psor]=2`, `Number[psor]=Sing\|POS=ADV\|Person[psor]=3`, `Degree=Sup\|Number=Sing\|POS=PROPN`, `POS=PROPN\|Polarity=Neg`, `Number=Sing\|Number[psor]=Sing\|POS=VERB\|Person[psor]=2\|Voice=Act`, `Number=Sing\|POS=PROPN\|Person=1\|Voice=Act`, `POS=SCONJ\|PronType=Dem`, `Number=Sing\|Number[psor]=Sing\|POS=ADV\|Person[psor]=2\|Voice=Act`, `Number=Sing\|POS=CCONJ`, `Degree=Sup\|Number=Sing\|POS=VERB`, `Number=Sing\|Number[psor]=Sing\|POS=ADJ\|Person[psor]=3`, `Number=Sing\|Number[psor]=Sing\|POS=ADJ\|Person[psor]=3\|Voice=Act`, `Degree=Pos\|Number=Sing\|POS=PRON`, `Number=Sing\|POS=ADV\|Voice=Pass`, `Number[psor]=Sing\|POS=ADP\|Person[psor]=2`, `Number=Sing\|POS=SYM`, `POS=ADJ\|Polarity=Neg`, `Degree=Pos\|NumType=Card\|Number=Sing\|POS=NUM`, `Number=Sing\|Number[psor]=Sing\|POS=SCONJ\|Person[psor]=3`, `Degree=Pos\|Number=Sing\|POS=CCONJ`, `Number[psor]=Sing\|POS=NOUN\|Person[psor]=1`, `Number=Sing\|POS=CCONJ\|Voice=Act`, `Gender=Masc\|Number=Sing\|POS=NOUN`, `Number=Sing\|Number[psor]=Sing\|POS=ADP\|Person[psor]=3\|Voice=Pass`, `Gender=Fem\|Number=Sing\|POS=PROPN`, `POS=VERB\|PronType=Dem`, `Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Gender=Masc\|Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=3`, `Number=Sing\|POS=PART\|Voice=Act`, `Degree=Sup\|Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=3`, `POS=ADP\|PronType=Int`, `Number[psor]=Sing\|POS=VERB\|Person[psor]=3`, `Number[psor]=Sing\|POS=PRON\|Person[psor]=3\|PronType=Rel`, `Degree=Pos\|Number=Sing\|POS=AUX`, `Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=1`, `Number=Sing\|POS=SCONJ\|Voice=Pass`, `Degree=Sup\|Number=Sing\|POS=ADP`, `Number=Sing\|POS=SCONJ\|Voice=Act`, `NumType=Card\|POS=DET\|PronType=Int`, `Degree=Pos\|Number=Sing\|POS=PART\|Polarity=Neg`, `Degree=Sup\|Number=Sing\|POS=SCONJ`, `Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=1\|Voice=Act`, `Number=Plur\|POS=ADJ`, `POS=VERB\|PronType=Int`, `Number=Sing\|POS=VERB\|Person=2\|Voice=Act`, `Degree=Pos\|Number=Sing\|Number[psor]=Sing\|POS=ADJ\|Person[psor]=2`, `Gender=Masc\|Number=Sing\|POS=ADJ`, `Number[psor]=Sing\|POS=ADV\|Person[psor]=3\|PronType=Tot`, `POS=DET\|PronType=Rel`, `Number=Sing\|POS=NOUN\|Polarity=Neg`, `Number=Sing\|Number[psor]=Sing\|POS=PROPN\|Person[psor]=2`, `NumType=Card\|Number=Sing\|POS=NUM\|Voice=Act`, `Degree=Pos\|Number=Plur\|POS=ADJ`, `Number[psor]=Sing\|POS=DET\|Person[psor]=3\|PronType=Tot`, `Number[psor]=Sing\|POS=PROPN\|Person[psor]=1`, `Gender=Fem\|Number=Sing\|POS=NOUN`, `Number=Sing\|POS=VERB\|Person=1`, `Degree=Pos\|Number=Sing\|Number[psor]=Sing\|POS=PROPN\|Person[psor]=3`, `NumType=Card\|Number[psor]=Sing\|POS=DET\|Person[psor]=3\|PronType=Ind`, `POS=ADV\|PronType=Tot`, `Degree=Pos\|Number=Plur\|POS=ADV`, `Number=Plur\|POS=ADV\|Voice=Act`, `POS=CCONJ\|PronType=Int`, `Degree=Pos\|Number=Sing\|POS=PART`, `Number[psor]=Sing\|POS=PRON\|Person[psor]=2`, `Number=Plur\|POS=VERB`, `Number=Sing\|Number[psor]=Sing\|POS=ADJ\|Person[psor]=3\|Voice=Pass`, `Degree=Pos\|Number=Sing\|POS=PUNCT`, `Number[psor]=Sing\|POS=ADP\|Person[psor]=1`, `Degree=Sup\|Number=Sing\|POS=NOUN`, `Number[psor]=Sing\|POS=PART\|Person[psor]=3\|Polarity=Neg`, `Number=Sing\|Number[psor]=Sing\|POS=ADP\|Person[psor]=3\|Voice=Act`, `POS=NOUN\|Polarity=Neg`, `Number[psor]=Sing\|POS=PROPN\|Person[psor]=2`, `Number=Sing\|Number[psor]=Sing\|POS=NOUN\|Person[psor]=2\|Voice=Act` |
| **`parser`** | `ROOT`, `acl`, `advcl`, `advmod`, `amod`, `appos`, `case`, `cc`, `ccomp`, `compound`, `compound:plur`, `conj`, `cop`, `csubj`, `csubj:pass`, `dep`, `det`, `fixed`, `flat`, `iobj`, `mark`, `nmod`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `parataxis`, `punct`, `xcomp` |
| **`experimental_edit_tree_lemmatizer`** | `1`, `2`, `4`, `6`, `8`, `10`, `12`, `15`, `19`, `22`, `24`, `26`, `27`, `29`, `30`, `31`, `34`, `36`, `37`, `40`, `42`, `44`, `46`, `48`, `50`, `51`, `53`, `54`, `56`, `58`, `47`, `59`, `62`, `64`, `66`, `68`, `70`, `71`, `3`, `72`, `74`, `75`, `77`, `78`, `79`, `81`, `84`, `86`, `87`, `88`, `89`, `92`, `11`, `93`, `95`, `96`, `97`, `98`, `99`, `101`, `103`, `105`, `106`, `107`, `108`, `110`, `111`, `113`, `115`, `116`, `118`, `120`, `122`, `123`, `124`, `125`, `126`, `127`, `128`, `130`, `131`, `132`, `134`, `135`, `137`, `140`, `142`, `143`, `144`, `146`, `147`, `148`, `149`, `150`, `151`, `152`, `153`, `43`, `155`, `157`, `158`, `160`, `161`, `162`, `163`, `164`, `165`, `166`, `167`, `168`, `170`, `171`, `172`, `174`, `175`, `177`, `178`, `179`, `180`, `181`, `182`, `183`, `25`, `184`, `185`, `186`, `187`, `188`, `190`, `192`, `193`, `194`, `196`, `57`, `197`, `198`, `199`, `201`, `203`, `204`, `206`, `207`, `208`, `209`, `210`, `211`, `212`, `213`, `214`, `215`, `217`, `218`, `219`, `220`, `221`, `223`, `225`, `227`, `228`, `230`, `232`, `234`, `236`, `237`, `238`, `240`, `242`, `243`, `244`, `246`, `247`, `248`, `249`, `250`, `251`, `252`, `253`, `254`, `256`, `257`, `258`, `260`, `261`, `262`, `263`, `264`, `266`, `267`, `268`, `269`, `270`, `272`, `41`, `273`, `274`, `275`, `276`, `277`, `278`, `280`, `281`, `282`, `283`, `284`, `285`, `286`, `287`, `288`, `289`, `290`, `291`, `292`, `293`, `294`, `295`, `297`, `298`, `299`, `300`, `301`, `302`, `303`, `304`, `306`, `307`, `308`, `309`, `310`, `312`, `313`, `314`, `317`, `315`, `318`, `320`, `321`, `322`, `323`, `324`, `9`, `325`, `326`, `327`, `329`, `330`, `331`, `332`, `333`, `334`, `336`, `337`, `339`, `341`, `342`, `343`, `345`, `346`, `347`, `348`, `80`, `241`, `349`, `350`, `351`, `353`, `354`, `355`, `356`, `357`, `358`, `359`, `360`, `361`, `363`, `49`, `364`, `365`, `366`, `23`, `367`, `368`, `369`, `370`, `371`, `372`, `373`, `374`, `375`, `376`, `378`, `379`, `380`, `381`, `382`, `383`, `385`, `386`, `387`, `388`, `389`, `390`, `391`, `393`, `394`, `45`, `35`, `395`, `396`, `63`, `397`, `398`, `399`, `400`, `401`, `402`, `403`, `404`, `405`, `406`, `407`, `408`, `409`, `410`, `412`, `413`, `415`, `416`, `417`, `419`, `421`, `422`, `173`, `28`, `424`, `425`, `426`, `427`, `428`, `429`, `430`, `431`, `432`, `434`, `435`, `437`, `439`, `440`, `441`, `442`, `443`, `444`, `445`, `446`, `447`, `448`, `450`, `451`, `453`, `454`, `455`, `457`, `459`, `461`, `463`, `464`, `465`, `466`, `467`, `469`, `470`, `0`, `471`, `472`, `473`, `474`, `475`, `477`, `478`, `479`, `480`, `481`, `482`, `483`, `484`, `485`, `486`, `487`, `489`, `490`, `491`, `493`, `495`, `496`, `497`, `498`, `499`, `500`, `501`, `502`, `503`, `504`, `52`, `506`, `507`, `508`, `509`, `510`, `511`, `512`, `514`, `515`, `516`, `519`, `520`, `67`, `522`, `523`, `525`, `526`, `527`, `528`, `529`, `530`, `531`, `533`, `534`, `535`, `536`, `537`, `538`, `539`, `540`, `541`, `542`, `543`, `544`, `545`, `546`, `548`, `549`, `551`, `553`, `554`, `555`, `556`, `557`, `559`, `560`, `561`, `562`, `563`, `564`, `565`, `566`, `568`, `569`, `570`, `571`, `572`, `573`, `575`, `576`, `577`, `578`, `579`, `513`, `580`, `582`, `583`, `584`, `586`, `587`, `588`, `589`, `591`, `592`, `593`, `594`, `595`, `597`, `599`, `600`, `602`, `607`, `608`, `609`, `610`, `611`, `612`, `613`, `614`, `615`, `616`, `617`, `618`, `619`, `620`, `621`, `623`, `625`, `626`, `627`, `628`, `629`, `630`, `631`, `632`, `633`, `634`, `635`, `636`, `637`, `638`, `639`, `640`, `641`, `642`, `644`, `645`, `646`, `647`, `648`, `649`, `651`, `652`, `653`, `655`, `656`, `657`, `658`, `659`, `660`, `661`, `662`, `664`, `665`, `666`, `667`, `668`, `669`, `670`, `672`, `674`, `675`, `676`, `677`, `169`, `678`, `679`, `680`, `681`, `682`, `683`, `684`, `685`, `686`, `687`, `688`, `689`, `690`, `7`, `691`, `692`, `693`, `694`, `695`, `696`, `697`, `698`, `699`, `701`, `702`, `703`, `704`, `705`, `706`, `708`, `709`, `710`, `711`, `712`, `713`, `715`, `717`, `719`, `720`, `721`, `722`, `723`, `724`, `725`, `726`, `727`, `728`, `729`, `730`, `731`, `732`, `733`, `735`, `736`, `737`, `738`, `740`, `741`, `742`, `743`, `744`, `745`, `746`, `747`, `748`, `749`, `750`, `752`, `753`, `754`, `755`, `756`, `757`, `758`, `760`, `761`, `763`, `764`, `765`, `766`, `767`, `768`, `769`, `770`, `771`, `772`, `773`, `774`, `775`, `776`, `65`, `777`, `778`, `779`, `780`, `781`, `782`, `783`, `784`, `785`, `786`, `788`, `790`, `791`, `792`, `793`, `794`, `795`, `796`, `797`, `798`, `799`, `145`, `800`, `801`, `802`, `803`, `804`, `805`, `806`, `807`, `808`, `809`, `810`, `811`, `812`, `813`, `815`, `817`, `818`, `819`, `820`, `821`, `822`, `823`, `824`, `826`, `829`, `830`, `831`, `832`, `833`, `834`, `835`, `836`, `837`, `838`, `839`, `840`, `841`, `843`, `845`, `847`, `849`, `850`, `851`, `852`, `853`, `854`, `855`, `856`, `857`, `858`, `5`, `859`, `860`, `861`, `862`, `863`, `864`, `865`, `866`, `867`, `868`, `869`, `871`, `872`, `873`, `874`, `875`, `876`, `877`, `878`, `879`, `880`, `881`, `882`, `884`, `885`, `887`, `888`, `889`, `891`, `892`, `893`, `894`, `896`, `897`, `898`, `899`, `900`, `901`, `902`, `903`, `904`, `905`, `906`, `907`, `908`, `69`, `909`, `910`, `912`, `913`, `914`, `915`, `916`, `917`, `919`, `920`, `921`, `922`, `923`, `924`, `925`, `926`, `927`, `929`, `229`, `930`, `931`, `932`, `933`, `934`, `935`, `936`, `937`, `938`, `939`, `940`, `941`, `942`, `944`, `945`, `946`, `947`, `948`, `949`, `950`, `951`, `953`, `954`, `955`, `956`, `957`, `958`, `959`, `960`, `962`, `963`, `964`, `965`, `967`, `968`, `969`, `970`, `971`, `972`, `973`, `974`, `976`, `977`, `978`, `979`, `980`, `981`, `982`, `983`, `984`, `986`, `987`, `988`, `990`, `993`, `994`, `995`, `996`, `997`, `998`, `999`, `1000`, `1001`, `1002`, `1003`, `1004`, `1005`, `1006`, `1007`, `1008`, `1009`, `1012`, `1014`, `1015`, `1016`, `1019`, `1020`, `1021`, `1022`, `1023`, `1024`, `1025`, `1026`, `1027`, `1028`, `1029`, `1030`, `1031`, `1032`, `1033`, `1034`, `1035`, `1036`, `1037`, `1038`, `1039`, `1040`, `1041`, `1042`, `1043`, `1044`, `1045`, `1046`, `1047`, `1048`, `1049`, `1051`, `1052`, `1053`, `1054`, `1055`, `1056`, `1057`, `1058`, `1059`, `1060`, `1062`, `1063`, `1064`, `1065`, `1066`, `1068`, `1069`, `1070`, `1072`, `1074`, `1075`, `1076`, `1077`, `1078`, `1079`, `1080`, `1082`, `1083`, `1085`, `1086`, `1087`, `1088`, `1090`, `1091`, `1092`, `1093`, `1094`, `1095`, `1096`, `1097`, `1098`, `1099`, `1100`, `1101`, `673`, `1102`, `1103`, `1104`, `1106`, `1108`, `1109`, `1110`, `1111`, `1115`, `1116`, `1119`, `1120`, `1089`, `418`, `1121`, `1122`, `1123`, `1124`, `1125`, `1126`, `1127`, `1128`, `1129`, `1130`, `1131`, `1132`, `1134`, `1136`, `1137`, `1138`, `1139`, `1140`, `1141`, `1133`, `1142`, `1143`, `1144`, `1145`, `1146`, `1147`, `1148`, `1149`, `1150`, `1151`, `1153`, `1154`, `1156`, `1157`, `1158`, `1159`, `1160`, `1162`, `1164`, `1165`, `377`, `1166`, `1167`, `1168`, `1169`, `1170`, `1171`, `1172`, `1173`, `1174`, `1175`, `1176`, `1177`, `1179`, `1180`, `1181`, `1182`, `191`, `1183`, `1184`, `1185`, `1186`, `1187`, `1188`, `1190`, `1191`, `1192`, `1194`, `1195`, `1196`, `1197`, `1198`, `1199`, `1200`, `1201` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_F` | 99.99 |
| `TOKEN_P` | 99.98 |
| `TOKEN_R` | 99.99 |
| `TOKEN_ACC` | 100.00 |
| `SENTS_F` | 92.98 |
| `SENTS_P` | 92.40 |
| `SENTS_R` | 93.56 |
| `TAG_ACC` | 94.79 |
| `POS_ACC` | 93.17 |
| `MORPH_ACC` | 95.90 |
| `DEP_UAS` | 86.16 |
| `DEP_LAS` | 78.38 |
| `LEMMA_ACC` | 98.05 |