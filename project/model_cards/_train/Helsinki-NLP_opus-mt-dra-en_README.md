---
language: 
- ta
- kn
- ml
- te
- dra
- en

tags:
- translation

license: apache-2.0
---

### dra-eng

* source group: Dravidian languages 
* target group: English 
*  OPUS readme: [dra-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/dra-eng/README.md)

*  model: transformer
* source language(s): kan mal tam tel
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/dra-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/dra-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/dra-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.kan-eng.kan.eng 	| 9.1 	| 0.312 |
| Tatoeba-test.mal-eng.mal.eng 	| 42.0 	| 0.584 |
| Tatoeba-test.multi.eng 	| 30.0 	| 0.493 |
| Tatoeba-test.tam-eng.tam.eng 	| 30.2 	| 0.467 |
| Tatoeba-test.tel-eng.tel.eng 	| 15.9 	| 0.378 |


### System Info: 
- hf_name: dra-eng

- source_languages: dra

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/dra-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ta', 'kn', 'ml', 'te', 'dra', 'en']

- src_constituents: {'tam', 'kan', 'mal', 'tel'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/dra-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/dra-eng/opus2m-2020-07-31.test.txt

- src_alpha3: dra

- tgt_alpha3: eng

- short_pair: dra-en

- chrF2_score: 0.493

- bleu: 30.0

- brevity_penalty: 1.0

- ref_len: 10641.0

- src_name: Dravidian languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: dra

- tgt_alpha2: en

- prefer_old: False

- long_pair: dra-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41