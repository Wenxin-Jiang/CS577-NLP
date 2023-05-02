---
language: 
- ru
- af

tags:
- translation

license: apache-2.0
---

### rus-afr

* source group: Russian 
* target group: Afrikaans 
*  OPUS readme: [rus-afr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-afr/README.md)

*  model: transformer-align
* source language(s): rus
* target language(s): afr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-afr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-afr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-afr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.afr 	| 48.1 	| 0.669 |


### System Info: 
- hf_name: rus-afr

- source_languages: rus

- target_languages: afr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-afr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'af']

- src_constituents: {'rus'}

- tgt_constituents: {'afr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-afr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-afr/opus-2020-06-17.test.txt

- src_alpha3: rus

- tgt_alpha3: afr

- short_pair: ru-af

- chrF2_score: 0.669

- bleu: 48.1

- brevity_penalty: 1.0

- ref_len: 1390.0

- src_name: Russian

- tgt_name: Afrikaans

- train_date: 2020-06-17

- src_alpha2: ru

- tgt_alpha2: af

- prefer_old: False

- long_pair: rus-afr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41