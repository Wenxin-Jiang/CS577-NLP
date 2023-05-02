---
language: 
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
- en

tags:
- translation

license: apache-2.0
---

### iir-eng

* source group: Indo-Iranian languages 
* target group: English 
*  OPUS readme: [iir-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/iir-eng/README.md)

*  model: transformer
* source language(s): asm awa ben bho gom guj hif_Latn hin jdt_Cyrl kur_Arab kur_Latn mai mar npi ori oss pan_Guru pes pes_Latn pes_Thaa pnb pus rom san_Deva sin snd_Arab tgk_Cyrl tly_Latn urd zza
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/iir-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/iir-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/iir-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2014-hineng.hin.eng 	| 8.1 	| 0.324 |
| newsdev2019-engu-gujeng.guj.eng 	| 8.1 	| 0.309 |
| newstest2014-hien-hineng.hin.eng 	| 12.1 	| 0.380 |
| newstest2019-guen-gujeng.guj.eng 	| 6.0 	| 0.280 |
| Tatoeba-test.asm-eng.asm.eng 	| 13.9 	| 0.327 |
| Tatoeba-test.awa-eng.awa.eng 	| 7.0 	| 0.219 |
| Tatoeba-test.ben-eng.ben.eng 	| 42.5 	| 0.576 |
| Tatoeba-test.bho-eng.bho.eng 	| 27.3 	| 0.452 |
| Tatoeba-test.fas-eng.fas.eng 	| 5.6 	| 0.262 |
| Tatoeba-test.guj-eng.guj.eng 	| 15.9 	| 0.350 |
| Tatoeba-test.hif-eng.hif.eng 	| 10.1 	| 0.247 |
| Tatoeba-test.hin-eng.hin.eng 	| 36.5 	| 0.544 |
| Tatoeba-test.jdt-eng.jdt.eng 	| 11.4 	| 0.094 |
| Tatoeba-test.kok-eng.kok.eng 	| 6.6 	| 0.256 |
| Tatoeba-test.kur-eng.kur.eng 	| 3.4 	| 0.149 |
| Tatoeba-test.lah-eng.lah.eng 	| 17.4 	| 0.301 |
| Tatoeba-test.mai-eng.mai.eng 	| 65.4 	| 0.703 |
| Tatoeba-test.mar-eng.mar.eng 	| 22.5 	| 0.468 |
| Tatoeba-test.multi.eng 	| 21.3 	| 0.424 |
| Tatoeba-test.nep-eng.nep.eng 	| 3.4 	| 0.185 |
| Tatoeba-test.ori-eng.ori.eng 	| 4.8 	| 0.244 |
| Tatoeba-test.oss-eng.oss.eng 	| 1.6 	| 0.173 |
| Tatoeba-test.pan-eng.pan.eng 	| 14.8 	| 0.348 |
| Tatoeba-test.pus-eng.pus.eng 	| 1.1 	| 0.182 |
| Tatoeba-test.rom-eng.rom.eng 	| 2.8 	| 0.185 |
| Tatoeba-test.san-eng.san.eng 	| 2.8 	| 0.185 |
| Tatoeba-test.sin-eng.sin.eng 	| 22.8 	| 0.474 |
| Tatoeba-test.snd-eng.snd.eng 	| 8.2 	| 0.287 |
| Tatoeba-test.tgk-eng.tgk.eng 	| 11.9 	| 0.321 |
| Tatoeba-test.tly-eng.tly.eng 	| 0.9 	| 0.076 |
| Tatoeba-test.urd-eng.urd.eng 	| 23.9 	| 0.438 |
| Tatoeba-test.zza-eng.zza.eng 	| 0.6 	| 0.098 |


### System Info: 
- hf_name: iir-eng

- source_languages: iir

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/iir-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bn', 'or', 'gu', 'mr', 'ur', 'hi', 'ps', 'os', 'as', 'si', 'iir', 'en']

- src_constituents: {'pnb', 'gom', 'ben', 'hif_Latn', 'ori', 'guj', 'pan_Guru', 'snd_Arab', 'npi', 'mar', 'urd', 'pes', 'bho', 'kur_Arab', 'tgk_Cyrl', 'hin', 'kur_Latn', 'pes_Thaa', 'pus', 'san_Deva', 'oss', 'tly_Latn', 'jdt_Cyrl', 'asm', 'zza', 'rom', 'mai', 'pes_Latn', 'awa', 'sin'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/iir-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/iir-eng/opus2m-2020-08-01.test.txt

- src_alpha3: iir

- tgt_alpha3: eng

- short_pair: iir-en

- chrF2_score: 0.424

- bleu: 21.3

- brevity_penalty: 1.0

- ref_len: 67026.0

- src_name: Indo-Iranian languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: iir

- tgt_alpha2: en

- prefer_old: False

- long_pair: iir-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41