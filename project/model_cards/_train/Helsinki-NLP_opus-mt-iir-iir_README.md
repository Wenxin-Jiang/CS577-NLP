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

tags:
- translation

license: apache-2.0
---

### iir-iir

* source group: Indo-Iranian languages 
* target group: Indo-Iranian languages 
*  OPUS readme: [iir-iir](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/iir-iir/README.md)

*  model: transformer
* source language(s): asm hin mar urd zza
* target language(s): asm hin mar urd zza
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/iir-iir/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/iir-iir/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/iir-iir/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.asm-hin.asm.hin 	| 3.5 	| 0.202 |
| Tatoeba-test.asm-zza.asm.zza 	| 12.4 	| 0.014 |
| Tatoeba-test.hin-asm.hin.asm 	| 6.2 	| 0.238 |
| Tatoeba-test.hin-mar.hin.mar 	| 27.0 	| 0.560 |
| Tatoeba-test.hin-urd.hin.urd 	| 21.4 	| 0.507 |
| Tatoeba-test.mar-hin.mar.hin 	| 13.4 	| 0.463 |
| Tatoeba-test.multi.multi 	| 17.7 	| 0.460 |
| Tatoeba-test.urd-hin.urd.hin 	| 13.4 	| 0.363 |
| Tatoeba-test.zza-asm.zza.asm 	| 5.3 	| 0.000 |


### System Info: 
- hf_name: iir-iir

- source_languages: iir

- target_languages: iir

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/iir-iir/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bn', 'or', 'gu', 'mr', 'ur', 'hi', 'ps', 'os', 'as', 'si', 'iir']

- src_constituents: {'pnb', 'gom', 'ben', 'hif_Latn', 'ori', 'guj', 'pan_Guru', 'snd_Arab', 'npi', 'mar', 'urd', 'pes', 'bho', 'kur_Arab', 'tgk_Cyrl', 'hin', 'kur_Latn', 'pes_Thaa', 'pus', 'san_Deva', 'oss', 'tly_Latn', 'jdt_Cyrl', 'asm', 'zza', 'rom', 'mai', 'pes_Latn', 'awa', 'sin'}

- tgt_constituents: {'pnb', 'gom', 'ben', 'hif_Latn', 'ori', 'guj', 'pan_Guru', 'snd_Arab', 'npi', 'mar', 'urd', 'pes', 'bho', 'kur_Arab', 'tgk_Cyrl', 'hin', 'kur_Latn', 'pes_Thaa', 'pus', 'san_Deva', 'oss', 'tly_Latn', 'jdt_Cyrl', 'asm', 'zza', 'rom', 'mai', 'pes_Latn', 'awa', 'sin'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/iir-iir/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/iir-iir/opus-2020-07-27.test.txt

- src_alpha3: iir

- tgt_alpha3: iir

- short_pair: iir-iir

- chrF2_score: 0.46

- bleu: 17.7

- brevity_penalty: 1.0

- ref_len: 4992.0

- src_name: Indo-Iranian languages

- tgt_name: Indo-Iranian languages

- train_date: 2020-07-27

- src_alpha2: iir

- tgt_alpha2: iir

- prefer_old: False

- long_pair: iir-iir

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41