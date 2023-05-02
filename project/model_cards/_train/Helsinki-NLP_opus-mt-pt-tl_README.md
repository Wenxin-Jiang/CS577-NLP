---
language: 
- pt
- tl

tags:
- translation

license: apache-2.0
---

### por-tgl

* source group: Portuguese 
* target group: Tagalog 
*  OPUS readme: [por-tgl](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/por-tgl/README.md)

*  model: transformer-align
* source language(s): por
* target language(s): tgl_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/por-tgl/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/por-tgl/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/por-tgl/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.por.tgl 	| 28.4 	| 0.565 |


### System Info: 
- hf_name: por-tgl

- source_languages: por

- target_languages: tgl

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/por-tgl/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['pt', 'tl']

- src_constituents: {'por'}

- tgt_constituents: {'tgl_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/por-tgl/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/por-tgl/opus-2020-06-17.test.txt

- src_alpha3: por

- tgt_alpha3: tgl

- short_pair: pt-tl

- chrF2_score: 0.565

- bleu: 28.4

- brevity_penalty: 1.0

- ref_len: 13620.0

- src_name: Portuguese

- tgt_name: Tagalog

- train_date: 2020-06-17

- src_alpha2: pt

- tgt_alpha2: tl

- prefer_old: False

- long_pair: por-tgl

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41