---
language: 
- sl
- ru

tags:
- translation

license: apache-2.0
---

### slv-rus

* source group: Slovenian 
* target group: Russian 
*  OPUS readme: [slv-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/slv-rus/README.md)

*  model: transformer-align
* source language(s): slv
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/slv-rus/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/slv-rus/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/slv-rus/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.slv.rus 	| 37.3 	| 0.504 |


### System Info: 
- hf_name: slv-rus

- source_languages: slv

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/slv-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['sl', 'ru']

- src_constituents: {'slv'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/slv-rus/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/slv-rus/opus-2020-06-17.test.txt

- src_alpha3: slv

- tgt_alpha3: rus

- short_pair: sl-ru

- chrF2_score: 0.504

- bleu: 37.3

- brevity_penalty: 0.988

- ref_len: 2101.0

- src_name: Slovenian

- tgt_name: Russian

- train_date: 2020-06-17

- src_alpha2: sl

- tgt_alpha2: ru

- prefer_old: False

- long_pair: slv-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41