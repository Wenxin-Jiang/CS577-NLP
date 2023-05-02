---
language: 
- be
- es

tags:
- translation

license: apache-2.0
---

### bel-spa

* source group: Belarusian 
* target group: Spanish 
*  OPUS readme: [bel-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bel-spa/README.md)

*  model: transformer-align
* source language(s): bel bel_Latn
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/bel-spa/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bel-spa/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bel-spa/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bel.spa 	| 11.8 	| 0.272 |


### System Info: 
- hf_name: bel-spa

- source_languages: bel

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bel-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['be', 'es']

- src_constituents: {'bel', 'bel_Latn'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/bel-spa/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/bel-spa/opus-2020-06-16.test.txt

- src_alpha3: bel

- tgt_alpha3: spa

- short_pair: be-es

- chrF2_score: 0.272

- bleu: 11.8

- brevity_penalty: 0.892

- ref_len: 1412.0

- src_name: Belarusian

- tgt_name: Spanish

- train_date: 2020-06-16

- src_alpha2: be

- tgt_alpha2: es

- prefer_old: False

- long_pair: bel-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41