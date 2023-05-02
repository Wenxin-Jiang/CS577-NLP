---
language: 
- pt
- gl

tags:
- translation

license: apache-2.0
---

### por-glg

* source group: Portuguese 
* target group: Galician 
*  OPUS readme: [por-glg](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/por-glg/README.md)

*  model: transformer-align
* source language(s): por
* target language(s): glg
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/por-glg/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/por-glg/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/por-glg/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.por.glg 	| 55.8 	| 0.737 |


### System Info: 
- hf_name: por-glg

- source_languages: por

- target_languages: glg

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/por-glg/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['pt', 'gl']

- src_constituents: {'por'}

- tgt_constituents: {'glg'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/por-glg/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/por-glg/opus-2020-06-16.test.txt

- src_alpha3: por

- tgt_alpha3: glg

- short_pair: pt-gl

- chrF2_score: 0.737

- bleu: 55.8

- brevity_penalty: 0.996

- ref_len: 2989.0

- src_name: Portuguese

- tgt_name: Galician

- train_date: 2020-06-16

- src_alpha2: pt

- tgt_alpha2: gl

- prefer_old: False

- long_pair: por-glg

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41