---
language: 
- se
- fi
- hu
- et
- urj
- en

tags:
- translation

license: apache-2.0
---

### urj-eng

* source group: Uralic languages 
* target group: English 
*  OPUS readme: [urj-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/urj-eng/README.md)

*  model: transformer
* source language(s): est fin fkv_Latn hun izh kpv krl liv_Latn mdf mhr myv sma sme udm vro
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/urj-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/urj-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/urj-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2015-enfi-fineng.fin.eng 	| 22.7 	| 0.511 |
| newsdev2018-enet-esteng.est.eng 	| 26.6 	| 0.545 |
| newssyscomb2009-huneng.hun.eng 	| 21.3 	| 0.493 |
| newstest2009-huneng.hun.eng 	| 20.1 	| 0.487 |
| newstest2015-enfi-fineng.fin.eng 	| 23.9 	| 0.521 |
| newstest2016-enfi-fineng.fin.eng 	| 25.8 	| 0.542 |
| newstest2017-enfi-fineng.fin.eng 	| 28.9 	| 0.562 |
| newstest2018-enet-esteng.est.eng 	| 27.0 	| 0.552 |
| newstest2018-enfi-fineng.fin.eng 	| 21.2 	| 0.492 |
| newstest2019-fien-fineng.fin.eng 	| 25.3 	| 0.531 |
| newstestB2016-enfi-fineng.fin.eng 	| 21.3 	| 0.500 |
| newstestB2017-enfi-fineng.fin.eng 	| 24.4 	| 0.528 |
| newstestB2017-fien-fineng.fin.eng 	| 24.4 	| 0.528 |
| Tatoeba-test.chm-eng.chm.eng 	| 0.8 	| 0.131 |
| Tatoeba-test.est-eng.est.eng 	| 34.5 	| 0.526 |
| Tatoeba-test.fin-eng.fin.eng 	| 28.1 	| 0.485 |
| Tatoeba-test.fkv-eng.fkv.eng 	| 6.8 	| 0.335 |
| Tatoeba-test.hun-eng.hun.eng 	| 25.1 	| 0.452 |
| Tatoeba-test.izh-eng.izh.eng 	| 11.6 	| 0.224 |
| Tatoeba-test.kom-eng.kom.eng 	| 2.4 	| 0.110 |
| Tatoeba-test.krl-eng.krl.eng 	| 18.6 	| 0.365 |
| Tatoeba-test.liv-eng.liv.eng 	| 0.5 	| 0.078 |
| Tatoeba-test.mdf-eng.mdf.eng 	| 1.5 	| 0.117 |
| Tatoeba-test.multi.eng 	| 47.8 	| 0.646 |
| Tatoeba-test.myv-eng.myv.eng 	| 0.5 	| 0.101 |
| Tatoeba-test.sma-eng.sma.eng 	| 1.2 	| 0.110 |
| Tatoeba-test.sme-eng.sme.eng 	| 1.5 	| 0.147 |
| Tatoeba-test.udm-eng.udm.eng 	| 1.0 	| 0.130 |


### System Info: 
- hf_name: urj-eng

- source_languages: urj

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/urj-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['se', 'fi', 'hu', 'et', 'urj', 'en']

- src_constituents: {'izh', 'mdf', 'vep', 'vro', 'sme', 'myv', 'fkv_Latn', 'krl', 'fin', 'hun', 'kpv', 'udm', 'liv_Latn', 'est', 'mhr', 'sma'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/urj-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/urj-eng/opus2m-2020-08-01.test.txt

- src_alpha3: urj

- tgt_alpha3: eng

- short_pair: urj-en

- chrF2_score: 0.6459999999999999

- bleu: 47.8

- brevity_penalty: 0.993

- ref_len: 70882.0

- src_name: Uralic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: urj

- tgt_alpha2: en

- prefer_old: False

- long_pair: urj-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41