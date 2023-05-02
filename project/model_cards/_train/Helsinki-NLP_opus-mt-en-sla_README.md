---
language: 
- en
- be
- hr
- mk
- cs
- ru
- pl
- bg
- uk
- sl
- sla

tags:
- translation

license: apache-2.0
---

### eng-sla

* source group: English 
* target group: Slavic languages 
*  OPUS readme: [eng-sla](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-sla/README.md)

*  model: transformer
* source language(s): eng
* target language(s): bel bel_Latn bos_Latn bul bul_Latn ces csb_Latn dsb hrv hsb mkd orv_Cyrl pol rue rus slv srp_Cyrl srp_Latn ukr
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sla/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sla/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sla/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-engces.eng.ces 	| 20.1 	| 0.484 |
| news-test2008-engces.eng.ces 	| 17.7 	| 0.461 |
| newstest2009-engces.eng.ces 	| 19.1 	| 0.479 |
| newstest2010-engces.eng.ces 	| 19.3 	| 0.483 |
| newstest2011-engces.eng.ces 	| 20.4 	| 0.486 |
| newstest2012-engces.eng.ces 	| 18.3 	| 0.461 |
| newstest2012-engrus.eng.rus 	| 27.4 	| 0.551 |
| newstest2013-engces.eng.ces 	| 21.5 	| 0.489 |
| newstest2013-engrus.eng.rus 	| 20.9 	| 0.490 |
| newstest2015-encs-engces.eng.ces 	| 21.1 	| 0.496 |
| newstest2015-enru-engrus.eng.rus 	| 24.5 	| 0.536 |
| newstest2016-encs-engces.eng.ces 	| 23.6 	| 0.515 |
| newstest2016-enru-engrus.eng.rus 	| 23.0 	| 0.519 |
| newstest2017-encs-engces.eng.ces 	| 19.2 	| 0.474 |
| newstest2017-enru-engrus.eng.rus 	| 25.0 	| 0.541 |
| newstest2018-encs-engces.eng.ces 	| 19.3 	| 0.479 |
| newstest2018-enru-engrus.eng.rus 	| 22.3 	| 0.526 |
| newstest2019-encs-engces.eng.ces 	| 20.4 	| 0.486 |
| newstest2019-enru-engrus.eng.rus 	| 24.0 	| 0.506 |
| Tatoeba-test.eng-bel.eng.bel 	| 22.9 	| 0.489 |
| Tatoeba-test.eng-bul.eng.bul 	| 46.7 	| 0.652 |
| Tatoeba-test.eng-ces.eng.ces 	| 42.7 	| 0.624 |
| Tatoeba-test.eng-csb.eng.csb 	| 1.4 	| 0.210 |
| Tatoeba-test.eng-dsb.eng.dsb 	| 1.4 	| 0.165 |
| Tatoeba-test.eng-hbs.eng.hbs 	| 40.3 	| 0.616 |
| Tatoeba-test.eng-hsb.eng.hsb 	| 14.3 	| 0.344 |
| Tatoeba-test.eng-mkd.eng.mkd 	| 44.1 	| 0.635 |
| Tatoeba-test.eng.multi 	| 41.0 	| 0.610 |
| Tatoeba-test.eng-orv.eng.orv 	| 0.3 	| 0.014 |
| Tatoeba-test.eng-pol.eng.pol 	| 42.0 	| 0.637 |
| Tatoeba-test.eng-rue.eng.rue 	| 0.3 	| 0.012 |
| Tatoeba-test.eng-rus.eng.rus 	| 40.5 	| 0.612 |
| Tatoeba-test.eng-slv.eng.slv 	| 18.8 	| 0.357 |
| Tatoeba-test.eng-ukr.eng.ukr 	| 38.8 	| 0.600 |


### System Info: 
- hf_name: eng-sla

- source_languages: eng

- target_languages: sla

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-sla/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'be', 'hr', 'mk', 'cs', 'ru', 'pl', 'bg', 'uk', 'sl', 'sla']

- src_constituents: {'eng'}

- tgt_constituents: {'bel', 'hrv', 'orv_Cyrl', 'mkd', 'bel_Latn', 'srp_Latn', 'bul_Latn', 'ces', 'bos_Latn', 'csb_Latn', 'dsb', 'hsb', 'rus', 'srp_Cyrl', 'pol', 'rue', 'bul', 'ukr', 'slv'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sla/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sla/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: sla

- short_pair: en-sla

- chrF2_score: 0.61

- bleu: 41.0

- brevity_penalty: 0.976

- ref_len: 64809.0

- src_name: English

- tgt_name: Slavic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: sla

- prefer_old: False

- long_pair: eng-sla

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41