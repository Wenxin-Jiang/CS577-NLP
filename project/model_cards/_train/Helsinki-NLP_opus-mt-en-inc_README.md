---
language: 
- en
- bn
- or
- gu
- mr
- ur
- hi
- as
- si
- inc

tags:
- translation

license: apache-2.0
---

### eng-inc

* source group: English 
* target group: Indic languages 
*  OPUS readme: [eng-inc](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-inc/README.md)

*  model: transformer
* source language(s): eng
* target language(s): asm awa ben bho gom guj hif_Latn hin mai mar npi ori pan_Guru pnb rom san_Deva sin snd_Arab urd
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-inc/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-inc/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-inc/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2014-enghin.eng.hin 	| 8.2 	| 0.342 |
| newsdev2019-engu-engguj.eng.guj 	| 6.5 	| 0.293 |
| newstest2014-hien-enghin.eng.hin 	| 11.4 	| 0.364 |
| newstest2019-engu-engguj.eng.guj 	| 7.2 	| 0.296 |
| Tatoeba-test.eng-asm.eng.asm 	| 2.7 	| 0.277 |
| Tatoeba-test.eng-awa.eng.awa 	| 0.5 	| 0.132 |
| Tatoeba-test.eng-ben.eng.ben 	| 16.7 	| 0.470 |
| Tatoeba-test.eng-bho.eng.bho 	| 4.3 	| 0.227 |
| Tatoeba-test.eng-guj.eng.guj 	| 17.5 	| 0.373 |
| Tatoeba-test.eng-hif.eng.hif 	| 0.6 	| 0.028 |
| Tatoeba-test.eng-hin.eng.hin 	| 17.7 	| 0.469 |
| Tatoeba-test.eng-kok.eng.kok 	| 1.7 	| 0.000 |
| Tatoeba-test.eng-lah.eng.lah 	| 0.3 	| 0.028 |
| Tatoeba-test.eng-mai.eng.mai 	| 15.6 	| 0.429 |
| Tatoeba-test.eng-mar.eng.mar 	| 21.3 	| 0.477 |
| Tatoeba-test.eng.multi 	| 17.3 	| 0.448 |
| Tatoeba-test.eng-nep.eng.nep 	| 0.8 	| 0.081 |
| Tatoeba-test.eng-ori.eng.ori 	| 2.2 	| 0.208 |
| Tatoeba-test.eng-pan.eng.pan 	| 8.0 	| 0.347 |
| Tatoeba-test.eng-rom.eng.rom 	| 0.4 	| 0.197 |
| Tatoeba-test.eng-san.eng.san 	| 0.5 	| 0.108 |
| Tatoeba-test.eng-sin.eng.sin 	| 9.1 	| 0.364 |
| Tatoeba-test.eng-snd.eng.snd 	| 4.4 	| 0.284 |
| Tatoeba-test.eng-urd.eng.urd 	| 13.3 	| 0.423 |


### System Info: 
- hf_name: eng-inc

- source_languages: eng

- target_languages: inc

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-inc/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'bn', 'or', 'gu', 'mr', 'ur', 'hi', 'as', 'si', 'inc']

- src_constituents: {'eng'}

- tgt_constituents: {'pnb', 'gom', 'ben', 'hif_Latn', 'ori', 'guj', 'pan_Guru', 'snd_Arab', 'npi', 'mar', 'urd', 'bho', 'hin', 'san_Deva', 'asm', 'rom', 'mai', 'awa', 'sin'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-inc/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-inc/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: inc

- short_pair: en-inc

- chrF2_score: 0.44799999999999995

- bleu: 17.3

- brevity_penalty: 1.0

- ref_len: 59917.0

- src_name: English

- tgt_name: Indic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: inc

- prefer_old: False

- long_pair: eng-inc

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41