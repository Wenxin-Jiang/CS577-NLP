---
language: 
- ca
- uk

tags:
- translation

license: apache-2.0
---

### cat-ukr

* source group: Catalan 
* target group: Ukrainian 
*  OPUS readme: [cat-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-ukr/README.md)

*  model: transformer-align
* source language(s): cat
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-ukr/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-ukr/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-ukr/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.cat.ukr 	| 28.6 	| 0.503 |


### System Info: 
- hf_name: cat-ukr

- source_languages: cat

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ca', 'uk']

- src_constituents: {'cat'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-ukr/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-ukr/opus-2020-06-16.test.txt

- src_alpha3: cat

- tgt_alpha3: ukr

- short_pair: ca-uk

- chrF2_score: 0.503

- bleu: 28.6

- brevity_penalty: 0.9670000000000001

- ref_len: 2438.0

- src_name: Catalan

- tgt_name: Ukrainian

- train_date: 2020-06-16

- src_alpha2: ca

- tgt_alpha2: uk

- prefer_old: False

- long_pair: cat-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41