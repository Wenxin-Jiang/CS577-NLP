---
language: 
- de
- no

tags:
- translation

license: apache-2.0
---

### deu-nor

* source group: German 
* target group: Norwegian 
*  OPUS readme: [deu-nor](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-nor/README.md)

*  model: transformer-align
* source language(s): deu
* target language(s): nno nob
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-nor/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-nor/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-nor/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.deu.nor 	| 33.2 	| 0.554 |


### System Info: 
- hf_name: deu-nor

- source_languages: deu

- target_languages: nor

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-nor/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['de', 'no']

- src_constituents: {'deu'}

- tgt_constituents: {'nob', 'nno'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-nor/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-nor/opus-2020-06-17.test.txt

- src_alpha3: deu

- tgt_alpha3: nor

- short_pair: de-no

- chrF2_score: 0.5539999999999999

- bleu: 33.2

- brevity_penalty: 0.956

- ref_len: 32928.0

- src_name: German

- tgt_name: Norwegian

- train_date: 2020-06-17

- src_alpha2: de

- tgt_alpha2: no

- prefer_old: False

- long_pair: deu-nor

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41