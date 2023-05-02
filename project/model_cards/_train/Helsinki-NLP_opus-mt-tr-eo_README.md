---
language: 
- tr
- eo

tags:
- translation

license: apache-2.0
---

### tur-epo

* source group: Turkish 
* target group: Esperanto 
*  OPUS readme: [tur-epo](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tur-epo/README.md)

*  model: transformer-align
* source language(s): tur
* target language(s): epo
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/tur-epo/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tur-epo/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tur-epo/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.tur.epo 	| 17.0 	| 0.373 |


### System Info: 
- hf_name: tur-epo

- source_languages: tur

- target_languages: epo

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tur-epo/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['tr', 'eo']

- src_constituents: {'tur'}

- tgt_constituents: {'epo'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/tur-epo/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/tur-epo/opus-2020-06-16.test.txt

- src_alpha3: tur

- tgt_alpha3: epo

- short_pair: tr-eo

- chrF2_score: 0.373

- bleu: 17.0

- brevity_penalty: 0.8809999999999999

- ref_len: 33762.0

- src_name: Turkish

- tgt_name: Esperanto

- train_date: 2020-06-16

- src_alpha2: tr

- tgt_alpha2: eo

- prefer_old: False

- long_pair: tur-epo

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41