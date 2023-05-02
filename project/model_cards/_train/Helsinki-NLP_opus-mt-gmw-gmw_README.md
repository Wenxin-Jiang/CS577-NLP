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

### gmw-gmw

* source group: West Germanic languages 
* target group: West Germanic languages 
*  OPUS readme: [gmw-gmw](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmw-gmw/README.md)

*  model: transformer
* source language(s): afr ang_Latn deu eng enm_Latn frr fry gos gsw ksh ltz nds nld pdc sco stq swg yid
* target language(s): afr ang_Latn deu eng enm_Latn frr fry gos gsw ksh ltz nds nld pdc sco stq swg yid
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-gmw/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-gmw/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-gmw/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-deueng.deu.eng 	| 25.3 	| 0.527 |
| newssyscomb2009-engdeu.eng.deu 	| 19.0 	| 0.502 |
| news-test2008-deueng.deu.eng 	| 23.7 	| 0.515 |
| news-test2008-engdeu.eng.deu 	| 19.2 	| 0.491 |
| newstest2009-deueng.deu.eng 	| 23.1 	| 0.514 |
| newstest2009-engdeu.eng.deu 	| 18.6 	| 0.495 |
| newstest2010-deueng.deu.eng 	| 25.8 	| 0.545 |
| newstest2010-engdeu.eng.deu 	| 20.3 	| 0.505 |
| newstest2011-deueng.deu.eng 	| 23.7 	| 0.523 |
| newstest2011-engdeu.eng.deu 	| 18.9 	| 0.490 |
| newstest2012-deueng.deu.eng 	| 24.4 	| 0.529 |
| newstest2012-engdeu.eng.deu 	| 19.2 	| 0.489 |
| newstest2013-deueng.deu.eng 	| 27.2 	| 0.545 |
| newstest2013-engdeu.eng.deu 	| 22.4 	| 0.514 |
| newstest2014-deen-deueng.deu.eng 	| 27.0 	| 0.546 |
| newstest2015-ende-deueng.deu.eng 	| 28.4 	| 0.552 |
| newstest2015-ende-engdeu.eng.deu 	| 25.3 	| 0.541 |
| newstest2016-ende-deueng.deu.eng 	| 33.2 	| 0.595 |
| newstest2016-ende-engdeu.eng.deu 	| 29.8 	| 0.578 |
| newstest2017-ende-deueng.deu.eng 	| 29.0 	| 0.557 |
| newstest2017-ende-engdeu.eng.deu 	| 23.9 	| 0.534 |
| newstest2018-ende-deueng.deu.eng 	| 35.9 	| 0.607 |
| newstest2018-ende-engdeu.eng.deu 	| 34.8 	| 0.609 |
| newstest2019-deen-deueng.deu.eng 	| 32.1 	| 0.579 |
| newstest2019-ende-engdeu.eng.deu 	| 31.0 	| 0.579 |
| Tatoeba-test.afr-ang.afr.ang 	| 0.0 	| 0.065 |
| Tatoeba-test.afr-deu.afr.deu 	| 46.8 	| 0.668 |
| Tatoeba-test.afr-eng.afr.eng 	| 58.5 	| 0.728 |
| Tatoeba-test.afr-enm.afr.enm 	| 13.4 	| 0.357 |
| Tatoeba-test.afr-fry.afr.fry 	| 5.3 	| 0.026 |
| Tatoeba-test.afr-gos.afr.gos 	| 3.5 	| 0.228 |
| Tatoeba-test.afr-ltz.afr.ltz 	| 1.6 	| 0.131 |
| Tatoeba-test.afr-nld.afr.nld 	| 55.4 	| 0.715 |
| Tatoeba-test.afr-yid.afr.yid 	| 3.4 	| 0.008 |
| Tatoeba-test.ang-afr.ang.afr 	| 3.1 	| 0.096 |
| Tatoeba-test.ang-deu.ang.deu 	| 2.6 	| 0.188 |
| Tatoeba-test.ang-eng.ang.eng 	| 5.4 	| 0.211 |
| Tatoeba-test.ang-enm.ang.enm 	| 1.7 	| 0.197 |
| Tatoeba-test.ang-gos.ang.gos 	| 6.6 	| 0.186 |
| Tatoeba-test.ang-ltz.ang.ltz 	| 5.3 	| 0.072 |
| Tatoeba-test.ang-yid.ang.yid 	| 0.9 	| 0.131 |
| Tatoeba-test.deu-afr.deu.afr 	| 52.7 	| 0.699 |
| Tatoeba-test.deu-ang.deu.ang 	| 0.8 	| 0.133 |
| Tatoeba-test.deu-eng.deu.eng 	| 43.5 	| 0.621 |
| Tatoeba-test.deu-enm.deu.enm 	| 6.9 	| 0.245 |
| Tatoeba-test.deu-frr.deu.frr 	| 0.8 	| 0.200 |
| Tatoeba-test.deu-fry.deu.fry 	| 15.1 	| 0.367 |
| Tatoeba-test.deu-gos.deu.gos 	| 2.2 	| 0.279 |
| Tatoeba-test.deu-gsw.deu.gsw 	| 1.0 	| 0.176 |
| Tatoeba-test.deu-ksh.deu.ksh 	| 0.6 	| 0.208 |
| Tatoeba-test.deu-ltz.deu.ltz 	| 12.1 	| 0.274 |
| Tatoeba-test.deu-nds.deu.nds 	| 18.8 	| 0.446 |
| Tatoeba-test.deu-nld.deu.nld 	| 48.6 	| 0.669 |
| Tatoeba-test.deu-pdc.deu.pdc 	| 4.6 	| 0.198 |
| Tatoeba-test.deu-sco.deu.sco 	| 12.0 	| 0.340 |
| Tatoeba-test.deu-stq.deu.stq 	| 3.2 	| 0.240 |
| Tatoeba-test.deu-swg.deu.swg 	| 0.5 	| 0.179 |
| Tatoeba-test.deu-yid.deu.yid 	| 1.7 	| 0.160 |
| Tatoeba-test.eng-afr.eng.afr 	| 55.8 	| 0.730 |
| Tatoeba-test.eng-ang.eng.ang 	| 5.7 	| 0.157 |
| Tatoeba-test.eng-deu.eng.deu 	| 36.7 	| 0.584 |
| Tatoeba-test.eng-enm.eng.enm 	| 2.0 	| 0.272 |
| Tatoeba-test.eng-frr.eng.frr 	| 6.1 	| 0.246 |
| Tatoeba-test.eng-fry.eng.fry 	| 15.3 	| 0.378 |
| Tatoeba-test.eng-gos.eng.gos 	| 1.2 	| 0.242 |
| Tatoeba-test.eng-gsw.eng.gsw 	| 0.9 	| 0.164 |
| Tatoeba-test.eng-ksh.eng.ksh 	| 0.9 	| 0.170 |
| Tatoeba-test.eng-ltz.eng.ltz 	| 13.7 	| 0.263 |
| Tatoeba-test.eng-nds.eng.nds 	| 17.1 	| 0.410 |
| Tatoeba-test.eng-nld.eng.nld 	| 49.6 	| 0.673 |
| Tatoeba-test.eng-pdc.eng.pdc 	| 5.1 	| 0.218 |
| Tatoeba-test.eng-sco.eng.sco 	| 34.8 	| 0.587 |
| Tatoeba-test.eng-stq.eng.stq 	| 2.1 	| 0.322 |
| Tatoeba-test.eng-swg.eng.swg 	| 1.7 	| 0.192 |
| Tatoeba-test.eng-yid.eng.yid 	| 1.7 	| 0.173 |
| Tatoeba-test.enm-afr.enm.afr 	| 13.4 	| 0.397 |
| Tatoeba-test.enm-ang.enm.ang 	| 0.7 	| 0.063 |
| Tatoeba-test.enm-deu.enm.deu 	| 41.5 	| 0.514 |
| Tatoeba-test.enm-eng.enm.eng 	| 21.3 	| 0.483 |
| Tatoeba-test.enm-fry.enm.fry 	| 0.0 	| 0.058 |
| Tatoeba-test.enm-gos.enm.gos 	| 10.7 	| 0.354 |
| Tatoeba-test.enm-ksh.enm.ksh 	| 7.0 	| 0.161 |
| Tatoeba-test.enm-nds.enm.nds 	| 18.6 	| 0.316 |
| Tatoeba-test.enm-nld.enm.nld 	| 38.3 	| 0.524 |
| Tatoeba-test.enm-yid.enm.yid 	| 0.7 	| 0.128 |
| Tatoeba-test.frr-deu.frr.deu 	| 4.1 	| 0.219 |
| Tatoeba-test.frr-eng.frr.eng 	| 14.1 	| 0.186 |
| Tatoeba-test.frr-fry.frr.fry 	| 3.1 	| 0.129 |
| Tatoeba-test.frr-gos.frr.gos 	| 3.6 	| 0.226 |
| Tatoeba-test.frr-nds.frr.nds 	| 12.4 	| 0.145 |
| Tatoeba-test.frr-nld.frr.nld 	| 9.8 	| 0.209 |
| Tatoeba-test.frr-stq.frr.stq 	| 2.8 	| 0.142 |
| Tatoeba-test.fry-afr.fry.afr 	| 0.0 	| 1.000 |
| Tatoeba-test.fry-deu.fry.deu 	| 30.1 	| 0.535 |
| Tatoeba-test.fry-eng.fry.eng 	| 28.0 	| 0.486 |
| Tatoeba-test.fry-enm.fry.enm 	| 16.0 	| 0.262 |
| Tatoeba-test.fry-frr.fry.frr 	| 5.5 	| 0.160 |
| Tatoeba-test.fry-gos.fry.gos 	| 1.6 	| 0.307 |
| Tatoeba-test.fry-ltz.fry.ltz 	| 30.4 	| 0.438 |
| Tatoeba-test.fry-nds.fry.nds 	| 8.1 	| 0.083 |
| Tatoeba-test.fry-nld.fry.nld 	| 41.4 	| 0.616 |
| Tatoeba-test.fry-stq.fry.stq 	| 1.6 	| 0.217 |
| Tatoeba-test.fry-yid.fry.yid 	| 1.6 	| 0.159 |
| Tatoeba-test.gos-afr.gos.afr 	| 6.3 	| 0.318 |
| Tatoeba-test.gos-ang.gos.ang 	| 6.2 	| 0.058 |
| Tatoeba-test.gos-deu.gos.deu 	| 11.7 	| 0.363 |
| Tatoeba-test.gos-eng.gos.eng 	| 14.9 	| 0.322 |
| Tatoeba-test.gos-enm.gos.enm 	| 9.1 	| 0.398 |
| Tatoeba-test.gos-frr.gos.frr 	| 3.3 	| 0.117 |
| Tatoeba-test.gos-fry.gos.fry 	| 13.1 	| 0.387 |
| Tatoeba-test.gos-ltz.gos.ltz 	| 3.1 	| 0.154 |
| Tatoeba-test.gos-nds.gos.nds 	| 2.4 	| 0.206 |
| Tatoeba-test.gos-nld.gos.nld 	| 13.9 	| 0.395 |
| Tatoeba-test.gos-stq.gos.stq 	| 2.1 	| 0.209 |
| Tatoeba-test.gos-yid.gos.yid 	| 1.7 	| 0.147 |
| Tatoeba-test.gsw-deu.gsw.deu 	| 10.5 	| 0.350 |
| Tatoeba-test.gsw-eng.gsw.eng 	| 10.7 	| 0.299 |
| Tatoeba-test.ksh-deu.ksh.deu 	| 12.0 	| 0.373 |
| Tatoeba-test.ksh-eng.ksh.eng 	| 3.2 	| 0.225 |
| Tatoeba-test.ksh-enm.ksh.enm 	| 13.4 	| 0.308 |
| Tatoeba-test.ltz-afr.ltz.afr 	| 37.4 	| 0.525 |
| Tatoeba-test.ltz-ang.ltz.ang 	| 2.8 	| 0.036 |
| Tatoeba-test.ltz-deu.ltz.deu 	| 40.3 	| 0.596 |
| Tatoeba-test.ltz-eng.ltz.eng 	| 31.7 	| 0.490 |
| Tatoeba-test.ltz-fry.ltz.fry 	| 36.3 	| 0.658 |
| Tatoeba-test.ltz-gos.ltz.gos 	| 2.9 	| 0.209 |
| Tatoeba-test.ltz-nld.ltz.nld 	| 38.8 	| 0.530 |
| Tatoeba-test.ltz-stq.ltz.stq 	| 5.8 	| 0.165 |
| Tatoeba-test.ltz-yid.ltz.yid 	| 1.0 	| 0.159 |
| Tatoeba-test.multi.multi 	| 36.4 	| 0.568 |
| Tatoeba-test.nds-deu.nds.deu 	| 35.0 	| 0.573 |
| Tatoeba-test.nds-eng.nds.eng 	| 29.6 	| 0.495 |
| Tatoeba-test.nds-enm.nds.enm 	| 3.7 	| 0.194 |
| Tatoeba-test.nds-frr.nds.frr 	| 6.6 	| 0.133 |
| Tatoeba-test.nds-fry.nds.fry 	| 4.2 	| 0.087 |
| Tatoeba-test.nds-gos.nds.gos 	| 2.0 	| 0.243 |
| Tatoeba-test.nds-nld.nds.nld 	| 41.4 	| 0.618 |
| Tatoeba-test.nds-swg.nds.swg 	| 0.6 	| 0.178 |
| Tatoeba-test.nds-yid.nds.yid 	| 8.3 	| 0.238 |
| Tatoeba-test.nld-afr.nld.afr 	| 59.4 	| 0.759 |
| Tatoeba-test.nld-deu.nld.deu 	| 49.9 	| 0.685 |
| Tatoeba-test.nld-eng.nld.eng 	| 54.1 	| 0.699 |
| Tatoeba-test.nld-enm.nld.enm 	| 5.0 	| 0.250 |
| Tatoeba-test.nld-frr.nld.frr 	| 2.4 	| 0.224 |
| Tatoeba-test.nld-fry.nld.fry 	| 19.4 	| 0.446 |
| Tatoeba-test.nld-gos.nld.gos 	| 2.5 	| 0.273 |
| Tatoeba-test.nld-ltz.nld.ltz 	| 13.8 	| 0.292 |
| Tatoeba-test.nld-nds.nld.nds 	| 21.3 	| 0.457 |
| Tatoeba-test.nld-sco.nld.sco 	| 14.7 	| 0.423 |
| Tatoeba-test.nld-stq.nld.stq 	| 1.9 	| 0.257 |
| Tatoeba-test.nld-swg.nld.swg 	| 4.2 	| 0.162 |
| Tatoeba-test.nld-yid.nld.yid 	| 2.6 	| 0.186 |
| Tatoeba-test.pdc-deu.pdc.deu 	| 39.7 	| 0.529 |
| Tatoeba-test.pdc-eng.pdc.eng 	| 25.0 	| 0.427 |
| Tatoeba-test.sco-deu.sco.deu 	| 28.4 	| 0.428 |
| Tatoeba-test.sco-eng.sco.eng 	| 41.8 	| 0.595 |
| Tatoeba-test.sco-nld.sco.nld 	| 36.4 	| 0.565 |
| Tatoeba-test.stq-deu.stq.deu 	| 7.7 	| 0.328 |
| Tatoeba-test.stq-eng.stq.eng 	| 21.1 	| 0.428 |
| Tatoeba-test.stq-frr.stq.frr 	| 2.0 	| 0.118 |
| Tatoeba-test.stq-fry.stq.fry 	| 6.3 	| 0.255 |
| Tatoeba-test.stq-gos.stq.gos 	| 1.4 	| 0.244 |
| Tatoeba-test.stq-ltz.stq.ltz 	| 4.4 	| 0.204 |
| Tatoeba-test.stq-nld.stq.nld 	| 10.7 	| 0.371 |
| Tatoeba-test.stq-yid.stq.yid 	| 1.4 	| 0.105 |
| Tatoeba-test.swg-deu.swg.deu 	| 9.5 	| 0.343 |
| Tatoeba-test.swg-eng.swg.eng 	| 15.1 	| 0.306 |
| Tatoeba-test.swg-nds.swg.nds 	| 0.7 	| 0.196 |
| Tatoeba-test.swg-nld.swg.nld 	| 11.6 	| 0.308 |
| Tatoeba-test.swg-yid.swg.yid 	| 0.9 	| 0.186 |
| Tatoeba-test.yid-afr.yid.afr 	| 100.0 	| 1.000 |
| Tatoeba-test.yid-ang.yid.ang 	| 0.6 	| 0.079 |
| Tatoeba-test.yid-deu.yid.deu 	| 16.7 	| 0.372 |
| Tatoeba-test.yid-eng.yid.eng 	| 15.8 	| 0.344 |
| Tatoeba-test.yid-enm.yid.enm 	| 1.3 	| 0.166 |
| Tatoeba-test.yid-fry.yid.fry 	| 5.6 	| 0.157 |
| Tatoeba-test.yid-gos.yid.gos 	| 2.2 	| 0.160 |
| Tatoeba-test.yid-ltz.yid.ltz 	| 2.1 	| 0.238 |
| Tatoeba-test.yid-nds.yid.nds 	| 14.4 	| 0.365 |
| Tatoeba-test.yid-nld.yid.nld 	| 20.9 	| 0.397 |
| Tatoeba-test.yid-stq.yid.stq 	| 3.7 	| 0.165 |
| Tatoeba-test.yid-swg.yid.swg 	| 1.8 	| 0.156 |


### System Info: 
- hf_name: gmw-gmw

- source_languages: gmw

- target_languages: gmw

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmw-gmw/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['nl', 'en', 'lb', 'af', 'de', 'fy', 'yi', 'gmw']

- src_constituents: {'ksh', 'nld', 'eng', 'enm_Latn', 'ltz', 'stq', 'afr', 'pdc', 'deu', 'gos', 'ang_Latn', 'fry', 'gsw', 'frr', 'nds', 'yid', 'swg', 'sco'}

- tgt_constituents: {'ksh', 'nld', 'eng', 'enm_Latn', 'ltz', 'stq', 'afr', 'pdc', 'deu', 'gos', 'ang_Latn', 'fry', 'gsw', 'frr', 'nds', 'yid', 'swg', 'sco'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-gmw/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/gmw-gmw/opus-2020-07-27.test.txt

- src_alpha3: gmw

- tgt_alpha3: gmw

- short_pair: gmw-gmw

- chrF2_score: 0.568

- bleu: 36.4

- brevity_penalty: 1.0

- ref_len: 72534.0

- src_name: West Germanic languages

- tgt_name: West Germanic languages

- train_date: 2020-07-27

- src_alpha2: gmw

- tgt_alpha2: gmw

- prefer_old: False

- long_pair: gmw-gmw

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41