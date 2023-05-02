---
language: 
- uk
- no

tags:
- translation

license: apache-2.0
---

### ukr-nor

* source group: Ukrainian 
* target group: Norwegian 
*  OPUS readme: [ukr-nor](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-nor/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): nob
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nor/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nor/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nor/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.nor 	| 21.3 	| 0.397 |


### System Info: 
- hf_name: ukr-nor

- source_languages: ukr

- target_languages: nor

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-nor/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'no']

- src_constituents: {'ukr'}

- tgt_constituents: {'nob', 'nno'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nor/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nor/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: nor

- short_pair: uk-no

- chrF2_score: 0.397

- bleu: 21.3

- brevity_penalty: 0.966

- ref_len: 4378.0

- src_name: Ukrainian

- tgt_name: Norwegian

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: no

- prefer_old: False

- long_pair: ukr-nor

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41