---
language: 
- eo
- pt

tags:
- translation

license: apache-2.0
---

### epo-por

* source group: Esperanto 
* target group: Portuguese 
*  OPUS readme: [epo-por](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-por/README.md)

*  model: transformer-align
* source language(s): epo
* target language(s): por
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-por/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-por/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-por/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.epo.por 	| 20.2 	| 0.438 |


### System Info: 
- hf_name: epo-por

- source_languages: epo

- target_languages: por

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-por/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eo', 'pt']

- src_constituents: {'epo'}

- tgt_constituents: {'por'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-por/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-por/opus-2020-06-16.test.txt

- src_alpha3: epo

- tgt_alpha3: por

- short_pair: eo-pt

- chrF2_score: 0.43799999999999994

- bleu: 20.2

- brevity_penalty: 0.895

- ref_len: 89991.0

- src_name: Esperanto

- tgt_name: Portuguese

- train_date: 2020-06-16

- src_alpha2: eo

- tgt_alpha2: pt

- prefer_old: False

- long_pair: epo-por

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41