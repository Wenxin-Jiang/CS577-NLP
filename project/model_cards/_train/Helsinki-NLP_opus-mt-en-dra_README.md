---
language: 
- en
- ta
- kn
- ml
- te
- dra

tags:
- translation

license: apache-2.0
---

### eng-dra

* source group: English 
* target group: Dravidian languages 
*  OPUS readme: [eng-dra](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-dra/README.md)

*  model: transformer
* source language(s): eng
* target language(s): kan mal tam tel
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-dra/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-dra/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-dra/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-kan.eng.kan 	| 4.7 	| 0.348 |
| Tatoeba-test.eng-mal.eng.mal 	| 13.1 	| 0.515 |
| Tatoeba-test.eng.multi 	| 10.7 	| 0.463 |
| Tatoeba-test.eng-tam.eng.tam 	| 9.0 	| 0.444 |
| Tatoeba-test.eng-tel.eng.tel 	| 7.1 	| 0.363 |


### System Info: 
- hf_name: eng-dra

- source_languages: eng

- target_languages: dra

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-dra/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'ta', 'kn', 'ml', 'te', 'dra']

- src_constituents: {'eng'}

- tgt_constituents: {'tam', 'kan', 'mal', 'tel'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-dra/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-dra/opus-2020-07-26.test.txt

- src_alpha3: eng

- tgt_alpha3: dra

- short_pair: en-dra

- chrF2_score: 0.46299999999999997

- bleu: 10.7

- brevity_penalty: 1.0

- ref_len: 7928.0

- src_name: English

- tgt_name: Dravidian languages

- train_date: 2020-07-26

- src_alpha2: en

- tgt_alpha2: dra

- prefer_old: False

- long_pair: eng-dra

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41