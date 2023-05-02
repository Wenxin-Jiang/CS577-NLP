---
language: 
- en
- ca
- es
- os
- ro
- fy
- cy
- sc
- is
- yi
- lb
- an
- sq
- fr
- ht
- rm
- ps
- af
- uk
- sl
- lt
- bg
- be
- gd
- si
- br
- mk
- or
- mr
- ru
- fo
- co
- oc
- pl
- gl
- nb
- bn
- id
- hy
- da
- gv
- nl
- pt
- hi
- as
- kw
- ga
- sv
- gu
- wa
- lv
- el
- it
- hr
- ur
- nn
- de
- cs
- ine

tags:
- translation

license: apache-2.0
---

### eng-ine

* source group: English 
* target group: Indo-European languages 
*  OPUS readme: [eng-ine](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-ine/README.md)

*  model: transformer
* source language(s): eng
* target language(s): afr aln ang_Latn arg asm ast awa bel bel_Latn ben bho bos_Latn bre bul bul_Latn cat ces cor cos csb_Latn cym dan deu dsb egl ell enm_Latn ext fao fra frm_Latn frr fry gcf_Latn gla gle glg glv gom gos got_Goth grc_Grek gsw guj hat hif_Latn hin hrv hsb hye ind isl ita jdt_Cyrl ksh kur_Arab kur_Latn lad lad_Latn lat_Latn lav lij lit lld_Latn lmo ltg ltz mai mar max_Latn mfe min mkd mwl nds nld nno nob nob_Hebr non_Latn npi oci ori orv_Cyrl oss pan_Guru pap pdc pes pes_Latn pes_Thaa pms pnb pol por prg_Latn pus roh rom ron rue rus san_Deva scn sco sgs sin slv snd_Arab spa sqi srp_Cyrl srp_Latn stq swe swg tgk_Cyrl tly_Latn tmw_Latn ukr urd vec wln yid zlm_Latn zsm_Latn zza
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ine/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ine/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ine/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2014-enghin.eng.hin 	| 6.2 	| 0.317 |
| newsdev2016-enro-engron.eng.ron 	| 22.1 	| 0.525 |
| newsdev2017-enlv-englav.eng.lav 	| 17.4 	| 0.486 |
| newsdev2019-engu-engguj.eng.guj 	| 6.5 	| 0.303 |
| newsdev2019-enlt-englit.eng.lit 	| 14.9 	| 0.476 |
| newsdiscussdev2015-enfr-engfra.eng.fra 	| 26.4 	| 0.547 |
| newsdiscusstest2015-enfr-engfra.eng.fra 	| 30.0 	| 0.575 |
| newssyscomb2009-engces.eng.ces 	| 14.7 	| 0.442 |
| newssyscomb2009-engdeu.eng.deu 	| 16.7 	| 0.487 |
| newssyscomb2009-engfra.eng.fra 	| 24.8 	| 0.547 |
| newssyscomb2009-engita.eng.ita 	| 25.2 	| 0.562 |
| newssyscomb2009-engspa.eng.spa 	| 27.0 	| 0.554 |
| news-test2008-engces.eng.ces 	| 13.0 	| 0.417 |
| news-test2008-engdeu.eng.deu 	| 17.4 	| 0.480 |
| news-test2008-engfra.eng.fra 	| 22.3 	| 0.519 |
| news-test2008-engspa.eng.spa 	| 24.9 	| 0.532 |
| newstest2009-engces.eng.ces 	| 13.6 	| 0.432 |
| newstest2009-engdeu.eng.deu 	| 16.6 	| 0.482 |
| newstest2009-engfra.eng.fra 	| 23.5 	| 0.535 |
| newstest2009-engita.eng.ita 	| 25.5 	| 0.561 |
| newstest2009-engspa.eng.spa 	| 26.3 	| 0.551 |
| newstest2010-engces.eng.ces 	| 14.2 	| 0.436 |
| newstest2010-engdeu.eng.deu 	| 18.3 	| 0.492 |
| newstest2010-engfra.eng.fra 	| 25.7 	| 0.550 |
| newstest2010-engspa.eng.spa 	| 30.5 	| 0.578 |
| newstest2011-engces.eng.ces 	| 15.1 	| 0.439 |
| newstest2011-engdeu.eng.deu 	| 17.1 	| 0.478 |
| newstest2011-engfra.eng.fra 	| 28.0 	| 0.569 |
| newstest2011-engspa.eng.spa 	| 31.9 	| 0.580 |
| newstest2012-engces.eng.ces 	| 13.6 	| 0.418 |
| newstest2012-engdeu.eng.deu 	| 17.0 	| 0.475 |
| newstest2012-engfra.eng.fra 	| 26.1 	| 0.553 |
| newstest2012-engrus.eng.rus 	| 21.4 	| 0.506 |
| newstest2012-engspa.eng.spa 	| 31.4 	| 0.577 |
| newstest2013-engces.eng.ces 	| 15.3 	| 0.438 |
| newstest2013-engdeu.eng.deu 	| 20.3 	| 0.501 |
| newstest2013-engfra.eng.fra 	| 26.0 	| 0.540 |
| newstest2013-engrus.eng.rus 	| 16.1 	| 0.449 |
| newstest2013-engspa.eng.spa 	| 28.6 	| 0.555 |
| newstest2014-hien-enghin.eng.hin 	| 9.5 	| 0.344 |
| newstest2015-encs-engces.eng.ces 	| 14.8 	| 0.440 |
| newstest2015-ende-engdeu.eng.deu 	| 22.6 	| 0.523 |
| newstest2015-enru-engrus.eng.rus 	| 18.8 	| 0.483 |
| newstest2016-encs-engces.eng.ces 	| 16.8 	| 0.457 |
| newstest2016-ende-engdeu.eng.deu 	| 26.2 	| 0.555 |
| newstest2016-enro-engron.eng.ron 	| 21.2 	| 0.510 |
| newstest2016-enru-engrus.eng.rus 	| 17.6 	| 0.471 |
| newstest2017-encs-engces.eng.ces 	| 13.6 	| 0.421 |
| newstest2017-ende-engdeu.eng.deu 	| 21.5 	| 0.516 |
| newstest2017-enlv-englav.eng.lav 	| 13.0 	| 0.452 |
| newstest2017-enru-engrus.eng.rus 	| 18.7 	| 0.486 |
| newstest2018-encs-engces.eng.ces 	| 13.5 	| 0.425 |
| newstest2018-ende-engdeu.eng.deu 	| 29.8 	| 0.581 |
| newstest2018-enru-engrus.eng.rus 	| 16.1 	| 0.472 |
| newstest2019-encs-engces.eng.ces 	| 14.8 	| 0.435 |
| newstest2019-ende-engdeu.eng.deu 	| 26.6 	| 0.554 |
| newstest2019-engu-engguj.eng.guj 	| 6.9 	| 0.313 |
| newstest2019-enlt-englit.eng.lit 	| 10.6 	| 0.429 |
| newstest2019-enru-engrus.eng.rus 	| 17.5 	| 0.452 |
| Tatoeba-test.eng-afr.eng.afr 	| 52.1 	| 0.708 |
| Tatoeba-test.eng-ang.eng.ang 	| 5.1 	| 0.131 |
| Tatoeba-test.eng-arg.eng.arg 	| 1.2 	| 0.099 |
| Tatoeba-test.eng-asm.eng.asm 	| 2.9 	| 0.259 |
| Tatoeba-test.eng-ast.eng.ast 	| 14.1 	| 0.408 |
| Tatoeba-test.eng-awa.eng.awa 	| 0.3 	| 0.002 |
| Tatoeba-test.eng-bel.eng.bel 	| 18.1 	| 0.450 |
| Tatoeba-test.eng-ben.eng.ben 	| 13.5 	| 0.432 |
| Tatoeba-test.eng-bho.eng.bho 	| 0.3 	| 0.003 |
| Tatoeba-test.eng-bre.eng.bre 	| 10.4 	| 0.318 |
| Tatoeba-test.eng-bul.eng.bul 	| 38.7 	| 0.592 |
| Tatoeba-test.eng-cat.eng.cat 	| 42.0 	| 0.633 |
| Tatoeba-test.eng-ces.eng.ces 	| 32.3 	| 0.546 |
| Tatoeba-test.eng-cor.eng.cor 	| 0.5 	| 0.079 |
| Tatoeba-test.eng-cos.eng.cos 	| 3.1 	| 0.148 |
| Tatoeba-test.eng-csb.eng.csb 	| 1.4 	| 0.216 |
| Tatoeba-test.eng-cym.eng.cym 	| 22.4 	| 0.470 |
| Tatoeba-test.eng-dan.eng.dan 	| 49.7 	| 0.671 |
| Tatoeba-test.eng-deu.eng.deu 	| 31.7 	| 0.554 |
| Tatoeba-test.eng-dsb.eng.dsb 	| 1.1 	| 0.139 |
| Tatoeba-test.eng-egl.eng.egl 	| 0.9 	| 0.089 |
| Tatoeba-test.eng-ell.eng.ell 	| 42.7 	| 0.640 |
| Tatoeba-test.eng-enm.eng.enm 	| 3.5 	| 0.259 |
| Tatoeba-test.eng-ext.eng.ext 	| 6.4 	| 0.235 |
| Tatoeba-test.eng-fao.eng.fao 	| 6.6 	| 0.285 |
| Tatoeba-test.eng-fas.eng.fas 	| 5.7 	| 0.257 |
| Tatoeba-test.eng-fra.eng.fra 	| 38.4 	| 0.595 |
| Tatoeba-test.eng-frm.eng.frm 	| 0.9 	| 0.149 |
| Tatoeba-test.eng-frr.eng.frr 	| 8.4 	| 0.145 |
| Tatoeba-test.eng-fry.eng.fry 	| 16.5 	| 0.411 |
| Tatoeba-test.eng-gcf.eng.gcf 	| 0.6 	| 0.098 |
| Tatoeba-test.eng-gla.eng.gla 	| 11.6 	| 0.361 |
| Tatoeba-test.eng-gle.eng.gle 	| 32.5 	| 0.546 |
| Tatoeba-test.eng-glg.eng.glg 	| 38.4 	| 0.602 |
| Tatoeba-test.eng-glv.eng.glv 	| 23.1 	| 0.418 |
| Tatoeba-test.eng-gos.eng.gos 	| 0.7 	| 0.137 |
| Tatoeba-test.eng-got.eng.got 	| 0.2 	| 0.010 |
| Tatoeba-test.eng-grc.eng.grc 	| 0.0 	| 0.005 |
| Tatoeba-test.eng-gsw.eng.gsw 	| 0.9 	| 0.108 |
| Tatoeba-test.eng-guj.eng.guj 	| 20.8 	| 0.391 |
| Tatoeba-test.eng-hat.eng.hat 	| 34.0 	| 0.537 |
| Tatoeba-test.eng-hbs.eng.hbs 	| 33.7 	| 0.567 |
| Tatoeba-test.eng-hif.eng.hif 	| 2.8 	| 0.269 |
| Tatoeba-test.eng-hin.eng.hin 	| 15.6 	| 0.437 |
| Tatoeba-test.eng-hsb.eng.hsb 	| 5.4 	| 0.320 |
| Tatoeba-test.eng-hye.eng.hye 	| 17.4 	| 0.426 |
| Tatoeba-test.eng-isl.eng.isl 	| 17.4 	| 0.436 |
| Tatoeba-test.eng-ita.eng.ita 	| 40.4 	| 0.636 |
| Tatoeba-test.eng-jdt.eng.jdt 	| 6.4 	| 0.008 |
| Tatoeba-test.eng-kok.eng.kok 	| 6.6 	| 0.005 |
| Tatoeba-test.eng-ksh.eng.ksh 	| 0.8 	| 0.123 |
| Tatoeba-test.eng-kur.eng.kur 	| 10.2 	| 0.209 |
| Tatoeba-test.eng-lad.eng.lad 	| 0.8 	| 0.163 |
| Tatoeba-test.eng-lah.eng.lah 	| 0.2 	| 0.001 |
| Tatoeba-test.eng-lat.eng.lat 	| 9.4 	| 0.372 |
| Tatoeba-test.eng-lav.eng.lav 	| 30.3 	| 0.559 |
| Tatoeba-test.eng-lij.eng.lij 	| 1.0 	| 0.130 |
| Tatoeba-test.eng-lit.eng.lit 	| 25.3 	| 0.560 |
| Tatoeba-test.eng-lld.eng.lld 	| 0.4 	| 0.139 |
| Tatoeba-test.eng-lmo.eng.lmo 	| 0.6 	| 0.108 |
| Tatoeba-test.eng-ltz.eng.ltz 	| 18.1 	| 0.388 |
| Tatoeba-test.eng-mai.eng.mai 	| 17.2 	| 0.464 |
| Tatoeba-test.eng-mar.eng.mar 	| 18.0 	| 0.451 |
| Tatoeba-test.eng-mfe.eng.mfe 	| 81.0 	| 0.899 |
| Tatoeba-test.eng-mkd.eng.mkd 	| 37.6 	| 0.587 |
| Tatoeba-test.eng-msa.eng.msa 	| 27.7 	| 0.519 |
| Tatoeba-test.eng.multi 	| 32.6 	| 0.539 |
| Tatoeba-test.eng-mwl.eng.mwl 	| 3.8 	| 0.134 |
| Tatoeba-test.eng-nds.eng.nds 	| 14.3 	| 0.401 |
| Tatoeba-test.eng-nep.eng.nep 	| 0.5 	| 0.002 |
| Tatoeba-test.eng-nld.eng.nld 	| 44.0 	| 0.642 |
| Tatoeba-test.eng-non.eng.non 	| 0.7 	| 0.118 |
| Tatoeba-test.eng-nor.eng.nor 	| 42.7 	| 0.623 |
| Tatoeba-test.eng-oci.eng.oci 	| 7.2 	| 0.295 |
| Tatoeba-test.eng-ori.eng.ori 	| 2.7 	| 0.257 |
| Tatoeba-test.eng-orv.eng.orv 	| 0.2 	| 0.008 |
| Tatoeba-test.eng-oss.eng.oss 	| 2.9 	| 0.264 |
| Tatoeba-test.eng-pan.eng.pan 	| 7.4 	| 0.337 |
| Tatoeba-test.eng-pap.eng.pap 	| 48.5 	| 0.656 |
| Tatoeba-test.eng-pdc.eng.pdc 	| 1.8 	| 0.145 |
| Tatoeba-test.eng-pms.eng.pms 	| 0.7 	| 0.136 |
| Tatoeba-test.eng-pol.eng.pol 	| 31.1 	| 0.563 |
| Tatoeba-test.eng-por.eng.por 	| 37.0 	| 0.605 |
| Tatoeba-test.eng-prg.eng.prg 	| 0.2 	| 0.100 |
| Tatoeba-test.eng-pus.eng.pus 	| 1.0 	| 0.134 |
| Tatoeba-test.eng-roh.eng.roh 	| 2.3 	| 0.236 |
| Tatoeba-test.eng-rom.eng.rom 	| 7.8 	| 0.340 |
| Tatoeba-test.eng-ron.eng.ron 	| 34.3 	| 0.585 |
| Tatoeba-test.eng-rue.eng.rue 	| 0.2 	| 0.010 |
| Tatoeba-test.eng-rus.eng.rus 	| 29.6 	| 0.526 |
| Tatoeba-test.eng-san.eng.san 	| 2.4 	| 0.125 |
| Tatoeba-test.eng-scn.eng.scn 	| 1.6 	| 0.079 |
| Tatoeba-test.eng-sco.eng.sco 	| 33.6 	| 0.562 |
| Tatoeba-test.eng-sgs.eng.sgs 	| 3.4 	| 0.114 |
| Tatoeba-test.eng-sin.eng.sin 	| 9.2 	| 0.349 |
| Tatoeba-test.eng-slv.eng.slv 	| 15.6 	| 0.334 |
| Tatoeba-test.eng-snd.eng.snd 	| 9.1 	| 0.324 |
| Tatoeba-test.eng-spa.eng.spa 	| 43.4 	| 0.645 |
| Tatoeba-test.eng-sqi.eng.sqi 	| 39.0 	| 0.621 |
| Tatoeba-test.eng-stq.eng.stq 	| 10.8 	| 0.373 |
| Tatoeba-test.eng-swe.eng.swe 	| 49.9 	| 0.663 |
| Tatoeba-test.eng-swg.eng.swg 	| 0.7 	| 0.137 |
| Tatoeba-test.eng-tgk.eng.tgk 	| 6.4 	| 0.346 |
| Tatoeba-test.eng-tly.eng.tly 	| 0.5 	| 0.055 |
| Tatoeba-test.eng-ukr.eng.ukr 	| 31.4 	| 0.536 |
| Tatoeba-test.eng-urd.eng.urd 	| 11.1 	| 0.389 |
| Tatoeba-test.eng-vec.eng.vec 	| 1.3 	| 0.110 |
| Tatoeba-test.eng-wln.eng.wln 	| 6.8 	| 0.233 |
| Tatoeba-test.eng-yid.eng.yid 	| 5.8 	| 0.295 |
| Tatoeba-test.eng-zza.eng.zza 	| 0.8 	| 0.086 |


### System Info: 
- hf_name: eng-ine

- source_languages: eng

- target_languages: ine

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-ine/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'ca', 'es', 'os', 'ro', 'fy', 'cy', 'sc', 'is', 'yi', 'lb', 'an', 'sq', 'fr', 'ht', 'rm', 'ps', 'af', 'uk', 'sl', 'lt', 'bg', 'be', 'gd', 'si', 'br', 'mk', 'or', 'mr', 'ru', 'fo', 'co', 'oc', 'pl', 'gl', 'nb', 'bn', 'id', 'hy', 'da', 'gv', 'nl', 'pt', 'hi', 'as', 'kw', 'ga', 'sv', 'gu', 'wa', 'lv', 'el', 'it', 'hr', 'ur', 'nn', 'de', 'cs', 'ine']

- src_constituents: {'eng'}

- tgt_constituents: {'cat', 'spa', 'pap', 'mwl', 'lij', 'bos_Latn', 'lad_Latn', 'lat_Latn', 'pcd', 'oss', 'ron', 'fry', 'cym', 'awa', 'swg', 'zsm_Latn', 'srd', 'gcf_Latn', 'isl', 'yid', 'bho', 'ltz', 'kur_Latn', 'arg', 'pes_Thaa', 'sqi', 'csb_Latn', 'fra', 'hat', 'non_Latn', 'sco', 'pnb', 'roh', 'bul_Latn', 'pus', 'afr', 'ukr', 'slv', 'lit', 'tmw_Latn', 'hsb', 'tly_Latn', 'bul', 'bel', 'got_Goth', 'lat_Grek', 'ext', 'gla', 'mai', 'sin', 'hif_Latn', 'eng', 'bre', 'nob_Hebr', 'prg_Latn', 'ang_Latn', 'aln', 'mkd', 'ori', 'mar', 'afr_Arab', 'san_Deva', 'gos', 'rus', 'fao', 'orv_Cyrl', 'bel_Latn', 'cos', 'zza', 'grc_Grek', 'oci', 'mfe', 'gom', 'bjn', 'sgs', 'tgk_Cyrl', 'hye_Latn', 'pdc', 'srp_Cyrl', 'pol', 'ast', 'glg', 'pms', 'nob', 'ben', 'min', 'srp_Latn', 'zlm_Latn', 'ind', 'rom', 'hye', 'scn', 'enm_Latn', 'lmo', 'npi', 'pes', 'dan', 'rus_Latn', 'jdt_Cyrl', 'gsw', 'glv', 'nld', 'snd_Arab', 'kur_Arab', 'por', 'hin', 'dsb', 'asm', 'lad', 'frm_Latn', 'ksh', 'pan_Guru', 'cor', 'gle', 'swe', 'guj', 'wln', 'lav', 'ell', 'frr', 'rue', 'ita', 'hrv', 'urd', 'stq', 'nno', 'deu', 'lld_Latn', 'ces', 'egl', 'vec', 'max_Latn', 'pes_Latn', 'ltg', 'nds'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ine/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ine/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: ine

- short_pair: en-ine

- chrF2_score: 0.539

- bleu: 32.6

- brevity_penalty: 0.973

- ref_len: 68664.0

- src_name: English

- tgt_name: Indo-European languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: ine

- prefer_old: False

- long_pair: eng-ine

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41