---
tags:
- spacy
- token-classification
language:
- af
license: cc-by-sa-4.0
model-index:
- name: af_udv25_afrikaansafribooms_trf
  results:
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9601278917
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9852374236
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9751739703
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9786593964
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.9078427294
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.8749739963
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 1.0
---
UD v2.5 benchmarking pipeline for UD_Afrikaans-AfriBooms

| Feature | Description |
| --- | --- |
| **Name** | `af_udv25_afrikaansafribooms_trf` |
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

<summary>View label scheme (455 labels for 6 components)</summary>

| Component | Labels |
| --- | --- |
| **`experimental_char_ner_tokenizer`** | `TOKEN` |
| **`senter`** | `I`, `S` |
| **`tagger`** | `AOA`, `AOP`, `ASA`, `ASP`, `AVA`, `AVP`, `BO`, `BS`, `BV`, `KN`, `KO`, `LB`, `LO`, `NA`, `NEE`, `NM`, `NME`, `NSE`, `NSED`, `NSM`, `PA`, `PB`, `PDHEB`, `PDHEDP`, `PDHENP`, `PDHEW`, `PDMB`, `PDMP`, `PDMW`, `PDOENP`, `PDOEW`, `PDVEB`, `PDVEDP`, `PDVENP`, `PDVEW`, `PEEB`, `PEEDP`, `PEENP`, `PEMB`, `PEMP`, `PEMW`, `PO`, `PTEB`, `PTEDP`, `PTENP`, `PTEW`, `PTMP`, `PV`, `PW`, `RA`, `RK`, `RL`, `RO`, `RS`, `RSF`, `RV`, `RWD`, `SVS`, `THAB`, `THAO`, `THBB`, `THBO`, `THNB`, `THPB`, `THPO`, `TRAB`, `TRAO`, `TRBB`, `UPB`, `UPD`, `UPI`, `UPO`, `UPS`, `UPV`, `UPW`, `UXD`, `VTHOG`, `VTHOK`, `VTHOO`, `VTHOV`, `VTHSG`, `VTHSO`, `VTUOA`, `VTUOM`, `VTUOP`, `VUOT`, `VVHOG`, `VVHOK`, `VVHOO`, `VVUOM`, `VVUOP`, `ZE`, `ZM`, `ZPL`, `ZPR` |
| **`morphologizer`** | `Definite=Def\|POS=DET\|PronType=Art`, `Number=Sing\|POS=NOUN`, `AdpType=Prep\|POS=ADP`, `AdjType=Attr\|Case=Nom\|Degree=Pos\|POS=ADJ`, `Number=Plur\|POS=NOUN`, `POS=AUX\|Tense=Pres\|VerbForm=Fin,Inf\|VerbType=Cop`, `Definite=Ind\|POS=DET\|PronType=Art`, `POS=NUM`, `POS=PART\|PartType=Inf`, `POS=VERB\|Subcat=Tran\|Tense=Pres\|VerbForm=Fin,Inf`, `POS=PRON\|PronType=Rel`, `POS=AUX\|Tense=Pres\|VerbForm=Fin,Inf\|VerbType=Pas`, `POS=PUNCT`, `POS=CCONJ`, `POS=SCONJ`, `POS=VERB\|Subcat=Intr\|Tense=Pres\|VerbForm=Fin,Inf`, `POS=VERB\|Subcat=Intr\|Tense=Past\|VerbForm=Part`, `POS=AUX\|Tense=Past\|VerbForm=Fin\|VerbType=Pas`, `Degree=Pos\|POS=ADV`, `POS=AUX\|Tense=Pres\|VerbForm=Fin,Inf\|VerbType=Mod`, `POS=DET\|PronType=Ind`, `POS=X`, `Number=Sing\|POS=PROPN`, `POS=PRON\|PronType=Ind`, `POS=PART\|PartType=Neg`, `POS=VERB\|Subcat=Tran\|Tense=Past\|VerbForm=Part`, `AdjType=Pred\|Case=Nom\|Degree=Pos\|POS=ADJ`, `POS=DET\|PronType=Dem`, `Degree=Cmp\|POS=ADV`, `Case=Nom\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `POS=SYM`, `Case=Acc,Nom\|Number=Plur\|POS=PRON\|Person=1\|PronType=Prs`, `POS=PART\|PartType=Gen`, `Case=Acc\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `Number=Sing\|POS=PRON\|Person=2\|PronType=Prs\|Reflex=Yes`, `Degree=Sup\|POS=ADV`, `Degree=Dim\|Number=Sing\|POS=NOUN`, `Number=Sing\|POS=PRON\|Person=2\|Poss=Yes\|PronType=Prs`, `POS=PRON\|PronType=Int`, `Number=Plur\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `Number=Sing\|POS=PRON\|Person=3\|PronType=Prs\|Reflex=Yes`, `Number=Plur\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `AdjType=Attr\|Case=Nom\|Degree=Sup\|POS=ADJ`, `Case=Nom\|Number=Sing\|POS=PRON\|Person=2\|PronType=Prs`, `AdjType=Pred\|Case=Nom\|Degree=Cmp\|POS=ADJ`, `POS=VERB\|Subcat=Prep\|Tense=Pres\|VerbForm=Fin,Inf`, `POS=AUX\|Tense=Pres\|VerbForm=Fin,Inf\|VerbType=Aux`, `Number=Sing\|POS=PRON\|Person=3\|Poss=Yes\|PronType=Prs`, `POS=PRON\|PronType=Rcp`, `POS=AUX\|Tense=Past\|VerbForm=Fin\|VerbType=Mod`, `Case=Acc,Nom\|Number=Plur\|POS=PRON\|Person=3\|PronType=Prs`, `POS=AUX\|Tense=Past\|VerbForm=Fin\|VerbType=Cop`, `Case=Acc\|Number=Sing\|POS=PRON\|Person=3\|PronType=Prs`, `Case=Nom\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `Number=Sing\|POS=PRON\|Person=1\|Poss=Yes\|PronType=Prs`, `Case=Acc,Nom\|Number=Plur\|POS=PRON\|Person=2\|PronType=Prs`, `Number=Plur\|POS=PRON\|Person=3\|PronType=Prs\|Reflex=Yes`, `AdjType=Attr\|Case=Nom\|Degree=Cmp\|POS=ADJ`, `Number=Plur\|POS=PRON\|Person=1\|PronType=Prs\|Reflex=Yes`, `Case=Acc\|Number=Sing\|POS=PRON\|Person=1\|PronType=Prs`, `AdjType=Pred\|Case=Nom\|Degree=Sup\|POS=ADJ` |
| **`parser`** | `ROOT`, `advmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `ccomp`, `compound:prt`, `conj`, `cop`, `dep`, `det`, `flat`, `iobj`, `mark`, `nmod`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `punct`, `xcomp` |
| **`experimental_edit_tree_lemmatizer`** | `1`, `2`, `4`, `7`, `8`, `10`, `12`, `14`, `16`, `18`, `21`, `24`, `26`, `28`, `31`, `32`, `34`, `37`, `39`, `40`, `42`, `44`, `46`, `47`, `49`, `51`, `53`, `54`, `56`, `57`, `58`, `59`, `61`, `64`, `66`, `68`, `69`, `72`, `74`, `75`, `77`, `78`, `81`, `83`, `84`, `85`, `86`, `87`, `90`, `92`, `94`, `96`, `99`, `101`, `103`, `105`, `108`, `110`, `113`, `116`, `117`, `118`, `121`, `123`, `124`, `125`, `127`, `128`, `129`, `133`, `136`, `138`, `141`, `143`, `145`, `147`, `151`, `153`, `154`, `156`, `158`, `159`, `160`, `162`, `164`, `165`, `167`, `168`, `170`, `172`, `174`, `176`, `178`, `179`, `180`, `181`, `183`, `185`, `189`, `190`, `191`, `192`, `194`, `195`, `197`, `198`, `201`, `202`, `203`, `204`, `206`, `207`, `209`, `213`, `214`, `216`, `217`, `218`, `220`, `221`, `222`, `223`, `225`, `226`, `228`, `229`, `231`, `233`, `234`, `236`, `238`, `240`, `241`, `244`, `247`, `248`, `249`, `250`, `252`, `253`, `255`, `256`, `257`, `258`, `261`, `262`, `263`, `265`, `267`, `269`, `270`, `271`, `273`, `275`, `276`, `278`, `279`, `281`, `283`, `285`, `287`, `289`, `291`, `294`, `296`, `297`, `298`, `299`, `300`, `301`, `302`, `303`, `305`, `306`, `307`, `309`, `310`, `311`, `313`, `314`, `315`, `317`, `320`, `321`, `323`, `325`, `326`, `327`, `328`, `329`, `330`, `332`, `333`, `335`, `336`, `337`, `338`, `339`, `340`, `341`, `343`, `344`, `347`, `348`, `349`, `351`, `353`, `355`, `357`, `359`, `360`, `361`, `362`, `365`, `366`, `367`, `369`, `371`, `373`, `374`, `375`, `377`, `379`, `381`, `383`, `386`, `388`, `390`, `392`, `393`, `395`, `397`, `398`, `400`, `401`, `402`, `403`, `405`, `406`, `408`, `409`, `411`, `412`, `414`, `417`, `215`, `418`, `419`, `420`, `421`, `422`, `424`, `425`, `426`, `427`, `429`, `431`, `432`, `433`, `434`, `436`, `438`, `439`, `440`, `442`, `443`, `444`, `447`, `449`, `450`, `452` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_F` | 99.92 |
| `TOKEN_P` | 99.89 |
| `TOKEN_R` | 99.94 |
| `TOKEN_ACC` | 100.00 |
| `SENTS_F` | 100.00 |
| `SENTS_P` | 100.00 |
| `SENTS_R` | 100.00 |
| `TAG_ACC` | 96.01 |
| `POS_ACC` | 98.52 |
| `MORPH_ACC` | 97.52 |
| `DEP_UAS` | 90.78 |
| `DEP_LAS` | 87.50 |
| `LEMMA_ACC` | 97.87 |