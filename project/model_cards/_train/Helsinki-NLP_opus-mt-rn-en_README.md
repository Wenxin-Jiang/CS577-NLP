---
language: 
- rn
- en

tags:
- translation

license: apache-2.0
---

### run-eng

* source group: Rundi 
* target group: English 
*  OPUS readme: [run-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/run-eng/README.md)

*  model: transformer-align
* source language(s): run
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/run-eng/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/run-eng/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/run-eng/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.run.eng 	| 26.7 	| 0.428 |


### System Info: 
- hf_name: run-eng

- source_languages: run

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/run-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['rn', 'en']

- src_constituents: {'run'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/run-eng/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/run-eng/opus-2020-06-16.test.txt

- src_alpha3: run

- tgt_alpha3: eng

- short_pair: rn-en

- chrF2_score: 0.428

- bleu: 26.7

- brevity_penalty: 0.99

- ref_len: 10041.0

- src_name: Rundi

- tgt_name: English

- train_date: 2020-06-16

- src_alpha2: rn

- tgt_alpha2: en

- prefer_old: False

- long_pair: run-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41