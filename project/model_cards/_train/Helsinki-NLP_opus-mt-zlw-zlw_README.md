---
language: 
- pl
- cs
- zlw

tags:
- translation

license: apache-2.0
---

### zlw-zlw

* source group: West Slavic languages 
* target group: West Slavic languages 
*  OPUS readme: [zlw-zlw](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zlw-zlw/README.md)

*  model: transformer
* source language(s): ces dsb hsb pol
* target language(s): ces dsb hsb pol
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-zlw/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-zlw/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-zlw/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ces-hsb.ces.hsb 	| 2.6 	| 0.167 |
| Tatoeba-test.ces-pol.ces.pol 	| 44.0 	| 0.649 |
| Tatoeba-test.dsb-pol.dsb.pol 	| 8.5 	| 0.250 |
| Tatoeba-test.hsb-ces.hsb.ces 	| 9.6 	| 0.276 |
| Tatoeba-test.multi.multi 	| 38.8 	| 0.580 |
| Tatoeba-test.pol-ces.pol.ces 	| 43.4 	| 0.620 |
| Tatoeba-test.pol-dsb.pol.dsb 	| 2.1 	| 0.159 |


### System Info: 
- hf_name: zlw-zlw

- source_languages: zlw

- target_languages: zlw

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zlw-zlw/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['pl', 'cs', 'zlw']

- src_constituents: {'csb_Latn', 'dsb', 'hsb', 'pol', 'ces'}

- tgt_constituents: {'csb_Latn', 'dsb', 'hsb', 'pol', 'ces'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-zlw/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zlw-zlw/opus-2020-07-27.test.txt

- src_alpha3: zlw

- tgt_alpha3: zlw

- short_pair: zlw-zlw

- chrF2_score: 0.58

- bleu: 38.8

- brevity_penalty: 0.99

- ref_len: 7792.0

- src_name: West Slavic languages

- tgt_name: West Slavic languages

- train_date: 2020-07-27

- src_alpha2: zlw

- tgt_alpha2: zlw

- prefer_old: False

- long_pair: zlw-zlw

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41