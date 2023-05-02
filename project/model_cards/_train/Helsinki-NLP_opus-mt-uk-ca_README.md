---
language: 
- uk
- ca

tags:
- translation

license: apache-2.0
---

### ukr-cat

* source group: Ukrainian 
* target group: Catalan 
*  OPUS readme: [ukr-cat](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-cat/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): cat
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-cat/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-cat/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-cat/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.cat 	| 33.7 	| 0.538 |


### System Info: 
- hf_name: ukr-cat

- source_languages: ukr

- target_languages: cat

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-cat/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'ca']

- src_constituents: {'ukr'}

- tgt_constituents: {'cat'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-cat/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-cat/opus-2020-06-16.test.txt

- src_alpha3: ukr

- tgt_alpha3: cat

- short_pair: uk-ca

- chrF2_score: 0.5379999999999999

- bleu: 33.7

- brevity_penalty: 0.972

- ref_len: 2670.0

- src_name: Ukrainian

- tgt_name: Catalan

- train_date: 2020-06-16

- src_alpha2: uk

- tgt_alpha2: ca

- prefer_old: False

- long_pair: ukr-cat

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41