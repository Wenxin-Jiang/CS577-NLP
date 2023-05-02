---
language: 
- en
- se
- fi
- hu
- et
- urj

tags:
- translation

license: apache-2.0
---

### eng-urj

* source group: English 
* target group: Uralic languages 
*  OPUS readme: [eng-urj](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-urj/README.md)

*  model: transformer
* source language(s): eng
* target language(s): est fin fkv_Latn hun izh kpv krl liv_Latn mdf mhr myv sma sme udm vro
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-02.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urj/opus2m-2020-08-02.zip)
* test set translations: [opus2m-2020-08-02.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urj/opus2m-2020-08-02.test.txt)
* test set scores: [opus2m-2020-08-02.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urj/opus2m-2020-08-02.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2015-enfi-engfin.eng.fin 	| 18.3 	| 0.519 |
| newsdev2018-enet-engest.eng.est 	| 19.3 	| 0.520 |
| newssyscomb2009-enghun.eng.hun 	| 15.4 	| 0.471 |
| newstest2009-enghun.eng.hun 	| 15.7 	| 0.468 |
| newstest2015-enfi-engfin.eng.fin 	| 20.2 	| 0.534 |
| newstest2016-enfi-engfin.eng.fin 	| 20.7 	| 0.541 |
| newstest2017-enfi-engfin.eng.fin 	| 23.6 	| 0.566 |
| newstest2018-enet-engest.eng.est 	| 20.8 	| 0.535 |
| newstest2018-enfi-engfin.eng.fin 	| 15.8 	| 0.499 |
| newstest2019-enfi-engfin.eng.fin 	| 19.9 	| 0.518 |
| newstestB2016-enfi-engfin.eng.fin 	| 16.6 	| 0.509 |
| newstestB2017-enfi-engfin.eng.fin 	| 19.4 	| 0.529 |
| Tatoeba-test.eng-chm.eng.chm 	| 1.3 	| 0.127 |
| Tatoeba-test.eng-est.eng.est 	| 51.0 	| 0.692 |
| Tatoeba-test.eng-fin.eng.fin 	| 34.6 	| 0.597 |
| Tatoeba-test.eng-fkv.eng.fkv 	| 2.2 	| 0.302 |
| Tatoeba-test.eng-hun.eng.hun 	| 35.6 	| 0.591 |
| Tatoeba-test.eng-izh.eng.izh 	| 5.7 	| 0.211 |
| Tatoeba-test.eng-kom.eng.kom 	| 3.0 	| 0.012 |
| Tatoeba-test.eng-krl.eng.krl 	| 8.5 	| 0.230 |
| Tatoeba-test.eng-liv.eng.liv 	| 2.7 	| 0.077 |
| Tatoeba-test.eng-mdf.eng.mdf 	| 2.8 	| 0.007 |
| Tatoeba-test.eng.multi 	| 35.1 	| 0.588 |
| Tatoeba-test.eng-myv.eng.myv 	| 1.3 	| 0.014 |
| Tatoeba-test.eng-sma.eng.sma 	| 1.8 	| 0.095 |
| Tatoeba-test.eng-sme.eng.sme 	| 6.8 	| 0.204 |
| Tatoeba-test.eng-udm.eng.udm 	| 1.1 	| 0.121 |


### System Info: 
- hf_name: eng-urj

- source_languages: eng

- target_languages: urj

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-urj/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'se', 'fi', 'hu', 'et', 'urj']

- src_constituents: {'eng'}

- tgt_constituents: {'izh', 'mdf', 'vep', 'vro', 'sme', 'myv', 'fkv_Latn', 'krl', 'fin', 'hun', 'kpv', 'udm', 'liv_Latn', 'est', 'mhr', 'sma'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urj/opus2m-2020-08-02.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-urj/opus2m-2020-08-02.test.txt

- src_alpha3: eng

- tgt_alpha3: urj

- short_pair: en-urj

- chrF2_score: 0.588

- bleu: 35.1

- brevity_penalty: 0.943

- ref_len: 59664.0

- src_name: English

- tgt_name: Uralic languages

- train_date: 2020-08-02

- src_alpha2: en

- tgt_alpha2: urj

- prefer_old: False

- long_pair: eng-urj

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41