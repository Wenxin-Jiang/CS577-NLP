---
language: 
- en
- bn
- or
- gu
- mr
- ur
- hi
- ps
- os
- as
- si
- iir

tags:
- translation

license: apache-2.0
---

### eng-iir

* source group: English 
* target group: Indo-Iranian languages 
*  OPUS readme: [eng-iir](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-iir/README.md)

*  model: transformer
* source language(s): eng
* target language(s): asm awa ben bho gom guj hif_Latn hin jdt_Cyrl kur_Arab kur_Latn mai mar npi ori oss pan_Guru pes pes_Latn pes_Thaa pnb pus rom san_Deva sin snd_Arab tgk_Cyrl tly_Latn urd zza
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-iir/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-iir/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-iir/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2014-enghin.eng.hin 	| 6.7 	| 0.326 |
| newsdev2019-engu-engguj.eng.guj 	| 6.0 	| 0.283 |
| newstest2014-hien-enghin.eng.hin 	| 10.4 	| 0.353 |
| newstest2019-engu-engguj.eng.guj 	| 6.6 	| 0.282 |
| Tatoeba-test.eng-asm.eng.asm 	| 2.7 	| 0.249 |
| Tatoeba-test.eng-awa.eng.awa 	| 0.4 	| 0.122 |
| Tatoeba-test.eng-ben.eng.ben 	| 15.3 	| 0.459 |
| Tatoeba-test.eng-bho.eng.bho 	| 3.7 	| 0.161 |
| Tatoeba-test.eng-fas.eng.fas 	| 3.4 	| 0.227 |
| Tatoeba-test.eng-guj.eng.guj 	| 18.5 	| 0.365 |
| Tatoeba-test.eng-hif.eng.hif 	| 1.0 	| 0.064 |
| Tatoeba-test.eng-hin.eng.hin 	| 17.0 	| 0.461 |
| Tatoeba-test.eng-jdt.eng.jdt 	| 3.9 	| 0.122 |
| Tatoeba-test.eng-kok.eng.kok 	| 5.5 	| 0.059 |
| Tatoeba-test.eng-kur.eng.kur 	| 4.0 	| 0.125 |
| Tatoeba-test.eng-lah.eng.lah 	| 0.3 	| 0.008 |
| Tatoeba-test.eng-mai.eng.mai 	| 9.3 	| 0.445 |
| Tatoeba-test.eng-mar.eng.mar 	| 20.7 	| 0.473 |
| Tatoeba-test.eng.multi 	| 13.7 	| 0.392 |
| Tatoeba-test.eng-nep.eng.nep 	| 0.6 	| 0.060 |
| Tatoeba-test.eng-ori.eng.ori 	| 2.4 	| 0.193 |
| Tatoeba-test.eng-oss.eng.oss 	| 2.1 	| 0.174 |
| Tatoeba-test.eng-pan.eng.pan 	| 9.7 	| 0.355 |
| Tatoeba-test.eng-pus.eng.pus 	| 1.0 	| 0.126 |
| Tatoeba-test.eng-rom.eng.rom 	| 1.3 	| 0.230 |
| Tatoeba-test.eng-san.eng.san 	| 1.3 	| 0.101 |
| Tatoeba-test.eng-sin.eng.sin 	| 11.7 	| 0.384 |
| Tatoeba-test.eng-snd.eng.snd 	| 2.8 	| 0.180 |
| Tatoeba-test.eng-tgk.eng.tgk 	| 8.1 	| 0.353 |
| Tatoeba-test.eng-tly.eng.tly 	| 0.5 	| 0.015 |
| Tatoeba-test.eng-urd.eng.urd 	| 12.3 	| 0.409 |
| Tatoeba-test.eng-zza.eng.zza 	| 0.5 	| 0.025 |


### System Info: 
- hf_name: eng-iir

- source_languages: eng

- target_languages: iir

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-iir/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'bn', 'or', 'gu', 'mr', 'ur', 'hi', 'ps', 'os', 'as', 'si', 'iir']

- src_constituents: {'eng'}

- tgt_constituents: {'pnb', 'gom', 'ben', 'hif_Latn', 'ori', 'guj', 'pan_Guru', 'snd_Arab', 'npi', 'mar', 'urd', 'pes', 'bho', 'kur_Arab', 'tgk_Cyrl', 'hin', 'kur_Latn', 'pes_Thaa', 'pus', 'san_Deva', 'oss', 'tly_Latn', 'jdt_Cyrl', 'asm', 'zza', 'rom', 'mai', 'pes_Latn', 'awa', 'sin'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-iir/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-iir/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: iir

- short_pair: en-iir

- chrF2_score: 0.392

- bleu: 13.7

- brevity_penalty: 1.0

- ref_len: 63351.0

- src_name: English

- tgt_name: Indo-Iranian languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: iir

- prefer_old: False

- long_pair: eng-iir

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41