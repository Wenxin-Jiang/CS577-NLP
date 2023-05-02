---
language: 
- es
- vi

tags:
- translation

license: apache-2.0
---

### spa-vie

* source group: Spanish 
* target group: Vietnamese 
*  OPUS readme: [spa-vie](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-vie/README.md)

*  model: transformer-align
* source language(s): spa
* target language(s): vie
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-vie/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-vie/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-vie/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.vie 	| 33.1 	| 0.508 |


### System Info: 
- hf_name: spa-vie

- source_languages: spa

- target_languages: vie

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-vie/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'vi']

- src_constituents: {'spa'}

- tgt_constituents: {'vie', 'vie_Hani'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-vie/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-vie/opus-2020-06-17.test.txt

- src_alpha3: spa

- tgt_alpha3: vie

- short_pair: es-vi

- chrF2_score: 0.508

- bleu: 33.1

- brevity_penalty: 0.98

- ref_len: 4654.0

- src_name: Spanish

- tgt_name: Vietnamese

- train_date: 2020-06-17

- src_alpha2: es

- tgt_alpha2: vi

- prefer_old: False

- long_pair: spa-vie

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41