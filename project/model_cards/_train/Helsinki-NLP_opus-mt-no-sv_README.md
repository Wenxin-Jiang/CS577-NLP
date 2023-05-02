---
language: 
- no
- sv

tags:
- translation

license: apache-2.0
---

### nor-swe

* source group: Norwegian 
* target group: Swedish 
*  OPUS readme: [nor-swe](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-swe/README.md)

*  model: transformer-align
* source language(s): nno nob
* target language(s): swe
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-swe/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-swe/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-swe/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.nor.swe 	| 63.7 	| 0.773 |


### System Info: 
- hf_name: nor-swe

- source_languages: nor

- target_languages: swe

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-swe/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['no', 'sv']

- src_constituents: {'nob', 'nno'}

- tgt_constituents: {'swe'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-swe/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-swe/opus-2020-06-17.test.txt

- src_alpha3: nor

- tgt_alpha3: swe

- short_pair: no-sv

- chrF2_score: 0.773

- bleu: 63.7

- brevity_penalty: 0.9670000000000001

- ref_len: 3672.0

- src_name: Norwegian

- tgt_name: Swedish

- train_date: 2020-06-17

- src_alpha2: no

- tgt_alpha2: sv

- prefer_old: False

- long_pair: nor-swe

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41