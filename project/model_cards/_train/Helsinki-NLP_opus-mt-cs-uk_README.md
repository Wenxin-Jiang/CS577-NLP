---
language: 
- cs
- uk

tags:
- translation

license: apache-2.0
---

### ces-ukr

* source group: Czech 
* target group: Ukrainian 
*  OPUS readme: [ces-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ces-ukr/README.md)

*  model: transformer-align
* source language(s): ces
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ces-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ces-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ces-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ces.ukr 	| 50.9 	| 0.680 |


### System Info: 
- hf_name: ces-ukr

- source_languages: ces

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ces-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['cs', 'uk']

- src_constituents: {'ces'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ces-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ces-ukr/opus-2020-06-17.test.txt

- src_alpha3: ces

- tgt_alpha3: ukr

- short_pair: cs-uk

- chrF2_score: 0.68

- bleu: 50.9

- brevity_penalty: 0.9940000000000001

- ref_len: 8891.0

- src_name: Czech

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: cs

- tgt_alpha2: uk

- prefer_old: False

- long_pair: ces-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41