---
language: 
- bn
- or
- gu
- mr
- ur
- hi
- as
- si
- inc
- en

tags:
- translation

license: apache-2.0
---

### inc-eng

* source group: Indic languages 
* target group: English 
*  OPUS readme: [inc-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/inc-eng/README.md)

*  model: transformer
* source language(s): asm awa ben bho gom guj hif_Latn hin mai mar npi ori pan_Guru pnb rom san_Deva sin snd_Arab urd
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/inc-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/inc-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/inc-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2014-hineng.hin.eng 	| 8.9 	| 0.341 |
| newsdev2019-engu-gujeng.guj.eng 	| 8.7 	| 0.321 |
| newstest2014-hien-hineng.hin.eng 	| 13.1 	| 0.396 |
| newstest2019-guen-gujeng.guj.eng 	| 6.5 	| 0.290 |
| Tatoeba-test.asm-eng.asm.eng 	| 18.1 	| 0.363 |
| Tatoeba-test.awa-eng.awa.eng 	| 6.2 	| 0.222 |
| Tatoeba-test.ben-eng.ben.eng 	| 44.7 	| 0.595 |
| Tatoeba-test.bho-eng.bho.eng 	| 29.4 	| 0.458 |
| Tatoeba-test.guj-eng.guj.eng 	| 19.3 	| 0.383 |
| Tatoeba-test.hif-eng.hif.eng 	| 3.7 	| 0.220 |
| Tatoeba-test.hin-eng.hin.eng 	| 38.6 	| 0.564 |
| Tatoeba-test.kok-eng.kok.eng 	| 6.6 	| 0.287 |
| Tatoeba-test.lah-eng.lah.eng 	| 16.0 	| 0.272 |
| Tatoeba-test.mai-eng.mai.eng 	| 75.6 	| 0.796 |
| Tatoeba-test.mar-eng.mar.eng 	| 25.9 	| 0.497 |
| Tatoeba-test.multi.eng 	| 29.0 	| 0.502 |
| Tatoeba-test.nep-eng.nep.eng 	| 4.5 	| 0.198 |
| Tatoeba-test.ori-eng.ori.eng 	| 5.0 	| 0.226 |
| Tatoeba-test.pan-eng.pan.eng 	| 17.4 	| 0.375 |
| Tatoeba-test.rom-eng.rom.eng 	| 1.7 	| 0.174 |
| Tatoeba-test.san-eng.san.eng 	| 5.0 	| 0.173 |
| Tatoeba-test.sin-eng.sin.eng 	| 31.2 	| 0.511 |
| Tatoeba-test.snd-eng.snd.eng 	| 45.7 	| 0.670 |
| Tatoeba-test.urd-eng.urd.eng 	| 25.6 	| 0.456 |


### System Info: 
- hf_name: inc-eng

- source_languages: inc

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/inc-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bn', 'or', 'gu', 'mr', 'ur', 'hi', 'as', 'si', 'inc', 'en']

- src_constituents: {'pnb', 'gom', 'ben', 'hif_Latn', 'ori', 'guj', 'pan_Guru', 'snd_Arab', 'npi', 'mar', 'urd', 'bho', 'hin', 'san_Deva', 'asm', 'rom', 'mai', 'awa', 'sin'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/inc-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/inc-eng/opus2m-2020-08-01.test.txt

- src_alpha3: inc

- tgt_alpha3: eng

- short_pair: inc-en

- chrF2_score: 0.502

- bleu: 29.0

- brevity_penalty: 1.0

- ref_len: 64706.0

- src_name: Indic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: inc

- tgt_alpha2: en

- prefer_old: False

- long_pair: inc-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41