---
language: 
- en
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

tags:
- translation

license: apache-2.0
---

### eng-roa

* source group: English 
* target group: Romance languages 
*  OPUS readme: [eng-roa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-roa/README.md)

*  model: transformer
* source language(s): eng
* target language(s): arg ast cat cos egl ext fra frm_Latn gcf_Latn glg hat ind ita lad lad_Latn lij lld_Latn lmo max_Latn mfe min mwl oci pap pms por roh ron scn spa tmw_Latn vec wln zlm_Latn zsm_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-roa/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-roa/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-roa/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2016-enro-engron.eng.ron 	| 27.6 	| 0.567 |
| newsdiscussdev2015-enfr-engfra.eng.fra 	| 30.2 	| 0.575 |
| newsdiscusstest2015-enfr-engfra.eng.fra 	| 35.5 	| 0.612 |
| newssyscomb2009-engfra.eng.fra 	| 27.9 	| 0.570 |
| newssyscomb2009-engita.eng.ita 	| 29.3 	| 0.590 |
| newssyscomb2009-engspa.eng.spa 	| 29.6 	| 0.570 |
| news-test2008-engfra.eng.fra 	| 25.2 	| 0.538 |
| news-test2008-engspa.eng.spa 	| 27.3 	| 0.548 |
| newstest2009-engfra.eng.fra 	| 26.9 	| 0.560 |
| newstest2009-engita.eng.ita 	| 28.7 	| 0.583 |
| newstest2009-engspa.eng.spa 	| 29.0 	| 0.568 |
| newstest2010-engfra.eng.fra 	| 29.3 	| 0.574 |
| newstest2010-engspa.eng.spa 	| 34.2 	| 0.601 |
| newstest2011-engfra.eng.fra 	| 31.4 	| 0.592 |
| newstest2011-engspa.eng.spa 	| 35.0 	| 0.599 |
| newstest2012-engfra.eng.fra 	| 29.5 	| 0.576 |
| newstest2012-engspa.eng.spa 	| 35.5 	| 0.603 |
| newstest2013-engfra.eng.fra 	| 29.9 	| 0.567 |
| newstest2013-engspa.eng.spa 	| 32.1 	| 0.578 |
| newstest2016-enro-engron.eng.ron 	| 26.1 	| 0.551 |
| Tatoeba-test.eng-arg.eng.arg 	| 1.4 	| 0.125 |
| Tatoeba-test.eng-ast.eng.ast 	| 17.8 	| 0.406 |
| Tatoeba-test.eng-cat.eng.cat 	| 48.3 	| 0.676 |
| Tatoeba-test.eng-cos.eng.cos 	| 3.2 	| 0.275 |
| Tatoeba-test.eng-egl.eng.egl 	| 0.2 	| 0.084 |
| Tatoeba-test.eng-ext.eng.ext 	| 11.2 	| 0.344 |
| Tatoeba-test.eng-fra.eng.fra 	| 45.3 	| 0.637 |
| Tatoeba-test.eng-frm.eng.frm 	| 1.1 	| 0.221 |
| Tatoeba-test.eng-gcf.eng.gcf 	| 0.6 	| 0.118 |
| Tatoeba-test.eng-glg.eng.glg 	| 44.2 	| 0.645 |
| Tatoeba-test.eng-hat.eng.hat 	| 28.0 	| 0.502 |
| Tatoeba-test.eng-ita.eng.ita 	| 45.6 	| 0.674 |
| Tatoeba-test.eng-lad.eng.lad 	| 8.2 	| 0.322 |
| Tatoeba-test.eng-lij.eng.lij 	| 1.4 	| 0.182 |
| Tatoeba-test.eng-lld.eng.lld 	| 0.8 	| 0.217 |
| Tatoeba-test.eng-lmo.eng.lmo 	| 0.7 	| 0.190 |
| Tatoeba-test.eng-mfe.eng.mfe 	| 91.9 	| 0.956 |
| Tatoeba-test.eng-msa.eng.msa 	| 31.1 	| 0.548 |
| Tatoeba-test.eng.multi 	| 42.9 	| 0.636 |
| Tatoeba-test.eng-mwl.eng.mwl 	| 2.1 	| 0.234 |
| Tatoeba-test.eng-oci.eng.oci 	| 7.9 	| 0.297 |
| Tatoeba-test.eng-pap.eng.pap 	| 44.1 	| 0.648 |
| Tatoeba-test.eng-pms.eng.pms 	| 2.1 	| 0.190 |
| Tatoeba-test.eng-por.eng.por 	| 41.8 	| 0.639 |
| Tatoeba-test.eng-roh.eng.roh 	| 3.5 	| 0.261 |
| Tatoeba-test.eng-ron.eng.ron 	| 41.0 	| 0.635 |
| Tatoeba-test.eng-scn.eng.scn 	| 1.7 	| 0.184 |
| Tatoeba-test.eng-spa.eng.spa 	| 50.1 	| 0.689 |
| Tatoeba-test.eng-vec.eng.vec 	| 3.2 	| 0.248 |
| Tatoeba-test.eng-wln.eng.wln 	| 7.2 	| 0.220 |


### System Info: 
- hf_name: eng-roa

- source_languages: eng

- target_languages: roa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-roa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'it', 'ca', 'rm', 'es', 'ro', 'gl', 'co', 'wa', 'pt', 'oc', 'an', 'id', 'fr', 'ht', 'roa']

- src_constituents: {'eng'}

- tgt_constituents: {'ita', 'cat', 'roh', 'spa', 'pap', 'lmo', 'mwl', 'lij', 'lad_Latn', 'ext', 'ron', 'ast', 'glg', 'pms', 'zsm_Latn', 'gcf_Latn', 'lld_Latn', 'min', 'tmw_Latn', 'cos', 'wln', 'zlm_Latn', 'por', 'egl', 'oci', 'vec', 'arg', 'ind', 'fra', 'hat', 'lad', 'max_Latn', 'frm_Latn', 'scn', 'mfe'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-roa/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-roa/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: roa

- short_pair: en-roa

- chrF2_score: 0.636

- bleu: 42.9

- brevity_penalty: 0.978

- ref_len: 72751.0

- src_name: English

- tgt_name: Romance languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: roa

- prefer_old: False

- long_pair: eng-roa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41