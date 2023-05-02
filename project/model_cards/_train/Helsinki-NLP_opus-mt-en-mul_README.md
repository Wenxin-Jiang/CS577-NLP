---
language: 
- en
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

tags:
- translation

license: apache-2.0
---

### eng-mul

* source group: English 
* target group: Multiple languages 
*  OPUS readme: [eng-mul](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-mul/README.md)

*  model: transformer
* source language(s): eng
* target language(s): abk acm ady afb afh_Latn afr akl_Latn aln amh ang_Latn apc ara arg arq ary arz asm ast avk_Latn awa aze_Latn bak bam_Latn bel bel_Latn ben bho bod bos_Latn bre brx brx_Latn bul bul_Latn cat ceb ces cha che chr chv cjy_Hans cjy_Hant cmn cmn_Hans cmn_Hant cor cos crh crh_Latn csb_Latn cym dan deu dsb dtp dws_Latn egl ell enm_Latn epo est eus ewe ext fao fij fin fkv_Latn fra frm_Latn frr fry fuc fuv gan gcf_Latn gil gla gle glg glv gom gos got_Goth grc_Grek grn gsw guj hat hau_Latn haw heb hif_Latn hil hin hnj_Latn hoc hoc_Latn hrv hsb hun hye iba ibo ido ido_Latn ike_Latn ile_Latn ilo ina_Latn ind isl ita izh jav jav_Java jbo jbo_Cyrl jbo_Latn jdt_Cyrl jpn kab kal kan kat kaz_Cyrl kaz_Latn kek_Latn kha khm khm_Latn kin kir_Cyrl kjh kpv krl ksh kum kur_Arab kur_Latn lad lad_Latn lao lat_Latn lav ldn_Latn lfn_Cyrl lfn_Latn lij lin lit liv_Latn lkt lld_Latn lmo ltg ltz lug lzh lzh_Hans mad mah mai mal mar max_Latn mdf mfe mhr mic min mkd mlg mlt mnw moh mon mri mwl mww mya myv nan nau nav nds niu nld nno nob nob_Hebr nog non_Latn nov_Latn npi nya oci ori orv_Cyrl oss ota_Arab ota_Latn pag pan_Guru pap pau pdc pes pes_Latn pes_Thaa pms pnb pol por ppl_Latn prg_Latn pus quc qya qya_Latn rap rif_Latn roh rom ron rue run rus sag sah san_Deva scn sco sgs shs_Latn shy_Latn sin sjn_Latn slv sma sme smo sna snd_Arab som spa sqi srp_Cyrl srp_Latn stq sun swe swg swh tah tam tat tat_Arab tat_Latn tel tet tgk_Cyrl tha tir tlh_Latn tly_Latn tmw_Latn toi_Latn ton tpw_Latn tso tuk tuk_Latn tur tvl tyv tzl tzl_Latn udm uig_Arab uig_Cyrl ukr umb urd uzb_Cyrl uzb_Latn vec vie vie_Hani vol_Latn vro war wln wol wuu xal xho yid yor yue yue_Hans yue_Hant zho zho_Hans zho_Hant zlm_Latn zsm_Latn zul zza
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mul/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mul/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mul/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2014-enghin.eng.hin 	| 5.0 	| 0.288 |
| newsdev2015-enfi-engfin.eng.fin 	| 9.3 	| 0.418 |
| newsdev2016-enro-engron.eng.ron 	| 17.2 	| 0.488 |
| newsdev2016-entr-engtur.eng.tur 	| 8.2 	| 0.402 |
| newsdev2017-enlv-englav.eng.lav 	| 12.9 	| 0.444 |
| newsdev2017-enzh-engzho.eng.zho 	| 17.6 	| 0.170 |
| newsdev2018-enet-engest.eng.est 	| 10.9 	| 0.423 |
| newsdev2019-engu-engguj.eng.guj 	| 5.2 	| 0.284 |
| newsdev2019-enlt-englit.eng.lit 	| 11.0 	| 0.431 |
| newsdiscussdev2015-enfr-engfra.eng.fra 	| 22.6 	| 0.521 |
| newsdiscusstest2015-enfr-engfra.eng.fra 	| 25.9 	| 0.546 |
| newssyscomb2009-engces.eng.ces 	| 10.3 	| 0.394 |
| newssyscomb2009-engdeu.eng.deu 	| 13.3 	| 0.459 |
| newssyscomb2009-engfra.eng.fra 	| 21.5 	| 0.522 |
| newssyscomb2009-enghun.eng.hun 	| 8.1 	| 0.371 |
| newssyscomb2009-engita.eng.ita 	| 22.1 	| 0.540 |
| newssyscomb2009-engspa.eng.spa 	| 23.8 	| 0.531 |
| news-test2008-engces.eng.ces 	| 9.0 	| 0.376 |
| news-test2008-engdeu.eng.deu 	| 14.2 	| 0.451 |
| news-test2008-engfra.eng.fra 	| 19.8 	| 0.500 |
| news-test2008-engspa.eng.spa 	| 22.8 	| 0.518 |
| newstest2009-engces.eng.ces 	| 9.8 	| 0.392 |
| newstest2009-engdeu.eng.deu 	| 13.7 	| 0.454 |
| newstest2009-engfra.eng.fra 	| 20.7 	| 0.514 |
| newstest2009-enghun.eng.hun 	| 8.4 	| 0.370 |
| newstest2009-engita.eng.ita 	| 22.4 	| 0.538 |
| newstest2009-engspa.eng.spa 	| 23.5 	| 0.532 |
| newstest2010-engces.eng.ces 	| 10.0 	| 0.393 |
| newstest2010-engdeu.eng.deu 	| 15.2 	| 0.463 |
| newstest2010-engfra.eng.fra 	| 22.0 	| 0.524 |
| newstest2010-engspa.eng.spa 	| 27.2 	| 0.556 |
| newstest2011-engces.eng.ces 	| 10.8 	| 0.392 |
| newstest2011-engdeu.eng.deu 	| 14.2 	| 0.449 |
| newstest2011-engfra.eng.fra 	| 24.3 	| 0.544 |
| newstest2011-engspa.eng.spa 	| 28.3 	| 0.559 |
| newstest2012-engces.eng.ces 	| 9.9 	| 0.377 |
| newstest2012-engdeu.eng.deu 	| 14.3 	| 0.449 |
| newstest2012-engfra.eng.fra 	| 23.2 	| 0.530 |
| newstest2012-engrus.eng.rus 	| 16.0 	| 0.463 |
| newstest2012-engspa.eng.spa 	| 27.8 	| 0.555 |
| newstest2013-engces.eng.ces 	| 11.0 	| 0.392 |
| newstest2013-engdeu.eng.deu 	| 16.4 	| 0.469 |
| newstest2013-engfra.eng.fra 	| 22.6 	| 0.515 |
| newstest2013-engrus.eng.rus 	| 12.1 	| 0.414 |
| newstest2013-engspa.eng.spa 	| 24.9 	| 0.532 |
| newstest2014-hien-enghin.eng.hin 	| 7.2 	| 0.311 |
| newstest2015-encs-engces.eng.ces 	| 10.9 	| 0.396 |
| newstest2015-ende-engdeu.eng.deu 	| 18.3 	| 0.490 |
| newstest2015-enfi-engfin.eng.fin 	| 10.1 	| 0.421 |
| newstest2015-enru-engrus.eng.rus 	| 14.5 	| 0.445 |
| newstest2016-encs-engces.eng.ces 	| 12.2 	| 0.408 |
| newstest2016-ende-engdeu.eng.deu 	| 21.4 	| 0.517 |
| newstest2016-enfi-engfin.eng.fin 	| 11.2 	| 0.435 |
| newstest2016-enro-engron.eng.ron 	| 16.6 	| 0.472 |
| newstest2016-enru-engrus.eng.rus 	| 13.4 	| 0.435 |
| newstest2016-entr-engtur.eng.tur 	| 8.1 	| 0.385 |
| newstest2017-encs-engces.eng.ces 	| 9.6 	| 0.377 |
| newstest2017-ende-engdeu.eng.deu 	| 17.9 	| 0.482 |
| newstest2017-enfi-engfin.eng.fin 	| 11.8 	| 0.440 |
| newstest2017-enlv-englav.eng.lav 	| 9.6 	| 0.412 |
| newstest2017-enru-engrus.eng.rus 	| 14.1 	| 0.446 |
| newstest2017-entr-engtur.eng.tur 	| 8.0 	| 0.378 |
| newstest2017-enzh-engzho.eng.zho 	| 16.8 	| 0.175 |
| newstest2018-encs-engces.eng.ces 	| 9.8 	| 0.380 |
| newstest2018-ende-engdeu.eng.deu 	| 23.8 	| 0.536 |
| newstest2018-enet-engest.eng.est 	| 11.8 	| 0.433 |
| newstest2018-enfi-engfin.eng.fin 	| 7.8 	| 0.398 |
| newstest2018-enru-engrus.eng.rus 	| 12.2 	| 0.434 |
| newstest2018-entr-engtur.eng.tur 	| 7.5 	| 0.383 |
| newstest2018-enzh-engzho.eng.zho 	| 18.3 	| 0.179 |
| newstest2019-encs-engces.eng.ces 	| 10.7 	| 0.389 |
| newstest2019-ende-engdeu.eng.deu 	| 21.0 	| 0.512 |
| newstest2019-enfi-engfin.eng.fin 	| 10.4 	| 0.420 |
| newstest2019-engu-engguj.eng.guj 	| 5.8 	| 0.297 |
| newstest2019-enlt-englit.eng.lit 	| 8.0 	| 0.388 |
| newstest2019-enru-engrus.eng.rus 	| 13.0 	| 0.415 |
| newstest2019-enzh-engzho.eng.zho 	| 15.0 	| 0.192 |
| newstestB2016-enfi-engfin.eng.fin 	| 9.0 	| 0.414 |
| newstestB2017-enfi-engfin.eng.fin 	| 9.5 	| 0.415 |
| Tatoeba-test.eng-abk.eng.abk 	| 4.2 	| 0.275 |
| Tatoeba-test.eng-ady.eng.ady 	| 0.4 	| 0.006 |
| Tatoeba-test.eng-afh.eng.afh 	| 1.0 	| 0.058 |
| Tatoeba-test.eng-afr.eng.afr 	| 47.0 	| 0.663 |
| Tatoeba-test.eng-akl.eng.akl 	| 2.7 	| 0.080 |
| Tatoeba-test.eng-amh.eng.amh 	| 8.5 	| 0.455 |
| Tatoeba-test.eng-ang.eng.ang 	| 6.2 	| 0.138 |
| Tatoeba-test.eng-ara.eng.ara 	| 6.3 	| 0.325 |
| Tatoeba-test.eng-arg.eng.arg 	| 1.5 	| 0.107 |
| Tatoeba-test.eng-asm.eng.asm 	| 2.1 	| 0.265 |
| Tatoeba-test.eng-ast.eng.ast 	| 15.7 	| 0.393 |
| Tatoeba-test.eng-avk.eng.avk 	| 0.2 	| 0.095 |
| Tatoeba-test.eng-awa.eng.awa 	| 0.1 	| 0.002 |
| Tatoeba-test.eng-aze.eng.aze 	| 19.0 	| 0.500 |
| Tatoeba-test.eng-bak.eng.bak 	| 12.7 	| 0.379 |
| Tatoeba-test.eng-bam.eng.bam 	| 8.3 	| 0.037 |
| Tatoeba-test.eng-bel.eng.bel 	| 13.5 	| 0.396 |
| Tatoeba-test.eng-ben.eng.ben 	| 10.0 	| 0.383 |
| Tatoeba-test.eng-bho.eng.bho 	| 0.1 	| 0.003 |
| Tatoeba-test.eng-bod.eng.bod 	| 0.0 	| 0.147 |
| Tatoeba-test.eng-bre.eng.bre 	| 7.6 	| 0.275 |
| Tatoeba-test.eng-brx.eng.brx 	| 0.8 	| 0.060 |
| Tatoeba-test.eng-bul.eng.bul 	| 32.1 	| 0.542 |
| Tatoeba-test.eng-cat.eng.cat 	| 37.0 	| 0.595 |
| Tatoeba-test.eng-ceb.eng.ceb 	| 9.6 	| 0.409 |
| Tatoeba-test.eng-ces.eng.ces 	| 24.0 	| 0.475 |
| Tatoeba-test.eng-cha.eng.cha 	| 3.9 	| 0.228 |
| Tatoeba-test.eng-che.eng.che 	| 0.7 	| 0.013 |
| Tatoeba-test.eng-chm.eng.chm 	| 2.6 	| 0.212 |
| Tatoeba-test.eng-chr.eng.chr 	| 6.0 	| 0.190 |
| Tatoeba-test.eng-chv.eng.chv 	| 6.5 	| 0.369 |
| Tatoeba-test.eng-cor.eng.cor 	| 0.9 	| 0.086 |
| Tatoeba-test.eng-cos.eng.cos 	| 4.2 	| 0.174 |
| Tatoeba-test.eng-crh.eng.crh 	| 9.9 	| 0.361 |
| Tatoeba-test.eng-csb.eng.csb 	| 3.4 	| 0.230 |
| Tatoeba-test.eng-cym.eng.cym 	| 18.0 	| 0.418 |
| Tatoeba-test.eng-dan.eng.dan 	| 42.5 	| 0.624 |
| Tatoeba-test.eng-deu.eng.deu 	| 25.2 	| 0.505 |
| Tatoeba-test.eng-dsb.eng.dsb 	| 0.9 	| 0.121 |
| Tatoeba-test.eng-dtp.eng.dtp 	| 0.3 	| 0.084 |
| Tatoeba-test.eng-dws.eng.dws 	| 0.2 	| 0.040 |
| Tatoeba-test.eng-egl.eng.egl 	| 0.4 	| 0.085 |
| Tatoeba-test.eng-ell.eng.ell 	| 28.7 	| 0.543 |
| Tatoeba-test.eng-enm.eng.enm 	| 3.3 	| 0.295 |
| Tatoeba-test.eng-epo.eng.epo 	| 33.4 	| 0.570 |
| Tatoeba-test.eng-est.eng.est 	| 30.3 	| 0.545 |
| Tatoeba-test.eng-eus.eng.eus 	| 18.5 	| 0.486 |
| Tatoeba-test.eng-ewe.eng.ewe 	| 6.8 	| 0.272 |
| Tatoeba-test.eng-ext.eng.ext 	| 5.0 	| 0.228 |
| Tatoeba-test.eng-fao.eng.fao 	| 5.2 	| 0.277 |
| Tatoeba-test.eng-fas.eng.fas 	| 6.9 	| 0.265 |
| Tatoeba-test.eng-fij.eng.fij 	| 31.5 	| 0.365 |
| Tatoeba-test.eng-fin.eng.fin 	| 18.5 	| 0.459 |
| Tatoeba-test.eng-fkv.eng.fkv 	| 0.9 	| 0.132 |
| Tatoeba-test.eng-fra.eng.fra 	| 31.5 	| 0.546 |
| Tatoeba-test.eng-frm.eng.frm 	| 0.9 	| 0.128 |
| Tatoeba-test.eng-frr.eng.frr 	| 3.0 	| 0.025 |
| Tatoeba-test.eng-fry.eng.fry 	| 14.4 	| 0.387 |
| Tatoeba-test.eng-ful.eng.ful 	| 0.4 	| 0.061 |
| Tatoeba-test.eng-gcf.eng.gcf 	| 0.3 	| 0.075 |
| Tatoeba-test.eng-gil.eng.gil 	| 47.4 	| 0.706 |
| Tatoeba-test.eng-gla.eng.gla 	| 10.9 	| 0.341 |
| Tatoeba-test.eng-gle.eng.gle 	| 26.8 	| 0.493 |
| Tatoeba-test.eng-glg.eng.glg 	| 32.5 	| 0.565 |
| Tatoeba-test.eng-glv.eng.glv 	| 21.5 	| 0.395 |
| Tatoeba-test.eng-gos.eng.gos 	| 0.3 	| 0.124 |
| Tatoeba-test.eng-got.eng.got 	| 0.2 	| 0.010 |
| Tatoeba-test.eng-grc.eng.grc 	| 0.0 	| 0.005 |
| Tatoeba-test.eng-grn.eng.grn 	| 1.5 	| 0.129 |
| Tatoeba-test.eng-gsw.eng.gsw 	| 0.6 	| 0.106 |
| Tatoeba-test.eng-guj.eng.guj 	| 15.4 	| 0.347 |
| Tatoeba-test.eng-hat.eng.hat 	| 31.1 	| 0.527 |
| Tatoeba-test.eng-hau.eng.hau 	| 6.5 	| 0.385 |
| Tatoeba-test.eng-haw.eng.haw 	| 0.2 	| 0.066 |
| Tatoeba-test.eng-hbs.eng.hbs 	| 28.7 	| 0.531 |
| Tatoeba-test.eng-heb.eng.heb 	| 21.3 	| 0.443 |
| Tatoeba-test.eng-hif.eng.hif 	| 2.8 	| 0.268 |
| Tatoeba-test.eng-hil.eng.hil 	| 12.0 	| 0.463 |
| Tatoeba-test.eng-hin.eng.hin 	| 13.0 	| 0.401 |
| Tatoeba-test.eng-hmn.eng.hmn 	| 0.2 	| 0.073 |
| Tatoeba-test.eng-hoc.eng.hoc 	| 0.2 	| 0.077 |
| Tatoeba-test.eng-hsb.eng.hsb 	| 5.7 	| 0.308 |
| Tatoeba-test.eng-hun.eng.hun 	| 17.1 	| 0.431 |
| Tatoeba-test.eng-hye.eng.hye 	| 15.0 	| 0.378 |
| Tatoeba-test.eng-iba.eng.iba 	| 16.0 	| 0.437 |
| Tatoeba-test.eng-ibo.eng.ibo 	| 2.9 	| 0.221 |
| Tatoeba-test.eng-ido.eng.ido 	| 11.5 	| 0.403 |
| Tatoeba-test.eng-iku.eng.iku 	| 2.3 	| 0.089 |
| Tatoeba-test.eng-ile.eng.ile 	| 4.3 	| 0.282 |
| Tatoeba-test.eng-ilo.eng.ilo 	| 26.4 	| 0.522 |
| Tatoeba-test.eng-ina.eng.ina 	| 20.9 	| 0.493 |
| Tatoeba-test.eng-isl.eng.isl 	| 12.5 	| 0.375 |
| Tatoeba-test.eng-ita.eng.ita 	| 33.9 	| 0.592 |
| Tatoeba-test.eng-izh.eng.izh 	| 4.6 	| 0.050 |
| Tatoeba-test.eng-jav.eng.jav 	| 7.8 	| 0.328 |
| Tatoeba-test.eng-jbo.eng.jbo 	| 0.1 	| 0.123 |
| Tatoeba-test.eng-jdt.eng.jdt 	| 6.4 	| 0.008 |
| Tatoeba-test.eng-jpn.eng.jpn 	| 0.0 	| 0.000 |
| Tatoeba-test.eng-kab.eng.kab 	| 5.9 	| 0.261 |
| Tatoeba-test.eng-kal.eng.kal 	| 13.4 	| 0.382 |
| Tatoeba-test.eng-kan.eng.kan 	| 4.8 	| 0.358 |
| Tatoeba-test.eng-kat.eng.kat 	| 1.8 	| 0.115 |
| Tatoeba-test.eng-kaz.eng.kaz 	| 8.8 	| 0.354 |
| Tatoeba-test.eng-kek.eng.kek 	| 3.7 	| 0.188 |
| Tatoeba-test.eng-kha.eng.kha 	| 0.5 	| 0.094 |
| Tatoeba-test.eng-khm.eng.khm 	| 0.4 	| 0.243 |
| Tatoeba-test.eng-kin.eng.kin 	| 5.2 	| 0.362 |
| Tatoeba-test.eng-kir.eng.kir 	| 17.2 	| 0.416 |
| Tatoeba-test.eng-kjh.eng.kjh 	| 0.6 	| 0.009 |
| Tatoeba-test.eng-kok.eng.kok 	| 5.5 	| 0.005 |
| Tatoeba-test.eng-kom.eng.kom 	| 2.4 	| 0.012 |
| Tatoeba-test.eng-krl.eng.krl 	| 2.0 	| 0.099 |
| Tatoeba-test.eng-ksh.eng.ksh 	| 0.4 	| 0.074 |
| Tatoeba-test.eng-kum.eng.kum 	| 0.9 	| 0.007 |
| Tatoeba-test.eng-kur.eng.kur 	| 9.1 	| 0.174 |
| Tatoeba-test.eng-lad.eng.lad 	| 1.2 	| 0.154 |
| Tatoeba-test.eng-lah.eng.lah 	| 0.1 	| 0.001 |
| Tatoeba-test.eng-lao.eng.lao 	| 0.6 	| 0.426 |
| Tatoeba-test.eng-lat.eng.lat 	| 8.2 	| 0.366 |
| Tatoeba-test.eng-lav.eng.lav 	| 20.4 	| 0.475 |
| Tatoeba-test.eng-ldn.eng.ldn 	| 0.3 	| 0.059 |
| Tatoeba-test.eng-lfn.eng.lfn 	| 0.5 	| 0.104 |
| Tatoeba-test.eng-lij.eng.lij 	| 0.2 	| 0.094 |
| Tatoeba-test.eng-lin.eng.lin 	| 1.2 	| 0.276 |
| Tatoeba-test.eng-lit.eng.lit 	| 17.4 	| 0.488 |
| Tatoeba-test.eng-liv.eng.liv 	| 0.3 	| 0.039 |
| Tatoeba-test.eng-lkt.eng.lkt 	| 0.3 	| 0.041 |
| Tatoeba-test.eng-lld.eng.lld 	| 0.1 	| 0.083 |
| Tatoeba-test.eng-lmo.eng.lmo 	| 1.4 	| 0.154 |
| Tatoeba-test.eng-ltz.eng.ltz 	| 19.1 	| 0.395 |
| Tatoeba-test.eng-lug.eng.lug 	| 4.2 	| 0.382 |
| Tatoeba-test.eng-mad.eng.mad 	| 2.1 	| 0.075 |
| Tatoeba-test.eng-mah.eng.mah 	| 9.5 	| 0.331 |
| Tatoeba-test.eng-mai.eng.mai 	| 9.3 	| 0.372 |
| Tatoeba-test.eng-mal.eng.mal 	| 8.3 	| 0.437 |
| Tatoeba-test.eng-mar.eng.mar 	| 13.5 	| 0.410 |
| Tatoeba-test.eng-mdf.eng.mdf 	| 2.3 	| 0.008 |
| Tatoeba-test.eng-mfe.eng.mfe 	| 83.6 	| 0.905 |
| Tatoeba-test.eng-mic.eng.mic 	| 7.6 	| 0.214 |
| Tatoeba-test.eng-mkd.eng.mkd 	| 31.8 	| 0.540 |
| Tatoeba-test.eng-mlg.eng.mlg 	| 31.3 	| 0.464 |
| Tatoeba-test.eng-mlt.eng.mlt 	| 11.7 	| 0.427 |
| Tatoeba-test.eng-mnw.eng.mnw 	| 0.1 	| 0.000 |
| Tatoeba-test.eng-moh.eng.moh 	| 0.6 	| 0.067 |
| Tatoeba-test.eng-mon.eng.mon 	| 8.5 	| 0.323 |
| Tatoeba-test.eng-mri.eng.mri 	| 8.5 	| 0.320 |
| Tatoeba-test.eng-msa.eng.msa 	| 24.5 	| 0.498 |
| Tatoeba-test.eng.multi 	| 22.4 	| 0.451 |
| Tatoeba-test.eng-mwl.eng.mwl 	| 3.8 	| 0.169 |
| Tatoeba-test.eng-mya.eng.mya 	| 0.2 	| 0.123 |
| Tatoeba-test.eng-myv.eng.myv 	| 1.1 	| 0.014 |
| Tatoeba-test.eng-nau.eng.nau 	| 0.6 	| 0.109 |
| Tatoeba-test.eng-nav.eng.nav 	| 1.8 	| 0.149 |
| Tatoeba-test.eng-nds.eng.nds 	| 11.3 	| 0.365 |
| Tatoeba-test.eng-nep.eng.nep 	| 0.5 	| 0.004 |
| Tatoeba-test.eng-niu.eng.niu 	| 34.4 	| 0.501 |
| Tatoeba-test.eng-nld.eng.nld 	| 37.6 	| 0.598 |
| Tatoeba-test.eng-nog.eng.nog 	| 0.2 	| 0.010 |
| Tatoeba-test.eng-non.eng.non 	| 0.2 	| 0.096 |
| Tatoeba-test.eng-nor.eng.nor 	| 36.3 	| 0.577 |
| Tatoeba-test.eng-nov.eng.nov 	| 0.9 	| 0.180 |
| Tatoeba-test.eng-nya.eng.nya 	| 9.8 	| 0.524 |
| Tatoeba-test.eng-oci.eng.oci 	| 6.3 	| 0.288 |
| Tatoeba-test.eng-ori.eng.ori 	| 5.3 	| 0.273 |
| Tatoeba-test.eng-orv.eng.orv 	| 0.2 	| 0.007 |
| Tatoeba-test.eng-oss.eng.oss 	| 3.0 	| 0.230 |
| Tatoeba-test.eng-ota.eng.ota 	| 0.2 	| 0.053 |
| Tatoeba-test.eng-pag.eng.pag 	| 20.2 	| 0.513 |
| Tatoeba-test.eng-pan.eng.pan 	| 6.4 	| 0.301 |
| Tatoeba-test.eng-pap.eng.pap 	| 44.7 	| 0.624 |
| Tatoeba-test.eng-pau.eng.pau 	| 0.8 	| 0.098 |
| Tatoeba-test.eng-pdc.eng.pdc 	| 2.9 	| 0.143 |
| Tatoeba-test.eng-pms.eng.pms 	| 0.6 	| 0.124 |
| Tatoeba-test.eng-pol.eng.pol 	| 22.7 	| 0.500 |
| Tatoeba-test.eng-por.eng.por 	| 31.6 	| 0.570 |
| Tatoeba-test.eng-ppl.eng.ppl 	| 0.5 	| 0.085 |
| Tatoeba-test.eng-prg.eng.prg 	| 0.1 	| 0.078 |
| Tatoeba-test.eng-pus.eng.pus 	| 0.9 	| 0.137 |
| Tatoeba-test.eng-quc.eng.quc 	| 2.7 	| 0.255 |
| Tatoeba-test.eng-qya.eng.qya 	| 0.4 	| 0.084 |
| Tatoeba-test.eng-rap.eng.rap 	| 1.9 	| 0.050 |
| Tatoeba-test.eng-rif.eng.rif 	| 1.3 	| 0.102 |
| Tatoeba-test.eng-roh.eng.roh 	| 1.4 	| 0.169 |
| Tatoeba-test.eng-rom.eng.rom 	| 7.8 	| 0.329 |
| Tatoeba-test.eng-ron.eng.ron 	| 27.0 	| 0.530 |
| Tatoeba-test.eng-rue.eng.rue 	| 0.1 	| 0.009 |
| Tatoeba-test.eng-run.eng.run 	| 9.8 	| 0.434 |
| Tatoeba-test.eng-rus.eng.rus 	| 22.2 	| 0.465 |
| Tatoeba-test.eng-sag.eng.sag 	| 4.8 	| 0.155 |
| Tatoeba-test.eng-sah.eng.sah 	| 0.2 	| 0.007 |
| Tatoeba-test.eng-san.eng.san 	| 1.7 	| 0.143 |
| Tatoeba-test.eng-scn.eng.scn 	| 1.5 	| 0.083 |
| Tatoeba-test.eng-sco.eng.sco 	| 30.3 	| 0.514 |
| Tatoeba-test.eng-sgs.eng.sgs 	| 1.6 	| 0.104 |
| Tatoeba-test.eng-shs.eng.shs 	| 0.7 	| 0.049 |
| Tatoeba-test.eng-shy.eng.shy 	| 0.6 	| 0.064 |
| Tatoeba-test.eng-sin.eng.sin 	| 5.4 	| 0.317 |
| Tatoeba-test.eng-sjn.eng.sjn 	| 0.3 	| 0.074 |
| Tatoeba-test.eng-slv.eng.slv 	| 12.8 	| 0.313 |
| Tatoeba-test.eng-sma.eng.sma 	| 0.8 	| 0.063 |
| Tatoeba-test.eng-sme.eng.sme 	| 13.2 	| 0.290 |
| Tatoeba-test.eng-smo.eng.smo 	| 12.1 	| 0.416 |
| Tatoeba-test.eng-sna.eng.sna 	| 27.1 	| 0.533 |
| Tatoeba-test.eng-snd.eng.snd 	| 6.0 	| 0.359 |
| Tatoeba-test.eng-som.eng.som 	| 16.0 	| 0.274 |
| Tatoeba-test.eng-spa.eng.spa 	| 36.7 	| 0.603 |
| Tatoeba-test.eng-sqi.eng.sqi 	| 32.3 	| 0.573 |
| Tatoeba-test.eng-stq.eng.stq 	| 0.6 	| 0.198 |
| Tatoeba-test.eng-sun.eng.sun 	| 39.0 	| 0.447 |
| Tatoeba-test.eng-swa.eng.swa 	| 1.1 	| 0.109 |
| Tatoeba-test.eng-swe.eng.swe 	| 42.7 	| 0.614 |
| Tatoeba-test.eng-swg.eng.swg 	| 0.6 	| 0.118 |
| Tatoeba-test.eng-tah.eng.tah 	| 12.4 	| 0.294 |
| Tatoeba-test.eng-tam.eng.tam 	| 5.0 	| 0.404 |
| Tatoeba-test.eng-tat.eng.tat 	| 9.9 	| 0.326 |
| Tatoeba-test.eng-tel.eng.tel 	| 4.7 	| 0.326 |
| Tatoeba-test.eng-tet.eng.tet 	| 0.7 	| 0.100 |
| Tatoeba-test.eng-tgk.eng.tgk 	| 5.5 	| 0.304 |
| Tatoeba-test.eng-tha.eng.tha 	| 2.2 	| 0.456 |
| Tatoeba-test.eng-tir.eng.tir 	| 1.5 	| 0.197 |
| Tatoeba-test.eng-tlh.eng.tlh 	| 0.0 	| 0.032 |
| Tatoeba-test.eng-tly.eng.tly 	| 0.3 	| 0.061 |
| Tatoeba-test.eng-toi.eng.toi 	| 8.3 	| 0.219 |
| Tatoeba-test.eng-ton.eng.ton 	| 32.7 	| 0.619 |
| Tatoeba-test.eng-tpw.eng.tpw 	| 1.4 	| 0.136 |
| Tatoeba-test.eng-tso.eng.tso 	| 9.6 	| 0.465 |
| Tatoeba-test.eng-tuk.eng.tuk 	| 9.4 	| 0.383 |
| Tatoeba-test.eng-tur.eng.tur 	| 24.1 	| 0.542 |
| Tatoeba-test.eng-tvl.eng.tvl 	| 8.9 	| 0.398 |
| Tatoeba-test.eng-tyv.eng.tyv 	| 10.4 	| 0.249 |
| Tatoeba-test.eng-tzl.eng.tzl 	| 0.2 	| 0.098 |
| Tatoeba-test.eng-udm.eng.udm 	| 6.5 	| 0.212 |
| Tatoeba-test.eng-uig.eng.uig 	| 2.1 	| 0.266 |
| Tatoeba-test.eng-ukr.eng.ukr 	| 24.3 	| 0.479 |
| Tatoeba-test.eng-umb.eng.umb 	| 4.4 	| 0.274 |
| Tatoeba-test.eng-urd.eng.urd 	| 8.6 	| 0.344 |
| Tatoeba-test.eng-uzb.eng.uzb 	| 6.9 	| 0.343 |
| Tatoeba-test.eng-vec.eng.vec 	| 1.0 	| 0.094 |
| Tatoeba-test.eng-vie.eng.vie 	| 23.2 	| 0.420 |
| Tatoeba-test.eng-vol.eng.vol 	| 0.3 	| 0.086 |
| Tatoeba-test.eng-war.eng.war 	| 11.4 	| 0.415 |
| Tatoeba-test.eng-wln.eng.wln 	| 8.4 	| 0.218 |
| Tatoeba-test.eng-wol.eng.wol 	| 11.5 	| 0.252 |
| Tatoeba-test.eng-xal.eng.xal 	| 0.1 	| 0.007 |
| Tatoeba-test.eng-xho.eng.xho 	| 19.5 	| 0.552 |
| Tatoeba-test.eng-yid.eng.yid 	| 4.0 	| 0.256 |
| Tatoeba-test.eng-yor.eng.yor 	| 8.8 	| 0.247 |
| Tatoeba-test.eng-zho.eng.zho 	| 21.8 	| 0.192 |
| Tatoeba-test.eng-zul.eng.zul 	| 34.3 	| 0.655 |
| Tatoeba-test.eng-zza.eng.zza 	| 0.5 	| 0.080 |


### System Info: 
- hf_name: eng-mul

- source_languages: eng

- target_languages: mul

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-mul/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'ca', 'es', 'os', 'eo', 'ro', 'fy', 'cy', 'is', 'lb', 'su', 'an', 'sq', 'fr', 'ht', 'rm', 'cv', 'ig', 'am', 'eu', 'tr', 'ps', 'af', 'ny', 'ch', 'uk', 'sl', 'lt', 'tk', 'sg', 'ar', 'lg', 'bg', 'be', 'ka', 'gd', 'ja', 'si', 'br', 'mh', 'km', 'th', 'ty', 'rw', 'te', 'mk', 'or', 'wo', 'kl', 'mr', 'ru', 'yo', 'hu', 'fo', 'zh', 'ti', 'co', 'ee', 'oc', 'sn', 'mt', 'ts', 'pl', 'gl', 'nb', 'bn', 'tt', 'bo', 'lo', 'id', 'gn', 'nv', 'hy', 'kn', 'to', 'io', 'so', 'vi', 'da', 'fj', 'gv', 'sm', 'nl', 'mi', 'pt', 'hi', 'se', 'as', 'ta', 'et', 'kw', 'ga', 'sv', 'ln', 'na', 'mn', 'gu', 'wa', 'lv', 'jv', 'el', 'my', 'ba', 'it', 'hr', 'ur', 'ce', 'nn', 'fi', 'mg', 'rn', 'xh', 'ab', 'de', 'cs', 'he', 'zu', 'yi', 'ml', 'mul']

- src_constituents: {'eng'}

- tgt_constituents: {'sjn_Latn', 'cat', 'nan', 'spa', 'ile_Latn', 'pap', 'mwl', 'uzb_Latn', 'mww', 'hil', 'lij', 'avk_Latn', 'lad_Latn', 'lat_Latn', 'bos_Latn', 'oss', 'epo', 'ron', 'fry', 'cym', 'toi_Latn', 'awa', 'swg', 'zsm_Latn', 'zho_Hant', 'gcf_Latn', 'uzb_Cyrl', 'isl', 'lfn_Latn', 'shs_Latn', 'nov_Latn', 'bho', 'ltz', 'lzh', 'kur_Latn', 'sun', 'arg', 'pes_Thaa', 'sqi', 'uig_Arab', 'csb_Latn', 'fra', 'hat', 'liv_Latn', 'non_Latn', 'sco', 'cmn_Hans', 'pnb', 'roh', 'chv', 'ibo', 'bul_Latn', 'amh', 'lfn_Cyrl', 'eus', 'fkv_Latn', 'tur', 'pus', 'afr', 'brx_Latn', 'nya', 'acm', 'ota_Latn', 'cha', 'ukr', 'xal', 'slv', 'lit', 'zho_Hans', 'tmw_Latn', 'kjh', 'ota_Arab', 'war', 'tuk', 'sag', 'myv', 'hsb', 'lzh_Hans', 'ara', 'tly_Latn', 'lug', 'brx', 'bul', 'bel', 'vol_Latn', 'kat', 'gan', 'got_Goth', 'vro', 'ext', 'afh_Latn', 'gla', 'jpn', 'udm', 'mai', 'ary', 'sin', 'tvl', 'hif_Latn', 'cjy_Hant', 'bre', 'ceb', 'mah', 'nob_Hebr', 'crh_Latn', 'prg_Latn', 'khm', 'ang_Latn', 'tha', 'tah', 'tzl', 'aln', 'kin', 'tel', 'ady', 'mkd', 'ori', 'wol', 'aze_Latn', 'jbo', 'niu', 'kal', 'mar', 'vie_Hani', 'arz', 'yue', 'kha', 'san_Deva', 'jbo_Latn', 'gos', 'hau_Latn', 'rus', 'quc', 'cmn', 'yor', 'hun', 'uig_Cyrl', 'fao', 'mnw', 'zho', 'orv_Cyrl', 'iba', 'bel_Latn', 'tir', 'afb', 'crh', 'mic', 'cos', 'swh', 'sah', 'krl', 'ewe', 'apc', 'zza', 'chr', 'grc_Grek', 'tpw_Latn', 'oci', 'mfe', 'sna', 'kir_Cyrl', 'tat_Latn', 'gom', 'ido_Latn', 'sgs', 'pau', 'tgk_Cyrl', 'nog', 'mlt', 'pdc', 'tso', 'srp_Cyrl', 'pol', 'ast', 'glg', 'pms', 'fuc', 'nob', 'qya', 'ben', 'tat', 'kab', 'min', 'srp_Latn', 'wuu', 'dtp', 'jbo_Cyrl', 'tet', 'bod', 'yue_Hans', 'zlm_Latn', 'lao', 'ind', 'grn', 'nav', 'kaz_Cyrl', 'rom', 'hye', 'kan', 'ton', 'ido', 'mhr', 'scn', 'som', 'rif_Latn', 'vie', 'enm_Latn', 'lmo', 'npi', 'pes', 'dan', 'fij', 'ina_Latn', 'cjy_Hans', 'jdt_Cyrl', 'gsw', 'glv', 'khm_Latn', 'smo', 'umb', 'sma', 'gil', 'nld', 'snd_Arab', 'arq', 'mri', 'kur_Arab', 'por', 'hin', 'shy_Latn', 'sme', 'rap', 'tyv', 'dsb', 'moh', 'asm', 'lad', 'yue_Hant', 'kpv', 'tam', 'est', 'frm_Latn', 'hoc_Latn', 'bam_Latn', 'kek_Latn', 'ksh', 'tlh_Latn', 'ltg', 'pan_Guru', 'hnj_Latn', 'cor', 'gle', 'swe', 'lin', 'qya_Latn', 'kum', 'mad', 'cmn_Hant', 'fuv', 'nau', 'mon', 'akl_Latn', 'guj', 'kaz_Latn', 'wln', 'tuk_Latn', 'jav_Java', 'lav', 'jav', 'ell', 'frr', 'mya', 'bak', 'rue', 'ita', 'hrv', 'izh', 'ilo', 'dws_Latn', 'urd', 'stq', 'tat_Arab', 'haw', 'che', 'pag', 'nno', 'fin', 'mlg', 'ppl_Latn', 'run', 'xho', 'abk', 'deu', 'hoc', 'lkt', 'lld_Latn', 'tzl_Latn', 'mdf', 'ike_Latn', 'ces', 'ldn_Latn', 'egl', 'heb', 'vec', 'zul', 'max_Latn', 'pes_Latn', 'yid', 'mal', 'nds'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mul/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mul/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: mul

- short_pair: en-mul

- chrF2_score: 0.451

- bleu: 22.4

- brevity_penalty: 0.987

- ref_len: 68724.0

- src_name: English

- tgt_name: Multiple languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: mul

- prefer_old: False

- long_pair: eng-mul

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41