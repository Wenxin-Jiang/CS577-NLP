---
language: 
- eo
- ro

tags:
- translation

license: apache-2.0
---

### epo-ron

* source group: Esperanto 
* target group: Romanian 
*  OPUS readme: [epo-ron](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-ron/README.md)

*  model: transformer-align
* source language(s): epo
* target language(s): ron
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ron/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ron/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ron/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.epo.ron 	| 19.4 	| 0.420 |


### System Info: 
- hf_name: epo-ron

- source_languages: epo

- target_languages: ron

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-ron/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eo', 'ro']

- src_constituents: {'epo'}

- tgt_constituents: {'ron'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ron/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ron/opus-2020-06-16.test.txt

- src_alpha3: epo

- tgt_alpha3: ron

- short_pair: eo-ro

- chrF2_score: 0.42

- bleu: 19.4

- brevity_penalty: 0.9179999999999999

- ref_len: 25619.0

- src_name: Esperanto

- tgt_name: Romanian

- train_date: 2020-06-16

- src_alpha2: eo

- tgt_alpha2: ro

- prefer_old: False

- long_pair: epo-ron

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41