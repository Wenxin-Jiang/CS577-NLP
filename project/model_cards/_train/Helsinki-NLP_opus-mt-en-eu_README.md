---
language: 
- en
- eu

tags:
- translation

license: apache-2.0
---

### eng-eus

* source group: English 
* target group: Basque 
*  OPUS readme: [eng-eus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-eus/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): eus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-eus/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-eus/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-eus/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.eus 	| 31.8 	| 0.590 |


### System Info: 
- hf_name: eng-eus

- source_languages: eng

- target_languages: eus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-eus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'eu']

- src_constituents: {'eng'}

- tgt_constituents: {'eus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-eus/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-eus/opus-2020-06-17.test.txt

- src_alpha3: eng

- tgt_alpha3: eus

- short_pair: en-eu

- chrF2_score: 0.59

- bleu: 31.8

- brevity_penalty: 0.9440000000000001

- ref_len: 7080.0

- src_name: English

- tgt_name: Basque

- train_date: 2020-06-17

- src_alpha2: en

- tgt_alpha2: eu

- prefer_old: False

- long_pair: eng-eus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41