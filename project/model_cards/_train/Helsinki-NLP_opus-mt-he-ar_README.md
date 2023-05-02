---
language: 
- he
- ar

tags:
- translation

license: apache-2.0
---

### heb-ara

* source group: Hebrew 
* target group: Arabic 
*  OPUS readme: [heb-ara](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-ara/README.md)

*  model: transformer
* source language(s): heb
* target language(s): apc apc_Latn ara arq arz
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ara/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ara/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ara/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.heb.ara 	| 23.6 	| 0.532 |


### System Info: 
- hf_name: heb-ara

- source_languages: heb

- target_languages: ara

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-ara/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['he', 'ar']

- src_constituents: {'heb'}

- tgt_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ara/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ara/opus-2020-07-03.test.txt

- src_alpha3: heb

- tgt_alpha3: ara

- short_pair: he-ar

- chrF2_score: 0.532

- bleu: 23.6

- brevity_penalty: 0.9259999999999999

- ref_len: 6372.0

- src_name: Hebrew

- tgt_name: Arabic

- train_date: 2020-07-03

- src_alpha2: he

- tgt_alpha2: ar

- prefer_old: False

- long_pair: heb-ara

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41