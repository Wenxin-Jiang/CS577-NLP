---
language: 
- uk
- cs

tags:
- translation

license: apache-2.0
---

### ukr-ces

* source group: Ukrainian 
* target group: Czech 
*  OPUS readme: [ukr-ces](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-ces/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): ces
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ces/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ces/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ces/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.ces 	| 52.0 	| 0.686 |


### System Info: 
- hf_name: ukr-ces

- source_languages: ukr

- target_languages: ces

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-ces/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'cs']

- src_constituents: {'ukr'}

- tgt_constituents: {'ces'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ces/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ces/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: ces

- short_pair: uk-cs

- chrF2_score: 0.6859999999999999

- bleu: 52.0

- brevity_penalty: 0.993

- ref_len: 8550.0

- src_name: Ukrainian

- tgt_name: Czech

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: cs

- prefer_old: False

- long_pair: ukr-ces

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41