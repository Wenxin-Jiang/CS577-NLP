---
language: 
- eo
- da

tags:
- translation

license: apache-2.0
---

### epo-dan

* source group: Esperanto 
* target group: Danish 
*  OPUS readme: [epo-dan](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-dan/README.md)

*  model: transformer-align
* source language(s): epo
* target language(s): dan
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-dan/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-dan/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-dan/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.epo.dan 	| 21.6 	| 0.407 |


### System Info: 
- hf_name: epo-dan

- source_languages: epo

- target_languages: dan

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-dan/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eo', 'da']

- src_constituents: {'epo'}

- tgt_constituents: {'dan'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-dan/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-dan/opus-2020-06-16.test.txt

- src_alpha3: epo

- tgt_alpha3: dan

- short_pair: eo-da

- chrF2_score: 0.40700000000000003

- bleu: 21.6

- brevity_penalty: 0.9359999999999999

- ref_len: 72349.0

- src_name: Esperanto

- tgt_name: Danish

- train_date: 2020-06-16

- src_alpha2: eo

- tgt_alpha2: da

- prefer_old: False

- long_pair: epo-dan

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41