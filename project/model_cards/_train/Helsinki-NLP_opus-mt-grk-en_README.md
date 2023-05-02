---
language: 
- el
- grk
- en

tags:
- translation

license: apache-2.0
---

### grk-eng

* source group: Greek languages 
* target group: English 
*  OPUS readme: [grk-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/grk-eng/README.md)

*  model: transformer
* source language(s): ell grc_Grek
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/grk-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/grk-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/grk-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ell-eng.ell.eng 	| 65.9 	| 0.779 |
| Tatoeba-test.grc-eng.grc.eng 	| 4.1 	| 0.187 |
| Tatoeba-test.multi.eng 	| 60.9 	| 0.733 |


### System Info: 
- hf_name: grk-eng

- source_languages: grk

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/grk-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['el', 'grk', 'en']

- src_constituents: {'grc_Grek', 'ell'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/grk-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/grk-eng/opus2m-2020-08-01.test.txt

- src_alpha3: grk

- tgt_alpha3: eng

- short_pair: grk-en

- chrF2_score: 0.733

- bleu: 60.9

- brevity_penalty: 0.973

- ref_len: 62205.0

- src_name: Greek languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: grk

- tgt_alpha2: en

- prefer_old: False

- long_pair: grk-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41