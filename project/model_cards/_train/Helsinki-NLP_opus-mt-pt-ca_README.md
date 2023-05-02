---
language: 
- pt
- ca

tags:
- translation

license: apache-2.0
---

### por-cat

* source group: Portuguese 
* target group: Catalan 
*  OPUS readme: [por-cat](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/por-cat/README.md)

*  model: transformer-align
* source language(s): por
* target language(s): cat
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/por-cat/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/por-cat/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/por-cat/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.por.cat 	| 45.7 	| 0.672 |


### System Info: 
- hf_name: por-cat

- source_languages: por

- target_languages: cat

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/por-cat/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['pt', 'ca']

- src_constituents: {'por'}

- tgt_constituents: {'cat'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/por-cat/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/por-cat/opus-2020-06-17.test.txt

- src_alpha3: por

- tgt_alpha3: cat

- short_pair: pt-ca

- chrF2_score: 0.672

- bleu: 45.7

- brevity_penalty: 0.972

- ref_len: 5878.0

- src_name: Portuguese

- tgt_name: Catalan

- train_date: 2020-06-17

- src_alpha2: pt

- tgt_alpha2: ca

- prefer_old: False

- long_pair: por-cat

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41