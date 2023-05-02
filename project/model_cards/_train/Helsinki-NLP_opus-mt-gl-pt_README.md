---
language: 
- gl
- pt

tags:
- translation

license: apache-2.0
---

### glg-por

* source group: Galician 
* target group: Portuguese 
*  OPUS readme: [glg-por](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/glg-por/README.md)

*  model: transformer-align
* source language(s): glg
* target language(s): por
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/glg-por/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/glg-por/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/glg-por/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.glg.por 	| 57.9 	| 0.758 |


### System Info: 
- hf_name: glg-por

- source_languages: glg

- target_languages: por

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/glg-por/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['gl', 'pt']

- src_constituents: {'glg'}

- tgt_constituents: {'por'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/glg-por/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/glg-por/opus-2020-06-16.test.txt

- src_alpha3: glg

- tgt_alpha3: por

- short_pair: gl-pt

- chrF2_score: 0.758

- bleu: 57.9

- brevity_penalty: 0.977

- ref_len: 3078.0

- src_name: Galician

- tgt_name: Portuguese

- train_date: 2020-06-16

- src_alpha2: gl

- tgt_alpha2: pt

- prefer_old: False

- long_pair: glg-por

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41