---
language: 
- ar
- de

tags:
- translation

license: apache-2.0
---

### ara-deu

* source group: Arabic 
* target group: German 
*  OPUS readme: [ara-deu](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-deu/README.md)

*  model: transformer-align
* source language(s): afb apc ara ara_Latn arq arz
* target language(s): deu
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-deu/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-deu/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-deu/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ara.deu 	| 44.7 	| 0.629 |


### System Info: 
- hf_name: ara-deu

- source_languages: ara

- target_languages: deu

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-deu/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ar', 'de']

- src_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- tgt_constituents: {'deu'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-deu/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-deu/opus-2020-07-03.test.txt

- src_alpha3: ara

- tgt_alpha3: deu

- short_pair: ar-de

- chrF2_score: 0.629

- bleu: 44.7

- brevity_penalty: 0.986

- ref_len: 8371.0

- src_name: Arabic

- tgt_name: German

- train_date: 2020-07-03

- src_alpha2: ar

- tgt_alpha2: de

- prefer_old: False

- long_pair: ara-deu

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41