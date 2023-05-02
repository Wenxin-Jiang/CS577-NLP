---
language: 
- es
- no

tags:
- translation

license: apache-2.0
---

### spa-nor

* source group: Spanish 
* target group: Norwegian 
*  OPUS readme: [spa-nor](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-nor/README.md)

*  model: transformer-align
* source language(s): spa
* target language(s): nno nob
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-nor/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-nor/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-nor/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.nor 	| 36.7 	| 0.565 |


### System Info: 
- hf_name: spa-nor

- source_languages: spa

- target_languages: nor

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-nor/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'no']

- src_constituents: {'spa'}

- tgt_constituents: {'nob', 'nno'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-nor/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-nor/opus-2020-06-17.test.txt

- src_alpha3: spa

- tgt_alpha3: nor

- short_pair: es-no

- chrF2_score: 0.565

- bleu: 36.7

- brevity_penalty: 0.99

- ref_len: 7217.0

- src_name: Spanish

- tgt_name: Norwegian

- train_date: 2020-06-17

- src_alpha2: es

- tgt_alpha2: no

- prefer_old: False

- long_pair: spa-nor

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41