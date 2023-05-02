---
language: 
- no
- es

tags:
- translation

license: apache-2.0
---

### nor-spa

* source group: Norwegian 
* target group: Spanish 
*  OPUS readme: [nor-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-spa/README.md)

*  model: transformer-align
* source language(s): nno nob
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-spa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-spa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-spa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.nor.spa 	| 34.2 	| 0.565 |


### System Info: 
- hf_name: nor-spa

- source_languages: nor

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['no', 'es']

- src_constituents: {'nob', 'nno'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-spa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-spa/opus-2020-06-17.test.txt

- src_alpha3: nor

- tgt_alpha3: spa

- short_pair: no-es

- chrF2_score: 0.565

- bleu: 34.2

- brevity_penalty: 0.997

- ref_len: 7311.0

- src_name: Norwegian

- tgt_name: Spanish

- train_date: 2020-06-17

- src_alpha2: no

- tgt_alpha2: es

- prefer_old: False

- long_pair: nor-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41