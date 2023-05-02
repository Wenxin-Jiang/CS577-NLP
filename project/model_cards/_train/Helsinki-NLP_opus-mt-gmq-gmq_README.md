---
language: 
- da
- nb
- sv
- is
- nn
- fo
- gmq

tags:
- translation

license: apache-2.0
---

### gmq-gmq

* source group: North Germanic languages 
* target group: North Germanic languages 
*  OPUS readme: [gmq-gmq](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-gmq/README.md)

*  model: transformer
* source language(s): dan fao isl nno nob swe
* target language(s): dan fao isl nno nob swe
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-gmq/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-gmq/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-gmq/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.dan-fao.dan.fao 	| 8.1 	| 0.173 |
| Tatoeba-test.dan-isl.dan.isl 	| 52.5 	| 0.827 |
| Tatoeba-test.dan-nor.dan.nor 	| 62.8 	| 0.772 |
| Tatoeba-test.dan-swe.dan.swe 	| 67.6 	| 0.802 |
| Tatoeba-test.fao-dan.fao.dan 	| 11.3 	| 0.306 |
| Tatoeba-test.fao-isl.fao.isl 	| 26.3 	| 0.359 |
| Tatoeba-test.fao-nor.fao.nor 	| 36.8 	| 0.531 |
| Tatoeba-test.fao-swe.fao.swe 	| 0.0 	| 0.632 |
| Tatoeba-test.isl-dan.isl.dan 	| 67.0 	| 0.739 |
| Tatoeba-test.isl-fao.isl.fao 	| 14.5 	| 0.243 |
| Tatoeba-test.isl-nor.isl.nor 	| 51.8 	| 0.674 |
| Tatoeba-test.isl-swe.isl.swe 	| 100.0 	| 1.000 |
| Tatoeba-test.multi.multi 	| 64.7 	| 0.782 |
| Tatoeba-test.nor-dan.nor.dan 	| 65.6 	| 0.797 |
| Tatoeba-test.nor-fao.nor.fao 	| 9.4 	| 0.362 |
| Tatoeba-test.nor-isl.nor.isl 	| 38.8 	| 0.587 |
| Tatoeba-test.nor-nor.nor.nor 	| 51.9 	| 0.721 |
| Tatoeba-test.nor-swe.nor.swe 	| 66.5 	| 0.789 |
| Tatoeba-test.swe-dan.swe.dan 	| 67.6 	| 0.802 |
| Tatoeba-test.swe-fao.swe.fao 	| 0.0 	| 0.268 |
| Tatoeba-test.swe-isl.swe.isl 	| 65.8 	| 0.914 |
| Tatoeba-test.swe-nor.swe.nor 	| 60.6 	| 0.755 |


### System Info: 
- hf_name: gmq-gmq

- source_languages: gmq

- target_languages: gmq

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-gmq/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['da', 'nb', 'sv', 'is', 'nn', 'fo', 'gmq']

- src_constituents: {'dan', 'nob', 'nob_Hebr', 'swe', 'isl', 'nno', 'non_Latn', 'fao'}

- tgt_constituents: {'dan', 'nob', 'nob_Hebr', 'swe', 'isl', 'nno', 'non_Latn', 'fao'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-gmq/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-gmq/opus-2020-07-27.test.txt

- src_alpha3: gmq

- tgt_alpha3: gmq

- short_pair: gmq-gmq

- chrF2_score: 0.782

- bleu: 64.7

- brevity_penalty: 0.9940000000000001

- ref_len: 49385.0

- src_name: North Germanic languages

- tgt_name: North Germanic languages

- train_date: 2020-07-27

- src_alpha2: gmq

- tgt_alpha2: gmq

- prefer_old: False

- long_pair: gmq-gmq

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41