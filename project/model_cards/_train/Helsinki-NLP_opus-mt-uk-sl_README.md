---
language: 
- uk
- sl

tags:
- translation

license: apache-2.0
---

### ukr-slv

* source group: Ukrainian 
* target group: Slovenian 
*  OPUS readme: [ukr-slv](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-slv/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): slv
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-slv/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-slv/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-slv/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.slv 	| 11.8 	| 0.280 |


### System Info: 
- hf_name: ukr-slv

- source_languages: ukr

- target_languages: slv

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-slv/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'sl']

- src_constituents: {'ukr'}

- tgt_constituents: {'slv'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-slv/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-slv/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: slv

- short_pair: uk-sl

- chrF2_score: 0.28

- bleu: 11.8

- brevity_penalty: 1.0

- ref_len: 3823.0

- src_name: Ukrainian

- tgt_name: Slovenian

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: sl

- prefer_old: False

- long_pair: ukr-slv

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41