---
language: 
- hy
- ru

tags:
- translation

license: apache-2.0
---

### hye-rus

* source group: Armenian 
* target group: Russian 
*  OPUS readme: [hye-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/hye-rus/README.md)

*  model: transformer-align
* source language(s): hye hye_Latn
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/hye-rus/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hye-rus/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hye-rus/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.hye.rus 	| 25.6 	| 0.476 |


### System Info: 
- hf_name: hye-rus

- source_languages: hye

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/hye-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['hy', 'ru']

- src_constituents: {'hye', 'hye_Latn'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/hye-rus/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/hye-rus/opus-2020-06-16.test.txt

- src_alpha3: hye

- tgt_alpha3: rus

- short_pair: hy-ru

- chrF2_score: 0.47600000000000003

- bleu: 25.6

- brevity_penalty: 0.929

- ref_len: 1624.0

- src_name: Armenian

- tgt_name: Russian

- train_date: 2020-06-16

- src_alpha2: hy

- tgt_alpha2: ru

- prefer_old: False

- long_pair: hye-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41