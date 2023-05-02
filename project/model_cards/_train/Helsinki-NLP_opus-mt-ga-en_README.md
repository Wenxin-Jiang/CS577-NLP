---
language: 
- ga
- en

tags:
- translation

license: apache-2.0
---

### gle-eng

* source group: Irish 
* target group: English 
*  OPUS readme: [gle-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gle-eng/README.md)

*  model: transformer-align
* source language(s): gle
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gle-eng/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gle-eng/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gle-eng/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.gle.eng 	| 51.6 	| 0.672 |


### System Info: 
- hf_name: gle-eng

- source_languages: gle

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gle-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ga', 'en']

- src_constituents: {'gle'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/gle-eng/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/gle-eng/opus-2020-06-17.test.txt

- src_alpha3: gle

- tgt_alpha3: eng

- short_pair: ga-en

- chrF2_score: 0.672

- bleu: 51.6

- brevity_penalty: 1.0

- ref_len: 11247.0

- src_name: Irish

- tgt_name: English

- train_date: 2020-06-17

- src_alpha2: ga

- tgt_alpha2: en

- prefer_old: False

- long_pair: gle-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41