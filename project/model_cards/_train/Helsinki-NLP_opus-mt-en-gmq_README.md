---
language: 
- en
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

### eng-gmq

* source group: English 
* target group: North Germanic languages 
*  OPUS readme: [eng-gmq](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-gmq/README.md)

*  model: transformer
* source language(s): eng
* target language(s): dan fao isl nno nob nob_Hebr non_Latn swe
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmq/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmq/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmq/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-dan.eng.dan 	| 57.7 	| 0.724 |
| Tatoeba-test.eng-fao.eng.fao 	| 9.2 	| 0.322 |
| Tatoeba-test.eng-isl.eng.isl 	| 23.8 	| 0.506 |
| Tatoeba-test.eng.multi 	| 52.8 	| 0.688 |
| Tatoeba-test.eng-non.eng.non 	| 0.7 	| 0.196 |
| Tatoeba-test.eng-nor.eng.nor 	| 50.3 	| 0.678 |
| Tatoeba-test.eng-swe.eng.swe 	| 57.8 	| 0.717 |


### System Info: 
- hf_name: eng-gmq

- source_languages: eng

- target_languages: gmq

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-gmq/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'da', 'nb', 'sv', 'is', 'nn', 'fo', 'gmq']

- src_constituents: {'eng'}

- tgt_constituents: {'dan', 'nob', 'nob_Hebr', 'swe', 'isl', 'nno', 'non_Latn', 'fao'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmq/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmq/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: gmq

- short_pair: en-gmq

- chrF2_score: 0.688

- bleu: 52.8

- brevity_penalty: 0.973

- ref_len: 71881.0

- src_name: English

- tgt_name: North Germanic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: gmq

- prefer_old: False

- long_pair: eng-gmq

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41