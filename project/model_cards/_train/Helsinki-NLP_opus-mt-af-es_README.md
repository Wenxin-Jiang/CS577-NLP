---
language: 
- af
- es

tags:
- translation

license: apache-2.0
---

### afr-spa

* source group: Afrikaans 
* target group: Spanish 
*  OPUS readme: [afr-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afr-spa/README.md)

*  model: transformer-align
* source language(s): afr
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/afr-spa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afr-spa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afr-spa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.afr.spa 	| 49.9 	| 0.680 |


### System Info: 
- hf_name: afr-spa

- source_languages: afr

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afr-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['af', 'es']

- src_constituents: {'afr'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/afr-spa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/afr-spa/opus-2020-06-17.test.txt

- src_alpha3: afr

- tgt_alpha3: spa

- short_pair: af-es

- chrF2_score: 0.68

- bleu: 49.9

- brevity_penalty: 1.0

- ref_len: 2783.0

- src_name: Afrikaans

- tgt_name: Spanish

- train_date: 2020-06-17

- src_alpha2: af

- tgt_alpha2: es

- prefer_old: False

- long_pair: afr-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41