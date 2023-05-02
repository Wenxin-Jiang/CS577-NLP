---
language: 
- tr
- uk

tags:
- translation

license: apache-2.0
---

### tur-ukr

* source group: Turkish 
* target group: Ukrainian 
*  OPUS readme: [tur-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tur-ukr/README.md)

*  model: transformer-align
* source language(s): tur
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.tur.ukr 	| 42.5 	| 0.624 |


### System Info: 
- hf_name: tur-ukr

- source_languages: tur

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tur-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['tr', 'uk']

- src_constituents: {'tur'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ukr/opus-2020-06-17.test.txt

- src_alpha3: tur

- tgt_alpha3: ukr

- short_pair: tr-uk

- chrF2_score: 0.624

- bleu: 42.5

- brevity_penalty: 0.983

- ref_len: 12988.0

- src_name: Turkish

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: tr

- tgt_alpha2: uk

- prefer_old: False

- long_pair: tur-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41