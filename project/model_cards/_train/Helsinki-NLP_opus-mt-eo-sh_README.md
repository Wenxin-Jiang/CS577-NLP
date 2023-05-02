---
language: 
- eo
- sh

tags:
- translation

license: apache-2.0
---

### epo-hbs

* source group: Esperanto 
* target group: Serbo-Croatian 
*  OPUS readme: [epo-hbs](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-hbs/README.md)

*  model: transformer-align
* source language(s): epo
* target language(s): bos_Latn hrv srp_Cyrl srp_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-hbs/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-hbs/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-hbs/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.epo.hbs 	| 13.6 	| 0.351 |


### System Info: 
- hf_name: epo-hbs

- source_languages: epo

- target_languages: hbs

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-hbs/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eo', 'sh']

- src_constituents: {'epo'}

- tgt_constituents: {'hrv', 'srp_Cyrl', 'bos_Latn', 'srp_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-hbs/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-hbs/opus-2020-06-16.test.txt

- src_alpha3: epo

- tgt_alpha3: hbs

- short_pair: eo-sh

- chrF2_score: 0.35100000000000003

- bleu: 13.6

- brevity_penalty: 0.888

- ref_len: 17999.0

- src_name: Esperanto

- tgt_name: Serbo-Croatian

- train_date: 2020-06-16

- src_alpha2: eo

- tgt_alpha2: sh

- prefer_old: False

- long_pair: epo-hbs

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41