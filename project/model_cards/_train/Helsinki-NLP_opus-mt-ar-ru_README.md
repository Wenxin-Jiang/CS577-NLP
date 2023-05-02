---
language: 
- ar
- ru

tags:
- translation

license: apache-2.0
---

### ara-rus

* source group: Arabic 
* target group: Russian 
*  OPUS readme: [ara-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-rus/README.md)

*  model: transformer
* source language(s): apc ara arz
* target language(s): rus
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-rus/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-rus/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-rus/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ara.rus 	| 42.5 	| 0.605 |


### System Info: 
- hf_name: ara-rus

- source_languages: ara

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ar', 'ru']

- src_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-rus/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-rus/opus-2020-07-03.test.txt

- src_alpha3: ara

- tgt_alpha3: rus

- short_pair: ar-ru

- chrF2_score: 0.605

- bleu: 42.5

- brevity_penalty: 0.97

- ref_len: 21830.0

- src_name: Arabic

- tgt_name: Russian

- train_date: 2020-07-03

- src_alpha2: ar

- tgt_alpha2: ru

- prefer_old: False

- long_pair: ara-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41