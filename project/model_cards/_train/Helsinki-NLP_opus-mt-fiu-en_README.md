---
language: 
- se
- fi
- hu
- et
- fiu
- en

tags:
- translation

license: apache-2.0
---

### fiu-eng

* source group: Finno-Ugrian languages 
* target group: English 
*  OPUS readme: [fiu-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fiu-eng/README.md)

*  model: transformer
* source language(s): est fin fkv_Latn hun izh kpv krl liv_Latn mdf mhr myv sma sme udm vro
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2015-enfi-fineng.fin.eng 	| 22.9 	| 0.513 |
| newsdev2018-enet-esteng.est.eng 	| 26.3 	| 0.543 |
| newssyscomb2009-huneng.hun.eng 	| 21.2 	| 0.494 |
| newstest2009-huneng.hun.eng 	| 19.8 	| 0.486 |
| newstest2015-enfi-fineng.fin.eng 	| 24.1 	| 0.521 |
| newstest2016-enfi-fineng.fin.eng 	| 25.6 	| 0.541 |
| newstest2017-enfi-fineng.fin.eng 	| 28.7 	| 0.560 |
| newstest2018-enet-esteng.est.eng 	| 26.5 	| 0.549 |
| newstest2018-enfi-fineng.fin.eng 	| 21.2 	| 0.490 |
| newstest2019-fien-fineng.fin.eng 	| 25.6 	| 0.533 |
| newstestB2016-enfi-fineng.fin.eng 	| 21.6 	| 0.500 |
| newstestB2017-enfi-fineng.fin.eng 	| 24.3 	| 0.526 |
| newstestB2017-fien-fineng.fin.eng 	| 24.3 	| 0.526 |
| Tatoeba-test.chm-eng.chm.eng 	| 1.2 	| 0.163 |
| Tatoeba-test.est-eng.est.eng 	| 55.3 	| 0.706 |
| Tatoeba-test.fin-eng.fin.eng 	| 48.7 	| 0.660 |
| Tatoeba-test.fkv-eng.fkv.eng 	| 11.5 	| 0.384 |
| Tatoeba-test.hun-eng.hun.eng 	| 46.7 	| 0.638 |
| Tatoeba-test.izh-eng.izh.eng 	| 48.3 	| 0.678 |
| Tatoeba-test.kom-eng.kom.eng 	| 0.7 	| 0.113 |
| Tatoeba-test.krl-eng.krl.eng 	| 36.1 	| 0.485 |
| Tatoeba-test.liv-eng.liv.eng 	| 2.1 	| 0.086 |
| Tatoeba-test.mdf-eng.mdf.eng 	| 0.9 	| 0.120 |
| Tatoeba-test.multi.eng 	| 47.8 	| 0.648 |
| Tatoeba-test.myv-eng.myv.eng 	| 0.7 	| 0.121 |
| Tatoeba-test.sma-eng.sma.eng 	| 1.7 	| 0.101 |
| Tatoeba-test.sme-eng.sme.eng 	| 7.8 	| 0.229 |
| Tatoeba-test.udm-eng.udm.eng 	| 0.9 	| 0.166 |


### System Info: 
- hf_name: fiu-eng

- source_languages: fiu

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fiu-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['se', 'fi', 'hu', 'et', 'fiu', 'en']

- src_constituents: {'izh', 'mdf', 'vep', 'vro', 'sme', 'myv', 'fkv_Latn', 'krl', 'fin', 'hun', 'kpv', 'udm', 'liv_Latn', 'est', 'mhr', 'sma'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-eng/opus2m-2020-07-31.test.txt

- src_alpha3: fiu

- tgt_alpha3: eng

- short_pair: fiu-en

- chrF2_score: 0.648

- bleu: 47.8

- brevity_penalty: 0.988

- ref_len: 71020.0

- src_name: Finno-Ugrian languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: fiu

- tgt_alpha2: en

- prefer_old: False

- long_pair: fiu-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41