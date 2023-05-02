---
language: 
- lt
- eo

tags:
- translation

license: apache-2.0
---

### lit-epo

* source group: Lithuanian 
* target group: Esperanto 
*  OPUS readme: [lit-epo](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/lit-epo/README.md)

*  model: transformer-align
* source language(s): lit
* target language(s): epo
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/lit-epo/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/lit-epo/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/lit-epo/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.lit.epo 	| 13.0 	| 0.313 |


### System Info: 
- hf_name: lit-epo

- source_languages: lit

- target_languages: epo

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/lit-epo/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['lt', 'eo']

- src_constituents: {'lit'}

- tgt_constituents: {'epo'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/lit-epo/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/lit-epo/opus-2020-06-16.test.txt

- src_alpha3: lit

- tgt_alpha3: epo

- short_pair: lt-eo

- chrF2_score: 0.313

- bleu: 13.0

- brevity_penalty: 1.0

- ref_len: 70340.0

- src_name: Lithuanian

- tgt_name: Esperanto

- train_date: 2020-06-16

- src_alpha2: lt

- tgt_alpha2: eo

- prefer_old: False

- long_pair: lit-epo

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41