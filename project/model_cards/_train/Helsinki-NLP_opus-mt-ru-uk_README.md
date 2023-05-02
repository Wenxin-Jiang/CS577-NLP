---
language: 
- ru
- uk

tags:
- translation

license: apache-2.0
---

### rus-ukr

* source group: Russian 
* target group: Ukrainian 
*  OPUS readme: [rus-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-ukr/README.md)

*  model: transformer-align
* source language(s): rus
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.ukr 	| 64.0 	| 0.793 |


### System Info: 
- hf_name: rus-ukr

- source_languages: rus

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'uk']

- src_constituents: {'rus'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-ukr/opus-2020-06-17.test.txt

- src_alpha3: rus

- tgt_alpha3: ukr

- short_pair: ru-uk

- chrF2_score: 0.7929999999999999

- bleu: 64.0

- brevity_penalty: 0.99

- ref_len: 60212.0

- src_name: Russian

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: ru

- tgt_alpha2: uk

- prefer_old: False

- long_pair: rus-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41