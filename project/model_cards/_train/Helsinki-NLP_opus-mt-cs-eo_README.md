---
language: 
- cs
- eo

tags:
- translation

license: apache-2.0
---

### ces-epo

* source group: Czech 
* target group: Esperanto 
*  OPUS readme: [ces-epo](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ces-epo/README.md)

*  model: transformer-align
* source language(s): ces
* target language(s): epo
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ces-epo/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ces-epo/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ces-epo/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ces.epo 	| 26.0 	| 0.459 |


### System Info: 
- hf_name: ces-epo

- source_languages: ces

- target_languages: epo

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ces-epo/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['cs', 'eo']

- src_constituents: {'ces'}

- tgt_constituents: {'epo'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ces-epo/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ces-epo/opus-2020-06-16.test.txt

- src_alpha3: ces

- tgt_alpha3: epo

- short_pair: cs-eo

- chrF2_score: 0.45899999999999996

- bleu: 26.0

- brevity_penalty: 0.94

- ref_len: 24901.0

- src_name: Czech

- tgt_name: Esperanto

- train_date: 2020-06-16

- src_alpha2: cs

- tgt_alpha2: eo

- prefer_old: False

- long_pair: ces-epo

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41