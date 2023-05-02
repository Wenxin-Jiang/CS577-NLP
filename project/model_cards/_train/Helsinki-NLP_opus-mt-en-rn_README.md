---
language: 
- en
- rn

tags:
- translation

license: apache-2.0
---

### eng-run

* source group: English 
* target group: Rundi 
*  OPUS readme: [eng-run](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-run/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): run
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-run/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-run/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-run/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.run 	| 10.4 	| 0.436 |


### System Info: 
- hf_name: eng-run

- source_languages: eng

- target_languages: run

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-run/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'rn']

- src_constituents: {'eng'}

- tgt_constituents: {'run'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-run/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-run/opus-2020-06-16.test.txt

- src_alpha3: eng

- tgt_alpha3: run

- short_pair: en-rn

- chrF2_score: 0.436

- bleu: 10.4

- brevity_penalty: 1.0

- ref_len: 6710.0

- src_name: English

- tgt_name: Rundi

- train_date: 2020-06-16

- src_alpha2: en

- tgt_alpha2: rn

- prefer_old: False

- long_pair: eng-run

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41