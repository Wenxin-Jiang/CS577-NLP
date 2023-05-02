---
language: 
- tl
- es

tags:
- translation

license: apache-2.0
---

### tgl-spa

* source group: Tagalog 
* target group: Spanish 
*  OPUS readme: [tgl-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tgl-spa/README.md)

*  model: transformer-align
* source language(s): tgl_Latn
* target language(s): spa
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-spa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-spa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-spa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.tgl.spa 	| 31.6 	| 0.531 |


### System Info: 
- hf_name: tgl-spa

- source_languages: tgl

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tgl-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['tl', 'es']

- src_constituents: {'tgl_Latn'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-spa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-spa/opus-2020-06-17.test.txt

- src_alpha3: tgl

- tgt_alpha3: spa

- short_pair: tl-es

- chrF2_score: 0.531

- bleu: 31.6

- brevity_penalty: 0.997

- ref_len: 4327.0

- src_name: Tagalog

- tgt_name: Spanish

- train_date: 2020-06-17

- src_alpha2: tl

- tgt_alpha2: es

- prefer_old: False

- long_pair: tgl-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41