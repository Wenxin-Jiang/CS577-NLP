---
language: 
- uk
- pt

tags:
- translation

license: apache-2.0
---

### ukr-por

* source group: Ukrainian 
* target group: Portuguese 
*  OPUS readme: [ukr-por](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-por/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): por
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-por/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-por/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-por/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.por 	| 38.1 	| 0.601 |


### System Info: 
- hf_name: ukr-por

- source_languages: ukr

- target_languages: por

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-por/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'pt']

- src_constituents: {'ukr'}

- tgt_constituents: {'por'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-por/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-por/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: por

- short_pair: uk-pt

- chrF2_score: 0.601

- bleu: 38.1

- brevity_penalty: 0.981

- ref_len: 21315.0

- src_name: Ukrainian

- tgt_name: Portuguese

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: pt

- prefer_old: False

- long_pair: ukr-por

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41