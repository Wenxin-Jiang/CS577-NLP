---
language: 
- ka
- ru

tags:
- translation

license: apache-2.0
---

### kat-rus

* source group: Georgian 
* target group: Russian 
*  OPUS readme: [kat-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/kat-rus/README.md)

*  model: transformer-align
* source language(s): kat
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/kat-rus/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/kat-rus/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/kat-rus/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.kat.rus 	| 38.2 	| 0.604 |


### System Info: 
- hf_name: kat-rus

- source_languages: kat

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/kat-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ka', 'ru']

- src_constituents: {'kat'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/kat-rus/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/kat-rus/opus-2020-06-16.test.txt

- src_alpha3: kat

- tgt_alpha3: rus

- short_pair: ka-ru

- chrF2_score: 0.604

- bleu: 38.2

- brevity_penalty: 0.996

- ref_len: 3899.0

- src_name: Georgian

- tgt_name: Russian

- train_date: 2020-06-16

- src_alpha2: ka

- tgt_alpha2: ru

- prefer_old: False

- long_pair: kat-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41