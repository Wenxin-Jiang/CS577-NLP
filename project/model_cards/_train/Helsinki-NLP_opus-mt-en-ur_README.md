---
language: 
- en
- ur

tags:
- translation

license: apache-2.0
---

### eng-urd

* source group: English 
* target group: Urdu 
*  OPUS readme: [eng-urd](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-urd/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): urd
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urd/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urd/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urd/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.urd 	| 12.1 	| 0.390 |


### System Info: 
- hf_name: eng-urd

- source_languages: eng

- target_languages: urd

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-urd/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'ur']

- src_constituents: {'eng'}

- tgt_constituents: {'urd'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urd/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urd/opus-2020-06-17.test.txt

- src_alpha3: eng

- tgt_alpha3: urd

- short_pair: en-ur

- chrF2_score: 0.39

- bleu: 12.1

- brevity_penalty: 1.0

- ref_len: 12155.0

- src_name: English

- tgt_name: Urdu

- train_date: 2020-06-17

- src_alpha2: en

- tgt_alpha2: ur

- prefer_old: False

- long_pair: eng-urd

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41