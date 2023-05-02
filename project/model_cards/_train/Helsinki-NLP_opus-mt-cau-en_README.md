---
language: 
- ab
- ka
- ce
- cau
- en

tags:
- translation

license: apache-2.0
---

### cau-eng

* source group: Caucasian languages 
* target group: English 
*  OPUS readme: [cau-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cau-eng/README.md)

*  model: transformer
* source language(s): abk ady che kat
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cau-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cau-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cau-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.abk-eng.abk.eng 	| 0.3 	| 0.134 |
| Tatoeba-test.ady-eng.ady.eng 	| 0.4 	| 0.104 |
| Tatoeba-test.che-eng.che.eng 	| 0.6 	| 0.128 |
| Tatoeba-test.kat-eng.kat.eng 	| 18.6 	| 0.366 |
| Tatoeba-test.multi.eng 	| 16.6 	| 0.351 |


### System Info: 
- hf_name: cau-eng

- source_languages: cau

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cau-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ab', 'ka', 'ce', 'cau', 'en']

- src_constituents: {'abk', 'kat', 'che', 'ady'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cau-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cau-eng/opus2m-2020-07-31.test.txt

- src_alpha3: cau

- tgt_alpha3: eng

- short_pair: cau-en

- chrF2_score: 0.35100000000000003

- bleu: 16.6

- brevity_penalty: 1.0

- ref_len: 6285.0

- src_name: Caucasian languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: cau

- tgt_alpha2: en

- prefer_old: False

- long_pair: cau-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41