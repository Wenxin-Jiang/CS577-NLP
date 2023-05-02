---
language: 
- es
- ar

tags:
- translation

license: apache-2.0
---

### spa-ara

* source group: Spanish 
* target group: Arabic 
*  OPUS readme: [spa-ara](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-ara/README.md)

*  model: transformer
* source language(s): spa
* target language(s): apc apc_Latn ara arq
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-ara/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-ara/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-ara/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.ara 	| 20.0 	| 0.517 |


### System Info: 
- hf_name: spa-ara

- source_languages: spa

- target_languages: ara

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-ara/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'ar']

- src_constituents: {'spa'}

- tgt_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-ara/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-ara/opus-2020-07-03.test.txt

- src_alpha3: spa

- tgt_alpha3: ara

- short_pair: es-ar

- chrF2_score: 0.517

- bleu: 20.0

- brevity_penalty: 0.9390000000000001

- ref_len: 7547.0

- src_name: Spanish

- tgt_name: Arabic

- train_date: 2020-07-03

- src_alpha2: es

- tgt_alpha2: ar

- prefer_old: False

- long_pair: spa-ara

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41