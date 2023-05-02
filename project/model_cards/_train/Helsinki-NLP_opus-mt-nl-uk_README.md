---
language: 
- nl
- uk

tags:
- translation

license: apache-2.0
---

### nld-ukr

* source group: Dutch 
* target group: Ukrainian 
*  OPUS readme: [nld-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nld-ukr/README.md)

*  model: transformer-align
* source language(s): nld
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/nld-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nld-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nld-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.nld.ukr 	| 40.8 	| 0.619 |


### System Info: 
- hf_name: nld-ukr

- source_languages: nld

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nld-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['nl', 'uk']

- src_constituents: {'nld'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/nld-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/nld-ukr/opus-2020-06-17.test.txt

- src_alpha3: nld

- tgt_alpha3: ukr

- short_pair: nl-uk

- chrF2_score: 0.619

- bleu: 40.8

- brevity_penalty: 0.992

- ref_len: 51674.0

- src_name: Dutch

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: nl

- tgt_alpha2: uk

- prefer_old: False

- long_pair: nld-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41