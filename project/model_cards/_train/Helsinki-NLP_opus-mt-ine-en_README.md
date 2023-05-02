---
language: 
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
- en
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

### ine-eng

* source group: Indo-European languages 
* target group: English 
*  OPUS readme: [ine-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ine-eng/README.md)

*  model: transformer
* source language(s): afr aln ang_Latn arg asm ast awa bel bel_Latn ben bho bos_Latn bre bul bul_Latn cat ces cor cos csb_Latn cym dan deu dsb egl ell enm_Latn ext fao fra frm_Latn frr fry gcf_Latn gla gle glg glv gom gos got_Goth grc_Grek gsw guj hat hif_Latn hin hrv hsb hye ind isl ita jdt_Cyrl ksh kur_Arab kur_Latn lad lad_Latn lat_Latn lav lij lit lld_Latn lmo ltg ltz mai mar max_Latn mfe min mkd mwl nds nld nno nob nob_Hebr non_Latn npi oci ori orv_Cyrl oss pan_Guru pap pdc pes pes_Latn pes_Thaa pms pnb pol por prg_Latn pus roh rom ron rue rus san_Deva scn sco sgs sin slv snd_Arab spa sqi srp_Cyrl srp_Latn stq swe swg tgk_Cyrl tly_Latn tmw_Latn ukr urd vec wln yid zlm_Latn zsm_Latn zza
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ine-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ine-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ine-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2014-hineng.hin.eng 	| 11.2 	| 0.375 |
| newsdev2016-enro-roneng.ron.eng 	| 35.5 	| 0.614 |
| newsdev2017-enlv-laveng.lav.eng 	| 25.1 	| 0.542 |
| newsdev2019-engu-gujeng.guj.eng 	| 16.0 	| 0.420 |
| newsdev2019-enlt-liteng.lit.eng 	| 24.0 	| 0.522 |
| newsdiscussdev2015-enfr-fraeng.fra.eng 	| 30.1 	| 0.550 |
| newsdiscusstest2015-enfr-fraeng.fra.eng 	| 33.4 	| 0.572 |
| newssyscomb2009-ceseng.ces.eng 	| 24.0 	| 0.520 |
| newssyscomb2009-deueng.deu.eng 	| 25.7 	| 0.526 |
| newssyscomb2009-fraeng.fra.eng 	| 27.9 	| 0.550 |
| newssyscomb2009-itaeng.ita.eng 	| 31.4 	| 0.574 |
| newssyscomb2009-spaeng.spa.eng 	| 28.3 	| 0.555 |
| news-test2008-deueng.deu.eng 	| 24.0 	| 0.515 |
| news-test2008-fraeng.fra.eng 	| 24.5 	| 0.524 |
| news-test2008-spaeng.spa.eng 	| 25.5 	| 0.533 |
| newstest2009-ceseng.ces.eng 	| 23.3 	| 0.516 |
| newstest2009-deueng.deu.eng 	| 23.2 	| 0.512 |
| newstest2009-fraeng.fra.eng 	| 27.3 	| 0.545 |
| newstest2009-itaeng.ita.eng 	| 30.3 	| 0.567 |
| newstest2009-spaeng.spa.eng 	| 27.9 	| 0.549 |
| newstest2010-ceseng.ces.eng 	| 23.8 	| 0.523 |
| newstest2010-deueng.deu.eng 	| 26.2 	| 0.545 |
| newstest2010-fraeng.fra.eng 	| 28.6 	| 0.562 |
| newstest2010-spaeng.spa.eng 	| 31.4 	| 0.581 |
| newstest2011-ceseng.ces.eng 	| 24.2 	| 0.521 |
| newstest2011-deueng.deu.eng 	| 23.9 	| 0.522 |
| newstest2011-fraeng.fra.eng 	| 29.5 	| 0.570 |
| newstest2011-spaeng.spa.eng 	| 30.3 	| 0.570 |
| newstest2012-ceseng.ces.eng 	| 23.5 	| 0.516 |
| newstest2012-deueng.deu.eng 	| 24.9 	| 0.529 |
| newstest2012-fraeng.fra.eng 	| 30.0 	| 0.568 |
| newstest2012-ruseng.rus.eng 	| 29.9 	| 0.565 |
| newstest2012-spaeng.spa.eng 	| 33.3 	| 0.593 |
| newstest2013-ceseng.ces.eng 	| 25.6 	| 0.531 |
| newstest2013-deueng.deu.eng 	| 27.7 	| 0.545 |
| newstest2013-fraeng.fra.eng 	| 30.0 	| 0.561 |
| newstest2013-ruseng.rus.eng 	| 24.4 	| 0.514 |
| newstest2013-spaeng.spa.eng 	| 30.8 	| 0.577 |
| newstest2014-csen-ceseng.ces.eng 	| 27.7 	| 0.558 |
| newstest2014-deen-deueng.deu.eng 	| 27.7 	| 0.545 |
| newstest2014-fren-fraeng.fra.eng 	| 32.2 	| 0.592 |
| newstest2014-hien-hineng.hin.eng 	| 16.7 	| 0.450 |
| newstest2014-ruen-ruseng.rus.eng 	| 27.2 	| 0.552 |
| newstest2015-encs-ceseng.ces.eng 	| 25.4 	| 0.518 |
| newstest2015-ende-deueng.deu.eng 	| 28.8 	| 0.552 |
| newstest2015-enru-ruseng.rus.eng 	| 25.6 	| 0.527 |
| newstest2016-encs-ceseng.ces.eng 	| 27.0 	| 0.540 |
| newstest2016-ende-deueng.deu.eng 	| 33.5 	| 0.592 |
| newstest2016-enro-roneng.ron.eng 	| 32.8 	| 0.591 |
| newstest2016-enru-ruseng.rus.eng 	| 24.8 	| 0.523 |
| newstest2017-encs-ceseng.ces.eng 	| 23.7 	| 0.510 |
| newstest2017-ende-deueng.deu.eng 	| 29.3 	| 0.556 |
| newstest2017-enlv-laveng.lav.eng 	| 18.9 	| 0.486 |
| newstest2017-enru-ruseng.rus.eng 	| 28.0 	| 0.546 |
| newstest2018-encs-ceseng.ces.eng 	| 24.9 	| 0.521 |
| newstest2018-ende-deueng.deu.eng 	| 36.0 	| 0.604 |
| newstest2018-enru-ruseng.rus.eng 	| 23.8 	| 0.517 |
| newstest2019-deen-deueng.deu.eng 	| 31.5 	| 0.570 |
| newstest2019-guen-gujeng.guj.eng 	| 12.1 	| 0.377 |
| newstest2019-lten-liteng.lit.eng 	| 26.6 	| 0.555 |
| newstest2019-ruen-ruseng.rus.eng 	| 27.5 	| 0.541 |
| Tatoeba-test.afr-eng.afr.eng 	| 59.0 	| 0.724 |
| Tatoeba-test.ang-eng.ang.eng 	| 9.9 	| 0.254 |
| Tatoeba-test.arg-eng.arg.eng 	| 41.6 	| 0.487 |
| Tatoeba-test.asm-eng.asm.eng 	| 22.8 	| 0.392 |
| Tatoeba-test.ast-eng.ast.eng 	| 36.1 	| 0.521 |
| Tatoeba-test.awa-eng.awa.eng 	| 11.6 	| 0.280 |
| Tatoeba-test.bel-eng.bel.eng 	| 42.2 	| 0.597 |
| Tatoeba-test.ben-eng.ben.eng 	| 45.8 	| 0.598 |
| Tatoeba-test.bho-eng.bho.eng 	| 34.4 	| 0.518 |
| Tatoeba-test.bre-eng.bre.eng 	| 24.4 	| 0.405 |
| Tatoeba-test.bul-eng.bul.eng 	| 50.8 	| 0.660 |
| Tatoeba-test.cat-eng.cat.eng 	| 51.2 	| 0.677 |
| Tatoeba-test.ces-eng.ces.eng 	| 47.6 	| 0.641 |
| Tatoeba-test.cor-eng.cor.eng 	| 5.4 	| 0.214 |
| Tatoeba-test.cos-eng.cos.eng 	| 61.0 	| 0.675 |
| Tatoeba-test.csb-eng.csb.eng 	| 22.5 	| 0.394 |
| Tatoeba-test.cym-eng.cym.eng 	| 34.7 	| 0.522 |
| Tatoeba-test.dan-eng.dan.eng 	| 56.2 	| 0.708 |
| Tatoeba-test.deu-eng.deu.eng 	| 44.9 	| 0.625 |
| Tatoeba-test.dsb-eng.dsb.eng 	| 21.0 	| 0.383 |
| Tatoeba-test.egl-eng.egl.eng 	| 6.9 	| 0.221 |
| Tatoeba-test.ell-eng.ell.eng 	| 62.1 	| 0.741 |
| Tatoeba-test.enm-eng.enm.eng 	| 22.6 	| 0.466 |
| Tatoeba-test.ext-eng.ext.eng 	| 33.2 	| 0.496 |
| Tatoeba-test.fao-eng.fao.eng 	| 28.1 	| 0.460 |
| Tatoeba-test.fas-eng.fas.eng 	| 9.6 	| 0.306 |
| Tatoeba-test.fra-eng.fra.eng 	| 50.3 	| 0.661 |
| Tatoeba-test.frm-eng.frm.eng 	| 30.0 	| 0.457 |
| Tatoeba-test.frr-eng.frr.eng 	| 15.2 	| 0.301 |
| Tatoeba-test.fry-eng.fry.eng 	| 34.4 	| 0.525 |
| Tatoeba-test.gcf-eng.gcf.eng 	| 18.4 	| 0.317 |
| Tatoeba-test.gla-eng.gla.eng 	| 24.1 	| 0.400 |
| Tatoeba-test.gle-eng.gle.eng 	| 52.2 	| 0.671 |
| Tatoeba-test.glg-eng.glg.eng 	| 50.5 	| 0.669 |
| Tatoeba-test.glv-eng.glv.eng 	| 5.7 	| 0.189 |
| Tatoeba-test.gos-eng.gos.eng 	| 19.2 	| 0.378 |
| Tatoeba-test.got-eng.got.eng 	| 0.1 	| 0.022 |
| Tatoeba-test.grc-eng.grc.eng 	| 0.9 	| 0.095 |
| Tatoeba-test.gsw-eng.gsw.eng 	| 23.9 	| 0.390 |
| Tatoeba-test.guj-eng.guj.eng 	| 28.0 	| 0.428 |
| Tatoeba-test.hat-eng.hat.eng 	| 44.2 	| 0.567 |
| Tatoeba-test.hbs-eng.hbs.eng 	| 51.6 	| 0.666 |
| Tatoeba-test.hif-eng.hif.eng 	| 22.3 	| 0.451 |
| Tatoeba-test.hin-eng.hin.eng 	| 41.7 	| 0.585 |
| Tatoeba-test.hsb-eng.hsb.eng 	| 46.4 	| 0.590 |
| Tatoeba-test.hye-eng.hye.eng 	| 40.4 	| 0.564 |
| Tatoeba-test.isl-eng.isl.eng 	| 43.8 	| 0.605 |
| Tatoeba-test.ita-eng.ita.eng 	| 60.7 	| 0.735 |
| Tatoeba-test.jdt-eng.jdt.eng 	| 5.5 	| 0.091 |
| Tatoeba-test.kok-eng.kok.eng 	| 7.8 	| 0.205 |
| Tatoeba-test.ksh-eng.ksh.eng 	| 15.8 	| 0.284 |
| Tatoeba-test.kur-eng.kur.eng 	| 11.6 	| 0.232 |
| Tatoeba-test.lad-eng.lad.eng 	| 30.7 	| 0.484 |
| Tatoeba-test.lah-eng.lah.eng 	| 11.0 	| 0.286 |
| Tatoeba-test.lat-eng.lat.eng 	| 24.4 	| 0.432 |
| Tatoeba-test.lav-eng.lav.eng 	| 47.2 	| 0.646 |
| Tatoeba-test.lij-eng.lij.eng 	| 9.0 	| 0.287 |
| Tatoeba-test.lit-eng.lit.eng 	| 51.7 	| 0.670 |
| Tatoeba-test.lld-eng.lld.eng 	| 22.4 	| 0.369 |
| Tatoeba-test.lmo-eng.lmo.eng 	| 26.1 	| 0.381 |
| Tatoeba-test.ltz-eng.ltz.eng 	| 39.8 	| 0.536 |
| Tatoeba-test.mai-eng.mai.eng 	| 72.3 	| 0.758 |
| Tatoeba-test.mar-eng.mar.eng 	| 32.0 	| 0.554 |
| Tatoeba-test.mfe-eng.mfe.eng 	| 63.1 	| 0.822 |
| Tatoeba-test.mkd-eng.mkd.eng 	| 49.5 	| 0.638 |
| Tatoeba-test.msa-eng.msa.eng 	| 38.6 	| 0.566 |
| Tatoeba-test.multi.eng 	| 45.6 	| 0.615 |
| Tatoeba-test.mwl-eng.mwl.eng 	| 40.4 	| 0.767 |
| Tatoeba-test.nds-eng.nds.eng 	| 35.5 	| 0.538 |
| Tatoeba-test.nep-eng.nep.eng 	| 4.9 	| 0.209 |
| Tatoeba-test.nld-eng.nld.eng 	| 54.2 	| 0.694 |
| Tatoeba-test.non-eng.non.eng 	| 39.3 	| 0.573 |
| Tatoeba-test.nor-eng.nor.eng 	| 50.9 	| 0.663 |
| Tatoeba-test.oci-eng.oci.eng 	| 19.6 	| 0.386 |
| Tatoeba-test.ori-eng.ori.eng 	| 16.2 	| 0.364 |
| Tatoeba-test.orv-eng.orv.eng 	| 13.6 	| 0.288 |
| Tatoeba-test.oss-eng.oss.eng 	| 9.4 	| 0.301 |
| Tatoeba-test.pan-eng.pan.eng 	| 17.1 	| 0.389 |
| Tatoeba-test.pap-eng.pap.eng 	| 57.0 	| 0.680 |
| Tatoeba-test.pdc-eng.pdc.eng 	| 41.6 	| 0.526 |
| Tatoeba-test.pms-eng.pms.eng 	| 13.7 	| 0.333 |
| Tatoeba-test.pol-eng.pol.eng 	| 46.5 	| 0.632 |
| Tatoeba-test.por-eng.por.eng 	| 56.4 	| 0.710 |
| Tatoeba-test.prg-eng.prg.eng 	| 2.3 	| 0.193 |
| Tatoeba-test.pus-eng.pus.eng 	| 3.2 	| 0.194 |
| Tatoeba-test.roh-eng.roh.eng 	| 17.5 	| 0.420 |
| Tatoeba-test.rom-eng.rom.eng 	| 5.0 	| 0.237 |
| Tatoeba-test.ron-eng.ron.eng 	| 51.4 	| 0.670 |
| Tatoeba-test.rue-eng.rue.eng 	| 26.0 	| 0.447 |
| Tatoeba-test.rus-eng.rus.eng 	| 47.8 	| 0.634 |
| Tatoeba-test.san-eng.san.eng 	| 4.0 	| 0.195 |
| Tatoeba-test.scn-eng.scn.eng 	| 45.1 	| 0.440 |
| Tatoeba-test.sco-eng.sco.eng 	| 41.9 	| 0.582 |
| Tatoeba-test.sgs-eng.sgs.eng 	| 38.7 	| 0.498 |
| Tatoeba-test.sin-eng.sin.eng 	| 29.7 	| 0.499 |
| Tatoeba-test.slv-eng.slv.eng 	| 38.2 	| 0.564 |
| Tatoeba-test.snd-eng.snd.eng 	| 12.7 	| 0.342 |
| Tatoeba-test.spa-eng.spa.eng 	| 53.2 	| 0.687 |
| Tatoeba-test.sqi-eng.sqi.eng 	| 51.9 	| 0.679 |
| Tatoeba-test.stq-eng.stq.eng 	| 9.0 	| 0.391 |
| Tatoeba-test.swe-eng.swe.eng 	| 57.4 	| 0.705 |
| Tatoeba-test.swg-eng.swg.eng 	| 18.0 	| 0.338 |
| Tatoeba-test.tgk-eng.tgk.eng 	| 24.3 	| 0.413 |
| Tatoeba-test.tly-eng.tly.eng 	| 1.1 	| 0.094 |
| Tatoeba-test.ukr-eng.ukr.eng 	| 48.0 	| 0.639 |
| Tatoeba-test.urd-eng.urd.eng 	| 27.2 	| 0.471 |
| Tatoeba-test.vec-eng.vec.eng 	| 28.0 	| 0.398 |
| Tatoeba-test.wln-eng.wln.eng 	| 17.5 	| 0.320 |
| Tatoeba-test.yid-eng.yid.eng 	| 26.9 	| 0.457 |
| Tatoeba-test.zza-eng.zza.eng 	| 1.7 	| 0.131 |


### System Info: 
- hf_name: ine-eng

- source_languages: ine

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ine-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ca', 'es', 'os', 'ro', 'fy', 'cy', 'sc', 'is', 'yi', 'lb', 'an', 'sq', 'fr', 'ht', 'rm', 'ps', 'af', 'uk', 'sl', 'lt', 'bg', 'be', 'gd', 'si', 'en', 'br', 'mk', 'or', 'mr', 'ru', 'fo', 'co', 'oc', 'pl', 'gl', 'nb', 'bn', 'id', 'hy', 'da', 'gv', 'nl', 'pt', 'hi', 'as', 'kw', 'ga', 'sv', 'gu', 'wa', 'lv', 'el', 'it', 'hr', 'ur', 'nn', 'de', 'cs', 'ine']

- src_constituents: {'cat', 'spa', 'pap', 'mwl', 'lij', 'bos_Latn', 'lad_Latn', 'lat_Latn', 'pcd', 'oss', 'ron', 'fry', 'cym', 'awa', 'swg', 'zsm_Latn', 'srd', 'gcf_Latn', 'isl', 'yid', 'bho', 'ltz', 'kur_Latn', 'arg', 'pes_Thaa', 'sqi', 'csb_Latn', 'fra', 'hat', 'non_Latn', 'sco', 'pnb', 'roh', 'bul_Latn', 'pus', 'afr', 'ukr', 'slv', 'lit', 'tmw_Latn', 'hsb', 'tly_Latn', 'bul', 'bel', 'got_Goth', 'lat_Grek', 'ext', 'gla', 'mai', 'sin', 'hif_Latn', 'eng', 'bre', 'nob_Hebr', 'prg_Latn', 'ang_Latn', 'aln', 'mkd', 'ori', 'mar', 'afr_Arab', 'san_Deva', 'gos', 'rus', 'fao', 'orv_Cyrl', 'bel_Latn', 'cos', 'zza', 'grc_Grek', 'oci', 'mfe', 'gom', 'bjn', 'sgs', 'tgk_Cyrl', 'hye_Latn', 'pdc', 'srp_Cyrl', 'pol', 'ast', 'glg', 'pms', 'nob', 'ben', 'min', 'srp_Latn', 'zlm_Latn', 'ind', 'rom', 'hye', 'scn', 'enm_Latn', 'lmo', 'npi', 'pes', 'dan', 'rus_Latn', 'jdt_Cyrl', 'gsw', 'glv', 'nld', 'snd_Arab', 'kur_Arab', 'por', 'hin', 'dsb', 'asm', 'lad', 'frm_Latn', 'ksh', 'pan_Guru', 'cor', 'gle', 'swe', 'guj', 'wln', 'lav', 'ell', 'frr', 'rue', 'ita', 'hrv', 'urd', 'stq', 'nno', 'deu', 'lld_Latn', 'ces', 'egl', 'vec', 'max_Latn', 'pes_Latn', 'ltg', 'nds'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ine-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ine-eng/opus2m-2020-08-01.test.txt

- src_alpha3: ine

- tgt_alpha3: eng

- short_pair: ine-en

- chrF2_score: 0.615

- bleu: 45.6

- brevity_penalty: 0.997

- ref_len: 71872.0

- src_name: Indo-European languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: ine

- tgt_alpha2: en

- prefer_old: False

- long_pair: ine-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41