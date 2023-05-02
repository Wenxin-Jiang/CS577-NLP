---
language: 
- az
- es

tags:
- translation

license: apache-2.0
---

### aze-spa

* source group: Azerbaijani 
* target group: Spanish 
*  OPUS readme: [aze-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/aze-spa/README.md)

*  model: transformer-align
* source language(s): aze_Latn
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/aze-spa/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/aze-spa/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/aze-spa/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.aze.spa 	| 11.8 	| 0.346 |


### System Info: 
- hf_name: aze-spa

- source_languages: aze

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/aze-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['az', 'es']

- src_constituents: {'aze_Latn'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/aze-spa/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/aze-spa/opus-2020-06-16.test.txt

- src_alpha3: aze

- tgt_alpha3: spa

- short_pair: az-es

- chrF2_score: 0.34600000000000003

- bleu: 11.8

- brevity_penalty: 1.0

- ref_len: 1144.0

- src_name: Azerbaijani

- tgt_name: Spanish

- train_date: 2020-06-16

- src_alpha2: az

- tgt_alpha2: es

- prefer_old: False

- long_pair: aze-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41