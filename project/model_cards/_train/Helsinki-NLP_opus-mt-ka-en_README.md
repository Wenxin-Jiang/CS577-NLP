---
language: 
- ka
- en

tags:
- translation

license: apache-2.0
---

### kat-eng

* source group: Georgian 
* target group: English 
*  OPUS readme: [kat-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/kat-eng/README.md)

*  model: transformer-align
* source language(s): kat
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/kat-eng/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/kat-eng/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/kat-eng/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.kat.eng 	| 37.9 	| 0.538 |


### System Info: 
- hf_name: kat-eng

- source_languages: kat

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/kat-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ka', 'en']

- src_constituents: {'kat'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/kat-eng/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/kat-eng/opus-2020-06-16.test.txt

- src_alpha3: kat

- tgt_alpha3: eng

- short_pair: ka-en

- chrF2_score: 0.5379999999999999

- bleu: 37.9

- brevity_penalty: 0.991

- ref_len: 5992.0

- src_name: Georgian

- tgt_name: English

- train_date: 2020-06-16

- src_alpha2: ka

- tgt_alpha2: en

- prefer_old: False

- long_pair: kat-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41