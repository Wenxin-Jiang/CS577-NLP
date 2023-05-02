---
language: 
- uk
- it

tags:
- translation

license: apache-2.0
---

### ukr-ita

* source group: Ukrainian 
* target group: Italian 
*  OPUS readme: [ukr-ita](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-ita/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): ita
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ita/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ita/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ita/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.ita 	| 46.0 	| 0.662 |


### System Info: 
- hf_name: ukr-ita

- source_languages: ukr

- target_languages: ita

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-ita/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'it']

- src_constituents: {'ukr'}

- tgt_constituents: {'ita'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ita/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-ita/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: ita

- short_pair: uk-it

- chrF2_score: 0.662

- bleu: 46.0

- brevity_penalty: 0.9490000000000001

- ref_len: 27846.0

- src_name: Ukrainian

- tgt_name: Italian

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: it

- prefer_old: False

- long_pair: ukr-ita

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41