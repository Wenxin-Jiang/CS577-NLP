---
language: 
- es
- rn

tags:
- translation

license: apache-2.0
---

### spa-run

* source group: Spanish 
* target group: Rundi 
*  OPUS readme: [spa-run](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-run/README.md)

*  model: transformer-align
* source language(s): spa
* target language(s): run
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-run/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-run/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-run/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.run 	| 10.1 	| 0.410 |


### System Info: 
- hf_name: spa-run

- source_languages: spa

- target_languages: run

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-run/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'rn']

- src_constituents: {'spa'}

- tgt_constituents: {'run'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-run/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-run/opus-2020-06-16.test.txt

- src_alpha3: spa

- tgt_alpha3: run

- short_pair: es-rn

- chrF2_score: 0.41

- bleu: 10.1

- brevity_penalty: 1.0

- ref_len: 3886.0

- src_name: Spanish

- tgt_name: Rundi

- train_date: 2020-06-16

- src_alpha2: es

- tgt_alpha2: rn

- prefer_old: False

- long_pair: spa-run

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41