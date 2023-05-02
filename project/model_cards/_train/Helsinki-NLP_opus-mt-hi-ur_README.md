---
language: 
- hi
- ur

tags:
- translation

license: apache-2.0
---

### hin-urd

* source group: Hindi 
* target group: Urdu 
*  OPUS readme: [hin-urd](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/hin-urd/README.md)

*  model: transformer-align
* source language(s): hin
* target language(s): urd
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/hin-urd/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hin-urd/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hin-urd/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.hin.urd 	| 12.4 	| 0.393 |


### System Info: 
- hf_name: hin-urd

- source_languages: hin

- target_languages: urd

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/hin-urd/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['hi', 'ur']

- src_constituents: {'hin'}

- tgt_constituents: {'urd'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/hin-urd/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/hin-urd/opus-2020-06-16.test.txt

- src_alpha3: hin

- tgt_alpha3: urd

- short_pair: hi-ur

- chrF2_score: 0.39299999999999996

- bleu: 12.4

- brevity_penalty: 1.0

- ref_len: 1618.0

- src_name: Hindi

- tgt_name: Urdu

- train_date: 2020-06-16

- src_alpha2: hi

- tgt_alpha2: ur

- prefer_old: False

- long_pair: hin-urd

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41