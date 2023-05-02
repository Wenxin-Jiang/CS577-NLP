---
language: 
- en
- be
- ru
- uk
- zle

tags:
- translation

license: apache-2.0
---

### eng-zle

* source group: English 
* target group: East Slavic languages 
*  OPUS readme: [eng-zle](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-zle/README.md)

*  model: transformer
* source language(s): eng
* target language(s): bel bel_Latn orv_Cyrl rue rus ukr
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-02.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zle/opus2m-2020-08-02.zip)
* test set translations: [opus2m-2020-08-02.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zle/opus2m-2020-08-02.test.txt)
* test set scores: [opus2m-2020-08-02.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zle/opus2m-2020-08-02.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2012-engrus.eng.rus 	| 27.4 	| 0.550 |
| newstest2013-engrus.eng.rus 	| 21.4 	| 0.493 |
| newstest2015-enru-engrus.eng.rus 	| 24.2 	| 0.534 |
| newstest2016-enru-engrus.eng.rus 	| 23.3 	| 0.518 |
| newstest2017-enru-engrus.eng.rus 	| 25.3 	| 0.541 |
| newstest2018-enru-engrus.eng.rus 	| 22.4 	| 0.527 |
| newstest2019-enru-engrus.eng.rus 	| 24.1 	| 0.505 |
| Tatoeba-test.eng-bel.eng.bel 	| 20.8 	| 0.471 |
| Tatoeba-test.eng.multi 	| 37.2 	| 0.580 |
| Tatoeba-test.eng-orv.eng.orv 	| 0.6 	| 0.130 |
| Tatoeba-test.eng-rue.eng.rue 	| 1.4 	| 0.168 |
| Tatoeba-test.eng-rus.eng.rus 	| 41.3 	| 0.616 |
| Tatoeba-test.eng-ukr.eng.ukr 	| 38.7 	| 0.596 |


### System Info: 
- hf_name: eng-zle

- source_languages: eng

- target_languages: zle

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-zle/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'be', 'ru', 'uk', 'zle']

- src_constituents: {'eng'}

- tgt_constituents: {'bel', 'orv_Cyrl', 'bel_Latn', 'rus', 'ukr', 'rue'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zle/opus2m-2020-08-02.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zle/opus2m-2020-08-02.test.txt

- src_alpha3: eng

- tgt_alpha3: zle

- short_pair: en-zle

- chrF2_score: 0.58

- bleu: 37.2

- brevity_penalty: 0.9890000000000001

- ref_len: 63493.0

- src_name: English

- tgt_name: East Slavic languages

- train_date: 2020-08-02

- src_alpha2: en

- tgt_alpha2: zle

- prefer_old: False

- long_pair: eng-zle

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41