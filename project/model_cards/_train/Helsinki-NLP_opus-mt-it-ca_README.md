---
language: 
- it
- ca

tags:
- translation

license: apache-2.0
---

### ita-cat

* source group: Italian 
* target group: Catalan 
*  OPUS readme: [ita-cat](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-cat/README.md)

*  model: transformer-align
* source language(s): ita
* target language(s): cat
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-cat/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-cat/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-cat/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ita.cat 	| 52.5 	| 0.706 |


### System Info: 
- hf_name: ita-cat

- source_languages: ita

- target_languages: cat

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-cat/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['it', 'ca']

- src_constituents: {'ita'}

- tgt_constituents: {'cat'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-cat/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-cat/opus-2020-06-16.test.txt

- src_alpha3: ita

- tgt_alpha3: cat

- short_pair: it-ca

- chrF2_score: 0.706

- bleu: 52.5

- brevity_penalty: 0.993

- ref_len: 2074.0

- src_name: Italian

- tgt_name: Catalan

- train_date: 2020-06-16

- src_alpha2: it

- tgt_alpha2: ca

- prefer_old: False

- long_pair: ita-cat

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41