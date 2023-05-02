---
language: 
- da
- nb
- sv
- is
- nn
- fo
- gmq
- en

tags:
- translation

license: apache-2.0
---

### gmq-eng

* source group: North Germanic languages 
* target group: English 
*  OPUS readme: [gmq-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-eng/README.md)

*  model: transformer
* source language(s): dan fao isl nno nob nob_Hebr non_Latn swe
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-eng/opus2m-2020-07-26.zip)
* test set translations: [opus2m-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-eng/opus2m-2020-07-26.test.txt)
* test set scores: [opus2m-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-eng/opus2m-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.multi.eng 	| 58.1 	| 0.720 |


### System Info: 
- hf_name: gmq-eng

- source_languages: gmq

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/gmq-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['da', 'nb', 'sv', 'is', 'nn', 'fo', 'gmq', 'en']

- src_constituents: {'dan', 'nob', 'nob_Hebr', 'swe', 'isl', 'nno', 'non_Latn', 'fao'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-eng/opus2m-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/gmq-eng/opus2m-2020-07-26.test.txt

- src_alpha3: gmq

- tgt_alpha3: eng

- short_pair: gmq-en

- chrF2_score: 0.72

- bleu: 58.1

- brevity_penalty: 0.982

- ref_len: 72641.0

- src_name: North Germanic languages

- tgt_name: English

- train_date: 2020-07-26

- src_alpha2: gmq

- tgt_alpha2: en

- prefer_old: False

- long_pair: gmq-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41