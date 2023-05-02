---
language: 
- es
- ca

tags:
- translation

license: apache-2.0
---

### spa-cat

* source group: Spanish 
* target group: Catalan 
*  OPUS readme: [spa-cat](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-cat/README.md)

*  model: transformer-align
* source language(s): spa
* target language(s): cat
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-cat/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-cat/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-cat/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.cat 	| 68.9 	| 0.832 |


### System Info: 
- hf_name: spa-cat

- source_languages: spa

- target_languages: cat

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-cat/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'ca']

- src_constituents: {'spa'}

- tgt_constituents: {'cat'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-cat/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-cat/opus-2020-06-17.test.txt

- src_alpha3: spa

- tgt_alpha3: cat

- short_pair: es-ca

- chrF2_score: 0.8320000000000001

- bleu: 68.9

- brevity_penalty: 1.0

- ref_len: 12343.0

- src_name: Spanish

- tgt_name: Catalan

- train_date: 2020-06-17

- src_alpha2: es

- tgt_alpha2: ca

- prefer_old: False

- long_pair: spa-cat

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41