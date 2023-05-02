---
language: 
- ru
- vi

tags:
- translation

license: apache-2.0
---

### rus-vie

* source group: Russian 
* target group: Vietnamese 
*  OPUS readme: [rus-vie](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-vie/README.md)

*  model: transformer-align
* source language(s): rus
* target language(s): vie
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-vie/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-vie/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-vie/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.vie 	| 16.9 	| 0.346 |


### System Info: 
- hf_name: rus-vie

- source_languages: rus

- target_languages: vie

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-vie/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'vi']

- src_constituents: {'rus'}

- tgt_constituents: {'vie', 'vie_Hani'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-vie/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-vie/opus-2020-06-17.test.txt

- src_alpha3: rus

- tgt_alpha3: vie

- short_pair: ru-vi

- chrF2_score: 0.34600000000000003

- bleu: 16.9

- brevity_penalty: 1.0

- ref_len: 2566.0

- src_name: Russian

- tgt_name: Vietnamese

- train_date: 2020-06-17

- src_alpha2: ru

- tgt_alpha2: vi

- prefer_old: False

- long_pair: rus-vie

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41