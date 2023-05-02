---
language: 
- da
- no

tags:
- translation

license: apache-2.0
---

### dan-nor

* source group: Danish 
* target group: Norwegian 
*  OPUS readme: [dan-nor](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/dan-nor/README.md)

*  model: transformer-align
* source language(s): dan
* target language(s): nno nob
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/dan-nor/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/dan-nor/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/dan-nor/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.dan.nor 	| 66.4 	| 0.801 |


### System Info: 
- hf_name: dan-nor

- source_languages: dan

- target_languages: nor

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/dan-nor/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['da', 'no']

- src_constituents: {'dan'}

- tgt_constituents: {'nob', 'nno'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/dan-nor/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/dan-nor/opus-2020-06-17.test.txt

- src_alpha3: dan

- tgt_alpha3: nor

- short_pair: da-no

- chrF2_score: 0.8009999999999999

- bleu: 66.4

- brevity_penalty: 0.996

- ref_len: 9691.0

- src_name: Danish

- tgt_name: Norwegian

- train_date: 2020-06-17

- src_alpha2: da

- tgt_alpha2: no

- prefer_old: False

- long_pair: dan-nor

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41