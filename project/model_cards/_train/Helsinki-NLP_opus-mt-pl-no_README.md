---
language: 
- pl
- no

tags:
- translation

license: apache-2.0
---

### pol-nor

* source group: Polish 
* target group: Norwegian 
*  OPUS readme: [pol-nor](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/pol-nor/README.md)

*  model: transformer-align
* source language(s): pol
* target language(s): nob
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/pol-nor/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/pol-nor/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/pol-nor/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.pol.nor 	| 27.5 	| 0.479 |


### System Info: 
- hf_name: pol-nor

- source_languages: pol

- target_languages: nor

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/pol-nor/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['pl', 'no']

- src_constituents: {'pol'}

- tgt_constituents: {'nob', 'nno'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/pol-nor/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/pol-nor/opus-2020-06-17.test.txt

- src_alpha3: pol

- tgt_alpha3: nor

- short_pair: pl-no

- chrF2_score: 0.479

- bleu: 27.5

- brevity_penalty: 0.9690000000000001

- ref_len: 2045.0

- src_name: Polish

- tgt_name: Norwegian

- train_date: 2020-06-17

- src_alpha2: pl

- tgt_alpha2: no

- prefer_old: False

- long_pair: pol-nor

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41