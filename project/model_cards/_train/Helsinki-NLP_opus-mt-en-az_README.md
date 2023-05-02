---
language: 
- en
- az

tags:
- translation

license: apache-2.0
---

### eng-aze

* source group: English 
* target group: Azerbaijani 
*  OPUS readme: [eng-aze](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-aze/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): aze_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aze/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aze/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aze/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.aze 	| 18.6 	| 0.477 |


### System Info: 
- hf_name: eng-aze

- source_languages: eng

- target_languages: aze

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-aze/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'az']

- src_constituents: {'eng'}

- tgt_constituents: {'aze_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aze/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aze/opus-2020-06-16.test.txt

- src_alpha3: eng

- tgt_alpha3: aze

- short_pair: en-az

- chrF2_score: 0.47700000000000004

- bleu: 18.6

- brevity_penalty: 1.0

- ref_len: 13012.0

- src_name: English

- tgt_name: Azerbaijani

- train_date: 2020-06-16

- src_alpha2: en

- tgt_alpha2: az

- prefer_old: False

- long_pair: eng-aze

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41