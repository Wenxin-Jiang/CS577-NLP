---
language: 
- es
- eu

tags:
- translation

license: apache-2.0
---

### spa-eus

* source group: Spanish 
* target group: Basque 
*  OPUS readme: [spa-eus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-eus/README.md)

*  model: transformer-align
* source language(s): spa
* target language(s): eus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eus/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eus/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eus/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.eus 	| 37.0 	| 0.638 |


### System Info: 
- hf_name: spa-eus

- source_languages: spa

- target_languages: eus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-eus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'eu']

- src_constituents: {'spa'}

- tgt_constituents: {'eus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eus/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eus/opus-2020-06-17.test.txt

- src_alpha3: spa

- tgt_alpha3: eus

- short_pair: es-eu

- chrF2_score: 0.638

- bleu: 37.0

- brevity_penalty: 0.983

- ref_len: 10945.0

- src_name: Spanish

- tgt_name: Basque

- train_date: 2020-06-17

- src_alpha2: es

- tgt_alpha2: eu

- prefer_old: False

- long_pair: spa-eus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41