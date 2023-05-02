---
language: 
- ca
- pt

tags:
- translation

license: apache-2.0
---

### cat-por

* source group: Catalan 
* target group: Portuguese 
*  OPUS readme: [cat-por](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-por/README.md)

*  model: transformer-align
* source language(s): cat
* target language(s): por
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-por/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-por/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-por/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.cat.por 	| 44.9 	| 0.658 |


### System Info: 
- hf_name: cat-por

- source_languages: cat

- target_languages: por

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-por/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ca', 'pt']

- src_constituents: {'cat'}

- tgt_constituents: {'por'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-por/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-por/opus-2020-06-17.test.txt

- src_alpha3: cat

- tgt_alpha3: por

- short_pair: ca-pt

- chrF2_score: 0.6579999999999999

- bleu: 44.9

- brevity_penalty: 0.953

- ref_len: 5847.0

- src_name: Catalan

- tgt_name: Portuguese

- train_date: 2020-06-17

- src_alpha2: ca

- tgt_alpha2: pt

- prefer_old: False

- long_pair: cat-por

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41