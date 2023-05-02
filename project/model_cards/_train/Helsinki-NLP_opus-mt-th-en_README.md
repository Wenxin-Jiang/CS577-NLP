---
language: 
- th
- en

tags:
- translation

license: apache-2.0
---

### tha-eng

* source group: Thai 
* target group: English 
*  OPUS readme: [tha-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tha-eng/README.md)

*  model: transformer-align
* source language(s): tha
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/tha-eng/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tha-eng/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tha-eng/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.tha.eng 	| 48.1 	| 0.644 |


### System Info: 
- hf_name: tha-eng

- source_languages: tha

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tha-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['th', 'en']

- src_constituents: {'tha'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/tha-eng/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/tha-eng/opus-2020-06-17.test.txt

- src_alpha3: tha

- tgt_alpha3: eng

- short_pair: th-en

- chrF2_score: 0.644

- bleu: 48.1

- brevity_penalty: 0.9740000000000001

- ref_len: 7407.0

- src_name: Thai

- tgt_name: English

- train_date: 2020-06-17

- src_alpha2: th

- tgt_alpha2: en

- prefer_old: False

- long_pair: tha-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41