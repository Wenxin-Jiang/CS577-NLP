---
language: 
- gl
- es

tags:
- translation

license: apache-2.0
---

### glg-spa

* source group: Galician 
* target group: Spanish 
*  OPUS readme: [glg-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/glg-spa/README.md)

*  model: transformer-align
* source language(s): glg
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/glg-spa/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/glg-spa/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/glg-spa/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.glg.spa 	| 72.2 	| 0.836 |


### System Info: 
- hf_name: glg-spa

- source_languages: glg

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/glg-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['gl', 'es']

- src_constituents: {'glg'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/glg-spa/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/glg-spa/opus-2020-06-16.test.txt

- src_alpha3: glg

- tgt_alpha3: spa

- short_pair: gl-es

- chrF2_score: 0.836

- bleu: 72.2

- brevity_penalty: 0.982

- ref_len: 17443.0

- src_name: Galician

- tgt_name: Spanish

- train_date: 2020-06-16

- src_alpha2: gl

- tgt_alpha2: es

- prefer_old: False

- long_pair: glg-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41