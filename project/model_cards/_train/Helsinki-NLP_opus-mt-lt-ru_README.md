---
language: 
- lt
- ru

tags:
- translation

license: apache-2.0
---

### lit-rus

* source group: Lithuanian 
* target group: Russian 
*  OPUS readme: [lit-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/lit-rus/README.md)

*  model: transformer-align
* source language(s): lit
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/lit-rus/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/lit-rus/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/lit-rus/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.lit.rus 	| 51.7 	| 0.695 |


### System Info: 
- hf_name: lit-rus

- source_languages: lit

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/lit-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['lt', 'ru']

- src_constituents: {'lit'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/lit-rus/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/lit-rus/opus-2020-06-17.test.txt

- src_alpha3: lit

- tgt_alpha3: rus

- short_pair: lt-ru

- chrF2_score: 0.695

- bleu: 51.7

- brevity_penalty: 0.982

- ref_len: 15395.0

- src_name: Lithuanian

- tgt_name: Russian

- train_date: 2020-06-17

- src_alpha2: lt

- tgt_alpha2: ru

- prefer_old: False

- long_pair: lit-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41