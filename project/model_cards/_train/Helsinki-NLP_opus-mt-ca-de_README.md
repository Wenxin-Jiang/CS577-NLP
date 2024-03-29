---
language: 
- ca
- de

tags:
- translation

license: apache-2.0
---

### cat-deu

* source group: Catalan 
* target group: German 
*  OPUS readme: [cat-deu](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-deu/README.md)

*  model: transformer-align
* source language(s): cat
* target language(s): deu
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-deu/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-deu/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-deu/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.cat.deu 	| 39.5 	| 0.593 |


### System Info: 
- hf_name: cat-deu

- source_languages: cat

- target_languages: deu

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-deu/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ca', 'de']

- src_constituents: {'cat'}

- tgt_constituents: {'deu'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-deu/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-deu/opus-2020-06-16.test.txt

- src_alpha3: cat

- tgt_alpha3: deu

- short_pair: ca-de

- chrF2_score: 0.593

- bleu: 39.5

- brevity_penalty: 1.0

- ref_len: 5643.0

- src_name: Catalan

- tgt_name: German

- train_date: 2020-06-16

- src_alpha2: ca

- tgt_alpha2: de

- prefer_old: False

- long_pair: cat-deu

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41