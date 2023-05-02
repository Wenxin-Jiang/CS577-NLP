---
language: 
- pl
- cs
- zlw
- en

tags:
- translation

license: apache-2.0
---

### zlw-eng

* source group: West Slavic languages 
* target group: English 
*  OPUS readme: [zlw-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zlw-eng/README.md)

*  model: transformer
* source language(s): ces csb_Latn dsb hsb pol
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-ceseng.ces.eng 	| 25.7 	| 0.536 |
| newstest2009-ceseng.ces.eng 	| 24.6 	| 0.530 |
| newstest2010-ceseng.ces.eng 	| 25.0 	| 0.540 |
| newstest2011-ceseng.ces.eng 	| 25.9 	| 0.539 |
| newstest2012-ceseng.ces.eng 	| 24.8 	| 0.533 |
| newstest2013-ceseng.ces.eng 	| 27.8 	| 0.551 |
| newstest2014-csen-ceseng.ces.eng 	| 30.3 	| 0.585 |
| newstest2015-encs-ceseng.ces.eng 	| 27.5 	| 0.542 |
| newstest2016-encs-ceseng.ces.eng 	| 29.1 	| 0.564 |
| newstest2017-encs-ceseng.ces.eng 	| 26.0 	| 0.537 |
| newstest2018-encs-ceseng.ces.eng 	| 27.3 	| 0.544 |
| Tatoeba-test.ces-eng.ces.eng 	| 53.3 	| 0.691 |
| Tatoeba-test.csb-eng.csb.eng 	| 10.2 	| 0.313 |
| Tatoeba-test.dsb-eng.dsb.eng 	| 11.7 	| 0.296 |
| Tatoeba-test.hsb-eng.hsb.eng 	| 24.6 	| 0.426 |
| Tatoeba-test.multi.eng 	| 51.8 	| 0.680 |
| Tatoeba-test.pol-eng.pol.eng 	| 50.4 	| 0.667 |


### System Info: 
- hf_name: zlw-eng

- source_languages: zlw

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zlw-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['pl', 'cs', 'zlw', 'en']

- src_constituents: {'csb_Latn', 'dsb', 'hsb', 'pol', 'ces'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-eng/opus2m-2020-08-01.test.txt

- src_alpha3: zlw

- tgt_alpha3: eng

- short_pair: zlw-en

- chrF2_score: 0.68

- bleu: 51.8

- brevity_penalty: 0.9620000000000001

- ref_len: 75742.0

- src_name: West Slavic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: zlw

- tgt_alpha2: en

- prefer_old: False

- long_pair: zlw-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41