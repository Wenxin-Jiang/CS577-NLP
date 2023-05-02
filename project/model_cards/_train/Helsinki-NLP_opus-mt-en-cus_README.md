---
language: 
- en
- so
- cus

tags:
- translation

license: apache-2.0
---

### eng-cus

* source group: English 
* target group: Cushitic languages 
*  OPUS readme: [eng-cus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-cus/README.md)

*  model: transformer
* source language(s): eng
* target language(s): som
* model: transformer
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cus/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cus/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cus/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.multi 	| 16.0 	| 0.173 |
| Tatoeba-test.eng-som.eng.som 	| 16.0 	| 0.173 |


### System Info: 
- hf_name: eng-cus

- source_languages: eng

- target_languages: cus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-cus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'so', 'cus']

- src_constituents: {'eng'}

- tgt_constituents: {'som'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cus/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cus/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: cus

- short_pair: en-cus

- chrF2_score: 0.17300000000000001

- bleu: 16.0

- brevity_penalty: 1.0

- ref_len: 3.0

- src_name: English

- tgt_name: Cushitic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: cus

- prefer_old: False

- long_pair: eng-cus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41