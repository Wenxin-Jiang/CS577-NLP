---
language: 
- no
- uk

tags:
- translation

license: apache-2.0
---

### nor-ukr

* source group: Norwegian 
* target group: Ukrainian 
*  OPUS readme: [nor-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-ukr/README.md)

*  model: transformer-align
* source language(s): nob
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.nor.ukr 	| 16.6 	| 0.384 |


### System Info: 
- hf_name: nor-ukr

- source_languages: nor

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['no', 'uk']

- src_constituents: {'nob', 'nno'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-ukr/opus-2020-06-17.test.txt

- src_alpha3: nor

- tgt_alpha3: ukr

- short_pair: no-uk

- chrF2_score: 0.384

- bleu: 16.6

- brevity_penalty: 1.0

- ref_len: 3982.0

- src_name: Norwegian

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: no

- tgt_alpha2: uk

- prefer_old: False

- long_pair: nor-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41