---
language: 
- ca
- es
- os
- eo
- ro
- fy
- cy
- is
- lb
- su
- an
- sq
- fr
- ht
- rm
- cv
- ig
- am
- eu
- tr
- ps
- af
- ny
- ch
- uk
- sl
- lt
- tk
- sg
- ar
- lg
- bg
- be
- ka
- gd
- ja
- si
- br
- mh
- km
- th
- ty
- rw
- te
- mk
- or
- wo
- kl
- mr
- ru
- yo
- hu
- fo
- zh
- ti
- co
- ee
- oc
- sn
- mt
- ts
- pl
- gl
- nb
- bn
- tt
- bo
- lo
- id
- gn
- nv
- hy
- kn
- to
- io
- so
- vi
- da
- fj
- gv
- sm
- nl
- mi
- pt
- hi
- se
- as
- ta
- et
- kw
- ga
- sv
- ln
- na
- mn
- gu
- wa
- lv
- jv
- el
- my
- ba
- it
- hr
- ur
- ce
- nn
- fi
- mg
- rn
- xh
- ab
- de
- cs
- he
- zu
- yi
- ml
- mul
- en

tags:
- translation

license: apache-2.0
---

### mul-eng

* source group: Multiple languages 
* target group: English 
*  OPUS readme: [mul-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/mul-eng/README.md)

*  model: transformer
* source language(s): abk acm ady afb afh_Latn afr akl_Latn aln amh ang_Latn apc ara arg arq ary arz asm ast avk_Latn awa aze_Latn bak bam_Latn bel bel_Latn ben bho bod bos_Latn bre brx brx_Latn bul bul_Latn cat ceb ces cha che chr chv cjy_Hans cjy_Hant cmn cmn_Hans cmn_Hant cor cos crh crh_Latn csb_Latn cym dan deu dsb dtp dws_Latn egl ell enm_Latn epo est eus ewe ext fao fij fin fkv_Latn fra frm_Latn frr fry fuc fuv gan gcf_Latn gil gla gle glg glv gom gos got_Goth grc_Grek grn gsw guj hat hau_Latn haw heb hif_Latn hil hin hnj_Latn hoc hoc_Latn hrv hsb hun hye iba ibo ido ido_Latn ike_Latn ile_Latn ilo ina_Latn ind isl ita izh jav jav_Java jbo jbo_Cyrl jbo_Latn jdt_Cyrl jpn kab kal kan kat kaz_Cyrl kaz_Latn kek_Latn kha khm khm_Latn kin kir_Cyrl kjh kpv krl ksh kum kur_Arab kur_Latn lad lad_Latn lao lat_Latn lav ldn_Latn lfn_Cyrl lfn_Latn lij lin lit liv_Latn lkt lld_Latn lmo ltg ltz lug lzh lzh_Hans mad mah mai mal mar max_Latn mdf mfe mhr mic min mkd mlg mlt mnw moh mon mri mwl mww mya myv nan nau nav nds niu nld nno nob nob_Hebr nog non_Latn nov_Latn npi nya oci ori orv_Cyrl oss ota_Arab ota_Latn pag pan_Guru pap pau pdc pes pes_Latn pes_Thaa pms pnb pol por ppl_Latn prg_Latn pus quc qya qya_Latn rap rif_Latn roh rom ron rue run rus sag sah san_Deva scn sco sgs shs_Latn shy_Latn sin sjn_Latn slv sma sme smo sna snd_Arab som spa sqi srp_Cyrl srp_Latn stq sun swe swg swh tah tam tat tat_Arab tat_Latn tel tet tgk_Cyrl tha tir tlh_Latn tly_Latn tmw_Latn toi_Latn ton tpw_Latn tso tuk tuk_Latn tur tvl tyv tzl tzl_Latn udm uig_Arab uig_Cyrl ukr umb urd uzb_Cyrl uzb_Latn vec vie vie_Hani vol_Latn vro war wln wol wuu xal xho yid yor yue yue_Hans yue_Hant zho zho_Hans zho_Hant zlm_Latn zsm_Latn zul zza
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/mul-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/mul-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/mul-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2014-hineng.hin.eng 	| 8.5 	| 0.341 |
| newsdev2015-enfi-fineng.fin.eng 	| 16.8 	| 0.441 |
| newsdev2016-enro-roneng.ron.eng 	| 31.3 	| 0.580 |
| newsdev2016-entr-tureng.tur.eng 	| 16.4 	| 0.422 |
| newsdev2017-enlv-laveng.lav.eng 	| 21.3 	| 0.502 |
| newsdev2017-enzh-zhoeng.zho.eng 	| 12.7 	| 0.409 |
| newsdev2018-enet-esteng.est.eng 	| 19.8 	| 0.467 |
| newsdev2019-engu-gujeng.guj.eng 	| 13.3 	| 0.385 |
| newsdev2019-enlt-liteng.lit.eng 	| 19.9 	| 0.482 |
| newsdiscussdev2015-enfr-fraeng.fra.eng 	| 26.7 	| 0.520 |
| newsdiscusstest2015-enfr-fraeng.fra.eng 	| 29.8 	| 0.541 |
| newssyscomb2009-ceseng.ces.eng 	| 21.1 	| 0.487 |
| newssyscomb2009-deueng.deu.eng 	| 22.6 	| 0.499 |
| newssyscomb2009-fraeng.fra.eng 	| 25.8 	| 0.530 |
| newssyscomb2009-huneng.hun.eng 	| 15.1 	| 0.430 |
| newssyscomb2009-itaeng.ita.eng 	| 29.4 	| 0.555 |
| newssyscomb2009-spaeng.spa.eng 	| 26.1 	| 0.534 |
| news-test2008-deueng.deu.eng 	| 21.6 	| 0.491 |
| news-test2008-fraeng.fra.eng 	| 22.3 	| 0.502 |
| news-test2008-spaeng.spa.eng 	| 23.6 	| 0.514 |
| newstest2009-ceseng.ces.eng 	| 19.8 	| 0.480 |
| newstest2009-deueng.deu.eng 	| 20.9 	| 0.487 |
| newstest2009-fraeng.fra.eng 	| 25.0 	| 0.523 |
| newstest2009-huneng.hun.eng 	| 14.7 	| 0.425 |
| newstest2009-itaeng.ita.eng 	| 27.6 	| 0.542 |
| newstest2009-spaeng.spa.eng 	| 25.7 	| 0.530 |
| newstest2010-ceseng.ces.eng 	| 20.6 	| 0.491 |
| newstest2010-deueng.deu.eng 	| 23.4 	| 0.517 |
| newstest2010-fraeng.fra.eng 	| 26.1 	| 0.537 |
| newstest2010-spaeng.spa.eng 	| 29.1 	| 0.561 |
| newstest2011-ceseng.ces.eng 	| 21.0 	| 0.489 |
| newstest2011-deueng.deu.eng 	| 21.3 	| 0.494 |
| newstest2011-fraeng.fra.eng 	| 26.8 	| 0.546 |
| newstest2011-spaeng.spa.eng 	| 28.2 	| 0.549 |
| newstest2012-ceseng.ces.eng 	| 20.5 	| 0.485 |
| newstest2012-deueng.deu.eng 	| 22.3 	| 0.503 |
| newstest2012-fraeng.fra.eng 	| 27.5 	| 0.545 |
| newstest2012-ruseng.rus.eng 	| 26.6 	| 0.532 |
| newstest2012-spaeng.spa.eng 	| 30.3 	| 0.567 |
| newstest2013-ceseng.ces.eng 	| 22.5 	| 0.498 |
| newstest2013-deueng.deu.eng 	| 25.0 	| 0.518 |
| newstest2013-fraeng.fra.eng 	| 27.4 	| 0.537 |
| newstest2013-ruseng.rus.eng 	| 21.6 	| 0.484 |
| newstest2013-spaeng.spa.eng 	| 28.4 	| 0.555 |
| newstest2014-csen-ceseng.ces.eng 	| 24.0 	| 0.517 |
| newstest2014-deen-deueng.deu.eng 	| 24.1 	| 0.511 |
| newstest2014-fren-fraeng.fra.eng 	| 29.1 	| 0.563 |
| newstest2014-hien-hineng.hin.eng 	| 14.0 	| 0.414 |
| newstest2014-ruen-ruseng.rus.eng 	| 24.0 	| 0.521 |
| newstest2015-encs-ceseng.ces.eng 	| 21.9 	| 0.481 |
| newstest2015-ende-deueng.deu.eng 	| 25.5 	| 0.519 |
| newstest2015-enfi-fineng.fin.eng 	| 17.4 	| 0.441 |
| newstest2015-enru-ruseng.rus.eng 	| 22.4 	| 0.494 |
| newstest2016-encs-ceseng.ces.eng 	| 23.0 	| 0.500 |
| newstest2016-ende-deueng.deu.eng 	| 30.1 	| 0.560 |
| newstest2016-enfi-fineng.fin.eng 	| 18.5 	| 0.461 |
| newstest2016-enro-roneng.ron.eng 	| 29.6 	| 0.562 |
| newstest2016-enru-ruseng.rus.eng 	| 22.0 	| 0.495 |
| newstest2016-entr-tureng.tur.eng 	| 14.8 	| 0.415 |
| newstest2017-encs-ceseng.ces.eng 	| 20.2 	| 0.475 |
| newstest2017-ende-deueng.deu.eng 	| 26.0 	| 0.523 |
| newstest2017-enfi-fineng.fin.eng 	| 19.6 	| 0.465 |
| newstest2017-enlv-laveng.lav.eng 	| 16.2 	| 0.454 |
| newstest2017-enru-ruseng.rus.eng 	| 24.2 	| 0.510 |
| newstest2017-entr-tureng.tur.eng 	| 15.0 	| 0.412 |
| newstest2017-enzh-zhoeng.zho.eng 	| 13.7 	| 0.412 |
| newstest2018-encs-ceseng.ces.eng 	| 21.2 	| 0.486 |
| newstest2018-ende-deueng.deu.eng 	| 31.5 	| 0.564 |
| newstest2018-enet-esteng.est.eng 	| 19.7 	| 0.473 |
| newstest2018-enfi-fineng.fin.eng 	| 15.1 	| 0.418 |
| newstest2018-enru-ruseng.rus.eng 	| 21.3 	| 0.490 |
| newstest2018-entr-tureng.tur.eng 	| 15.4 	| 0.421 |
| newstest2018-enzh-zhoeng.zho.eng 	| 12.9 	| 0.408 |
| newstest2019-deen-deueng.deu.eng 	| 27.0 	| 0.529 |
| newstest2019-fien-fineng.fin.eng 	| 17.2 	| 0.438 |
| newstest2019-guen-gujeng.guj.eng 	| 9.0 	| 0.342 |
| newstest2019-lten-liteng.lit.eng 	| 22.6 	| 0.512 |
| newstest2019-ruen-ruseng.rus.eng 	| 24.1 	| 0.503 |
| newstest2019-zhen-zhoeng.zho.eng 	| 13.9 	| 0.427 |
| newstestB2016-enfi-fineng.fin.eng 	| 15.2 	| 0.428 |
| newstestB2017-enfi-fineng.fin.eng 	| 16.8 	| 0.442 |
| newstestB2017-fien-fineng.fin.eng 	| 16.8 	| 0.442 |
| Tatoeba-test.abk-eng.abk.eng 	| 2.4 	| 0.190 |
| Tatoeba-test.ady-eng.ady.eng 	| 1.1 	| 0.111 |
| Tatoeba-test.afh-eng.afh.eng 	| 1.7 	| 0.108 |
| Tatoeba-test.afr-eng.afr.eng 	| 53.0 	| 0.672 |
| Tatoeba-test.akl-eng.akl.eng 	| 5.9 	| 0.239 |
| Tatoeba-test.amh-eng.amh.eng 	| 25.6 	| 0.464 |
| Tatoeba-test.ang-eng.ang.eng 	| 11.7 	| 0.289 |
| Tatoeba-test.ara-eng.ara.eng 	| 26.4 	| 0.443 |
| Tatoeba-test.arg-eng.arg.eng 	| 35.9 	| 0.473 |
| Tatoeba-test.asm-eng.asm.eng 	| 19.8 	| 0.365 |
| Tatoeba-test.ast-eng.ast.eng 	| 31.8 	| 0.467 |
| Tatoeba-test.avk-eng.avk.eng 	| 0.4 	| 0.119 |
| Tatoeba-test.awa-eng.awa.eng 	| 9.7 	| 0.271 |
| Tatoeba-test.aze-eng.aze.eng 	| 37.0 	| 0.542 |
| Tatoeba-test.bak-eng.bak.eng 	| 13.9 	| 0.395 |
| Tatoeba-test.bam-eng.bam.eng 	| 2.2 	| 0.094 |
| Tatoeba-test.bel-eng.bel.eng 	| 36.8 	| 0.549 |
| Tatoeba-test.ben-eng.ben.eng 	| 39.7 	| 0.546 |
| Tatoeba-test.bho-eng.bho.eng 	| 33.6 	| 0.540 |
| Tatoeba-test.bod-eng.bod.eng 	| 1.1 	| 0.147 |
| Tatoeba-test.bre-eng.bre.eng 	| 14.2 	| 0.303 |
| Tatoeba-test.brx-eng.brx.eng 	| 1.7 	| 0.130 |
| Tatoeba-test.bul-eng.bul.eng 	| 46.0 	| 0.621 |
| Tatoeba-test.cat-eng.cat.eng 	| 46.6 	| 0.636 |
| Tatoeba-test.ceb-eng.ceb.eng 	| 17.4 	| 0.347 |
| Tatoeba-test.ces-eng.ces.eng 	| 41.3 	| 0.586 |
| Tatoeba-test.cha-eng.cha.eng 	| 7.9 	| 0.232 |
| Tatoeba-test.che-eng.che.eng 	| 0.7 	| 0.104 |
| Tatoeba-test.chm-eng.chm.eng 	| 7.3 	| 0.261 |
| Tatoeba-test.chr-eng.chr.eng 	| 8.8 	| 0.244 |
| Tatoeba-test.chv-eng.chv.eng 	| 11.0 	| 0.319 |
| Tatoeba-test.cor-eng.cor.eng 	| 5.4 	| 0.204 |
| Tatoeba-test.cos-eng.cos.eng 	| 58.2 	| 0.643 |
| Tatoeba-test.crh-eng.crh.eng 	| 26.3 	| 0.399 |
| Tatoeba-test.csb-eng.csb.eng 	| 18.8 	| 0.389 |
| Tatoeba-test.cym-eng.cym.eng 	| 23.4 	| 0.407 |
| Tatoeba-test.dan-eng.dan.eng 	| 50.5 	| 0.659 |
| Tatoeba-test.deu-eng.deu.eng 	| 39.6 	| 0.579 |
| Tatoeba-test.dsb-eng.dsb.eng 	| 24.3 	| 0.449 |
| Tatoeba-test.dtp-eng.dtp.eng 	| 1.0 	| 0.149 |
| Tatoeba-test.dws-eng.dws.eng 	| 1.6 	| 0.061 |
| Tatoeba-test.egl-eng.egl.eng 	| 7.6 	| 0.236 |
| Tatoeba-test.ell-eng.ell.eng 	| 55.4 	| 0.682 |
| Tatoeba-test.enm-eng.enm.eng 	| 28.0 	| 0.489 |
| Tatoeba-test.epo-eng.epo.eng 	| 41.8 	| 0.591 |
| Tatoeba-test.est-eng.est.eng 	| 41.5 	| 0.581 |
| Tatoeba-test.eus-eng.eus.eng 	| 37.8 	| 0.557 |
| Tatoeba-test.ewe-eng.ewe.eng 	| 10.7 	| 0.262 |
| Tatoeba-test.ext-eng.ext.eng 	| 25.5 	| 0.405 |
| Tatoeba-test.fao-eng.fao.eng 	| 28.7 	| 0.469 |
| Tatoeba-test.fas-eng.fas.eng 	| 7.5 	| 0.281 |
| Tatoeba-test.fij-eng.fij.eng 	| 24.2 	| 0.320 |
| Tatoeba-test.fin-eng.fin.eng 	| 35.8 	| 0.534 |
| Tatoeba-test.fkv-eng.fkv.eng 	| 15.5 	| 0.434 |
| Tatoeba-test.fra-eng.fra.eng 	| 45.1 	| 0.618 |
| Tatoeba-test.frm-eng.frm.eng 	| 29.6 	| 0.427 |
| Tatoeba-test.frr-eng.frr.eng 	| 5.5 	| 0.138 |
| Tatoeba-test.fry-eng.fry.eng 	| 25.3 	| 0.455 |
| Tatoeba-test.ful-eng.ful.eng 	| 1.1 	| 0.127 |
| Tatoeba-test.gcf-eng.gcf.eng 	| 16.0 	| 0.315 |
| Tatoeba-test.gil-eng.gil.eng 	| 46.7 	| 0.587 |
| Tatoeba-test.gla-eng.gla.eng 	| 20.2 	| 0.358 |
| Tatoeba-test.gle-eng.gle.eng 	| 43.9 	| 0.592 |
| Tatoeba-test.glg-eng.glg.eng 	| 45.1 	| 0.623 |
| Tatoeba-test.glv-eng.glv.eng 	| 3.3 	| 0.119 |
| Tatoeba-test.gos-eng.gos.eng 	| 20.1 	| 0.364 |
| Tatoeba-test.got-eng.got.eng 	| 0.1 	| 0.041 |
| Tatoeba-test.grc-eng.grc.eng 	| 2.1 	| 0.137 |
| Tatoeba-test.grn-eng.grn.eng 	| 1.7 	| 0.152 |
| Tatoeba-test.gsw-eng.gsw.eng 	| 18.2 	| 0.334 |
| Tatoeba-test.guj-eng.guj.eng 	| 21.7 	| 0.373 |
| Tatoeba-test.hat-eng.hat.eng 	| 34.5 	| 0.502 |
| Tatoeba-test.hau-eng.hau.eng 	| 10.5 	| 0.295 |
| Tatoeba-test.haw-eng.haw.eng 	| 2.8 	| 0.160 |
| Tatoeba-test.hbs-eng.hbs.eng 	| 46.7 	| 0.623 |
| Tatoeba-test.heb-eng.heb.eng 	| 33.0 	| 0.492 |
| Tatoeba-test.hif-eng.hif.eng 	| 17.0 	| 0.391 |
| Tatoeba-test.hil-eng.hil.eng 	| 16.0 	| 0.339 |
| Tatoeba-test.hin-eng.hin.eng 	| 36.4 	| 0.533 |
| Tatoeba-test.hmn-eng.hmn.eng 	| 0.4 	| 0.131 |
| Tatoeba-test.hoc-eng.hoc.eng 	| 0.7 	| 0.132 |
| Tatoeba-test.hsb-eng.hsb.eng 	| 41.9 	| 0.551 |
| Tatoeba-test.hun-eng.hun.eng 	| 33.2 	| 0.510 |
| Tatoeba-test.hye-eng.hye.eng 	| 32.2 	| 0.487 |
| Tatoeba-test.iba-eng.iba.eng 	| 9.4 	| 0.278 |
| Tatoeba-test.ibo-eng.ibo.eng 	| 5.8 	| 0.200 |
| Tatoeba-test.ido-eng.ido.eng 	| 31.7 	| 0.503 |
| Tatoeba-test.iku-eng.iku.eng 	| 9.1 	| 0.164 |
| Tatoeba-test.ile-eng.ile.eng 	| 42.2 	| 0.595 |
| Tatoeba-test.ilo-eng.ilo.eng 	| 29.7 	| 0.485 |
| Tatoeba-test.ina-eng.ina.eng 	| 42.1 	| 0.607 |
| Tatoeba-test.isl-eng.isl.eng 	| 35.7 	| 0.527 |
| Tatoeba-test.ita-eng.ita.eng 	| 54.8 	| 0.686 |
| Tatoeba-test.izh-eng.izh.eng 	| 28.3 	| 0.526 |
| Tatoeba-test.jav-eng.jav.eng 	| 10.0 	| 0.282 |
| Tatoeba-test.jbo-eng.jbo.eng 	| 0.3 	| 0.115 |
| Tatoeba-test.jdt-eng.jdt.eng 	| 5.3 	| 0.140 |
| Tatoeba-test.jpn-eng.jpn.eng 	| 18.8 	| 0.387 |
| Tatoeba-test.kab-eng.kab.eng 	| 3.9 	| 0.205 |
| Tatoeba-test.kal-eng.kal.eng 	| 16.9 	| 0.329 |
| Tatoeba-test.kan-eng.kan.eng 	| 16.2 	| 0.374 |
| Tatoeba-test.kat-eng.kat.eng 	| 31.1 	| 0.493 |
| Tatoeba-test.kaz-eng.kaz.eng 	| 24.5 	| 0.437 |
| Tatoeba-test.kek-eng.kek.eng 	| 7.4 	| 0.192 |
| Tatoeba-test.kha-eng.kha.eng 	| 1.0 	| 0.154 |
| Tatoeba-test.khm-eng.khm.eng 	| 12.2 	| 0.290 |
| Tatoeba-test.kin-eng.kin.eng 	| 22.5 	| 0.355 |
| Tatoeba-test.kir-eng.kir.eng 	| 27.2 	| 0.470 |
| Tatoeba-test.kjh-eng.kjh.eng 	| 2.1 	| 0.129 |
| Tatoeba-test.kok-eng.kok.eng 	| 4.5 	| 0.259 |
| Tatoeba-test.kom-eng.kom.eng 	| 1.4 	| 0.099 |
| Tatoeba-test.krl-eng.krl.eng 	| 26.1 	| 0.387 |
| Tatoeba-test.ksh-eng.ksh.eng 	| 5.5 	| 0.256 |
| Tatoeba-test.kum-eng.kum.eng 	| 9.3 	| 0.288 |
| Tatoeba-test.kur-eng.kur.eng 	| 9.6 	| 0.208 |
| Tatoeba-test.lad-eng.lad.eng 	| 30.1 	| 0.475 |
| Tatoeba-test.lah-eng.lah.eng 	| 11.6 	| 0.284 |
| Tatoeba-test.lao-eng.lao.eng 	| 4.5 	| 0.214 |
| Tatoeba-test.lat-eng.lat.eng 	| 21.5 	| 0.402 |
| Tatoeba-test.lav-eng.lav.eng 	| 40.2 	| 0.577 |
| Tatoeba-test.ldn-eng.ldn.eng 	| 0.8 	| 0.115 |
| Tatoeba-test.lfn-eng.lfn.eng 	| 23.0 	| 0.433 |
| Tatoeba-test.lij-eng.lij.eng 	| 9.3 	| 0.287 |
| Tatoeba-test.lin-eng.lin.eng 	| 2.4 	| 0.196 |
| Tatoeba-test.lit-eng.lit.eng 	| 44.0 	| 0.597 |
| Tatoeba-test.liv-eng.liv.eng 	| 1.6 	| 0.115 |
| Tatoeba-test.lkt-eng.lkt.eng 	| 2.0 	| 0.113 |
| Tatoeba-test.lld-eng.lld.eng 	| 18.3 	| 0.312 |
| Tatoeba-test.lmo-eng.lmo.eng 	| 25.4 	| 0.395 |
| Tatoeba-test.ltz-eng.ltz.eng 	| 35.9 	| 0.509 |
| Tatoeba-test.lug-eng.lug.eng 	| 5.1 	| 0.357 |
| Tatoeba-test.mad-eng.mad.eng 	| 2.8 	| 0.123 |
| Tatoeba-test.mah-eng.mah.eng 	| 5.7 	| 0.175 |
| Tatoeba-test.mai-eng.mai.eng 	| 56.3 	| 0.703 |
| Tatoeba-test.mal-eng.mal.eng 	| 37.5 	| 0.534 |
| Tatoeba-test.mar-eng.mar.eng 	| 22.8 	| 0.470 |
| Tatoeba-test.mdf-eng.mdf.eng 	| 2.0 	| 0.110 |
| Tatoeba-test.mfe-eng.mfe.eng 	| 59.2 	| 0.764 |
| Tatoeba-test.mic-eng.mic.eng 	| 9.0 	| 0.199 |
| Tatoeba-test.mkd-eng.mkd.eng 	| 44.3 	| 0.593 |
| Tatoeba-test.mlg-eng.mlg.eng 	| 31.9 	| 0.424 |
| Tatoeba-test.mlt-eng.mlt.eng 	| 38.6 	| 0.540 |
| Tatoeba-test.mnw-eng.mnw.eng 	| 2.5 	| 0.101 |
| Tatoeba-test.moh-eng.moh.eng 	| 0.3 	| 0.110 |
| Tatoeba-test.mon-eng.mon.eng 	| 13.5 	| 0.334 |
| Tatoeba-test.mri-eng.mri.eng 	| 8.5 	| 0.260 |
| Tatoeba-test.msa-eng.msa.eng 	| 33.9 	| 0.520 |
| Tatoeba-test.multi.eng 	| 34.7 	| 0.518 |
| Tatoeba-test.mwl-eng.mwl.eng 	| 37.4 	| 0.630 |
| Tatoeba-test.mya-eng.mya.eng 	| 15.5 	| 0.335 |
| Tatoeba-test.myv-eng.myv.eng 	| 0.8 	| 0.118 |
| Tatoeba-test.nau-eng.nau.eng 	| 9.0 	| 0.186 |
| Tatoeba-test.nav-eng.nav.eng 	| 1.3 	| 0.144 |
| Tatoeba-test.nds-eng.nds.eng 	| 30.7 	| 0.495 |
| Tatoeba-test.nep-eng.nep.eng 	| 3.5 	| 0.168 |
| Tatoeba-test.niu-eng.niu.eng 	| 42.7 	| 0.492 |
| Tatoeba-test.nld-eng.nld.eng 	| 47.9 	| 0.640 |
| Tatoeba-test.nog-eng.nog.eng 	| 12.7 	| 0.284 |
| Tatoeba-test.non-eng.non.eng 	| 43.8 	| 0.586 |
| Tatoeba-test.nor-eng.nor.eng 	| 45.5 	| 0.619 |
| Tatoeba-test.nov-eng.nov.eng 	| 26.9 	| 0.472 |
| Tatoeba-test.nya-eng.nya.eng 	| 33.2 	| 0.456 |
| Tatoeba-test.oci-eng.oci.eng 	| 17.9 	| 0.370 |
| Tatoeba-test.ori-eng.ori.eng 	| 14.6 	| 0.305 |
| Tatoeba-test.orv-eng.orv.eng 	| 11.0 	| 0.283 |
| Tatoeba-test.oss-eng.oss.eng 	| 4.1 	| 0.211 |
| Tatoeba-test.ota-eng.ota.eng 	| 4.1 	| 0.216 |
| Tatoeba-test.pag-eng.pag.eng 	| 24.3 	| 0.468 |
| Tatoeba-test.pan-eng.pan.eng 	| 16.4 	| 0.358 |
| Tatoeba-test.pap-eng.pap.eng 	| 53.2 	| 0.628 |
| Tatoeba-test.pau-eng.pau.eng 	| 3.7 	| 0.173 |
| Tatoeba-test.pdc-eng.pdc.eng 	| 45.3 	| 0.569 |
| Tatoeba-test.pms-eng.pms.eng 	| 14.0 	| 0.345 |
| Tatoeba-test.pol-eng.pol.eng 	| 41.7 	| 0.588 |
| Tatoeba-test.por-eng.por.eng 	| 51.4 	| 0.669 |
| Tatoeba-test.ppl-eng.ppl.eng 	| 0.4 	| 0.134 |
| Tatoeba-test.prg-eng.prg.eng 	| 4.1 	| 0.198 |
| Tatoeba-test.pus-eng.pus.eng 	| 6.7 	| 0.233 |
| Tatoeba-test.quc-eng.quc.eng 	| 3.5 	| 0.091 |
| Tatoeba-test.qya-eng.qya.eng 	| 0.2 	| 0.090 |
| Tatoeba-test.rap-eng.rap.eng 	| 17.5 	| 0.230 |
| Tatoeba-test.rif-eng.rif.eng 	| 4.2 	| 0.164 |
| Tatoeba-test.roh-eng.roh.eng 	| 24.6 	| 0.464 |
| Tatoeba-test.rom-eng.rom.eng 	| 3.4 	| 0.212 |
| Tatoeba-test.ron-eng.ron.eng 	| 45.2 	| 0.620 |
| Tatoeba-test.rue-eng.rue.eng 	| 21.4 	| 0.390 |
| Tatoeba-test.run-eng.run.eng 	| 24.5 	| 0.392 |
| Tatoeba-test.rus-eng.rus.eng 	| 42.7 	| 0.591 |
| Tatoeba-test.sag-eng.sag.eng 	| 3.4 	| 0.187 |
| Tatoeba-test.sah-eng.sah.eng 	| 5.0 	| 0.177 |
| Tatoeba-test.san-eng.san.eng 	| 2.0 	| 0.172 |
| Tatoeba-test.scn-eng.scn.eng 	| 35.8 	| 0.410 |
| Tatoeba-test.sco-eng.sco.eng 	| 34.6 	| 0.520 |
| Tatoeba-test.sgs-eng.sgs.eng 	| 21.8 	| 0.299 |
| Tatoeba-test.shs-eng.shs.eng 	| 1.8 	| 0.122 |
| Tatoeba-test.shy-eng.shy.eng 	| 1.4 	| 0.104 |
| Tatoeba-test.sin-eng.sin.eng 	| 20.6 	| 0.429 |
| Tatoeba-test.sjn-eng.sjn.eng 	| 1.2 	| 0.095 |
| Tatoeba-test.slv-eng.slv.eng 	| 37.0 	| 0.545 |
| Tatoeba-test.sma-eng.sma.eng 	| 4.4 	| 0.147 |
| Tatoeba-test.sme-eng.sme.eng 	| 8.9 	| 0.229 |
| Tatoeba-test.smo-eng.smo.eng 	| 37.7 	| 0.483 |
| Tatoeba-test.sna-eng.sna.eng 	| 18.0 	| 0.359 |
| Tatoeba-test.snd-eng.snd.eng 	| 28.1 	| 0.444 |
| Tatoeba-test.som-eng.som.eng 	| 23.6 	| 0.472 |
| Tatoeba-test.spa-eng.spa.eng 	| 47.9 	| 0.645 |
| Tatoeba-test.sqi-eng.sqi.eng 	| 46.9 	| 0.634 |
| Tatoeba-test.stq-eng.stq.eng 	| 8.1 	| 0.379 |
| Tatoeba-test.sun-eng.sun.eng 	| 23.8 	| 0.369 |
| Tatoeba-test.swa-eng.swa.eng 	| 6.5 	| 0.193 |
| Tatoeba-test.swe-eng.swe.eng 	| 51.4 	| 0.655 |
| Tatoeba-test.swg-eng.swg.eng 	| 18.5 	| 0.342 |
| Tatoeba-test.tah-eng.tah.eng 	| 25.6 	| 0.249 |
| Tatoeba-test.tam-eng.tam.eng 	| 29.1 	| 0.437 |
| Tatoeba-test.tat-eng.tat.eng 	| 12.9 	| 0.327 |
| Tatoeba-test.tel-eng.tel.eng 	| 21.2 	| 0.386 |
| Tatoeba-test.tet-eng.tet.eng 	| 9.2 	| 0.215 |
| Tatoeba-test.tgk-eng.tgk.eng 	| 12.7 	| 0.374 |
| Tatoeba-test.tha-eng.tha.eng 	| 36.3 	| 0.531 |
| Tatoeba-test.tir-eng.tir.eng 	| 9.1 	| 0.267 |
| Tatoeba-test.tlh-eng.tlh.eng 	| 0.2 	| 0.084 |
| Tatoeba-test.tly-eng.tly.eng 	| 2.1 	| 0.128 |
| Tatoeba-test.toi-eng.toi.eng 	| 5.3 	| 0.150 |
| Tatoeba-test.ton-eng.ton.eng 	| 39.5 	| 0.473 |
| Tatoeba-test.tpw-eng.tpw.eng 	| 1.5 	| 0.160 |
| Tatoeba-test.tso-eng.tso.eng 	| 44.7 	| 0.526 |
| Tatoeba-test.tuk-eng.tuk.eng 	| 18.6 	| 0.401 |
| Tatoeba-test.tur-eng.tur.eng 	| 40.5 	| 0.573 |
| Tatoeba-test.tvl-eng.tvl.eng 	| 55.0 	| 0.593 |
| Tatoeba-test.tyv-eng.tyv.eng 	| 19.1 	| 0.477 |
| Tatoeba-test.tzl-eng.tzl.eng 	| 17.7 	| 0.333 |
| Tatoeba-test.udm-eng.udm.eng 	| 3.4 	| 0.217 |
| Tatoeba-test.uig-eng.uig.eng 	| 11.4 	| 0.289 |
| Tatoeba-test.ukr-eng.ukr.eng 	| 43.1 	| 0.595 |
| Tatoeba-test.umb-eng.umb.eng 	| 9.2 	| 0.260 |
| Tatoeba-test.urd-eng.urd.eng 	| 23.2 	| 0.426 |
| Tatoeba-test.uzb-eng.uzb.eng 	| 19.0 	| 0.342 |
| Tatoeba-test.vec-eng.vec.eng 	| 41.1 	| 0.409 |
| Tatoeba-test.vie-eng.vie.eng 	| 30.6 	| 0.481 |
| Tatoeba-test.vol-eng.vol.eng 	| 1.8 	| 0.143 |
| Tatoeba-test.war-eng.war.eng 	| 15.9 	| 0.352 |
| Tatoeba-test.wln-eng.wln.eng 	| 12.6 	| 0.291 |
| Tatoeba-test.wol-eng.wol.eng 	| 4.4 	| 0.138 |
| Tatoeba-test.xal-eng.xal.eng 	| 0.9 	| 0.153 |
| Tatoeba-test.xho-eng.xho.eng 	| 35.4 	| 0.513 |
| Tatoeba-test.yid-eng.yid.eng 	| 19.4 	| 0.387 |
| Tatoeba-test.yor-eng.yor.eng 	| 19.3 	| 0.327 |
| Tatoeba-test.zho-eng.zho.eng 	| 25.8 	| 0.448 |
| Tatoeba-test.zul-eng.zul.eng 	| 40.9 	| 0.567 |
| Tatoeba-test.zza-eng.zza.eng 	| 1.6 	| 0.125 |


### System Info: 
- hf_name: mul-eng

- source_languages: mul

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/mul-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ca', 'es', 'os', 'eo', 'ro', 'fy', 'cy', 'is', 'lb', 'su', 'an', 'sq', 'fr', 'ht', 'rm', 'cv', 'ig', 'am', 'eu', 'tr', 'ps', 'af', 'ny', 'ch', 'uk', 'sl', 'lt', 'tk', 'sg', 'ar', 'lg', 'bg', 'be', 'ka', 'gd', 'ja', 'si', 'br', 'mh', 'km', 'th', 'ty', 'rw', 'te', 'mk', 'or', 'wo', 'kl', 'mr', 'ru', 'yo', 'hu', 'fo', 'zh', 'ti', 'co', 'ee', 'oc', 'sn', 'mt', 'ts', 'pl', 'gl', 'nb', 'bn', 'tt', 'bo', 'lo', 'id', 'gn', 'nv', 'hy', 'kn', 'to', 'io', 'so', 'vi', 'da', 'fj', 'gv', 'sm', 'nl', 'mi', 'pt', 'hi', 'se', 'as', 'ta', 'et', 'kw', 'ga', 'sv', 'ln', 'na', 'mn', 'gu', 'wa', 'lv', 'jv', 'el', 'my', 'ba', 'it', 'hr', 'ur', 'ce', 'nn', 'fi', 'mg', 'rn', 'xh', 'ab', 'de', 'cs', 'he', 'zu', 'yi', 'ml', 'mul', 'en']

- src_constituents: {'sjn_Latn', 'cat', 'nan', 'spa', 'ile_Latn', 'pap', 'mwl', 'uzb_Latn', 'mww', 'hil', 'lij', 'avk_Latn', 'lad_Latn', 'lat_Latn', 'bos_Latn', 'oss', 'epo', 'ron', 'fry', 'cym', 'toi_Latn', 'awa', 'swg', 'zsm_Latn', 'zho_Hant', 'gcf_Latn', 'uzb_Cyrl', 'isl', 'lfn_Latn', 'shs_Latn', 'nov_Latn', 'bho', 'ltz', 'lzh', 'kur_Latn', 'sun', 'arg', 'pes_Thaa', 'sqi', 'uig_Arab', 'csb_Latn', 'fra', 'hat', 'liv_Latn', 'non_Latn', 'sco', 'cmn_Hans', 'pnb', 'roh', 'chv', 'ibo', 'bul_Latn', 'amh', 'lfn_Cyrl', 'eus', 'fkv_Latn', 'tur', 'pus', 'afr', 'brx_Latn', 'nya', 'acm', 'ota_Latn', 'cha', 'ukr', 'xal', 'slv', 'lit', 'zho_Hans', 'tmw_Latn', 'kjh', 'ota_Arab', 'war', 'tuk', 'sag', 'myv', 'hsb', 'lzh_Hans', 'ara', 'tly_Latn', 'lug', 'brx', 'bul', 'bel', 'vol_Latn', 'kat', 'gan', 'got_Goth', 'vro', 'ext', 'afh_Latn', 'gla', 'jpn', 'udm', 'mai', 'ary', 'sin', 'tvl', 'hif_Latn', 'cjy_Hant', 'bre', 'ceb', 'mah', 'nob_Hebr', 'crh_Latn', 'prg_Latn', 'khm', 'ang_Latn', 'tha', 'tah', 'tzl', 'aln', 'kin', 'tel', 'ady', 'mkd', 'ori', 'wol', 'aze_Latn', 'jbo', 'niu', 'kal', 'mar', 'vie_Hani', 'arz', 'yue', 'kha', 'san_Deva', 'jbo_Latn', 'gos', 'hau_Latn', 'rus', 'quc', 'cmn', 'yor', 'hun', 'uig_Cyrl', 'fao', 'mnw', 'zho', 'orv_Cyrl', 'iba', 'bel_Latn', 'tir', 'afb', 'crh', 'mic', 'cos', 'swh', 'sah', 'krl', 'ewe', 'apc', 'zza', 'chr', 'grc_Grek', 'tpw_Latn', 'oci', 'mfe', 'sna', 'kir_Cyrl', 'tat_Latn', 'gom', 'ido_Latn', 'sgs', 'pau', 'tgk_Cyrl', 'nog', 'mlt', 'pdc', 'tso', 'srp_Cyrl', 'pol', 'ast', 'glg', 'pms', 'fuc', 'nob', 'qya', 'ben', 'tat', 'kab', 'min', 'srp_Latn', 'wuu', 'dtp', 'jbo_Cyrl', 'tet', 'bod', 'yue_Hans', 'zlm_Latn', 'lao', 'ind', 'grn', 'nav', 'kaz_Cyrl', 'rom', 'hye', 'kan', 'ton', 'ido', 'mhr', 'scn', 'som', 'rif_Latn', 'vie', 'enm_Latn', 'lmo', 'npi', 'pes', 'dan', 'fij', 'ina_Latn', 'cjy_Hans', 'jdt_Cyrl', 'gsw', 'glv', 'khm_Latn', 'smo', 'umb', 'sma', 'gil', 'nld', 'snd_Arab', 'arq', 'mri', 'kur_Arab', 'por', 'hin', 'shy_Latn', 'sme', 'rap', 'tyv', 'dsb', 'moh', 'asm', 'lad', 'yue_Hant', 'kpv', 'tam', 'est', 'frm_Latn', 'hoc_Latn', 'bam_Latn', 'kek_Latn', 'ksh', 'tlh_Latn', 'ltg', 'pan_Guru', 'hnj_Latn', 'cor', 'gle', 'swe', 'lin', 'qya_Latn', 'kum', 'mad', 'cmn_Hant', 'fuv', 'nau', 'mon', 'akl_Latn', 'guj', 'kaz_Latn', 'wln', 'tuk_Latn', 'jav_Java', 'lav', 'jav', 'ell', 'frr', 'mya', 'bak', 'rue', 'ita', 'hrv', 'izh', 'ilo', 'dws_Latn', 'urd', 'stq', 'tat_Arab', 'haw', 'che', 'pag', 'nno', 'fin', 'mlg', 'ppl_Latn', 'run', 'xho', 'abk', 'deu', 'hoc', 'lkt', 'lld_Latn', 'tzl_Latn', 'mdf', 'ike_Latn', 'ces', 'ldn_Latn', 'egl', 'heb', 'vec', 'zul', 'max_Latn', 'pes_Latn', 'yid', 'mal', 'nds'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/mul-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/mul-eng/opus2m-2020-08-01.test.txt

- src_alpha3: mul

- tgt_alpha3: eng

- short_pair: mul-en

- chrF2_score: 0.518

- bleu: 34.7

- brevity_penalty: 1.0

- ref_len: 72346.0

- src_name: Multiple languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: mul

- tgt_alpha2: en

- prefer_old: False

- long_pair: mul-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41