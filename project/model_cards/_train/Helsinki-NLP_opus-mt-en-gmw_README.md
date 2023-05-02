---
language: 
- en
- nl
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

### eng-gmw

* source group: English 
* target group: West Germanic languages 
*  OPUS readme: [eng-gmw](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-gmw/README.md)

*  model: transformer
* source language(s): eng
* target language(s): afr ang_Latn deu enm_Latn frr fry gos gsw ksh ltz nds nld pdc sco stq swg yid
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmw/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmw/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmw/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-engdeu.eng.deu 	| 21.4 	| 0.518 |
| news-test2008-engdeu.eng.deu 	| 21.0 	| 0.510 |
| newstest2009-engdeu.eng.deu 	| 20.4 	| 0.513 |
| newstest2010-engdeu.eng.deu 	| 22.9 	| 0.528 |
| newstest2011-engdeu.eng.deu 	| 20.5 	| 0.508 |
| newstest2012-engdeu.eng.deu 	| 21.0 	| 0.507 |
| newstest2013-engdeu.eng.deu 	| 24.7 	| 0.533 |
| newstest2015-ende-engdeu.eng.deu 	| 28.2 	| 0.568 |
| newstest2016-ende-engdeu.eng.deu 	| 33.3 	| 0.605 |
| newstest2017-ende-engdeu.eng.deu 	| 26.5 	| 0.559 |
| newstest2018-ende-engdeu.eng.deu 	| 39.9 	| 0.649 |
| newstest2019-ende-engdeu.eng.deu 	| 35.9 	| 0.616 |
| Tatoeba-test.eng-afr.eng.afr 	| 55.7 	| 0.740 |
| Tatoeba-test.eng-ang.eng.ang 	| 6.5 	| 0.164 |
| Tatoeba-test.eng-deu.eng.deu 	| 40.4 	| 0.614 |
| Tatoeba-test.eng-enm.eng.enm 	| 2.3 	| 0.254 |
| Tatoeba-test.eng-frr.eng.frr 	| 8.4 	| 0.248 |
| Tatoeba-test.eng-fry.eng.fry 	| 17.9 	| 0.424 |
| Tatoeba-test.eng-gos.eng.gos 	| 2.2 	| 0.309 |
| Tatoeba-test.eng-gsw.eng.gsw 	| 1.6 	| 0.186 |
| Tatoeba-test.eng-ksh.eng.ksh 	| 1.5 	| 0.189 |
| Tatoeba-test.eng-ltz.eng.ltz 	| 20.2 	| 0.383 |
| Tatoeba-test.eng.multi 	| 41.6 	| 0.609 |
| Tatoeba-test.eng-nds.eng.nds 	| 18.9 	| 0.437 |
| Tatoeba-test.eng-nld.eng.nld 	| 53.1 	| 0.699 |
| Tatoeba-test.eng-pdc.eng.pdc 	| 7.7 	| 0.262 |
| Tatoeba-test.eng-sco.eng.sco 	| 37.7 	| 0.557 |
| Tatoeba-test.eng-stq.eng.stq 	| 5.9 	| 0.380 |
| Tatoeba-test.eng-swg.eng.swg 	| 6.2 	| 0.236 |
| Tatoeba-test.eng-yid.eng.yid 	| 6.8 	| 0.296 |


### System Info: 
- hf_name: eng-gmw

- source_languages: eng

- target_languages: gmw

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-gmw/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'nl', 'lb', 'af', 'de', 'fy', 'yi', 'gmw']

- src_constituents: {'eng'}

- tgt_constituents: {'ksh', 'nld', 'eng', 'enm_Latn', 'ltz', 'stq', 'afr', 'pdc', 'deu', 'gos', 'ang_Latn', 'fry', 'gsw', 'frr', 'nds', 'yid', 'swg', 'sco'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmw/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gmw/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: gmw

- short_pair: en-gmw

- chrF2_score: 0.609

- bleu: 41.6

- brevity_penalty: 0.9890000000000001

- ref_len: 74922.0

- src_name: English

- tgt_name: West Germanic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: gmw

- prefer_old: False

- long_pair: eng-gmw

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41