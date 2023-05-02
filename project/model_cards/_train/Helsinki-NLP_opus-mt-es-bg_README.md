---
language: 
- es
- bg

tags:
- translation

license: apache-2.0
---

### spa-bul

* source group: Spanish 
* target group: Bulgarian 
*  OPUS readme: [spa-bul](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-bul/README.md)

*  model: transformer
* source language(s): spa
* target language(s): bul
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-bul/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-bul/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-bul/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.bul 	| 50.9 	| 0.674 |


### System Info: 
- hf_name: spa-bul

- source_languages: spa

- target_languages: bul

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-bul/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'bg']

- src_constituents: {'spa'}

- tgt_constituents: {'bul', 'bul_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-bul/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-bul/opus-2020-07-03.test.txt

- src_alpha3: spa

- tgt_alpha3: bul

- short_pair: es-bg

- chrF2_score: 0.674

- bleu: 50.9

- brevity_penalty: 0.955

- ref_len: 1707.0

- src_name: Spanish

- tgt_name: Bulgarian

- train_date: 2020-07-03

- src_alpha2: es

- tgt_alpha2: bg

- prefer_old: False

- long_pair: spa-bul

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41