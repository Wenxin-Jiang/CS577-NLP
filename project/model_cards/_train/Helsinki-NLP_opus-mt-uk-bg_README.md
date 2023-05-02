---
language: 
- uk
- bg

tags:
- translation

license: apache-2.0
---

### ukr-bul

* source group: Ukrainian 
* target group: Bulgarian 
*  OPUS readme: [ukr-bul](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-bul/README.md)

*  model: transformer-align
* source language(s): ukr
* target language(s): bul
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-bul/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-bul/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-bul/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ukr.bul 	| 55.7 	| 0.734 |


### System Info: 
- hf_name: ukr-bul

- source_languages: ukr

- target_languages: bul

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ukr-bul/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['uk', 'bg']

- src_constituents: {'ukr'}

- tgt_constituents: {'bul', 'bul_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-bul/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ukr-bul/opus-2020-06-17.test.txt

- src_alpha3: ukr

- tgt_alpha3: bul

- short_pair: uk-bg

- chrF2_score: 0.7340000000000001

- bleu: 55.7

- brevity_penalty: 0.976

- ref_len: 5181.0

- src_name: Ukrainian

- tgt_name: Bulgarian

- train_date: 2020-06-17

- src_alpha2: uk

- tgt_alpha2: bg

- prefer_old: False

- long_pair: ukr-bul

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41