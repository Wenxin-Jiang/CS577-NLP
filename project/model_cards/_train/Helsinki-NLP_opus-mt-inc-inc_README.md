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

tags:
- translation

license: apache-2.0
---

### inc-inc

* source group: Indic languages 
* target group: Indic languages 
*  OPUS readme: [inc-inc](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/inc-inc/README.md)

*  model: transformer
* source language(s): asm hin mar urd
* target language(s): asm hin mar urd
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/inc-inc/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/inc-inc/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/inc-inc/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.asm-hin.asm.hin 	| 2.6 	| 0.231 |
| Tatoeba-test.hin-asm.hin.asm 	| 9.1 	| 0.262 |
| Tatoeba-test.hin-mar.hin.mar 	| 28.1 	| 0.548 |
| Tatoeba-test.hin-urd.hin.urd 	| 19.9 	| 0.508 |
| Tatoeba-test.mar-hin.mar.hin 	| 11.6 	| 0.466 |
| Tatoeba-test.multi.multi 	| 17.1 	| 0.464 |
| Tatoeba-test.urd-hin.urd.hin 	| 13.5 	| 0.377 |


### System Info: 
- hf_name: inc-inc

- source_languages: inc

- target_languages: inc

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/inc-inc/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bn', 'or', 'gu', 'mr', 'ur', 'hi', 'as', 'si', 'inc']

- src_constituents: {'pnb', 'gom', 'ben', 'hif_Latn', 'ori', 'guj', 'pan_Guru', 'snd_Arab', 'npi', 'mar', 'urd', 'bho', 'hin', 'san_Deva', 'asm', 'rom', 'mai', 'awa', 'sin'}

- tgt_constituents: {'pnb', 'gom', 'ben', 'hif_Latn', 'ori', 'guj', 'pan_Guru', 'snd_Arab', 'npi', 'mar', 'urd', 'bho', 'hin', 'san_Deva', 'asm', 'rom', 'mai', 'awa', 'sin'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/inc-inc/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/inc-inc/opus-2020-07-27.test.txt

- src_alpha3: inc

- tgt_alpha3: inc

- short_pair: inc-inc

- chrF2_score: 0.46399999999999997

- bleu: 17.1

- brevity_penalty: 1.0

- ref_len: 4985.0

- src_name: Indic languages

- tgt_name: Indic languages

- train_date: 2020-07-27

- src_alpha2: inc

- tgt_alpha2: inc

- prefer_old: False

- long_pair: inc-inc

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41