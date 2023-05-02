---
language: 
- en
- hy

tags:
- translation

license: apache-2.0
---

### eng-hye

* source group: English 
* target group: Armenian 
*  OPUS readme: [eng-hye](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-hye/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): hye
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hye/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hye/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hye/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.hye 	| 16.6 	| 0.404 |


### System Info: 
- hf_name: eng-hye

- source_languages: eng

- target_languages: hye

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-hye/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'hy']

- src_constituents: {'eng'}

- tgt_constituents: {'hye', 'hye_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hye/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hye/opus-2020-06-16.test.txt

- src_alpha3: eng

- tgt_alpha3: hye

- short_pair: en-hy

- chrF2_score: 0.40399999999999997

- bleu: 16.6

- brevity_penalty: 1.0

- ref_len: 5115.0

- src_name: English

- tgt_name: Armenian

- train_date: 2020-06-16

- src_alpha2: en

- tgt_alpha2: hy

- prefer_old: False

- long_pair: eng-hye

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41