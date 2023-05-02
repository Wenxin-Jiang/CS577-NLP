---
language: 
- rn
- ru

tags:
- translation

license: apache-2.0
---

### run-rus

* source group: Rundi 
* target group: Russian 
*  OPUS readme: [run-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/run-rus/README.md)

*  model: transformer-align
* source language(s): run
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/run-rus/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/run-rus/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/run-rus/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.run.rus 	| 17.1 	| 0.321 |


### System Info: 
- hf_name: run-rus

- source_languages: run

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/run-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['rn', 'ru']

- src_constituents: {'run'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/run-rus/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/run-rus/opus-2020-06-16.test.txt

- src_alpha3: run

- tgt_alpha3: rus

- short_pair: rn-ru

- chrF2_score: 0.321

- bleu: 17.1

- brevity_penalty: 1.0

- ref_len: 6635.0

- src_name: Rundi

- tgt_name: Russian

- train_date: 2020-06-16

- src_alpha2: rn

- tgt_alpha2: ru

- prefer_old: False

- long_pair: run-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41