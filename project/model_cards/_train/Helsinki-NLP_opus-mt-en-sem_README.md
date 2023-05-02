---
language: 
- en
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

### eng-sem

* source group: English 
* target group: Semitic languages 
*  OPUS readme: [eng-sem](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-sem/README.md)

*  model: transformer
* source language(s): eng
* target language(s): acm afb amh apc ara arq ary arz heb mlt tir
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sem/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sem/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sem/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-amh.eng.amh 	| 11.2 	| 0.480 |
| Tatoeba-test.eng-ara.eng.ara 	| 12.7 	| 0.417 |
| Tatoeba-test.eng-heb.eng.heb 	| 33.8 	| 0.564 |
| Tatoeba-test.eng-mlt.eng.mlt 	| 18.7 	| 0.554 |
| Tatoeba-test.eng.multi 	| 23.5 	| 0.486 |
| Tatoeba-test.eng-tir.eng.tir 	| 2.7 	| 0.248 |


### System Info: 
- hf_name: eng-sem

- source_languages: eng

- target_languages: sem

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-sem/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'mt', 'ar', 'he', 'ti', 'am', 'sem']

- src_constituents: {'eng'}

- tgt_constituents: {'apc', 'mlt', 'arz', 'ara', 'heb', 'tir', 'arq', 'afb', 'amh', 'acm', 'ary'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sem/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sem/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: sem

- short_pair: en-sem

- chrF2_score: 0.486

- bleu: 23.5

- brevity_penalty: 1.0

- ref_len: 59258.0

- src_name: English

- tgt_name: Semitic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: sem

- prefer_old: False

- long_pair: eng-sem

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41