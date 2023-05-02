---
language: 
- mk
- es

tags:
- translation

license: apache-2.0
---

### mkd-spa

* source group: Macedonian 
* target group: Spanish 
*  OPUS readme: [mkd-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/mkd-spa/README.md)

*  model: transformer-align
* source language(s): mkd
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/mkd-spa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/mkd-spa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/mkd-spa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.mkd.spa 	| 56.5 	| 0.717 |


### System Info: 
- hf_name: mkd-spa

- source_languages: mkd

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/mkd-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['mk', 'es']

- src_constituents: {'mkd'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/mkd-spa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/mkd-spa/opus-2020-06-17.test.txt

- src_alpha3: mkd

- tgt_alpha3: spa

- short_pair: mk-es

- chrF2_score: 0.7170000000000001

- bleu: 56.5

- brevity_penalty: 0.997

- ref_len: 1121.0

- src_name: Macedonian

- tgt_name: Spanish

- train_date: 2020-06-17

- src_alpha2: mk

- tgt_alpha2: es

- prefer_old: False

- long_pair: mkd-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41