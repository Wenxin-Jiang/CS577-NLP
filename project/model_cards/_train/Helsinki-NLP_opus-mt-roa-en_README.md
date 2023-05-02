---
language: 
- it
- ca
- rm
- es
- ro
- gl
- co
- wa
- pt
- oc
- an
- id
- fr
- ht
- roa
- en

tags:
- translation

license: apache-2.0
---

### roa-eng

* source group: Romance languages 
* target group: English 
*  OPUS readme: [roa-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/roa-eng/README.md)

*  model: transformer
* source language(s): arg ast cat cos egl ext fra frm_Latn gcf_Latn glg hat ind ita lad lad_Latn lij lld_Latn lmo max_Latn mfe min mwl oci pap pms por roh ron scn spa tmw_Latn vec wln zlm_Latn zsm_Latn
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/roa-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/roa-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/roa-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2016-enro-roneng.ron.eng 	| 37.1 	| 0.631 |
| newsdiscussdev2015-enfr-fraeng.fra.eng 	| 31.6 	| 0.564 |
| newsdiscusstest2015-enfr-fraeng.fra.eng 	| 36.1 	| 0.592 |
| newssyscomb2009-fraeng.fra.eng 	| 29.3 	| 0.563 |
| newssyscomb2009-itaeng.ita.eng 	| 33.1 	| 0.589 |
| newssyscomb2009-spaeng.spa.eng 	| 29.2 	| 0.562 |
| news-test2008-fraeng.fra.eng 	| 25.2 	| 0.533 |
| news-test2008-spaeng.spa.eng 	| 26.6 	| 0.542 |
| newstest2009-fraeng.fra.eng 	| 28.6 	| 0.557 |
| newstest2009-itaeng.ita.eng 	| 32.0 	| 0.580 |
| newstest2009-spaeng.spa.eng 	| 28.9 	| 0.559 |
| newstest2010-fraeng.fra.eng 	| 29.9 	| 0.573 |
| newstest2010-spaeng.spa.eng 	| 33.3 	| 0.596 |
| newstest2011-fraeng.fra.eng 	| 31.2 	| 0.585 |
| newstest2011-spaeng.spa.eng 	| 32.3 	| 0.584 |
| newstest2012-fraeng.fra.eng 	| 31.3 	| 0.580 |
| newstest2012-spaeng.spa.eng 	| 35.3 	| 0.606 |
| newstest2013-fraeng.fra.eng 	| 31.9 	| 0.575 |
| newstest2013-spaeng.spa.eng 	| 32.8 	| 0.592 |
| newstest2014-fren-fraeng.fra.eng 	| 34.6 	| 0.611 |
| newstest2016-enro-roneng.ron.eng 	| 35.8 	| 0.614 |
| Tatoeba-test.arg-eng.arg.eng 	| 38.7 	| 0.512 |
| Tatoeba-test.ast-eng.ast.eng 	| 35.2 	| 0.520 |
| Tatoeba-test.cat-eng.cat.eng 	| 54.9 	| 0.703 |
| Tatoeba-test.cos-eng.cos.eng 	| 68.1 	| 0.666 |
| Tatoeba-test.egl-eng.egl.eng 	| 6.7 	| 0.209 |
| Tatoeba-test.ext-eng.ext.eng 	| 24.2 	| 0.427 |
| Tatoeba-test.fra-eng.fra.eng 	| 53.9 	| 0.691 |
| Tatoeba-test.frm-eng.frm.eng 	| 25.7 	| 0.423 |
| Tatoeba-test.gcf-eng.gcf.eng 	| 14.8 	| 0.288 |
| Tatoeba-test.glg-eng.glg.eng 	| 54.6 	| 0.703 |
| Tatoeba-test.hat-eng.hat.eng 	| 37.0 	| 0.540 |
| Tatoeba-test.ita-eng.ita.eng 	| 64.8 	| 0.768 |
| Tatoeba-test.lad-eng.lad.eng 	| 21.7 	| 0.452 |
| Tatoeba-test.lij-eng.lij.eng 	| 11.2 	| 0.299 |
| Tatoeba-test.lld-eng.lld.eng 	| 10.8 	| 0.273 |
| Tatoeba-test.lmo-eng.lmo.eng 	| 5.8 	| 0.260 |
| Tatoeba-test.mfe-eng.mfe.eng 	| 63.1 	| 0.819 |
| Tatoeba-test.msa-eng.msa.eng 	| 40.9 	| 0.592 |
| Tatoeba-test.multi.eng 	| 54.9 	| 0.697 |
| Tatoeba-test.mwl-eng.mwl.eng 	| 44.6 	| 0.674 |
| Tatoeba-test.oci-eng.oci.eng 	| 20.5 	| 0.404 |
| Tatoeba-test.pap-eng.pap.eng 	| 56.2 	| 0.669 |
| Tatoeba-test.pms-eng.pms.eng 	| 10.3 	| 0.324 |
| Tatoeba-test.por-eng.por.eng 	| 59.7 	| 0.738 |
| Tatoeba-test.roh-eng.roh.eng 	| 14.8 	| 0.378 |
| Tatoeba-test.ron-eng.ron.eng 	| 55.2 	| 0.703 |
| Tatoeba-test.scn-eng.scn.eng 	| 10.2 	| 0.259 |
| Tatoeba-test.spa-eng.spa.eng 	| 56.2 	| 0.714 |
| Tatoeba-test.vec-eng.vec.eng 	| 13.8 	| 0.317 |
| Tatoeba-test.wln-eng.wln.eng 	| 17.3 	| 0.323 |


### System Info: 
- hf_name: roa-eng

- source_languages: roa

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/roa-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['it', 'ca', 'rm', 'es', 'ro', 'gl', 'co', 'wa', 'pt', 'oc', 'an', 'id', 'fr', 'ht', 'roa', 'en']

- src_constituents: {'ita', 'cat', 'roh', 'spa', 'pap', 'lmo', 'mwl', 'lij', 'lad_Latn', 'ext', 'ron', 'ast', 'glg', 'pms', 'zsm_Latn', 'gcf_Latn', 'lld_Latn', 'min', 'tmw_Latn', 'cos', 'wln', 'zlm_Latn', 'por', 'egl', 'oci', 'vec', 'arg', 'ind', 'fra', 'hat', 'lad', 'max_Latn', 'frm_Latn', 'scn', 'mfe'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/roa-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/roa-eng/opus2m-2020-08-01.test.txt

- src_alpha3: roa

- tgt_alpha3: eng

- short_pair: roa-en

- chrF2_score: 0.6970000000000001

- bleu: 54.9

- brevity_penalty: 0.9790000000000001

- ref_len: 74762.0

- src_name: Romance languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: roa

- tgt_alpha2: en

- prefer_old: False

- long_pair: roa-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41