---
language: 
- nl
- no

tags:
- translation

license: apache-2.0
---

### nld-nor

* source group: Dutch 
* target group: Norwegian 
*  OPUS readme: [nld-nor](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nld-nor/README.md)

*  model: transformer-align
* source language(s): nld
* target language(s): nob
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/nld-nor/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nld-nor/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nld-nor/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.nld.nor 	| 36.1 	| 0.562 |


### System Info: 
- hf_name: nld-nor

- source_languages: nld

- target_languages: nor

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nld-nor/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['nl', 'no']

- src_constituents: {'nld'}

- tgt_constituents: {'nob', 'nno'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/nld-nor/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/nld-nor/opus-2020-06-17.test.txt

- src_alpha3: nld

- tgt_alpha3: nor

- short_pair: nl-no

- chrF2_score: 0.562

- bleu: 36.1

- brevity_penalty: 0.966

- ref_len: 1459.0

- src_name: Dutch

- tgt_name: Norwegian

- train_date: 2020-06-17

- src_alpha2: nl

- tgt_alpha2: no

- prefer_old: False

- long_pair: nld-nor

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41