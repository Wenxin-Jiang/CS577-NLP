---
language: 
- sl
- uk

tags:
- translation

license: apache-2.0
---

### slv-ukr

* source group: Slovenian 
* target group: Ukrainian 
*  OPUS readme: [slv-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/slv-ukr/README.md)

*  model: transformer-align
* source language(s): slv
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/slv-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/slv-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/slv-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.slv.ukr 	| 10.6 	| 0.236 |


### System Info: 
- hf_name: slv-ukr

- source_languages: slv

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/slv-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['sl', 'uk']

- src_constituents: {'slv'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/slv-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/slv-ukr/opus-2020-06-17.test.txt

- src_alpha3: slv

- tgt_alpha3: ukr

- short_pair: sl-uk

- chrF2_score: 0.23600000000000002

- bleu: 10.6

- brevity_penalty: 1.0

- ref_len: 3906.0

- src_name: Slovenian

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: sl

- tgt_alpha2: uk

- prefer_old: False

- long_pair: slv-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41