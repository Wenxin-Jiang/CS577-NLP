---
language: 
- be
- ru
- uk
- zle
- en

tags:
- translation

license: apache-2.0
---

### zle-eng

* source group: East Slavic languages 
* target group: English 
*  OPUS readme: [zle-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-eng/README.md)

*  model: transformer
* source language(s): bel bel_Latn orv_Cyrl rue rus ukr
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2012-ruseng.rus.eng 	| 31.1 	| 0.579 |
| newstest2013-ruseng.rus.eng 	| 24.9 	| 0.522 |
| newstest2014-ruen-ruseng.rus.eng 	| 27.9 	| 0.563 |
| newstest2015-enru-ruseng.rus.eng 	| 26.8 	| 0.541 |
| newstest2016-enru-ruseng.rus.eng 	| 25.8 	| 0.535 |
| newstest2017-enru-ruseng.rus.eng 	| 29.1 	| 0.561 |
| newstest2018-enru-ruseng.rus.eng 	| 25.4 	| 0.537 |
| newstest2019-ruen-ruseng.rus.eng 	| 26.8 	| 0.545 |
| Tatoeba-test.bel-eng.bel.eng 	| 38.3 	| 0.569 |
| Tatoeba-test.multi.eng 	| 50.1 	| 0.656 |
| Tatoeba-test.orv-eng.orv.eng 	| 6.9 	| 0.217 |
| Tatoeba-test.rue-eng.rue.eng 	| 15.4 	| 0.345 |
| Tatoeba-test.rus-eng.rus.eng 	| 52.5 	| 0.674 |
| Tatoeba-test.ukr-eng.ukr.eng 	| 52.1 	| 0.673 |


### System Info: 
- hf_name: zle-eng

- source_languages: zle

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['be', 'ru', 'uk', 'zle', 'en']

- src_constituents: {'bel', 'orv_Cyrl', 'bel_Latn', 'rus', 'ukr', 'rue'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zle-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zle-eng/opus2m-2020-08-01.test.txt

- src_alpha3: zle

- tgt_alpha3: eng

- short_pair: zle-en

- chrF2_score: 0.6559999999999999

- bleu: 50.1

- brevity_penalty: 0.97

- ref_len: 69599.0

- src_name: East Slavic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: zle

- tgt_alpha2: en

- prefer_old: False

- long_pair: zle-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41