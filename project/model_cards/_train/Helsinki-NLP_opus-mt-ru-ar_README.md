---
language: 
- ru
- ar

tags:
- translation

license: apache-2.0
---

### rus-ara

* source group: Russian 
* target group: Arabic 
*  OPUS readme: [rus-ara](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-ara/README.md)

*  model: transformer
* source language(s): rus
* target language(s): apc ara arz
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ara/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ara/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ara/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.ara 	| 16.6 	| 0.486 |


### System Info: 
- hf_name: rus-ara

- source_languages: rus

- target_languages: ara

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-ara/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'ar']

- src_constituents: {'rus'}

- tgt_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ara/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ara/opus-2020-07-03.test.txt

- src_alpha3: rus

- tgt_alpha3: ara

- short_pair: ru-ar

- chrF2_score: 0.486

- bleu: 16.6

- brevity_penalty: 0.9690000000000001

- ref_len: 18878.0

- src_name: Russian

- tgt_name: Arabic

- train_date: 2020-07-03

- src_alpha2: ru

- tgt_alpha2: ar

- prefer_old: False

- long_pair: rus-ara

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41