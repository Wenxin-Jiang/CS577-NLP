---
language: 
- en
- pl
- cs
- zlw

tags:
- translation

license: apache-2.0
---

### eng-zlw

* source group: English 
* target group: West Slavic languages 
*  OPUS readme: [eng-zlw](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-zlw/README.md)

*  model: transformer
* source language(s): eng
* target language(s): ces csb_Latn dsb hsb pol
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-02.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zlw/opus2m-2020-08-02.zip)
* test set translations: [opus2m-2020-08-02.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zlw/opus2m-2020-08-02.test.txt)
* test set scores: [opus2m-2020-08-02.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zlw/opus2m-2020-08-02.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-engces.eng.ces 	| 20.6 	| 0.488 |
| news-test2008-engces.eng.ces 	| 18.3 	| 0.466 |
| newstest2009-engces.eng.ces 	| 19.8 	| 0.483 |
| newstest2010-engces.eng.ces 	| 19.8 	| 0.486 |
| newstest2011-engces.eng.ces 	| 20.6 	| 0.489 |
| newstest2012-engces.eng.ces 	| 18.6 	| 0.464 |
| newstest2013-engces.eng.ces 	| 22.3 	| 0.495 |
| newstest2015-encs-engces.eng.ces 	| 21.7 	| 0.502 |
| newstest2016-encs-engces.eng.ces 	| 24.5 	| 0.521 |
| newstest2017-encs-engces.eng.ces 	| 20.1 	| 0.480 |
| newstest2018-encs-engces.eng.ces 	| 19.9 	| 0.483 |
| newstest2019-encs-engces.eng.ces 	| 21.2 	| 0.490 |
| Tatoeba-test.eng-ces.eng.ces 	| 43.7 	| 0.632 |
| Tatoeba-test.eng-csb.eng.csb 	| 1.2 	| 0.188 |
| Tatoeba-test.eng-dsb.eng.dsb 	| 1.5 	| 0.167 |
| Tatoeba-test.eng-hsb.eng.hsb 	| 5.7 	| 0.199 |
| Tatoeba-test.eng.multi 	| 42.8 	| 0.632 |
| Tatoeba-test.eng-pol.eng.pol 	| 43.2 	| 0.641 |


### System Info: 
- hf_name: eng-zlw

- source_languages: eng

- target_languages: zlw

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-zlw/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'pl', 'cs', 'zlw']

- src_constituents: {'eng'}

- tgt_constituents: {'csb_Latn', 'dsb', 'hsb', 'pol', 'ces'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zlw/opus2m-2020-08-02.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zlw/opus2m-2020-08-02.test.txt

- src_alpha3: eng

- tgt_alpha3: zlw

- short_pair: en-zlw

- chrF2_score: 0.632

- bleu: 42.8

- brevity_penalty: 0.973

- ref_len: 65397.0

- src_name: English

- tgt_name: West Slavic languages

- train_date: 2020-08-02

- src_alpha2: en

- tgt_alpha2: zlw

- prefer_old: False

- long_pair: eng-zlw

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41