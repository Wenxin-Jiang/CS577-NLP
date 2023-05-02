---
language: 
- en
- lt
- lv
- bat

tags:
- translation

license: apache-2.0
---

### eng-bat

* source group: English 
* target group: Baltic languages 
*  OPUS readme: [eng-bat](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-bat/README.md)

*  model: transformer
* source language(s): eng
* target language(s): lav lit ltg prg_Latn sgs
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bat/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bat/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bat/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2017-enlv-englav.eng.lav 	| 24.0 	| 0.546 |
| newsdev2019-enlt-englit.eng.lit 	| 20.9 	| 0.533 |
| newstest2017-enlv-englav.eng.lav 	| 18.3 	| 0.506 |
| newstest2019-enlt-englit.eng.lit 	| 13.6 	| 0.466 |
| Tatoeba-test.eng-lav.eng.lav 	| 42.8 	| 0.652 |
| Tatoeba-test.eng-lit.eng.lit 	| 37.1 	| 0.650 |
| Tatoeba-test.eng.multi 	| 37.0 	| 0.616 |
| Tatoeba-test.eng-prg.eng.prg 	| 0.5 	| 0.130 |
| Tatoeba-test.eng-sgs.eng.sgs 	| 4.1 	| 0.178 |


### System Info: 
- hf_name: eng-bat

- source_languages: eng

- target_languages: bat

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-bat/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'lt', 'lv', 'bat']

- src_constituents: {'eng'}

- tgt_constituents: {'lit', 'lav', 'prg_Latn', 'ltg', 'sgs'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bat/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bat/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: bat

- short_pair: en-bat

- chrF2_score: 0.616

- bleu: 37.0

- brevity_penalty: 0.956

- ref_len: 26417.0

- src_name: English

- tgt_name: Baltic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: bat

- prefer_old: False

- long_pair: eng-bat

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41