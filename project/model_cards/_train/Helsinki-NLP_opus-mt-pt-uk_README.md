---
language: 
- pt
- uk

tags:
- translation

license: apache-2.0
---

### por-ukr

* source group: Portuguese 
* target group: Ukrainian 
*  OPUS readme: [por-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/por-ukr/README.md)

*  model: transformer-align
* source language(s): por
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/por-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/por-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/por-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.por.ukr 	| 39.8 	| 0.616 |


### System Info: 
- hf_name: por-ukr

- source_languages: por

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/por-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['pt', 'uk']

- src_constituents: {'por'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/por-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/por-ukr/opus-2020-06-17.test.txt

- src_alpha3: por

- tgt_alpha3: ukr

- short_pair: pt-uk

- chrF2_score: 0.616

- bleu: 39.8

- brevity_penalty: 0.9990000000000001

- ref_len: 18933.0

- src_name: Portuguese

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: pt

- tgt_alpha2: uk

- prefer_old: False

- long_pair: por-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41