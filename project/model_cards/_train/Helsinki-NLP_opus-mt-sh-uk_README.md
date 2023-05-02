---
language: 
- sh
- uk

tags:
- translation

license: apache-2.0
---

### hbs-ukr

* source group: Serbo-Croatian 
* target group: Ukrainian 
*  OPUS readme: [hbs-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/hbs-ukr/README.md)

*  model: transformer-align
* source language(s): hrv srp_Cyrl srp_Latn
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/hbs-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hbs-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hbs-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.hbs.ukr 	| 49.6 	| 0.665 |


### System Info: 
- hf_name: hbs-ukr

- source_languages: hbs

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/hbs-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['sh', 'uk']

- src_constituents: {'hrv', 'srp_Cyrl', 'bos_Latn', 'srp_Latn'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/hbs-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/hbs-ukr/opus-2020-06-17.test.txt

- src_alpha3: hbs

- tgt_alpha3: ukr

- short_pair: sh-uk

- chrF2_score: 0.665

- bleu: 49.6

- brevity_penalty: 0.9840000000000001

- ref_len: 4959.0

- src_name: Serbo-Croatian

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: sh

- tgt_alpha2: uk

- prefer_old: False

- long_pair: hbs-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41