---
language: 
- ar
- el

tags:
- translation

license: apache-2.0
---

### ara-ell

* source group: Arabic 
* target group: Modern Greek (1453-) 
*  OPUS readme: [ara-ell](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-ell/README.md)

*  model: transformer-align
* source language(s): ara arz
* target language(s): ell
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ell/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ell/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ell/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ara.ell 	| 43.9 	| 0.636 |


### System Info: 
- hf_name: ara-ell

- source_languages: ara

- target_languages: ell

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-ell/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ar', 'el']

- src_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- tgt_constituents: {'ell'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ell/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ell/opus-2020-07-03.test.txt

- src_alpha3: ara

- tgt_alpha3: ell

- short_pair: ar-el

- chrF2_score: 0.636

- bleu: 43.9

- brevity_penalty: 0.993

- ref_len: 2009.0

- src_name: Arabic

- tgt_name: Modern Greek (1453-)

- train_date: 2020-07-03

- src_alpha2: ar

- tgt_alpha2: el

- prefer_old: False

- long_pair: ara-ell

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41