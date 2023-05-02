---
language: 
- ar
- es

tags:
- translation

license: apache-2.0
---

### ara-spa

* source group: Arabic 
* target group: Spanish 
*  OPUS readme: [ara-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-spa/README.md)

*  model: transformer
* source language(s): apc apc_Latn ara arq
* target language(s): spa
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-spa/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-spa/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-spa/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ara.spa 	| 46.0 	| 0.641 |


### System Info: 
- hf_name: ara-spa

- source_languages: ara

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ar', 'es']

- src_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- tgt_constituents: {'spa'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-spa/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-spa/opus-2020-07-03.test.txt

- src_alpha3: ara

- tgt_alpha3: spa

- short_pair: ar-es

- chrF2_score: 0.6409999999999999

- bleu: 46.0

- brevity_penalty: 0.9620000000000001

- ref_len: 9708.0

- src_name: Arabic

- tgt_name: Spanish

- train_date: 2020-07-03

- src_alpha2: ar

- tgt_alpha2: es

- prefer_old: False

- long_pair: ara-spa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41