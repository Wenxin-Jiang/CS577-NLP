---
language: 
- he
- uk

tags:
- translation

license: apache-2.0
---

### heb-ukr

* source group: Hebrew 
* target group: Ukrainian 
*  OPUS readme: [heb-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-ukr/README.md)

*  model: transformer-align
* source language(s): heb
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.heb.ukr 	| 35.4 	| 0.552 |


### System Info: 
- hf_name: heb-ukr

- source_languages: heb

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['he', 'uk']

- src_constituents: {'heb'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ukr/opus-2020-06-17.test.txt

- src_alpha3: heb

- tgt_alpha3: ukr

- short_pair: he-uk

- chrF2_score: 0.552

- bleu: 35.4

- brevity_penalty: 0.971

- ref_len: 5163.0

- src_name: Hebrew

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: he

- tgt_alpha2: uk

- prefer_old: False

- long_pair: heb-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41