---
language: 
- az
- en

tags:
- translation

license: apache-2.0
---

### aze-eng

* source group: Azerbaijani 
* target group: English 
*  OPUS readme: [aze-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/aze-eng/README.md)

*  model: transformer-align
* source language(s): aze_Latn
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/aze-eng/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/aze-eng/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/aze-eng/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.aze.eng 	| 31.9 	| 0.490 |


### System Info: 
- hf_name: aze-eng

- source_languages: aze

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/aze-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['az', 'en']

- src_constituents: {'aze_Latn'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/aze-eng/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/aze-eng/opus-2020-06-16.test.txt

- src_alpha3: aze

- tgt_alpha3: eng

- short_pair: az-en

- chrF2_score: 0.49

- bleu: 31.9

- brevity_penalty: 0.997

- ref_len: 16165.0

- src_name: Azerbaijani

- tgt_name: English

- train_date: 2020-06-16

- src_alpha2: az

- tgt_alpha2: en

- prefer_old: False

- long_pair: aze-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41