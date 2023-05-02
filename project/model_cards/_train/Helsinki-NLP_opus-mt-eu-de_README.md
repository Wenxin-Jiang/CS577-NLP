---
language: 
- eu
- de

tags:
- translation

license: apache-2.0
---

### eus-deu

* source group: Basque 
* target group: German 
*  OPUS readme: [eus-deu](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eus-deu/README.md)

*  model: transformer-align
* source language(s): eus
* target language(s): deu
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eus-deu/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eus-deu/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eus-deu/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eus.deu 	| 36.3 	| 0.562 |


### System Info: 
- hf_name: eus-deu

- source_languages: eus

- target_languages: deu

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eus-deu/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eu', 'de']

- src_constituents: {'eus'}

- tgt_constituents: {'deu'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eus-deu/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eus-deu/opus-2020-06-16.test.txt

- src_alpha3: eus

- tgt_alpha3: deu

- short_pair: eu-de

- chrF2_score: 0.562

- bleu: 36.3

- brevity_penalty: 0.953

- ref_len: 3315.0

- src_name: Basque

- tgt_name: German

- train_date: 2020-06-16

- src_alpha2: eu

- tgt_alpha2: de

- prefer_old: False

- long_pair: eus-deu

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41