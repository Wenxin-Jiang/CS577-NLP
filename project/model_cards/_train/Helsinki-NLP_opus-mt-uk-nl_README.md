---
language: 
- uk
- nl

tags:
- translation

license: apache-2.0
---

### ukr-nld

* source group: Ukrainian 
* target group: Dutch 
*  OPUS readme: [ukr-nld](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-nld/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): nld
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nld/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nld/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nld/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.nld 	| 48.7 	| 0.656 |


### System Info: 
- hf_name: ukr-nld

- source_languages: ukr

- target_languages: nld

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-nld/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'nl']

- src_constituents: {'ukr'}

- tgt_constituents: {'nld'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nld/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-nld/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: nld

- short_pair: uk-nl

- chrF2_score: 0.6559999999999999

- bleu: 48.7

- brevity_penalty: 0.985

- ref_len: 59943.0

- src_name: Ukrainian

- tgt_name: Dutch

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: nl

- prefer_old: False

- long_pair: ukr-nld

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41