---
language: 
- ru
- hy

tags:
- translation

license: apache-2.0
---

### rus-hye

* source group: Russian 
* target group: Armenian 
*  OPUS readme: [rus-hye](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-hye/README.md)

*  model: transformer-align
* source language(s): rus
* target language(s): hye hye_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-hye/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-hye/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-hye/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.hye 	| 21.7 	| 0.494 |


### System Info: 
- hf_name: rus-hye

- source_languages: rus

- target_languages: hye

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-hye/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'hy']

- src_constituents: {'rus'}

- tgt_constituents: {'hye', 'hye_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-hye/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-hye/opus-2020-06-16.test.txt

- src_alpha3: rus

- tgt_alpha3: hye

- short_pair: ru-hy

- chrF2_score: 0.494

- bleu: 21.7

- brevity_penalty: 1.0

- ref_len: 1602.0

- src_name: Russian

- tgt_name: Armenian

- train_date: 2020-06-16

- src_alpha2: ru

- tgt_alpha2: hy

- prefer_old: False

- long_pair: rus-hye

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41