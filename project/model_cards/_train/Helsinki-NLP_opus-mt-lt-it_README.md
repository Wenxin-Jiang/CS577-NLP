---
language: 
- lt
- it

tags:
- translation

license: apache-2.0
---

### lit-ita

* source group: Lithuanian 
* target group: Italian 
*  OPUS readme: [lit-ita](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/lit-ita/README.md)

*  model: transformer-align
* source language(s): lit
* target language(s): ita
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/lit-ita/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/lit-ita/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/lit-ita/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.lit.ita 	| 42.2 	| 0.657 |


### System Info: 
- hf_name: lit-ita

- source_languages: lit

- target_languages: ita

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/lit-ita/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['lt', 'it']

- src_constituents: {'lit'}

- tgt_constituents: {'ita'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/lit-ita/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/lit-ita/opus-2020-06-17.test.txt

- src_alpha3: lit

- tgt_alpha3: ita

- short_pair: lt-it

- chrF2_score: 0.657

- bleu: 42.2

- brevity_penalty: 0.9740000000000001

- ref_len: 1505.0

- src_name: Lithuanian

- tgt_name: Italian

- train_date: 2020-06-17

- src_alpha2: lt

- tgt_alpha2: it

- prefer_old: False

- long_pair: lit-ita

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41