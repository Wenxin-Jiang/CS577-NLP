---
language: 
- en
- se
- fi
- hu
- et
- fiu

tags:
- translation

license: apache-2.0
---

### eng-fiu

* source group: English 
* target group: Finno-Ugrian languages 
*  OPUS readme: [eng-fiu](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-fiu/README.md)

*  model: transformer
* source language(s): eng
* target language(s): est fin fkv_Latn hun izh kpv krl liv_Latn mdf mhr myv sma sme udm vro
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fiu/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fiu/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fiu/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2015-enfi-engfin.eng.fin 	| 18.7 	| 0.522 |
| newsdev2018-enet-engest.eng.est 	| 19.4 	| 0.521 |
| newssyscomb2009-enghun.eng.hun 	| 15.5 	| 0.472 |
| newstest2009-enghun.eng.hun 	| 15.4 	| 0.468 |
| newstest2015-enfi-engfin.eng.fin 	| 19.9 	| 0.532 |
| newstest2016-enfi-engfin.eng.fin 	| 21.1 	| 0.544 |
| newstest2017-enfi-engfin.eng.fin 	| 23.8 	| 0.567 |
| newstest2018-enet-engest.eng.est 	| 20.4 	| 0.532 |
| newstest2018-enfi-engfin.eng.fin 	| 15.6 	| 0.498 |
| newstest2019-enfi-engfin.eng.fin 	| 20.0 	| 0.520 |
| newstestB2016-enfi-engfin.eng.fin 	| 17.0 	| 0.512 |
| newstestB2017-enfi-engfin.eng.fin 	| 19.7 	| 0.531 |
| Tatoeba-test.eng-chm.eng.chm 	| 0.9 	| 0.115 |
| Tatoeba-test.eng-est.eng.est 	| 49.8 	| 0.689 |
| Tatoeba-test.eng-fin.eng.fin 	| 34.7 	| 0.597 |
| Tatoeba-test.eng-fkv.eng.fkv 	| 1.3 	| 0.187 |
| Tatoeba-test.eng-hun.eng.hun 	| 35.2 	| 0.589 |
| Tatoeba-test.eng-izh.eng.izh 	| 6.0 	| 0.163 |
| Tatoeba-test.eng-kom.eng.kom 	| 3.4 	| 0.012 |
| Tatoeba-test.eng-krl.eng.krl 	| 6.4 	| 0.202 |
| Tatoeba-test.eng-liv.eng.liv 	| 1.6 	| 0.102 |
| Tatoeba-test.eng-mdf.eng.mdf 	| 3.7 	| 0.008 |
| Tatoeba-test.eng.multi 	| 35.4 	| 0.590 |
| Tatoeba-test.eng-myv.eng.myv 	| 1.4 	| 0.014 |
| Tatoeba-test.eng-sma.eng.sma 	| 2.6 	| 0.097 |
| Tatoeba-test.eng-sme.eng.sme 	| 7.3 	| 0.221 |
| Tatoeba-test.eng-udm.eng.udm 	| 1.4 	| 0.079 |


### System Info: 
- hf_name: eng-fiu

- source_languages: eng

- target_languages: fiu

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-fiu/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'se', 'fi', 'hu', 'et', 'fiu']

- src_constituents: {'eng'}

- tgt_constituents: {'izh', 'mdf', 'vep', 'vro', 'sme', 'myv', 'fkv_Latn', 'krl', 'fin', 'hun', 'kpv', 'udm', 'liv_Latn', 'est', 'mhr', 'sma'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fiu/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-fiu/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: fiu

- short_pair: en-fiu

- chrF2_score: 0.59

- bleu: 35.4

- brevity_penalty: 0.9440000000000001

- ref_len: 59311.0

- src_name: English

- tgt_name: Finno-Ugrian languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: fiu

- prefer_old: False

- long_pair: eng-fiu

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41