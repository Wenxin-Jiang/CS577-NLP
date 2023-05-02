---
language: 
- bg
- eo

tags:
- translation

license: apache-2.0
---

### bul-epo

* source group: Bulgarian 
* target group: Esperanto 
*  OPUS readme: [bul-epo](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-epo/README.md)

*  model: transformer-align
* source language(s): bul
* target language(s): epo
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-epo/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-epo/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-epo/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bul.epo 	| 24.5 	| 0.438 |


### System Info: 
- hf_name: bul-epo

- source_languages: bul

- target_languages: epo

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-epo/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bg', 'eo']

- src_constituents: {'bul', 'bul_Latn'}

- tgt_constituents: {'epo'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-epo/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-epo/opus-2020-06-16.test.txt

- src_alpha3: bul

- tgt_alpha3: epo

- short_pair: bg-eo

- chrF2_score: 0.43799999999999994

- bleu: 24.5

- brevity_penalty: 0.9670000000000001

- ref_len: 4043.0

- src_name: Bulgarian

- tgt_name: Esperanto

- train_date: 2020-06-16

- src_alpha2: bg

- tgt_alpha2: eo

- prefer_old: False

- long_pair: bul-epo

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41