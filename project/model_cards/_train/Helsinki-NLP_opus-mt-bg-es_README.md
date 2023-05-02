---
language: 
- bg
- es

tags:
- translation

license: apache-2.0
---

### bul-spa

* source group: Bulgarian 
* target group: Spanish 
*  OPUS readme: [bul-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-spa/README.md)

*  model: transformer
* source language(s): bul
* target language(s): spa
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-spa/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-spa/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-spa/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bul.spa 	| 49.1 	| 0.661 |


### System Info: 
- hf_name: bul-spa

- source_languages: bul

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bg', 'es']

- src_constituents: {'bul', 'bul_Latn'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-spa/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-spa/opus-2020-07-03.test.txt

- src_alpha3: bul

- tgt_alpha3: spa

- short_pair: bg-es

- chrF2_score: 0.6609999999999999

- bleu: 49.1

- brevity_penalty: 0.992

- ref_len: 1783.0

- src_name: Bulgarian

- tgt_name: Spanish

- train_date: 2020-07-03

- src_alpha2: bg

- tgt_alpha2: es

- prefer_old: False

- long_pair: bul-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41