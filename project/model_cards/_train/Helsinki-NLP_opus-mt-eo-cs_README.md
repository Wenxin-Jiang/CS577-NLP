---
language: 
- eo
- cs

tags:
- translation

license: apache-2.0
---

### epo-ces

* source group: Esperanto 
* target group: Czech 
*  OPUS readme: [epo-ces](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-ces/README.md)

*  model: transformer-align
* source language(s): epo
* target language(s): ces
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ces/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ces/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ces/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.epo.ces 	| 17.5 	| 0.376 |


### System Info: 
- hf_name: epo-ces

- source_languages: epo

- target_languages: ces

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-ces/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eo', 'cs']

- src_constituents: {'epo'}

- tgt_constituents: {'ces'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ces/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-ces/opus-2020-06-16.test.txt

- src_alpha3: epo

- tgt_alpha3: ces

- short_pair: eo-cs

- chrF2_score: 0.376

- bleu: 17.5

- brevity_penalty: 0.922

- ref_len: 22148.0

- src_name: Esperanto

- tgt_name: Czech

- train_date: 2020-06-16

- src_alpha2: eo

- tgt_alpha2: cs

- prefer_old: False

- long_pair: epo-ces

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41