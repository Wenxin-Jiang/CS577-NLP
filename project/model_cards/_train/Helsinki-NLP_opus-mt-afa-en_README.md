---
language: 
- so
- ti
- am
- he
- mt
- ar
- afa
- en

tags:
- translation

license: apache-2.0
---

### afa-eng

* source group: Afro-Asiatic languages 
* target group: English 
*  OPUS readme: [afa-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afa-eng/README.md)

*  model: transformer
* source language(s): acm afb amh apc ara arq ary arz hau_Latn heb kab mlt rif_Latn shy_Latn som tir
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/afa-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afa-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afa-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.amh-eng.amh.eng 	| 35.9 	| 0.550 |
| Tatoeba-test.ara-eng.ara.eng 	| 36.6 	| 0.543 |
| Tatoeba-test.hau-eng.hau.eng 	| 11.9 	| 0.327 |
| Tatoeba-test.heb-eng.heb.eng 	| 42.7 	| 0.591 |
| Tatoeba-test.kab-eng.kab.eng 	| 4.3 	| 0.213 |
| Tatoeba-test.mlt-eng.mlt.eng 	| 44.3 	| 0.618 |
| Tatoeba-test.multi.eng 	| 27.1 	| 0.464 |
| Tatoeba-test.rif-eng.rif.eng 	| 3.5 	| 0.141 |
| Tatoeba-test.shy-eng.shy.eng 	| 0.6 	| 0.125 |
| Tatoeba-test.som-eng.som.eng 	| 23.6 	| 0.472 |
| Tatoeba-test.tir-eng.tir.eng 	| 13.1 	| 0.328 |


### System Info: 
- hf_name: afa-eng

- source_languages: afa

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afa-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['so', 'ti', 'am', 'he', 'mt', 'ar', 'afa', 'en']

- src_constituents: {'som', 'rif_Latn', 'tir', 'kab', 'arq', 'afb', 'amh', 'arz', 'heb', 'shy_Latn', 'apc', 'mlt', 'thv', 'ara', 'hau_Latn', 'acm', 'ary'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/afa-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/afa-eng/opus2m-2020-07-31.test.txt

- src_alpha3: afa

- tgt_alpha3: eng

- short_pair: afa-en

- chrF2_score: 0.46399999999999997

- bleu: 27.1

- brevity_penalty: 1.0

- ref_len: 69373.0

- src_name: Afro-Asiatic languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: afa

- tgt_alpha2: en

- prefer_old: False

- long_pair: afa-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41