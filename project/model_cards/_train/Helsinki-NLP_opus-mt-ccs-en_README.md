---
language: 
- ka
- ccs
- en

tags:
- translation

license: apache-2.0
---

### ccs-eng

* source group: South Caucasian languages 
* target group: English 
*  OPUS readme: [ccs-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ccs-eng/README.md)

*  model: transformer
* source language(s): kat
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ccs-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ccs-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ccs-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.kat-eng.kat.eng 	| 18.0 	| 0.357 |
| Tatoeba-test.multi.eng 	| 18.0 	| 0.357 |


### System Info: 
- hf_name: ccs-eng

- source_languages: ccs

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ccs-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ka', 'ccs', 'en']

- src_constituents: {'kat'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ccs-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ccs-eng/opus2m-2020-07-31.test.txt

- src_alpha3: ccs

- tgt_alpha3: eng

- short_pair: ccs-en

- chrF2_score: 0.35700000000000004

- bleu: 18.0

- brevity_penalty: 1.0

- ref_len: 5992.0

- src_name: South Caucasian languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: ccs

- tgt_alpha2: en

- prefer_old: False

- long_pair: ccs-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41