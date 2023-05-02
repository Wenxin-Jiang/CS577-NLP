---
language: 
- mt
- ar
- he
- ti
- am
- sem

tags:
- translation

license: apache-2.0
---

### sem-sem

* source group: Semitic languages 
* target group: Semitic languages 
*  OPUS readme: [sem-sem](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sem-sem/README.md)

*  model: transformer
* source language(s): apc ara arq arz heb mlt
* target language(s): apc ara arq arz heb mlt
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/sem-sem/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sem-sem/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sem-sem/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ara-ara.ara.ara 	| 4.2 	| 0.200 |
| Tatoeba-test.ara-heb.ara.heb 	| 34.0 	| 0.542 |
| Tatoeba-test.ara-mlt.ara.mlt 	| 16.6 	| 0.513 |
| Tatoeba-test.heb-ara.heb.ara 	| 18.8 	| 0.477 |
| Tatoeba-test.mlt-ara.mlt.ara 	| 20.7 	| 0.388 |
| Tatoeba-test.multi.multi 	| 27.1 	| 0.507 |


### System Info: 
- hf_name: sem-sem

- source_languages: sem

- target_languages: sem

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sem-sem/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['mt', 'ar', 'he', 'ti', 'am', 'sem']

- src_constituents: {'apc', 'mlt', 'arz', 'ara', 'heb', 'tir', 'arq', 'afb', 'amh', 'acm', 'ary'}

- tgt_constituents: {'apc', 'mlt', 'arz', 'ara', 'heb', 'tir', 'arq', 'afb', 'amh', 'acm', 'ary'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/sem-sem/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/sem-sem/opus-2020-07-27.test.txt

- src_alpha3: sem

- tgt_alpha3: sem

- short_pair: sem-sem

- chrF2_score: 0.507

- bleu: 27.1

- brevity_penalty: 0.972

- ref_len: 13472.0

- src_name: Semitic languages

- tgt_name: Semitic languages

- train_date: 2020-07-27

- src_alpha2: sem

- tgt_alpha2: sem

- prefer_old: False

- long_pair: sem-sem

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41