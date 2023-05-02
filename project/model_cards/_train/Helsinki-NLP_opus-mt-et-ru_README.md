---
language: 
- et
- ru

tags:
- translation

license: apache-2.0
---

### est-rus

* source group: Estonian 
* target group: Russian 
*  OPUS readme: [est-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/est-rus/README.md)

*  model: transformer-align
* source language(s): est
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/est-rus/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/est-rus/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/est-rus/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.est.rus 	| 50.2 	| 0.702 |


### System Info: 
- hf_name: est-rus

- source_languages: est

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/est-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['et', 'ru']

- src_constituents: {'est'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/est-rus/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/est-rus/opus-2020-06-17.test.txt

- src_alpha3: est

- tgt_alpha3: rus

- short_pair: et-ru

- chrF2_score: 0.7020000000000001

- bleu: 50.2

- brevity_penalty: 0.988

- ref_len: 3569.0

- src_name: Estonian

- tgt_name: Russian

- train_date: 2020-06-17

- src_alpha2: et

- tgt_alpha2: ru

- prefer_old: False

- long_pair: est-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41