---
language: 
- it
- uk

tags:
- translation

license: apache-2.0
---

### ita-ukr

* source group: Italian 
* target group: Ukrainian 
*  OPUS readme: [ita-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-ukr/README.md)

*  model: transformer-align
* source language(s): ita
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-ukr/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-ukr/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-ukr/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ita.ukr 	| 45.9 	| 0.657 |


### System Info: 
- hf_name: ita-ukr

- source_languages: ita

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['it', 'uk']

- src_constituents: {'ita'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-ukr/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-ukr/opus-2020-06-17.test.txt

- src_alpha3: ita

- tgt_alpha3: ukr

- short_pair: it-uk

- chrF2_score: 0.657

- bleu: 45.9

- brevity_penalty: 0.9890000000000001

- ref_len: 25353.0

- src_name: Italian

- tgt_name: Ukrainian

- train_date: 2020-06-17

- src_alpha2: it

- tgt_alpha2: uk

- prefer_old: False

- long_pair: ita-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41