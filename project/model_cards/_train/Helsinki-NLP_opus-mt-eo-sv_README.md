---
language: 
- eo
- sv

tags:
- translation

license: apache-2.0
---

### epo-swe

* source group: Esperanto 
* target group: Swedish 
*  OPUS readme: [epo-swe](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-swe/README.md)

*  model: transformer-align
* source language(s): epo
* target language(s): swe
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-swe/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-swe/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-swe/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.epo.swe 	| 29.5 	| 0.463 |


### System Info: 
- hf_name: epo-swe

- source_languages: epo

- target_languages: swe

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-swe/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eo', 'sv']

- src_constituents: {'epo'}

- tgt_constituents: {'swe'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-swe/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-swe/opus-2020-06-16.test.txt

- src_alpha3: epo

- tgt_alpha3: swe

- short_pair: eo-sv

- chrF2_score: 0.46299999999999997

- bleu: 29.5

- brevity_penalty: 0.9640000000000001

- ref_len: 10977.0

- src_name: Esperanto

- tgt_name: Swedish

- train_date: 2020-06-16

- src_alpha2: eo

- tgt_alpha2: sv

- prefer_old: False

- long_pair: epo-swe

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41