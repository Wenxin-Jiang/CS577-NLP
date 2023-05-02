---
language: 
- eo
- he

tags:
- translation

license: apache-2.0
---

### epo-heb

* source group: Esperanto 
* target group: Hebrew 
*  OPUS readme: [epo-heb](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-heb/README.md)

*  model: transformer-align
* source language(s): epo
* target language(s): heb
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-heb/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-heb/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-heb/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.epo.heb 	| 11.5 	| 0.306 |


### System Info: 
- hf_name: epo-heb

- source_languages: epo

- target_languages: heb

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-heb/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eo', 'he']

- src_constituents: {'epo'}

- tgt_constituents: {'heb'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-heb/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-heb/opus-2020-06-16.test.txt

- src_alpha3: epo

- tgt_alpha3: heb

- short_pair: eo-he

- chrF2_score: 0.306

- bleu: 11.5

- brevity_penalty: 0.943

- ref_len: 65645.0

- src_name: Esperanto

- tgt_name: Hebrew

- train_date: 2020-06-16

- src_alpha2: eo

- tgt_alpha2: he

- prefer_old: False

- long_pair: epo-heb

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41