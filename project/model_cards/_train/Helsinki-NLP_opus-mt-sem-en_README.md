---
language: 
- mt
- ar
- he
- ti
- am
- sem
- en

tags:
- translation

license: apache-2.0
---

### sem-eng

* source group: Semitic languages 
* target group: English 
*  OPUS readme: [sem-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sem-eng/README.md)

*  model: transformer
* source language(s): acm afb amh apc ara arq ary arz heb mlt tir
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/sem-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sem-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sem-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.amh-eng.amh.eng 	| 37.5 	| 0.565 |
| Tatoeba-test.ara-eng.ara.eng 	| 38.9 	| 0.566 |
| Tatoeba-test.heb-eng.heb.eng 	| 44.6 	| 0.610 |
| Tatoeba-test.mlt-eng.mlt.eng 	| 53.7 	| 0.688 |
| Tatoeba-test.multi.eng 	| 41.7 	| 0.588 |
| Tatoeba-test.tir-eng.tir.eng 	| 18.3 	| 0.370 |


### System Info: 
- hf_name: sem-eng

- source_languages: sem

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sem-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['mt', 'ar', 'he', 'ti', 'am', 'sem', 'en']

- src_constituents: {'apc', 'mlt', 'arz', 'ara', 'heb', 'tir', 'arq', 'afb', 'amh', 'acm', 'ary'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/sem-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/sem-eng/opus2m-2020-08-01.test.txt

- src_alpha3: sem

- tgt_alpha3: eng

- short_pair: sem-en

- chrF2_score: 0.588

- bleu: 41.7

- brevity_penalty: 0.987

- ref_len: 72950.0

- src_name: Semitic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: sem

- tgt_alpha2: en

- prefer_old: False

- long_pair: sem-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41