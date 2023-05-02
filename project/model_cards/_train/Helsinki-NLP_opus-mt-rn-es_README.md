---
language: 
- rn
- es

tags:
- translation

license: apache-2.0
---

### run-spa

* source group: Rundi 
* target group: Spanish 
*  OPUS readme: [run-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/run-spa/README.md)

*  model: transformer-align
* source language(s): run
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/run-spa/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/run-spa/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/run-spa/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.run.spa 	| 14.4 	| 0.376 |


### System Info: 
- hf_name: run-spa

- source_languages: run

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/run-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['rn', 'es']

- src_constituents: {'run'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/run-spa/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/run-spa/opus-2020-06-16.test.txt

- src_alpha3: run

- tgt_alpha3: spa

- short_pair: rn-es

- chrF2_score: 0.376

- bleu: 14.4

- brevity_penalty: 1.0

- ref_len: 5167.0

- src_name: Rundi

- tgt_name: Spanish

- train_date: 2020-06-16

- src_alpha2: rn

- tgt_alpha2: es

- prefer_old: False

- long_pair: run-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41