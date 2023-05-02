---
language: 
- so
- ti
- am
- he
- mt
- ar
- afa

tags:
- translation

license: apache-2.0
---

### afa-afa

* source group: Afro-Asiatic languages 
* target group: Afro-Asiatic languages 
*  OPUS readme: [afa-afa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afa-afa/README.md)

*  model: transformer
* source language(s): apc ara arq arz heb kab mlt shy_Latn thv
* target language(s): apc ara arq arz heb kab mlt shy_Latn thv
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/afa-afa/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afa-afa/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afa-afa/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ara-ara.ara.ara 	| 4.3 	| 0.148 |
| Tatoeba-test.ara-heb.ara.heb 	| 31.9 	| 0.525 |
| Tatoeba-test.ara-kab.ara.kab 	| 0.3 	| 0.120 |
| Tatoeba-test.ara-mlt.ara.mlt 	| 14.0 	| 0.428 |
| Tatoeba-test.ara-shy.ara.shy 	| 1.3 	| 0.050 |
| Tatoeba-test.heb-ara.heb.ara 	| 17.0 	| 0.464 |
| Tatoeba-test.heb-kab.heb.kab 	| 1.9 	| 0.104 |
| Tatoeba-test.kab-ara.kab.ara 	| 0.3 	| 0.044 |
| Tatoeba-test.kab-heb.kab.heb 	| 5.1 	| 0.099 |
| Tatoeba-test.kab-shy.kab.shy 	| 2.2 	| 0.009 |
| Tatoeba-test.kab-tmh.kab.tmh 	| 10.7 	| 0.007 |
| Tatoeba-test.mlt-ara.mlt.ara 	| 29.1 	| 0.498 |
| Tatoeba-test.multi.multi 	| 20.8 	| 0.434 |
| Tatoeba-test.shy-ara.shy.ara 	| 1.2 	| 0.053 |
| Tatoeba-test.shy-kab.shy.kab 	| 2.0 	| 0.134 |
| Tatoeba-test.tmh-kab.tmh.kab 	| 0.0 	| 0.047 |


### System Info: 
- hf_name: afa-afa

- source_languages: afa

- target_languages: afa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afa-afa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['so', 'ti', 'am', 'he', 'mt', 'ar', 'afa']

- src_constituents: {'som', 'rif_Latn', 'tir', 'kab', 'arq', 'afb', 'amh', 'arz', 'heb', 'shy_Latn', 'apc', 'mlt', 'thv', 'ara', 'hau_Latn', 'acm', 'ary'}

- tgt_constituents: {'som', 'rif_Latn', 'tir', 'kab', 'arq', 'afb', 'amh', 'arz', 'heb', 'shy_Latn', 'apc', 'mlt', 'thv', 'ara', 'hau_Latn', 'acm', 'ary'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/afa-afa/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/afa-afa/opus-2020-07-26.test.txt

- src_alpha3: afa

- tgt_alpha3: afa

- short_pair: afa-afa

- chrF2_score: 0.434

- bleu: 20.8

- brevity_penalty: 1.0

- ref_len: 15215.0

- src_name: Afro-Asiatic languages

- tgt_name: Afro-Asiatic languages

- train_date: 2020-07-26

- src_alpha2: afa

- tgt_alpha2: afa

- prefer_old: False

- long_pair: afa-afa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41