---
language: 
- is
- it

tags:
- translation

license: apache-2.0
---

### isl-ita

* source group: Icelandic 
* target group: Italian 
*  OPUS readme: [isl-ita](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/isl-ita/README.md)

*  model: transformer-align
* source language(s): isl
* target language(s): ita
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/isl-ita/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/isl-ita/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/isl-ita/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.isl.ita 	| 46.7 	| 0.662 |


### System Info: 
- hf_name: isl-ita

- source_languages: isl

- target_languages: ita

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/isl-ita/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['is', 'it']

- src_constituents: {'isl'}

- tgt_constituents: {'ita'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/isl-ita/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/isl-ita/opus-2020-06-17.test.txt

- src_alpha3: isl

- tgt_alpha3: ita

- short_pair: is-it

- chrF2_score: 0.662

- bleu: 46.7

- brevity_penalty: 0.977

- ref_len: 1450.0

- src_name: Icelandic

- tgt_name: Italian

- train_date: 2020-06-17

- src_alpha2: is

- tgt_alpha2: it

- prefer_old: False

- long_pair: isl-ita

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41