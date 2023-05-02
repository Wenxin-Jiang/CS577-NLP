---
language: 
- da
- ru

tags:
- translation

license: apache-2.0
---

### dan-rus

* source group: Danish 
* target group: Russian 
*  OPUS readme: [dan-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/dan-rus/README.md)

*  model: transformer-align
* source language(s): dan
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/dan-rus/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/dan-rus/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/dan-rus/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.dan.rus 	| 52.5 	| 0.715 |


### System Info: 
- hf_name: dan-rus

- source_languages: dan

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/dan-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['da', 'ru']

- src_constituents: {'dan'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/dan-rus/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/dan-rus/opus-2020-06-17.test.txt

- src_alpha3: dan

- tgt_alpha3: rus

- short_pair: da-ru

- chrF2_score: 0.715

- bleu: 52.5

- brevity_penalty: 0.991

- ref_len: 10480.0

- src_name: Danish

- tgt_name: Russian

- train_date: 2020-06-17

- src_alpha2: da

- tgt_alpha2: ru

- prefer_old: False

- long_pair: dan-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41