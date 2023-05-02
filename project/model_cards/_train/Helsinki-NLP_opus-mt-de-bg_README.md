---
language: 
- de
- bg

tags:
- translation

license: apache-2.0
---

### deu-bul

* source group: German 
* target group: Bulgarian 
*  OPUS readme: [deu-bul](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-bul/README.md)

*  model: transformer
* source language(s): deu
* target language(s): bul
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-bul/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-bul/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-bul/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.deu.bul 	| 50.7 	| 0.683 |


### System Info: 
- hf_name: deu-bul

- source_languages: deu

- target_languages: bul

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-bul/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['de', 'bg']

- src_constituents: {'deu'}

- tgt_constituents: {'bul', 'bul_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-bul/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-bul/opus-2020-07-03.test.txt

- src_alpha3: deu

- tgt_alpha3: bul

- short_pair: de-bg

- chrF2_score: 0.6829999999999999

- bleu: 50.7

- brevity_penalty: 0.98

- ref_len: 2032.0

- src_name: German

- tgt_name: Bulgarian

- train_date: 2020-07-03

- src_alpha2: de

- tgt_alpha2: bg

- prefer_old: False

- long_pair: deu-bul

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41