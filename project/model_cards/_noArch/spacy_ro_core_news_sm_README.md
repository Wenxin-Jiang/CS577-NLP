---
tags:
- spacy
- token-classification
language:
- ro
license: cc-by-sa-4.0
model-index:
- name: ro_core_news_sm
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.7232530596
    - name: NER Recall
      type: recall
      value: 0.7038033039
    - name: NER F Score
      type: f_score
      value: 0.7133956386
  - task:
      name: TAG
      type: token-classification
    metrics:
    - name: TAG (XPOS) Accuracy
      type: accuracy
      value: 0.9557849059
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS (UPOS) Accuracy
      type: accuracy
      value: 0.9282856599
  - task:
      name: MORPH
      type: token-classification
    metrics:
    - name: Morph (UFeats) Accuracy
      type: accuracy
      value: 0.9405383217
  - task:
      name: LEMMA
      type: token-classification
    metrics:
    - name: Lemma Accuracy
      type: accuracy
      value: 0.9504793737
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Attachment Score (UAS)
      type: f_score
      value: 0.8715455315
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Attachment Score (LAS)
      type: f_score
      value: 0.812886226
  - task:
      name: SENTS
      type: token-classification
    metrics:
    - name: Sentences F-Score
      type: f_score
      value: 0.960106383
---
### Details: https://spacy.io/models/ro#ro_core_news_sm

Romanian pipeline optimized for CPU. Components: tok2vec, tagger, parser, lemmatizer (trainable_lemmatizer), senter, ner, attribute_ruler.

| Feature | Description |
| --- | --- |
| **Name** | `ro_core_news_sm` |
| **Version** | `3.5.0` |
| **spaCy** | `>=3.5.0,<3.6.0` |
| **Default Pipeline** | `tok2vec`, `tagger`, `parser`, `lemmatizer`, `attribute_ruler`, `ner` |
| **Components** | `tok2vec`, `tagger`, `parser`, `lemmatizer`, `senter`, `attribute_ruler`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [UD Romanian RRT v2.8](https://github.com/UniversalDependencies/UD_Romanian-RRT) (Barbu Mititelu, Verginica; Irimia, Elena; Perez, Cenel-Augusto; Ion, Radu; Simionescu, Radu; Popel, Martin)<br />[RONEC - the Romanian Named Entity Corpus (ca9ce460)](https://github.com/dumitrescustefan/ronec) (Dumitrescu, Stefan Daniel; Avram, Andrei-Marius; Morogan, Luciana; Toma; Stefan) |
| **License** | `CC BY-SA 4.0` |
| **Author** | [Explosion](https://explosion.ai) |

### Label Scheme

<details>

<summary>View label scheme (540 labels for 3 components)</summary>

| Component | Labels |
| --- | --- |
| **`tagger`** | `ARROW`, `Af`, `Afcfp-n`, `Afcfson`, `Afcfsrn`, `Afcmpoy`, `Afcms-n`, `Afp`, `Afp-p-n`, `Afp-poy`, `Afp-srn`, `Afpf--n`, `Afpfp-n`, `Afpfp-ny`, `Afpfpoy`, `Afpfpry`, `Afpfson`, `Afpfsoy`, `Afpfsrn`, `Afpfsry`, `Afpm--n`, `Afpmp-n`, `Afpmpoy`, `Afpmpry`, `Afpms-n`, `Afpmsoy`, `Afpmsry`, `Afsfp-n`, `Afsfsrn`, `BULLET`, `COLON`, `COMMA`, `Ccssp`, `Ccsspy`, `Crssp`, `Csssp`, `Cssspy`, `DASH`, `DBLQ`, `Dd3-po---e`, `Dd3-po---o`, `Dd3fpo`, `Dd3fpr`, `Dd3fpr---e`, `Dd3fpr---o`, `Dd3fpr--y`, `Dd3fso`, `Dd3fso---e`, `Dd3fsr`, `Dd3fsr---e`, `Dd3fsr---o`, `Dd3fsr--yo`, `Dd3mpo`, `Dd3mpr`, `Dd3mpr---e`, `Dd3mpr---o`, `Dd3mso---e`, `Dd3msr`, `Dd3msr---e`, `Dd3msr---o`, `Dh1ms`, `Dh3fp`, `Dh3fso`, `Dh3fsr`, `Dh3mp`, `Dh3ms`, `Di3`, `Di3-----y`, `Di3--r---e`, `Di3-po`, `Di3-po---e`, `Di3-sr`, `Di3-sr---e`, `Di3-sr--y`, `Di3fp`, `Di3fpr`, `Di3fpr---e`, `Di3fso`, `Di3fso---e`, `Di3fsr`, `Di3fsr---e`, `Di3mp`, `Di3mpr`, `Di3mpr---e`, `Di3ms`, `Di3ms----e`, `Di3mso---e`, `Di3msr`, `Di3msr---e`, `Ds1fp-p`, `Ds1fp-s`, `Ds1fsop`, `Ds1fsos`, `Ds1fsrp`, `Ds1fsrs`, `Ds1fsrs-y`, `Ds1mp-p`, `Ds1mp-s`, `Ds1ms-p`, `Ds1ms-s`, `Ds1msrs-y`, `Ds2---s`, `Ds2fp-p`, `Ds2fp-s`, `Ds2fsrp`, `Ds2fsrs`, `Ds2mp-p`, `Ds2mp-s`, `Ds2ms-p`, `Ds2ms-s`, `Ds3---p`, `Ds3---s`, `Ds3---sy`, `Ds3fp-s`, `Ds3fsos`, `Ds3fsrs`, `Ds3mp-s`, `Ds3ms-s`, `Dw3--r---e`, `Dw3-po---e`, `Dw3fpr`, `Dw3fso---e`, `Dw3fsr`, `Dw3mpr`, `Dw3mso---e`, `Dw3msr`, `Dz3fsr---e`, `Dz3mso---e`, `Dz3msr---e`, `EQUAL`, `EXCL`, `EXCLHELLIP`, `GE`, `GT`, `HELLIP`, `I`, `LCURL`, `LPAR`, `LSQR`, `LT`, `M`, `Mc-p-d`, `Mc-p-l`, `Mc-s-b`, `Mc-s-d`, `Mc-s-l`, `Mcfp-l`, `Mcfp-ln`, `Mcfprln`, `Mcfprly`, `Mcfsoln`, `Mcfsrl`, `Mcfsrln`, `Mcfsrly`, `Mcmp-l`, `Mcms-ln`, `Mcmsrl`, `Mcmsrln`, `Mcmsrly`, `Mffprln`, `Mffsrln`, `Mlfpo`, `Mlfpr`, `Mlmpr`, `Mo---l`, `Mo---ln`, `Mo-s-r`, `Mofp-ln`, `Mofpoly`, `Mofprly`, `Mofs-l`, `Mofsoln`, `Mofsoly`, `Mofsrln`, `Mofsrly`, `Mompoly`, `Momprly`, `Moms-l`, `Moms-ln`, `Momsoly`, `Momsrly`, `Nc`, `Nc---n`, `Ncf--n`, `Ncfp-n`, `Ncfpoy`, `Ncfpry`, `Ncfs-n`, `Ncfson`, `Ncfsoy`, `Ncfsrn`, `Ncfsry`, `Ncfsryy`, `Ncfsvy`, `Ncm--n`, `Ncmp-n`, `Ncmpoy`, `Ncmpry`, `Ncms-n`, `Ncms-ny`, `Ncms-y`, `Ncmsoy`, `Ncmsrn`, `Ncmsry`, `Ncmsryy`, `Ncmsvn`, `Ncmsvy`, `Np`, `Npfson`, `Npfsoy`, `Npfsrn`, `Npfsry`, `Npmpoy`, `Npmpry`, `Npms-n`, `Npmsoy`, `Npmsry`, `PERCENT`, `PERIOD`, `PLUS`, `PLUSMINUS`, `Pd3-po`, `Pd3fpr`, `Pd3fso`, `Pd3fsr`, `Pd3mpo`, `Pd3mpr`, `Pd3mpr--y`, `Pd3mso`, `Pd3msr`, `Pi3--r`, `Pi3-po`, `Pi3-so`, `Pi3-sr`, `Pi3fpr`, `Pi3fso`, `Pi3fsr`, `Pi3mpr`, `Pi3mso`, `Pi3msr`, `Pi3msr--y`, `Pp1-pa--------w`, `Pp1-pa--y-----w`, `Pp1-pd--------s`, `Pp1-pd--------w`, `Pp1-pd--y-----w`, `Pp1-pr--------s`, `Pp1-sa--------s`, `Pp1-sa--------w`, `Pp1-sa--y-----w`, `Pp1-sd--------s`, `Pp1-sd--------w`, `Pp1-sd--y-----w`, `Pp1-sn--------s`, `Pp2-----------s`, `Pp2-pa--------w`, `Pp2-pa--y-----w`, `Pp2-pd--------w`, `Pp2-pd--y-----w`, `Pp2-pr--------s`, `Pp2-sa--------s`, `Pp2-sa--------w`, `Pp2-sa--y-----w`, `Pp2-sd--------s`, `Pp2-sd--------w`, `Pp2-sd--y-----w`, `Pp2-sn--------s`, `Pp2-so--------s`, `Pp2-sr--------s`, `Pp3-p---------s`, `Pp3-pd--------w`, `Pp3-pd--y-----w`, `Pp3-po--------s`, `Pp3-sd--------w`, `Pp3-sd--y-----w`, `Pp3-so--------s`, `Pp3fpa--------w`, `Pp3fpa--y-----w`, `Pp3fpr--------s`, `Pp3fs---------s`, `Pp3fsa--------w`, `Pp3fsa--y-----w`, `Pp3fso--------s`, `Pp3fsr--------s`, `Pp3fsr--y-----s`, `Pp3mpa--------w`, `Pp3mpa--y-----w`, `Pp3mpr--------s`, `Pp3ms---------s`, `Pp3msa--------w`, `Pp3msa--y-----w`, `Pp3mso--------s`, `Pp3msr--------s`, `Pp3msr--y-----s`, `Ps1fp-s`, `Ps1fsrp`, `Ps1fsrs`, `Ps1mp-p`, `Ps1ms-p`, `Ps2fp-s`, `Ps2fsrp`, `Ps2fsrs`, `Ps3---p`, `Ps3---s`, `Ps3fp-s`, `Ps3fsrs`, `Ps3mp-s`, `Ps3ms-s`, `Pw3--r`, `Pw3-po`, `Pw3-so`, `Pw3fpr`, `Pw3fso`, `Pw3mpr`, `Pw3mso`, `Px3--a--------s`, `Px3--a--------w`, `Px3--a--y-----w`, `Px3--d--------w`, `Px3--d--y-----w`, `Pz3-sr`, `Pz3fsr`, `QUEST`, `QUOT`, `Qf`, `Qn`, `Qs`, `Qs-y`, `Qz`, `Qz-y`, `RCURL`, `RPAR`, `RSQR`, `Rc`, `Rgp`, `Rgpy`, `Rgs`, `Rp`, `Rw`, `Rw-y`, `Rz`, `SCOLON`, `SLASH`, `STAR`, `Sp`, `Spsa`, `Spsay`, `Spsd`, `Spsg`, `Td-po`, `Tdfpr`, `Tdfso`, `Tdfsr`, `Tdmpr`, `Tdmso`, `Tdmsr`, `Tf-so`, `Tffpoy`, `Tffpry`, `Tffs-y`, `Tfmpoy`, `Tfms-y`, `Tfmsoy`, `Tfmsry`, `Ti-po`, `Tifp-y`, `Tifso`, `Tifsr`, `Timso`, `Timsr`, `Tsfp`, `Tsfs`, `Tsmp`, `Tsms`, `UNDERSC`, `Va--1`, `Va--1-----y`, `Va--1p`, `Va--1s`, `Va--1s----y`, `Va--2p`, `Va--2p----y`, `Va--2s`, `Va--2s----y`, `Va--3`, `Va--3-----y`, `Va--3p`, `Va--3p----y`, `Va--3s`, `Va--3s----y`, `Vag`, `Vag-------y`, `Vaii1`, `Vaii2s`, `Vaii3p`, `Vaii3s`, `Vail3p`, `Vail3s`, `Vaip1p`, `Vaip1s`, `Vaip2p`, `Vaip2s`, `Vaip3p`, `Vaip3p----y`, `Vaip3s`, `Vaip3s----y`, `Vais3p`, `Vais3s`, `Vam-2s`, `Vanp`, `Vap--sm`, `Vasp1p`, `Vasp1s`, `Vasp2p`, `Vasp2s`, `Vasp3`, `Vmg`, `Vmg-------y`, `Vmii1`, `Vmii1-----y`, `Vmii2p`, `Vmii2s`, `Vmii3p`, `Vmii3p----y`, `Vmii3s`, `Vmii3s----y`, `Vmil1`, `Vmil1p`, `Vmil2s`, `Vmil3p`, `Vmil3p----y`, `Vmil3s`, `Vmil3s----y`, `Vmip1p`, `Vmip1p----y`, `Vmip1s`, `Vmip1s----y`, `Vmip2p`, `Vmip2s`, `Vmip2s----y`, `Vmip3`, `Vmip3-----y`, `Vmip3p`, `Vmip3s`, `Vmip3s----y`, `Vmis1p`, `Vmis1s`, `Vmis3p`, `Vmis3p----y`, `Vmis3s`, `Vmis3s----y`, `Vmm-2p`, `Vmm-2s`, `Vmnp`, `Vmnp------y`, `Vmp--pf`, `Vmp--pm`, `Vmp--sf`, `Vmp--sm`, `Vmp--sm---y`, `Vmsp1p`, `Vmsp2p`, `Vmsp2s`, `Vmsp3`, `Vmsp3-----y`, `X`, `Y`, `Ya`, `Yn`, `Ynfsoy`, `Ynfsry`, `Ynmsoy`, `Ynmsry`, `Yp`, `Yp,Yn`, `Yp-sr`, `Yr`, `_SP` |
| **`parser`** | `ROOT`, `acl`, `advcl`, `advcl:tcl`, `advmod`, `advmod:tmod`, `amod`, `appos`, `aux`, `aux:pass`, `case`, `cc`, `cc:preconj`, `ccomp`, `ccomp:pmod`, `compound`, `conj`, `cop`, `csubj`, `csubj:pass`, `dep`, `det`, `expl`, `expl:impers`, `expl:pass`, `expl:poss`, `expl:pv`, `fixed`, `flat`, `goeswith`, `iobj`, `mark`, `nmod`, `nmod:tmod`, `nsubj`, `nsubj:pass`, `nummod`, `obj`, `obl`, `obl:agent`, `obl:pmod`, `orphan`, `parataxis`, `punct`, `vocative`, `xcomp` |
| **`ner`** | `DATETIME`, `EVENT`, `FACILITY`, `GPE`, `LANGUAGE`, `LOC`, `MONEY`, `NAT_REL_POL`, `NUMERIC_VALUE`, `ORDINAL`, `ORGANIZATION`, `PERIOD`, `PERSON`, `PRODUCT`, `QUANTITY`, `WORK_OF_ART` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `TOKEN_ACC` | 99.80 |
| `TOKEN_P` | 99.67 |
| `TOKEN_R` | 99.57 |
| `TOKEN_F` | 99.59 |
| `TAG_ACC` | 95.58 |
| `SENTS_P` | 96.01 |
| `SENTS_R` | 96.01 |
| `SENTS_F` | 96.01 |
| `DEP_UAS` | 87.15 |
| `DEP_LAS` | 81.29 |
| `LEMMA_ACC` | 95.05 |
| `POS_ACC` | 92.83 |
| `MORPH_ACC` | 94.05 |
| `MORPH_MICRO_P` | 98.20 |
| `MORPH_MICRO_R` | 95.20 |
| `MORPH_MICRO_F` | 96.43 |
| `ENTS_P` | 72.33 |
| `ENTS_R` | 70.38 |
| `ENTS_F` | 71.34 |