---
language: 
- bn
- en

tags:
- translation

license: apache-2.0
---

### ben-eng

* source group: Bengali 
* target group: English 
*  OPUS readme: [ben-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ben-eng/README.md)

*  model: transformer-align
* source language(s): ben
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ben-eng/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ben-eng/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ben-eng/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ben.eng 	| 49.7 	| 0.641 |


### System Info: 
- hf_name: ben-eng

- source_languages: ben

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ben-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bn', 'en']

- src_constituents: {'ben'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ben-eng/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ben-eng/opus-2020-06-17.test.txt

- src_alpha3: ben

- tgt_alpha3: eng

- short_pair: bn-en

- chrF2_score: 0.6409999999999999

- bleu: 49.7

- brevity_penalty: 0.976

- ref_len: 13978.0

- src_name: Bengali

- tgt_name: English

- train_date: 2020-06-17

- src_alpha2: bn

- tgt_alpha2: en

- prefer_old: False

- long_pair: ben-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41