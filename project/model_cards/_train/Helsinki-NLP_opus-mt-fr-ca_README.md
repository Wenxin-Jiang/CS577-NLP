---
language: 
- fr
- ca

tags:
- translation

license: apache-2.0
---

### fra-cat

* source group: French 
* target group: Catalan 
*  OPUS readme: [fra-cat](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fra-cat/README.md)

*  model: transformer-align
* source language(s): fra
* target language(s): cat
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-cat/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-cat/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-cat/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.fra.cat 	| 43.4 	| 0.645 |


### System Info: 
- hf_name: fra-cat

- source_languages: fra

- target_languages: cat

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fra-cat/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['fr', 'ca']

- src_constituents: {'fra'}

- tgt_constituents: {'cat'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/fra-cat/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/fra-cat/opus-2020-06-16.test.txt

- src_alpha3: fra

- tgt_alpha3: cat

- short_pair: fr-ca

- chrF2_score: 0.645

- bleu: 43.4

- brevity_penalty: 0.982

- ref_len: 5214.0

- src_name: French

- tgt_name: Catalan

- train_date: 2020-06-16

- src_alpha2: fr

- tgt_alpha2: ca

- prefer_old: False

- long_pair: fra-cat

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41