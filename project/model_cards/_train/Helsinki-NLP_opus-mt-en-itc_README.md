---
language: 
- en
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

tags:
- translation

license: apache-2.0
---

### eng-itc

* source group: English 
* target group: Italic languages 
*  OPUS readme: [eng-itc](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-itc/README.md)

*  model: transformer
* source language(s): eng
* target language(s): arg ast cat cos egl ext fra frm_Latn gcf_Latn glg hat ind ita lad lad_Latn lat_Latn lij lld_Latn lmo max_Latn mfe min mwl oci pap pms por roh ron scn spa tmw_Latn vec wln zlm_Latn zsm_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-itc/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-itc/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-itc/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2016-enro-engron.eng.ron 	| 27.1 	| 0.565 |
| newsdiscussdev2015-enfr-engfra.eng.fra 	| 29.9 	| 0.574 |
| newsdiscusstest2015-enfr-engfra.eng.fra 	| 35.3 	| 0.609 |
| newssyscomb2009-engfra.eng.fra 	| 27.7 	| 0.567 |
| newssyscomb2009-engita.eng.ita 	| 28.6 	| 0.586 |
| newssyscomb2009-engspa.eng.spa 	| 29.8 	| 0.569 |
| news-test2008-engfra.eng.fra 	| 25.0 	| 0.536 |
| news-test2008-engspa.eng.spa 	| 27.1 	| 0.548 |
| newstest2009-engfra.eng.fra 	| 26.7 	| 0.557 |
| newstest2009-engita.eng.ita 	| 28.9 	| 0.583 |
| newstest2009-engspa.eng.spa 	| 28.9 	| 0.567 |
| newstest2010-engfra.eng.fra 	| 29.6 	| 0.574 |
| newstest2010-engspa.eng.spa 	| 33.8 	| 0.598 |
| newstest2011-engfra.eng.fra 	| 30.9 	| 0.590 |
| newstest2011-engspa.eng.spa 	| 34.8 	| 0.598 |
| newstest2012-engfra.eng.fra 	| 29.1 	| 0.574 |
| newstest2012-engspa.eng.spa 	| 34.9 	| 0.600 |
| newstest2013-engfra.eng.fra 	| 30.1 	| 0.567 |
| newstest2013-engspa.eng.spa 	| 31.8 	| 0.576 |
| newstest2016-enro-engron.eng.ron 	| 25.9 	| 0.548 |
| Tatoeba-test.eng-arg.eng.arg 	| 1.6 	| 0.120 |
| Tatoeba-test.eng-ast.eng.ast 	| 17.2 	| 0.389 |
| Tatoeba-test.eng-cat.eng.cat 	| 47.6 	| 0.668 |
| Tatoeba-test.eng-cos.eng.cos 	| 4.3 	| 0.287 |
| Tatoeba-test.eng-egl.eng.egl 	| 0.9 	| 0.101 |
| Tatoeba-test.eng-ext.eng.ext 	| 8.7 	| 0.287 |
| Tatoeba-test.eng-fra.eng.fra 	| 44.9 	| 0.635 |
| Tatoeba-test.eng-frm.eng.frm 	| 1.0 	| 0.225 |
| Tatoeba-test.eng-gcf.eng.gcf 	| 0.7 	| 0.115 |
| Tatoeba-test.eng-glg.eng.glg 	| 44.9 	| 0.648 |
| Tatoeba-test.eng-hat.eng.hat 	| 30.9 	| 0.533 |
| Tatoeba-test.eng-ita.eng.ita 	| 45.4 	| 0.673 |
| Tatoeba-test.eng-lad.eng.lad 	| 5.6 	| 0.279 |
| Tatoeba-test.eng-lat.eng.lat 	| 12.1 	| 0.380 |
| Tatoeba-test.eng-lij.eng.lij 	| 1.4 	| 0.183 |
| Tatoeba-test.eng-lld.eng.lld 	| 0.5 	| 0.199 |
| Tatoeba-test.eng-lmo.eng.lmo 	| 0.7 	| 0.187 |
| Tatoeba-test.eng-mfe.eng.mfe 	| 83.6 	| 0.909 |
| Tatoeba-test.eng-msa.eng.msa 	| 31.3 	| 0.549 |
| Tatoeba-test.eng.multi 	| 38.0 	| 0.588 |
| Tatoeba-test.eng-mwl.eng.mwl 	| 2.7 	| 0.322 |
| Tatoeba-test.eng-oci.eng.oci 	| 8.2 	| 0.293 |
| Tatoeba-test.eng-pap.eng.pap 	| 46.7 	| 0.663 |
| Tatoeba-test.eng-pms.eng.pms 	| 2.1 	| 0.194 |
| Tatoeba-test.eng-por.eng.por 	| 41.2 	| 0.635 |
| Tatoeba-test.eng-roh.eng.roh 	| 2.6 	| 0.237 |
| Tatoeba-test.eng-ron.eng.ron 	| 40.6 	| 0.632 |
| Tatoeba-test.eng-scn.eng.scn 	| 1.6 	| 0.181 |
| Tatoeba-test.eng-spa.eng.spa 	| 49.5 	| 0.685 |
| Tatoeba-test.eng-vec.eng.vec 	| 1.6 	| 0.223 |
| Tatoeba-test.eng-wln.eng.wln 	| 7.1 	| 0.250 |


### System Info: 
- hf_name: eng-itc

- source_languages: eng

- target_languages: itc

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-itc/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'it', 'ca', 'rm', 'es', 'ro', 'gl', 'sc', 'co', 'wa', 'pt', 'oc', 'an', 'id', 'fr', 'ht', 'itc']

- src_constituents: {'eng'}

- tgt_constituents: {'ita', 'cat', 'roh', 'spa', 'pap', 'bjn', 'lmo', 'mwl', 'lij', 'lat_Latn', 'lad_Latn', 'pcd', 'lat_Grek', 'ext', 'ron', 'ast', 'glg', 'pms', 'zsm_Latn', 'srd', 'gcf_Latn', 'lld_Latn', 'min', 'tmw_Latn', 'cos', 'wln', 'zlm_Latn', 'por', 'egl', 'oci', 'vec', 'arg', 'ind', 'fra', 'hat', 'lad', 'max_Latn', 'frm_Latn', 'scn', 'mfe'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-itc/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-itc/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: itc

- short_pair: en-itc

- chrF2_score: 0.588

- bleu: 38.0

- brevity_penalty: 0.9670000000000001

- ref_len: 73951.0

- src_name: English

- tgt_name: Italic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: itc

- prefer_old: False

- long_pair: eng-itc

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41