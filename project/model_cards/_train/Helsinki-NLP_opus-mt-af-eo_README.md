---
language: 
- af
- eo

tags:
- translation

license: apache-2.0
---

### afr-epo

* source group: Afrikaans 
* target group: Esperanto 
*  OPUS readme: [afr-epo](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afr-epo/README.md)

*  model: transformer-align
* source language(s): afr
* target language(s): epo
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/afr-epo/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afr-epo/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afr-epo/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.afr.epo 	| 18.3 	| 0.411 |


### System Info: 
- hf_name: afr-epo

- source_languages: afr

- target_languages: epo

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afr-epo/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['af', 'eo']

- src_constituents: {'afr'}

- tgt_constituents: {'epo'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/afr-epo/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/afr-epo/opus-2020-06-16.test.txt

- src_alpha3: afr

- tgt_alpha3: epo

- short_pair: af-eo

- chrF2_score: 0.41100000000000003

- bleu: 18.3

- brevity_penalty: 0.995

- ref_len: 7517.0

- src_name: Afrikaans

- tgt_name: Esperanto

- train_date: 2020-06-16

- src_alpha2: af

- tgt_alpha2: eo

- prefer_old: False

- long_pair: afr-epo

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41