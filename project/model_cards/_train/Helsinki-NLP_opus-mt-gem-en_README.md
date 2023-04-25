---
language: 
- da
- sv
- af
- nn
- fy
- fo
- de
- nb
- nl
- is
- en
- lb
- yi
- gem

tags:
- translation

license: apache-2.0
---

### gem-eng

* source group: Germanic languages 
* target group: English 
*  OPUS readme: [gem-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gem-eng/README.md)

*  model: transformer
* source language(s): afr ang_Latn dan deu enm_Latn fao frr fry gos got_Goth gsw isl ksh ltz nds nld nno nob nob_Hebr non_Latn pdc sco stq swe swg yid
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gem-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gem-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gem-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-deueng.deu.eng 	| 27.2 	| 0.542 |
| news-test2008-deueng.deu.eng 	| 26.3 	| 0.536 |
| newstest2009-deueng.deu.eng 	| 25.1 	| 0.531 |
| newstest2010-deueng.deu.eng 	| 28.3 	| 0.569 |
| newstest2011-deueng.deu.eng 	| 26.0 	| 0.543 |
| newstest2012-deueng.deu.eng 	| 26.8 	| 0.550 |
| newstest2013-deueng.deu.eng 	| 30.2 	| 0.570 |
| newstest2014-deen-deueng.deu.eng 	| 30.7 	| 0.574 |
| newstest2015-ende-deueng.deu.eng 	| 32.1 	| 0.581 |
| newstest2016-ende-deueng.deu.eng 	| 36.9 	| 0.624 |
| newstest2017-ende-deueng.deu.eng 	| 32.8 	| 0.588 |
| newstest2018-ende-deueng.deu.eng 	| 40.2 	| 0.640 |
| newstest2019-deen-deueng.deu.eng 	| 36.8 	| 0.614 |
| Tatoeba-test.afr-eng.afr.eng 	| 62.8 	| 0.758 |
| Tatoeba-test.ang-eng.ang.eng 	| 10.5 	| 0.262 |
| Tatoeba-test.dan-eng.dan.eng 	| 61.6 	| 0.754 |
| Tatoeba-test.deu-eng.deu.eng 	| 49.7 	| 0.665 |
| Tatoeba-test.enm-eng.enm.eng 	| 23.9 	| 0.491 |
| Tatoeba-test.fao-eng.fao.eng 	| 23.4 	| 0.446 |
| Tatoeba-test.frr-eng.frr.eng 	| 10.2 	| 0.184 |
| Tatoeba-test.fry-eng.fry.eng 	| 29.6 	| 0.486 |
| Tatoeba-test.gos-eng.gos.eng 	| 17.8 	| 0.352 |
| Tatoeba-test.got-eng.got.eng 	| 0.1 	| 0.058 |
| Tatoeba-test.gsw-eng.gsw.eng 	| 15.3 	| 0.333 |
| Tatoeba-test.isl-eng.isl.eng 	| 51.0 	| 0.669 |
| Tatoeba-test.ksh-eng.ksh.eng 	| 6.7 	| 0.266 |
| Tatoeba-test.ltz-eng.ltz.eng 	| 33.0 	| 0.505 |
| Tatoeba-test.multi.eng 	| 54.0 	| 0.687 |
| Tatoeba-test.nds-eng.nds.eng 	| 33.6 	| 0.529 |
| Tatoeba-test.nld-eng.nld.eng 	| 58.9 	| 0.733 |
| Tatoeba-test.non-eng.non.eng 	| 37.3 	| 0.546 |
| Tatoeba-test.nor-eng.nor.eng 	| 54.9 	| 0.696 |
| Tatoeba-test.pdc-eng.pdc.eng 	| 29.6 	| 0.446 |
| Tatoeba-test.sco-eng.sco.eng 	| 40.5 	| 0.581 |
| Tatoeba-test.stq-eng.stq.eng 	| 14.5 	| 0.361 |
| Tatoeba-test.swe-eng.swe.eng 	| 62.0 	| 0.745 |
| Tatoeba-test.swg-eng.swg.eng 	| 17.1 	| 0.334 |
| Tatoeba-test.yid-eng.yid.eng 	| 19.4 	| 0.400 |


### System Info: 
- hf_name: gem-eng

- source_languages: gem

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gem-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['da', 'sv', 'af', 'nn', 'fy', 'fo', 'de', 'nb', 'nl', 'is', 'en', 'lb', 'yi', 'gem']

- src_constituents: {'ksh', 'enm_Latn', 'got_Goth', 'stq', 'dan', 'swe', 'afr', 'pdc', 'gos', 'nno', 'fry', 'gsw', 'fao', 'deu', 'swg', 'sco', 'nob', 'nld', 'isl', 'eng', 'ltz', 'nob_Hebr', 'ang_Latn', 'frr', 'non_Latn', 'yid', 'nds'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/gem-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/gem-eng/opus2m-2020-08-01.test.txt

- src_alpha3: gem

- tgt_alpha3: eng

- short_pair: gem-en

- chrF2_score: 0.687

- bleu: 54.0

- brevity_penalty: 0.993

- ref_len: 72120.0

- src_name: Germanic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: gem

- tgt_alpha2: en

- prefer_old: False

- long_pair: gem-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41