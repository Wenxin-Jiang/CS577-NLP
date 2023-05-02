---
language: 
- eu
- es

tags:
- translation

license: apache-2.0
---

### eus-spa

* source group: Basque 
* target group: Spanish 
*  OPUS readme: [eus-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eus-spa/README.md)

*  model: transformer-align
* source language(s): eus
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eus-spa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eus-spa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eus-spa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eus.spa 	| 48.8 	| 0.673 |


### System Info: 
- hf_name: eus-spa

- source_languages: eus

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eus-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eu', 'es']

- src_constituents: {'eus'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eus-spa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eus-spa/opus-2020-06-17.test.txt

- src_alpha3: eus

- tgt_alpha3: spa

- short_pair: eu-es

- chrF2_score: 0.6729999999999999

- bleu: 48.8

- brevity_penalty: 0.9640000000000001

- ref_len: 12469.0

- src_name: Basque

- tgt_name: Spanish

- train_date: 2020-06-17

- src_alpha2: eu

- tgt_alpha2: es

- prefer_old: False

- long_pair: eus-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41