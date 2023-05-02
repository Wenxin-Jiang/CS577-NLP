---
language: 
- uk
- he

tags:
- translation

license: apache-2.0
---

### ukr-heb

* source group: Ukrainian 
* target group: Hebrew 
*  OPUS readme: [ukr-heb](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-heb/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): heb
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-heb/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-heb/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-heb/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.heb 	| 35.7 	| 0.557 |


### System Info: 
- hf_name: ukr-heb

- source_languages: ukr

- target_languages: heb

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-heb/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'he']

- src_constituents: {'ukr'}

- tgt_constituents: {'heb'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-heb/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-heb/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: heb

- short_pair: uk-he

- chrF2_score: 0.557

- bleu: 35.7

- brevity_penalty: 1.0

- ref_len: 4765.0

- src_name: Ukrainian

- tgt_name: Hebrew

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: he

- prefer_old: False

- long_pair: ukr-heb

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41