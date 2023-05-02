---
language: 
- se
- fi
- hu
- et
- fiu

tags:
- translation

license: apache-2.0
---

### fiu-fiu

* source group: Finno-Ugrian languages 
* target group: Finno-Ugrian languages 
*  OPUS readme: [fiu-fiu](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fiu-fiu/README.md)

*  model: transformer
* source language(s): est fin fkv_Latn hun izh krl liv_Latn vep vro
* target language(s): est fin fkv_Latn hun izh krl liv_Latn vep vro
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-fiu/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-fiu/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-fiu/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.est-est.est.est 	| 2.0 	| 0.252 |
| Tatoeba-test.est-fin.est.fin 	| 51.0 	| 0.704 |
| Tatoeba-test.est-fkv.est.fkv 	| 1.1 	| 0.211 |
| Tatoeba-test.est-vep.est.vep 	| 3.1 	| 0.272 |
| Tatoeba-test.fin-est.fin.est 	| 55.2 	| 0.722 |
| Tatoeba-test.fin-fkv.fin.fkv 	| 1.6 	| 0.207 |
| Tatoeba-test.fin-hun.fin.hun 	| 42.4 	| 0.663 |
| Tatoeba-test.fin-izh.fin.izh 	| 12.9 	| 0.509 |
| Tatoeba-test.fin-krl.fin.krl 	| 4.6 	| 0.292 |
| Tatoeba-test.fkv-est.fkv.est 	| 2.4 	| 0.148 |
| Tatoeba-test.fkv-fin.fkv.fin 	| 15.1 	| 0.427 |
| Tatoeba-test.fkv-liv.fkv.liv 	| 1.2 	| 0.261 |
| Tatoeba-test.fkv-vep.fkv.vep 	| 1.2 	| 0.233 |
| Tatoeba-test.hun-fin.hun.fin 	| 47.8 	| 0.681 |
| Tatoeba-test.izh-fin.izh.fin 	| 24.0 	| 0.615 |
| Tatoeba-test.izh-krl.izh.krl 	| 1.8 	| 0.114 |
| Tatoeba-test.krl-fin.krl.fin 	| 13.6 	| 0.407 |
| Tatoeba-test.krl-izh.krl.izh 	| 2.7 	| 0.096 |
| Tatoeba-test.liv-fkv.liv.fkv 	| 1.2 	| 0.164 |
| Tatoeba-test.liv-vep.liv.vep 	| 3.4 	| 0.181 |
| Tatoeba-test.multi.multi 	| 36.7 	| 0.581 |
| Tatoeba-test.vep-est.vep.est 	| 3.4 	| 0.251 |
| Tatoeba-test.vep-fkv.vep.fkv 	| 1.2 	| 0.215 |
| Tatoeba-test.vep-liv.vep.liv 	| 3.4 	| 0.179 |


### System Info: 
- hf_name: fiu-fiu

- source_languages: fiu

- target_languages: fiu

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fiu-fiu/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['se', 'fi', 'hu', 'et', 'fiu']

- src_constituents: {'izh', 'mdf', 'vep', 'vro', 'sme', 'myv', 'fkv_Latn', 'krl', 'fin', 'hun', 'kpv', 'udm', 'liv_Latn', 'est', 'mhr', 'sma'}

- tgt_constituents: {'izh', 'mdf', 'vep', 'vro', 'sme', 'myv', 'fkv_Latn', 'krl', 'fin', 'hun', 'kpv', 'udm', 'liv_Latn', 'est', 'mhr', 'sma'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-fiu/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/fiu-fiu/opus-2020-07-26.test.txt

- src_alpha3: fiu

- tgt_alpha3: fiu

- short_pair: fiu-fiu

- chrF2_score: 0.581

- bleu: 36.7

- brevity_penalty: 0.981

- ref_len: 19444.0

- src_name: Finno-Ugrian languages

- tgt_name: Finno-Ugrian languages

- train_date: 2020-07-26

- src_alpha2: fiu

- tgt_alpha2: fiu

- prefer_old: False

- long_pair: fiu-fiu

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41