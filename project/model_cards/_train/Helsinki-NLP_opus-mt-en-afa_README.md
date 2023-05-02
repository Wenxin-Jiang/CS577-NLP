---
language: 
- en
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

### eng-afa

* source group: English 
* target group: Afro-Asiatic languages 
*  OPUS readme: [eng-afa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-afa/README.md)

*  model: transformer
* source language(s): eng
* target language(s): acm afb amh apc ara arq ary arz hau_Latn heb kab mlt rif_Latn shy_Latn som tir
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-afa/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-afa/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-afa/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-amh.eng.amh 	| 11.6 	| 0.504 |
| Tatoeba-test.eng-ara.eng.ara 	| 12.0 	| 0.404 |
| Tatoeba-test.eng-hau.eng.hau 	| 10.2 	| 0.429 |
| Tatoeba-test.eng-heb.eng.heb 	| 32.3 	| 0.551 |
| Tatoeba-test.eng-kab.eng.kab 	| 1.6 	| 0.191 |
| Tatoeba-test.eng-mlt.eng.mlt 	| 17.7 	| 0.551 |
| Tatoeba-test.eng.multi 	| 14.4 	| 0.375 |
| Tatoeba-test.eng-rif.eng.rif 	| 1.7 	| 0.103 |
| Tatoeba-test.eng-shy.eng.shy 	| 0.8 	| 0.090 |
| Tatoeba-test.eng-som.eng.som 	| 16.0 	| 0.429 |
| Tatoeba-test.eng-tir.eng.tir 	| 2.7 	| 0.238 |


### System Info: 
- hf_name: eng-afa

- source_languages: eng

- target_languages: afa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-afa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'so', 'ti', 'am', 'he', 'mt', 'ar', 'afa']

- src_constituents: {'eng'}

- tgt_constituents: {'som', 'rif_Latn', 'tir', 'kab', 'arq', 'afb', 'amh', 'arz', 'heb', 'shy_Latn', 'apc', 'mlt', 'thv', 'ara', 'hau_Latn', 'acm', 'ary'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-afa/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-afa/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: afa

- short_pair: en-afa

- chrF2_score: 0.375

- bleu: 14.4

- brevity_penalty: 1.0

- ref_len: 58110.0

- src_name: English

- tgt_name: Afro-Asiatic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: afa

- prefer_old: False

- long_pair: eng-afa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41