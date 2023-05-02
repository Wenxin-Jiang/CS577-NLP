---
language: 
- ru
- eu

tags:
- translation

license: apache-2.0
---

### rus-eus

* source group: Russian 
* target group: Basque 
*  OPUS readme: [rus-eus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-eus/README.md)

*  model: transformer-align
* source language(s): rus
* target language(s): eus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-eus/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-eus/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-eus/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.eus 	| 29.7 	| 0.539 |


### System Info: 
- hf_name: rus-eus

- source_languages: rus

- target_languages: eus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-eus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'eu']

- src_constituents: {'rus'}

- tgt_constituents: {'eus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-eus/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-eus/opus-2020-06-16.test.txt

- src_alpha3: rus

- tgt_alpha3: eus

- short_pair: ru-eu

- chrF2_score: 0.539

- bleu: 29.7

- brevity_penalty: 0.9440000000000001

- ref_len: 2373.0

- src_name: Russian

- tgt_name: Basque

- train_date: 2020-06-16

- src_alpha2: ru

- tgt_alpha2: eu

- prefer_old: False

- long_pair: rus-eus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41