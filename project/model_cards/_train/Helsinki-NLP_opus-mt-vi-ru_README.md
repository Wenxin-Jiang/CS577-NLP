---
language: 
- vi
- ru

tags:
- translation

license: apache-2.0
---

### vie-rus

* source group: Vietnamese 
* target group: Russian 
*  OPUS readme: [vie-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/vie-rus/README.md)

*  model: transformer-align
* source language(s): vie
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/vie-rus/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/vie-rus/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/vie-rus/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.vie.rus 	| 16.9 	| 0.331 |


### System Info: 
- hf_name: vie-rus

- source_languages: vie

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/vie-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['vi', 'ru']

- src_constituents: {'vie', 'vie_Hani'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/vie-rus/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/vie-rus/opus-2020-06-17.test.txt

- src_alpha3: vie

- tgt_alpha3: rus

- short_pair: vi-ru

- chrF2_score: 0.331

- bleu: 16.9

- brevity_penalty: 0.878

- ref_len: 2207.0

- src_name: Vietnamese

- tgt_name: Russian

- train_date: 2020-06-17

- src_alpha2: vi

- tgt_alpha2: ru

- prefer_old: False

- long_pair: vie-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41