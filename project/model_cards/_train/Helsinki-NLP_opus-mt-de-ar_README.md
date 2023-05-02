---
language: 
- de
- ar

tags:
- translation

license: apache-2.0
---

### deu-ara

* source group: German 
* target group: Arabic 
*  OPUS readme: [deu-ara](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-ara/README.md)

*  model: transformer-align
* source language(s): deu
* target language(s): afb apc ara ara_Latn arq arz
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ara/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ara/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ara/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.deu.ara 	| 19.7 	| 0.486 |


### System Info: 
- hf_name: deu-ara

- source_languages: deu

- target_languages: ara

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-ara/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['de', 'ar']

- src_constituents: {'deu'}

- tgt_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ara/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ara/opus-2020-07-03.test.txt

- src_alpha3: deu

- tgt_alpha3: ara

- short_pair: de-ar

- chrF2_score: 0.486

- bleu: 19.7

- brevity_penalty: 0.993

- ref_len: 6324.0

- src_name: German

- tgt_name: Arabic

- train_date: 2020-07-03

- src_alpha2: de

- tgt_alpha2: ar

- prefer_old: False

- long_pair: deu-ara

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41