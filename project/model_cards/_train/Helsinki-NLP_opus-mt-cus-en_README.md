---
language: 
- so
- cus
- en

tags:
- translation

license: apache-2.0
---

### cus-eng

* source group: Cushitic languages 
* target group: English 
*  OPUS readme: [cus-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cus-eng/README.md)

*  model: transformer
* source language(s): som
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cus-eng/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cus-eng/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cus-eng/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.multi.eng 	| 16.2 	| 0.303 |
| Tatoeba-test.som-eng.som.eng 	| 16.2 	| 0.303 |


### System Info: 
- hf_name: cus-eng

- source_languages: cus

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cus-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['so', 'cus', 'en']

- src_constituents: {'som'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cus-eng/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cus-eng/opus-2020-07-26.test.txt

- src_alpha3: cus

- tgt_alpha3: eng

- short_pair: cus-en

- chrF2_score: 0.303

- bleu: 16.2

- brevity_penalty: 1.0

- ref_len: 3.0

- src_name: Cushitic languages

- tgt_name: English

- train_date: 2020-07-26

- src_alpha2: cus

- tgt_alpha2: en

- prefer_old: False

- long_pair: cus-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41