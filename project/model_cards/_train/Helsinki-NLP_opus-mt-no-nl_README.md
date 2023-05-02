---
language: 
- no
- nl

tags:
- translation

license: apache-2.0
---

### nor-nld

* source group: Norwegian 
* target group: Dutch 
*  OPUS readme: [nor-nld](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-nld/README.md)

*  model: transformer-align
* source language(s): nob
* target language(s): nld
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-nld/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-nld/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nor-nld/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.nor.nld 	| 40.2 	| 0.596 |


### System Info: 
- hf_name: nor-nld

- source_languages: nor

- target_languages: nld

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nor-nld/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['no', 'nl']

- src_constituents: {'nob', 'nno'}

- tgt_constituents: {'nld'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-nld/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/nor-nld/opus-2020-06-17.test.txt

- src_alpha3: nor

- tgt_alpha3: nld

- short_pair: no-nl

- chrF2_score: 0.596

- bleu: 40.2

- brevity_penalty: 0.9590000000000001

- ref_len: 1535.0

- src_name: Norwegian

- tgt_name: Dutch

- train_date: 2020-06-17

- src_alpha2: no

- tgt_alpha2: nl

- prefer_old: False

- long_pair: nor-nld

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41