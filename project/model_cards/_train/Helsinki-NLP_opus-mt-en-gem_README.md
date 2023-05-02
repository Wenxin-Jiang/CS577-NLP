---
language: 
- en
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
- lb
- yi
- gem

tags:
- translation

license: apache-2.0
---

### eng-gem

* source group: English 
* target group: Germanic languages 
*  OPUS readme: [eng-gem](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-gem/README.md)

*  model: transformer
* source language(s): eng
* target language(s): afr ang_Latn dan deu enm_Latn fao frr fry gos got_Goth gsw isl ksh ltz nds nld nno nob nob_Hebr non_Latn pdc sco stq swe swg yid
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gem/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gem/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gem/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-engdeu.eng.deu 	| 20.9 	| 0.521 |
| news-test2008-engdeu.eng.deu 	| 21.1 	| 0.511 |
| newstest2009-engdeu.eng.deu 	| 20.5 	| 0.516 |
| newstest2010-engdeu.eng.deu 	| 22.5 	| 0.526 |
| newstest2011-engdeu.eng.deu 	| 20.5 	| 0.508 |
| newstest2012-engdeu.eng.deu 	| 20.8 	| 0.507 |
| newstest2013-engdeu.eng.deu 	| 24.6 	| 0.534 |
| newstest2015-ende-engdeu.eng.deu 	| 27.9 	| 0.569 |
| newstest2016-ende-engdeu.eng.deu 	| 33.2 	| 0.607 |
| newstest2017-ende-engdeu.eng.deu 	| 26.5 	| 0.560 |
| newstest2018-ende-engdeu.eng.deu 	| 39.4 	| 0.648 |
| newstest2019-ende-engdeu.eng.deu 	| 35.0 	| 0.613 |
| Tatoeba-test.eng-afr.eng.afr 	| 56.5 	| 0.745 |
| Tatoeba-test.eng-ang.eng.ang 	| 6.7 	| 0.154 |
| Tatoeba-test.eng-dan.eng.dan 	| 58.0 	| 0.726 |
| Tatoeba-test.eng-deu.eng.deu 	| 40.3 	| 0.615 |
| Tatoeba-test.eng-enm.eng.enm 	| 1.4 	| 0.215 |
| Tatoeba-test.eng-fao.eng.fao 	| 7.2 	| 0.304 |
| Tatoeba-test.eng-frr.eng.frr 	| 5.5 	| 0.159 |
| Tatoeba-test.eng-fry.eng.fry 	| 19.4 	| 0.433 |
| Tatoeba-test.eng-gos.eng.gos 	| 1.0 	| 0.182 |
| Tatoeba-test.eng-got.eng.got 	| 0.3 	| 0.012 |
| Tatoeba-test.eng-gsw.eng.gsw 	| 0.9 	| 0.130 |
| Tatoeba-test.eng-isl.eng.isl 	| 23.4 	| 0.505 |
| Tatoeba-test.eng-ksh.eng.ksh 	| 1.1 	| 0.141 |
| Tatoeba-test.eng-ltz.eng.ltz 	| 20.3 	| 0.379 |
| Tatoeba-test.eng.multi 	| 46.5 	| 0.641 |
| Tatoeba-test.eng-nds.eng.nds 	| 20.6 	| 0.458 |
| Tatoeba-test.eng-nld.eng.nld 	| 53.4 	| 0.702 |
| Tatoeba-test.eng-non.eng.non 	| 0.6 	| 0.166 |
| Tatoeba-test.eng-nor.eng.nor 	| 50.3 	| 0.679 |
| Tatoeba-test.eng-pdc.eng.pdc 	| 3.9 	| 0.189 |
| Tatoeba-test.eng-sco.eng.sco 	| 33.0 	| 0.542 |
| Tatoeba-test.eng-stq.eng.stq 	| 2.3 	| 0.274 |
| Tatoeba-test.eng-swe.eng.swe 	| 57.9 	| 0.719 |
| Tatoeba-test.eng-swg.eng.swg 	| 1.2 	| 0.171 |
| Tatoeba-test.eng-yid.eng.yid 	| 7.2 	| 0.304 |


### System Info: 
- hf_name: eng-gem

- source_languages: eng

- target_languages: gem

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-gem/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'da', 'sv', 'af', 'nn', 'fy', 'fo', 'de', 'nb', 'nl', 'is', 'lb', 'yi', 'gem']

- src_constituents: {'eng'}

- tgt_constituents: {'ksh', 'enm_Latn', 'got_Goth', 'stq', 'dan', 'swe', 'afr', 'pdc', 'gos', 'nno', 'fry', 'gsw', 'fao', 'deu', 'swg', 'sco', 'nob', 'nld', 'isl', 'eng', 'ltz', 'nob_Hebr', 'ang_Latn', 'frr', 'non_Latn', 'yid', 'nds'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gem/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gem/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: gem

- short_pair: en-gem

- chrF2_score: 0.6409999999999999

- bleu: 46.5

- brevity_penalty: 0.9790000000000001

- ref_len: 73328.0

- src_name: English

- tgt_name: Germanic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: gem

- prefer_old: False

- long_pair: eng-gem

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41