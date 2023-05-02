---
language: 
- hu
- uk

tags:
- translation

license: apache-2.0
---

### hun-ukr

* source group: Hungarian 
* target group: Ukrainian 
*  OPUS readme: [hun-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/hun-ukr/README.md)

*  model: transformer-align
* source language(s): hun
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/hun-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hun-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/hun-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.hun.ukr 	| 41.2 	| 0.611 |


### System Info: 
- hf_name: hun-ukr

- source_languages: hun

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/hun-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['hu', 'uk']

- src_constituents: {'hun'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/hun-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/hun-ukr/opus-2020-06-17.test.txt

- src_alpha3: hun

- tgt_alpha3: ukr

- short_pair: hu-uk

- chrF2_score: 0.611

- bleu: 41.2

- brevity_penalty: 0.966

- ref_len: 2568.0

- src_name: Hungarian

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: hu

- tgt_alpha2: uk

- prefer_old: False

- long_pair: hun-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41