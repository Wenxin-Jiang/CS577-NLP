---
language: 
- ru
- sl

tags:
- translation

license: apache-2.0
---

### rus-slv

* source group: Russian 
* target group: Slovenian 
*  OPUS readme: [rus-slv](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-slv/README.md)

*  model: transformer-align
* source language(s): rus
* target language(s): slv
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-slv/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-slv/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-slv/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.slv 	| 32.3 	| 0.492 |


### System Info: 
- hf_name: rus-slv

- source_languages: rus

- target_languages: slv

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-slv/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'sl']

- src_constituents: {'rus'}

- tgt_constituents: {'slv'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-slv/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-slv/opus-2020-06-17.test.txt

- src_alpha3: rus

- tgt_alpha3: slv

- short_pair: ru-sl

- chrF2_score: 0.49200000000000005

- bleu: 32.3

- brevity_penalty: 0.992

- ref_len: 2135.0

- src_name: Russian

- tgt_name: Slovenian

- train_date: 2020-06-17

- src_alpha2: ru

- tgt_alpha2: sl

- prefer_old: False

- long_pair: rus-slv

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41