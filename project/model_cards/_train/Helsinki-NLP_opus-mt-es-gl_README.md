---
language: 
- es
- gl

tags:
- translation

license: apache-2.0
---

### spa-glg

* source group: Spanish 
* target group: Galician 
*  OPUS readme: [spa-glg](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-glg/README.md)

*  model: transformer-align
* source language(s): spa
* target language(s): glg
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-glg/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-glg/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-glg/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.glg 	| 67.6 	| 0.808 |


### System Info: 
- hf_name: spa-glg

- source_languages: spa

- target_languages: glg

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-glg/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'gl']

- src_constituents: {'spa'}

- tgt_constituents: {'glg'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-glg/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-glg/opus-2020-06-16.test.txt

- src_alpha3: spa

- tgt_alpha3: glg

- short_pair: es-gl

- chrF2_score: 0.8079999999999999

- bleu: 67.6

- brevity_penalty: 0.993

- ref_len: 16581.0

- src_name: Spanish

- tgt_name: Galician

- train_date: 2020-06-16

- src_alpha2: es

- tgt_alpha2: gl

- prefer_old: False

- long_pair: spa-glg

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41