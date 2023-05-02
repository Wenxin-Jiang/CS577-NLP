---
language: 
- en
- el
- grk

tags:
- translation

license: apache-2.0
---

### eng-grk

* source group: English 
* target group: Greek languages 
*  OPUS readme: [eng-grk](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-grk/README.md)

*  model: transformer
* source language(s): eng
* target language(s): ell grc_Grek
* model: transformer
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-grk/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-grk/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-grk/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-ell.eng.ell 	| 53.8 	| 0.723 |
| Tatoeba-test.eng-grc.eng.grc 	| 0.1 	| 0.102 |
| Tatoeba-test.eng.multi 	| 45.6 	| 0.677 |


### System Info: 
- hf_name: eng-grk

- source_languages: eng

- target_languages: grk

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-grk/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'el', 'grk']

- src_constituents: {'eng'}

- tgt_constituents: {'grc_Grek', 'ell'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-grk/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-grk/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: grk

- short_pair: en-grk

- chrF2_score: 0.677

- bleu: 45.6

- brevity_penalty: 1.0

- ref_len: 59951.0

- src_name: English

- tgt_name: Greek languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: grk

- prefer_old: False

- long_pair: eng-grk

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41