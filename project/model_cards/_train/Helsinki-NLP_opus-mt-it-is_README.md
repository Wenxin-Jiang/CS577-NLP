---
language: 
- it
- is

tags:
- translation

license: apache-2.0
---

### ita-isl

* source group: Italian 
* target group: Icelandic 
*  OPUS readme: [ita-isl](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-isl/README.md)

*  model: transformer-align
* source language(s): ita
* target language(s): isl
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-isl/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-isl/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-isl/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ita.isl 	| 28.6 	| 0.524 |


### System Info: 
- hf_name: ita-isl

- source_languages: ita

- target_languages: isl

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-isl/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['it', 'is']

- src_constituents: {'ita'}

- tgt_constituents: {'isl'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-isl/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-isl/opus-2020-06-17.test.txt

- src_alpha3: ita

- tgt_alpha3: isl

- short_pair: it-is

- chrF2_score: 0.524

- bleu: 28.6

- brevity_penalty: 0.972

- ref_len: 1459.0

- src_name: Italian

- tgt_name: Icelandic

- train_date: 2020-06-17

- src_alpha2: it

- tgt_alpha2: is

- prefer_old: False

- long_pair: ita-isl

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41