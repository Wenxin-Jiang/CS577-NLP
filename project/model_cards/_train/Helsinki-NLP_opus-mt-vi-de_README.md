---
language: 
- vi
- de

tags:
- translation

license: apache-2.0
---

### vie-deu

* source group: Vietnamese 
* target group: German 
*  OPUS readme: [vie-deu](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/vie-deu/README.md)

*  model: transformer-align
* source language(s): vie
* target language(s): deu
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/vie-deu/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/vie-deu/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/vie-deu/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.vie.deu 	| 27.6 	| 0.484 |


### System Info: 
- hf_name: vie-deu

- source_languages: vie

- target_languages: deu

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/vie-deu/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['vi', 'de']

- src_constituents: {'vie', 'vie_Hani'}

- tgt_constituents: {'deu'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/vie-deu/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/vie-deu/opus-2020-06-17.test.txt

- src_alpha3: vie

- tgt_alpha3: deu

- short_pair: vi-de

- chrF2_score: 0.484

- bleu: 27.6

- brevity_penalty: 0.958

- ref_len: 3365.0

- src_name: Vietnamese

- tgt_name: German

- train_date: 2020-06-17

- src_alpha2: vi

- tgt_alpha2: de

- prefer_old: False

- long_pair: vie-deu

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41