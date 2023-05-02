---
language: 
- az
- tr

tags:
- translation

license: apache-2.0
---

### aze-tur

* source group: Azerbaijani 
* target group: Turkish 
*  OPUS readme: [aze-tur](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/aze-tur/README.md)

*  model: transformer-align
* source language(s): aze_Latn
* target language(s): tur
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/aze-tur/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/aze-tur/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/aze-tur/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.aze.tur 	| 24.4 	| 0.529 |


### System Info: 
- hf_name: aze-tur

- source_languages: aze

- target_languages: tur

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/aze-tur/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['az', 'tr']

- src_constituents: {'aze_Latn'}

- tgt_constituents: {'tur'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/aze-tur/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/aze-tur/opus-2020-06-16.test.txt

- src_alpha3: aze

- tgt_alpha3: tur

- short_pair: az-tr

- chrF2_score: 0.529

- bleu: 24.4

- brevity_penalty: 0.956

- ref_len: 5380.0

- src_name: Azerbaijani

- tgt_name: Turkish

- train_date: 2020-06-16

- src_alpha2: az

- tgt_alpha2: tr

- prefer_old: False

- long_pair: aze-tur

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41