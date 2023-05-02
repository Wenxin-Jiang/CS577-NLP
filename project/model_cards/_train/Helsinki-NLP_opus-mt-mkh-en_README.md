---
language: 
- vi
- km
- mkh
- en

tags:
- translation

license: apache-2.0
---

### mkh-eng

* source group: Mon-Khmer languages 
* target group: English 
*  OPUS readme: [mkh-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/mkh-eng/README.md)

*  model: transformer
* source language(s): kha khm khm_Latn mnw vie vie_Hani
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/mkh-eng/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/mkh-eng/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/mkh-eng/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.kha-eng.kha.eng 	| 0.5 	| 0.108 |
| Tatoeba-test.khm-eng.khm.eng 	| 8.5 	| 0.206 |
| Tatoeba-test.mnw-eng.mnw.eng 	| 0.7 	| 0.110 |
| Tatoeba-test.multi.eng 	| 24.5 	| 0.407 |
| Tatoeba-test.vie-eng.vie.eng 	| 34.4 	| 0.529 |


### System Info: 
- hf_name: mkh-eng

- source_languages: mkh

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/mkh-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['vi', 'km', 'mkh', 'en']

- src_constituents: {'vie_Hani', 'mnw', 'vie', 'kha', 'khm_Latn', 'khm'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/mkh-eng/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/mkh-eng/opus-2020-07-27.test.txt

- src_alpha3: mkh

- tgt_alpha3: eng

- short_pair: mkh-en

- chrF2_score: 0.40700000000000003

- bleu: 24.5

- brevity_penalty: 1.0

- ref_len: 33985.0

- src_name: Mon-Khmer languages

- tgt_name: English

- train_date: 2020-07-27

- src_alpha2: mkh

- tgt_alpha2: en

- prefer_old: False

- long_pair: mkh-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41