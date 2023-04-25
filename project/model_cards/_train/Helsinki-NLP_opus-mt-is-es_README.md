---
language: 
- is
- es

tags:
- translation

license: apache-2.0
---

### isl-spa

* source group: Icelandic 
* target group: Spanish 
*  OPUS readme: [isl-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/isl-spa/README.md)

*  model: transformer-align
* source language(s): isl
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/isl-spa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/isl-spa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/isl-spa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.isl.spa 	| 51.2 	| 0.665 |


### System Info: 
- hf_name: isl-spa

- source_languages: isl

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/isl-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['is', 'es']

- src_constituents: {'isl'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/isl-spa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/isl-spa/opus-2020-06-17.test.txt

- src_alpha3: isl

- tgt_alpha3: spa

- short_pair: is-es

- chrF2_score: 0.665

- bleu: 51.2

- brevity_penalty: 0.985

- ref_len: 1229.0

- src_name: Icelandic

- tgt_name: Spanish

- train_date: 2020-06-17

- src_alpha2: is

- tgt_alpha2: es

- prefer_old: False

- long_pair: isl-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41