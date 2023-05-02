---
language: 
- se
- fi
- hu
- et
- urj

tags:
- translation

license: apache-2.0
---

### urj-urj

* source group: Uralic languages 
* target group: Uralic languages 
*  OPUS readme: [urj-urj](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/urj-urj/README.md)

*  model: transformer
* source language(s): est fin fkv_Latn hun izh krl liv_Latn vep vro
* target language(s): est fin fkv_Latn hun izh krl liv_Latn vep vro
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/urj-urj/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/urj-urj/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/urj-urj/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.est-est.est.est 	| 5.1 	| 0.288 |
| Tatoeba-test.est-fin.est.fin 	| 50.9 	| 0.709 |
| Tatoeba-test.est-fkv.est.fkv 	| 0.7 	| 0.215 |
| Tatoeba-test.est-vep.est.vep 	| 1.0 	| 0.154 |
| Tatoeba-test.fin-est.fin.est 	| 55.5 	| 0.718 |
| Tatoeba-test.fin-fkv.fin.fkv 	| 1.8 	| 0.254 |
| Tatoeba-test.fin-hun.fin.hun 	| 45.0 	| 0.672 |
| Tatoeba-test.fin-izh.fin.izh 	| 7.1 	| 0.492 |
| Tatoeba-test.fin-krl.fin.krl 	| 2.6 	| 0.278 |
| Tatoeba-test.fkv-est.fkv.est 	| 0.6 	| 0.099 |
| Tatoeba-test.fkv-fin.fkv.fin 	| 15.5 	| 0.444 |
| Tatoeba-test.fkv-liv.fkv.liv 	| 0.6 	| 0.101 |
| Tatoeba-test.fkv-vep.fkv.vep 	| 0.6 	| 0.113 |
| Tatoeba-test.hun-fin.hun.fin 	| 46.3 	| 0.675 |
| Tatoeba-test.izh-fin.izh.fin 	| 13.4 	| 0.431 |
| Tatoeba-test.izh-krl.izh.krl 	| 2.9 	| 0.078 |
| Tatoeba-test.krl-fin.krl.fin 	| 14.1 	| 0.439 |
| Tatoeba-test.krl-izh.krl.izh 	| 1.0 	| 0.125 |
| Tatoeba-test.liv-fkv.liv.fkv 	| 0.9 	| 0.170 |
| Tatoeba-test.liv-vep.liv.vep 	| 2.6 	| 0.176 |
| Tatoeba-test.multi.multi 	| 32.9 	| 0.580 |
| Tatoeba-test.vep-est.vep.est 	| 3.4 	| 0.265 |
| Tatoeba-test.vep-fkv.vep.fkv 	| 0.9 	| 0.239 |
| Tatoeba-test.vep-liv.vep.liv 	| 2.6 	| 0.190 |


### System Info: 
- hf_name: urj-urj

- source_languages: urj

- target_languages: urj

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/urj-urj/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['se', 'fi', 'hu', 'et', 'urj']

- src_constituents: {'izh', 'mdf', 'vep', 'vro', 'sme', 'myv', 'fkv_Latn', 'krl', 'fin', 'hun', 'kpv', 'udm', 'liv_Latn', 'est', 'mhr', 'sma'}

- tgt_constituents: {'izh', 'mdf', 'vep', 'vro', 'sme', 'myv', 'fkv_Latn', 'krl', 'fin', 'hun', 'kpv', 'udm', 'liv_Latn', 'est', 'mhr', 'sma'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/urj-urj/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/urj-urj/opus-2020-07-27.test.txt

- src_alpha3: urj

- tgt_alpha3: urj

- short_pair: urj-urj

- chrF2_score: 0.58

- bleu: 32.9

- brevity_penalty: 1.0

- ref_len: 19444.0

- src_name: Uralic languages

- tgt_name: Uralic languages

- train_date: 2020-07-27

- src_alpha2: urj

- tgt_alpha2: urj

- prefer_old: False

- long_pair: urj-urj

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41