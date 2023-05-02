---
language: 
- de
- ca

tags:
- translation

license: apache-2.0
---

### deu-cat

* source group: German 
* target group: Catalan 
*  OPUS readme: [deu-cat](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-cat/README.md)

*  model: transformer-align
* source language(s): deu
* target language(s): cat
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-cat/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-cat/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-cat/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.deu.cat 	| 37.4 	| 0.582 |


### System Info: 
- hf_name: deu-cat

- source_languages: deu

- target_languages: cat

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-cat/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['de', 'ca']

- src_constituents: {'deu'}

- tgt_constituents: {'cat'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-cat/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-cat/opus-2020-06-16.test.txt

- src_alpha3: deu

- tgt_alpha3: cat

- short_pair: de-ca

- chrF2_score: 0.5820000000000001

- bleu: 37.4

- brevity_penalty: 0.956

- ref_len: 5507.0

- src_name: German

- tgt_name: Catalan

- train_date: 2020-06-16

- src_alpha2: de

- tgt_alpha2: ca

- prefer_old: False

- long_pair: deu-cat

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41