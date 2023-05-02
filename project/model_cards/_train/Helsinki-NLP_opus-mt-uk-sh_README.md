---
language: 
- uk
- sh

tags:
- translation

license: apache-2.0
---

### ukr-hbs

* source group: Ukrainian 
* target group: Serbo-Croatian 
*  OPUS readme: [ukr-hbs](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-hbs/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): hrv srp_Cyrl srp_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-hbs/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-hbs/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-hbs/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.hbs 	| 42.8 	| 0.631 |


### System Info: 
- hf_name: ukr-hbs

- source_languages: ukr

- target_languages: hbs

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-hbs/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'sh']

- src_constituents: {'ukr'}

- tgt_constituents: {'hrv', 'srp_Cyrl', 'bos_Latn', 'srp_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-hbs/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-hbs/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: hbs

- short_pair: uk-sh

- chrF2_score: 0.631

- bleu: 42.8

- brevity_penalty: 0.96

- ref_len: 5128.0

- src_name: Ukrainian

- tgt_name: Serbo-Croatian

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: sh

- prefer_old: False

- long_pair: ukr-hbs

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41