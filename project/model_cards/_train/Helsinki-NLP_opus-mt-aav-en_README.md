---
language: 
- vi
- km
- aav
- en

tags:
- translation

license: apache-2.0
---

### aav-eng

* source group: Austro-Asiatic languages 
* target group: English 
*  OPUS readme: [aav-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/aav-eng/README.md)

*  model: transformer
* source language(s): hoc hoc_Latn kha khm khm_Latn mnw vie vie_Hani
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/aav-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/aav-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/aav-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.hoc-eng.hoc.eng 	| 0.3 	| 0.095 |
| Tatoeba-test.kha-eng.kha.eng 	| 1.0 	| 0.115 |
| Tatoeba-test.khm-eng.khm.eng 	| 8.9 	| 0.271 |
| Tatoeba-test.mnw-eng.mnw.eng 	| 0.8 	| 0.118 |
| Tatoeba-test.multi.eng 	| 24.8 	| 0.391 |
| Tatoeba-test.vie-eng.vie.eng 	| 38.7 	| 0.567 |


### System Info: 
- hf_name: aav-eng

- source_languages: aav

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/aav-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['vi', 'km', 'aav', 'en']

- src_constituents: {'mnw', 'vie', 'kha', 'khm', 'vie_Hani', 'khm_Latn', 'hoc_Latn', 'hoc'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/aav-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/aav-eng/opus2m-2020-07-31.test.txt

- src_alpha3: aav

- tgt_alpha3: eng

- short_pair: aav-en

- chrF2_score: 0.391

- bleu: 24.8

- brevity_penalty: 0.968

- ref_len: 36693.0

- src_name: Austro-Asiatic languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: aav

- tgt_alpha2: en

- prefer_old: False

- long_pair: aav-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41