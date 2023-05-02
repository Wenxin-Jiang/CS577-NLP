---
language: 
- nl
- en
- lb
- af
- de
- fy
- yi
- gmw

tags:
- translation

license: apache-2.0
---

### gmw-eng

* source group: West Germanic languages 
* target group: English 
*  OPUS readme: [gmw-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmw-eng/README.md)

*  model: transformer
* source language(s): afr ang_Latn deu enm_Latn frr fry gos gsw ksh ltz nds nld pdc sco stq swg yid
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-deueng.deu.eng 	| 27.2 	| 0.538 |
| news-test2008-deueng.deu.eng 	| 25.7 	| 0.534 |
| newstest2009-deueng.deu.eng 	| 25.1 	| 0.530 |
| newstest2010-deueng.deu.eng 	| 27.9 	| 0.565 |
| newstest2011-deueng.deu.eng 	| 25.3 	| 0.539 |
| newstest2012-deueng.deu.eng 	| 26.6 	| 0.548 |
| newstest2013-deueng.deu.eng 	| 29.6 	| 0.565 |
| newstest2014-deen-deueng.deu.eng 	| 30.2 	| 0.571 |
| newstest2015-ende-deueng.deu.eng 	| 31.5 	| 0.577 |
| newstest2016-ende-deueng.deu.eng 	| 36.7 	| 0.622 |
| newstest2017-ende-deueng.deu.eng 	| 32.3 	| 0.585 |
| newstest2018-ende-deueng.deu.eng 	| 39.9 	| 0.638 |
| newstest2019-deen-deueng.deu.eng 	| 35.9 	| 0.611 |
| Tatoeba-test.afr-eng.afr.eng 	| 61.8 	| 0.750 |
| Tatoeba-test.ang-eng.ang.eng 	| 7.3 	| 0.220 |
| Tatoeba-test.deu-eng.deu.eng 	| 48.3 	| 0.657 |
| Tatoeba-test.enm-eng.enm.eng 	| 16.1 	| 0.423 |
| Tatoeba-test.frr-eng.frr.eng 	| 7.0 	| 0.168 |
| Tatoeba-test.fry-eng.fry.eng 	| 28.6 	| 0.488 |
| Tatoeba-test.gos-eng.gos.eng 	| 15.5 	| 0.326 |
| Tatoeba-test.gsw-eng.gsw.eng 	| 12.7 	| 0.308 |
| Tatoeba-test.ksh-eng.ksh.eng 	| 8.4 	| 0.254 |
| Tatoeba-test.ltz-eng.ltz.eng 	| 28.7 	| 0.453 |
| Tatoeba-test.multi.eng 	| 48.5 	| 0.646 |
| Tatoeba-test.nds-eng.nds.eng 	| 31.4 	| 0.509 |
| Tatoeba-test.nld-eng.nld.eng 	| 58.1 	| 0.728 |
| Tatoeba-test.pdc-eng.pdc.eng 	| 25.1 	| 0.406 |
| Tatoeba-test.sco-eng.sco.eng 	| 40.8 	| 0.570 |
| Tatoeba-test.stq-eng.stq.eng 	| 20.3 	| 0.380 |
| Tatoeba-test.swg-eng.swg.eng 	| 20.5 	| 0.315 |
| Tatoeba-test.yid-eng.yid.eng 	| 16.0 	| 0.366 |


### System Info: 
- hf_name: gmw-eng

- source_languages: gmw

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmw-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['nl', 'en', 'lb', 'af', 'de', 'fy', 'yi', 'gmw']

- src_constituents: {'ksh', 'nld', 'eng', 'enm_Latn', 'ltz', 'stq', 'afr', 'pdc', 'deu', 'gos', 'ang_Latn', 'fry', 'gsw', 'frr', 'nds', 'yid', 'swg', 'sco'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-eng/opus2m-2020-08-01.test.txt

- src_alpha3: gmw

- tgt_alpha3: eng

- short_pair: gmw-en

- chrF2_score: 0.6459999999999999

- bleu: 48.5

- brevity_penalty: 0.997

- ref_len: 72584.0

- src_name: West Germanic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: gmw

- tgt_alpha2: en

- prefer_old: False

- long_pair: gmw-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41