---
language: 
- da
- eo

tags:
- translation

license: apache-2.0
---

### dan-epo

* source group: Danish 
* target group: Esperanto 
*  OPUS readme: [dan-epo](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/dan-epo/README.md)

*  model: transformer-align
* source language(s): dan
* target language(s): epo
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/dan-epo/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/dan-epo/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/dan-epo/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.dan.epo 	| 23.6 	| 0.432 |


### System Info: 
- hf_name: dan-epo

- source_languages: dan

- target_languages: epo

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/dan-epo/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['da', 'eo']

- src_constituents: {'dan'}

- tgt_constituents: {'epo'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/dan-epo/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/dan-epo/opus-2020-06-16.test.txt

- src_alpha3: dan

- tgt_alpha3: epo

- short_pair: da-eo

- chrF2_score: 0.43200000000000005

- bleu: 23.6

- brevity_penalty: 0.9420000000000001

- ref_len: 69856.0

- src_name: Danish

- tgt_name: Esperanto

- train_date: 2020-06-16

- src_alpha2: da

- tgt_alpha2: eo

- prefer_old: False

- long_pair: dan-epo

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41