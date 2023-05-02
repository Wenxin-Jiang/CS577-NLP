---
language: 
- it
- ca
- rm
- es
- ro
- gl
- sc
- co
- wa
- pt
- oc
- an
- id
- fr
- ht
- itc
- en

tags:
- translation

license: apache-2.0
---

### itc-eng

* source group: Italic languages 
* target group: English 
*  OPUS readme: [itc-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/itc-eng/README.md)

*  model: transformer
* source language(s): arg ast cat cos egl ext fra frm_Latn gcf_Latn glg hat ind ita lad lad_Latn lat_Latn lij lld_Latn lmo max_Latn mfe min mwl oci pap pms por roh ron scn spa tmw_Latn vec wln zlm_Latn zsm_Latn
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/itc-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2016-enro-roneng.ron.eng 	| 36.5 	| 0.628 |
| newsdiscussdev2015-enfr-fraeng.fra.eng 	| 30.9 	| 0.561 |
| newsdiscusstest2015-enfr-fraeng.fra.eng 	| 35.5 	| 0.590 |
| newssyscomb2009-fraeng.fra.eng 	| 29.2 	| 0.560 |
| newssyscomb2009-itaeng.ita.eng 	| 32.2 	| 0.583 |
| newssyscomb2009-spaeng.spa.eng 	| 29.3 	| 0.563 |
| news-test2008-fraeng.fra.eng 	| 25.2 	| 0.531 |
| news-test2008-spaeng.spa.eng 	| 26.3 	| 0.539 |
| newstest2009-fraeng.fra.eng 	| 28.5 	| 0.555 |
| newstest2009-itaeng.ita.eng 	| 31.6 	| 0.578 |
| newstest2009-spaeng.spa.eng 	| 28.7 	| 0.558 |
| newstest2010-fraeng.fra.eng 	| 29.7 	| 0.571 |
| newstest2010-spaeng.spa.eng 	| 32.8 	| 0.593 |
| newstest2011-fraeng.fra.eng 	| 30.9 	| 0.580 |
| newstest2011-spaeng.spa.eng 	| 31.8 	| 0.582 |
| newstest2012-fraeng.fra.eng 	| 31.1 	| 0.576 |
| newstest2012-spaeng.spa.eng 	| 35.0 	| 0.604 |
| newstest2013-fraeng.fra.eng 	| 31.7 	| 0.573 |
| newstest2013-spaeng.spa.eng 	| 32.4 	| 0.589 |
| newstest2014-fren-fraeng.fra.eng 	| 34.0 	| 0.606 |
| newstest2016-enro-roneng.ron.eng 	| 34.8 	| 0.608 |
| Tatoeba-test.arg-eng.arg.eng 	| 41.5 	| 0.528 |
| Tatoeba-test.ast-eng.ast.eng 	| 36.0 	| 0.519 |
| Tatoeba-test.cat-eng.cat.eng 	| 53.7 	| 0.696 |
| Tatoeba-test.cos-eng.cos.eng 	| 56.5 	| 0.640 |
| Tatoeba-test.egl-eng.egl.eng 	| 4.6 	| 0.217 |
| Tatoeba-test.ext-eng.ext.eng 	| 39.1 	| 0.547 |
| Tatoeba-test.fra-eng.fra.eng 	| 53.4 	| 0.688 |
| Tatoeba-test.frm-eng.frm.eng 	| 22.3 	| 0.409 |
| Tatoeba-test.gcf-eng.gcf.eng 	| 18.7 	| 0.308 |
| Tatoeba-test.glg-eng.glg.eng 	| 54.8 	| 0.701 |
| Tatoeba-test.hat-eng.hat.eng 	| 42.6 	| 0.583 |
| Tatoeba-test.ita-eng.ita.eng 	| 64.8 	| 0.767 |
| Tatoeba-test.lad-eng.lad.eng 	| 14.4 	| 0.433 |
| Tatoeba-test.lat-eng.lat.eng 	| 19.5 	| 0.390 |
| Tatoeba-test.lij-eng.lij.eng 	| 8.9 	| 0.280 |
| Tatoeba-test.lld-eng.lld.eng 	| 17.4 	| 0.331 |
| Tatoeba-test.lmo-eng.lmo.eng 	| 10.8 	| 0.306 |
| Tatoeba-test.mfe-eng.mfe.eng 	| 66.0 	| 0.820 |
| Tatoeba-test.msa-eng.msa.eng 	| 40.8 	| 0.590 |
| Tatoeba-test.multi.eng 	| 47.6 	| 0.634 |
| Tatoeba-test.mwl-eng.mwl.eng 	| 41.3 	| 0.707 |
| Tatoeba-test.oci-eng.oci.eng 	| 20.3 	| 0.401 |
| Tatoeba-test.pap-eng.pap.eng 	| 53.9 	| 0.642 |
| Tatoeba-test.pms-eng.pms.eng 	| 12.2 	| 0.334 |
| Tatoeba-test.por-eng.por.eng 	| 59.3 	| 0.734 |
| Tatoeba-test.roh-eng.roh.eng 	| 17.7 	| 0.420 |
| Tatoeba-test.ron-eng.ron.eng 	| 54.5 	| 0.697 |
| Tatoeba-test.scn-eng.scn.eng 	| 40.0 	| 0.443 |
| Tatoeba-test.spa-eng.spa.eng 	| 55.9 	| 0.712 |
| Tatoeba-test.vec-eng.vec.eng 	| 11.2 	| 0.304 |
| Tatoeba-test.wln-eng.wln.eng 	| 20.9 	| 0.360 |


### System Info: 
- hf_name: itc-eng

- source_languages: itc

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/itc-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['it', 'ca', 'rm', 'es', 'ro', 'gl', 'sc', 'co', 'wa', 'pt', 'oc', 'an', 'id', 'fr', 'ht', 'itc', 'en']

- src_constituents: {'ita', 'cat', 'roh', 'spa', 'pap', 'bjn', 'lmo', 'mwl', 'lij', 'lat_Latn', 'lad_Latn', 'pcd', 'lat_Grek', 'ext', 'ron', 'ast', 'glg', 'pms', 'zsm_Latn', 'srd', 'gcf_Latn', 'lld_Latn', 'min', 'tmw_Latn', 'cos', 'wln', 'zlm_Latn', 'por', 'egl', 'oci', 'vec', 'arg', 'ind', 'fra', 'hat', 'lad', 'max_Latn', 'frm_Latn', 'scn', 'mfe'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/itc-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/itc-eng/opus2m-2020-08-01.test.txt

- src_alpha3: itc

- tgt_alpha3: eng

- short_pair: itc-en

- chrF2_score: 0.634

- bleu: 47.6

- brevity_penalty: 0.981

- ref_len: 77633.0

- src_name: Italic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: itc

- tgt_alpha2: en

- prefer_old: False

- long_pair: itc-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41