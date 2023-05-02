---
language: 
- ru
- sv

tags:
- translation

license: apache-2.0
---

### rus-swe

* source group: Russian 
* target group: Swedish 
*  OPUS readme: [rus-swe](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-swe/README.md)

*  model: transformer-align
* source language(s): rus
* target language(s): swe
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-swe/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-swe/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-swe/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.swe 	| 51.9 	| 0.677 |


### System Info: 
- hf_name: rus-swe

- source_languages: rus

- target_languages: swe

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-swe/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'sv']

- src_constituents: {'rus'}

- tgt_constituents: {'swe'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-swe/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-swe/opus-2020-06-17.test.txt

- src_alpha3: rus

- tgt_alpha3: swe

- short_pair: ru-sv

- chrF2_score: 0.677

- bleu: 51.9

- brevity_penalty: 0.968

- ref_len: 8449.0

- src_name: Russian

- tgt_name: Swedish

- train_date: 2020-06-17

- src_alpha2: ru

- tgt_alpha2: sv

- prefer_old: False

- long_pair: rus-swe

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41