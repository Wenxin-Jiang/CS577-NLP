---
language: 
- ar
- he

tags:
- translation

license: apache-2.0
---

### ara-heb

* source group: Arabic 
* target group: Hebrew 
*  OPUS readme: [ara-heb](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-heb/README.md)

*  model: transformer
* source language(s): apc apc_Latn ara arq arz
* target language(s): heb
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-heb/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-heb/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-heb/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ara.heb 	| 40.4 	| 0.605 |


### System Info: 
- hf_name: ara-heb

- source_languages: ara

- target_languages: heb

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-heb/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ar', 'he']

- src_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- tgt_constituents: {'heb'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-heb/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-heb/opus-2020-07-03.test.txt

- src_alpha3: ara

- tgt_alpha3: heb

- short_pair: ar-he

- chrF2_score: 0.605

- bleu: 40.4

- brevity_penalty: 1.0

- ref_len: 6801.0

- src_name: Arabic

- tgt_name: Hebrew

- train_date: 2020-07-03

- src_alpha2: ar

- tgt_alpha2: he

- prefer_old: False

- long_pair: ara-heb

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41