---
language: 
- uk
- tr

tags:
- translation

license: apache-2.0
---

### ukr-tur

* source group: Ukrainian 
* target group: Turkish 
*  OPUS readme: [ukr-tur](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-tur/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): tur
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-tur/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-tur/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-tur/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.tur 	| 39.3 	| 0.655 |


### System Info: 
- hf_name: ukr-tur

- source_languages: ukr

- target_languages: tur

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-tur/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'tr']

- src_constituents: {'ukr'}

- tgt_constituents: {'tur'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-tur/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-tur/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: tur

- short_pair: uk-tr

- chrF2_score: 0.655

- bleu: 39.3

- brevity_penalty: 0.934

- ref_len: 11844.0

- src_name: Ukrainian

- tgt_name: Turkish

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: tr

- prefer_old: False

- long_pair: ukr-tur

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41