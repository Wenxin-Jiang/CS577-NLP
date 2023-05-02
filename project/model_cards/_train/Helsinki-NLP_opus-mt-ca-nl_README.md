---
language: 
- ca
- nl

tags:
- translation

license: apache-2.0
---

### cat-nld

* source group: Catalan 
* target group: Dutch 
*  OPUS readme: [cat-nld](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-nld/README.md)

*  model: transformer-align
* source language(s): cat
* target language(s): nld
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-nld/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-nld/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-nld/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.cat.nld 	| 45.1 	| 0.632 |


### System Info: 
- hf_name: cat-nld

- source_languages: cat

- target_languages: nld

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-nld/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ca', 'nl']

- src_constituents: {'cat'}

- tgt_constituents: {'nld'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-nld/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-nld/opus-2020-06-16.test.txt

- src_alpha3: cat

- tgt_alpha3: nld

- short_pair: ca-nl

- chrF2_score: 0.632

- bleu: 45.1

- brevity_penalty: 0.965

- ref_len: 4157.0

- src_name: Catalan

- tgt_name: Dutch

- train_date: 2020-06-16

- src_alpha2: ca

- tgt_alpha2: nl

- prefer_old: False

- long_pair: cat-nld

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41