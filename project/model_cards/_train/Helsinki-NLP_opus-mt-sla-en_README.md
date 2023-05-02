---
language: 
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
- en

tags:
- translation

license: apache-2.0
---

### sla-eng

* source group: Slavic languages 
* target group: English 
*  OPUS readme: [sla-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sla-eng/README.md)

*  model: transformer
* source language(s): bel bel_Latn bos_Latn bul bul_Latn ces csb_Latn dsb hrv hsb mkd orv_Cyrl pol rue rus slv srp_Cyrl srp_Latn ukr
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/sla-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sla-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sla-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-ceseng.ces.eng 	| 26.7 	| 0.542 |
| newstest2009-ceseng.ces.eng 	| 25.2 	| 0.534 |
| newstest2010-ceseng.ces.eng 	| 25.9 	| 0.545 |
| newstest2011-ceseng.ces.eng 	| 26.8 	| 0.544 |
| newstest2012-ceseng.ces.eng 	| 25.6 	| 0.536 |
| newstest2012-ruseng.rus.eng 	| 32.5 	| 0.588 |
| newstest2013-ceseng.ces.eng 	| 28.8 	| 0.556 |
| newstest2013-ruseng.rus.eng 	| 26.4 	| 0.532 |
| newstest2014-csen-ceseng.ces.eng 	| 31.4 	| 0.591 |
| newstest2014-ruen-ruseng.rus.eng 	| 29.6 	| 0.576 |
| newstest2015-encs-ceseng.ces.eng 	| 28.2 	| 0.545 |
| newstest2015-enru-ruseng.rus.eng 	| 28.1 	| 0.551 |
| newstest2016-encs-ceseng.ces.eng 	| 30.0 	| 0.567 |
| newstest2016-enru-ruseng.rus.eng 	| 27.4 	| 0.548 |
| newstest2017-encs-ceseng.ces.eng 	| 26.5 	| 0.537 |
| newstest2017-enru-ruseng.rus.eng 	| 31.0 	| 0.574 |
| newstest2018-encs-ceseng.ces.eng 	| 27.9 	| 0.548 |
| newstest2018-enru-ruseng.rus.eng 	| 26.8 	| 0.545 |
| newstest2019-ruen-ruseng.rus.eng 	| 29.1 	| 0.562 |
| Tatoeba-test.bel-eng.bel.eng 	| 42.5 	| 0.609 |
| Tatoeba-test.bul-eng.bul.eng 	| 55.4 	| 0.697 |
| Tatoeba-test.ces-eng.ces.eng 	| 53.1 	| 0.688 |
| Tatoeba-test.csb-eng.csb.eng 	| 23.1 	| 0.446 |
| Tatoeba-test.dsb-eng.dsb.eng 	| 31.1 	| 0.467 |
| Tatoeba-test.hbs-eng.hbs.eng 	| 56.1 	| 0.702 |
| Tatoeba-test.hsb-eng.hsb.eng 	| 46.2 	| 0.597 |
| Tatoeba-test.mkd-eng.mkd.eng 	| 54.5 	| 0.680 |
| Tatoeba-test.multi.eng 	| 53.2 	| 0.683 |
| Tatoeba-test.orv-eng.orv.eng 	| 12.1 	| 0.292 |
| Tatoeba-test.pol-eng.pol.eng 	| 51.1 	| 0.671 |
| Tatoeba-test.rue-eng.rue.eng 	| 19.6 	| 0.389 |
| Tatoeba-test.rus-eng.rus.eng 	| 54.1 	| 0.686 |
| Tatoeba-test.slv-eng.slv.eng 	| 43.4 	| 0.610 |
| Tatoeba-test.ukr-eng.ukr.eng 	| 53.8 	| 0.685 |


### System Info: 
- hf_name: sla-eng

- source_languages: sla

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sla-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['be', 'hr', 'mk', 'cs', 'ru', 'pl', 'bg', 'uk', 'sl', 'sla', 'en']

- src_constituents: {'bel', 'hrv', 'orv_Cyrl', 'mkd', 'bel_Latn', 'srp_Latn', 'bul_Latn', 'ces', 'bos_Latn', 'csb_Latn', 'dsb', 'hsb', 'rus', 'srp_Cyrl', 'pol', 'rue', 'bul', 'ukr', 'slv'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/sla-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/sla-eng/opus2m-2020-08-01.test.txt

- src_alpha3: sla

- tgt_alpha3: eng

- short_pair: sla-en

- chrF2_score: 0.6829999999999999

- bleu: 53.2

- brevity_penalty: 0.9740000000000001

- ref_len: 70897.0

- src_name: Slavic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: sla

- tgt_alpha2: en

- prefer_old: False

- long_pair: sla-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41