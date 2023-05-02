---
language: 
- no
- pl

tags:
- translation

license: apache-2.0
---

### nor-pol

* source group: Norwegian 
* target group: Polish 
*  OPUS readme: [nor-pol](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-pol/README.md)

*  model: transformer-align
* source language(s): nob
* target language(s): pol
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-pol/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-pol/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-pol/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.nor.pol 	| 20.9 	| 0.455 |


### System Info: 
- hf_name: nor-pol

- source_languages: nor

- target_languages: pol

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-pol/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['no', 'pl']

- src_constituents: {'nob', 'nno'}

- tgt_constituents: {'pol'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-pol/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-pol/opus-2020-06-17.test.txt

- src_alpha3: nor

- tgt_alpha3: pol

- short_pair: no-pl

- chrF2_score: 0.455

- bleu: 20.9

- brevity_penalty: 0.941

- ref_len: 1828.0

- src_name: Norwegian

- tgt_name: Polish

- train_date: 2020-06-17

- src_alpha2: no

- tgt_alpha2: pl

- prefer_old: False

- long_pair: nor-pol

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41