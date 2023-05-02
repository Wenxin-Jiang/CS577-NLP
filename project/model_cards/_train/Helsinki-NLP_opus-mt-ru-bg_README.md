---
language: 
- ru
- bg

tags:
- translation

license: apache-2.0
---

### rus-bul

* source group: Russian 
* target group: Bulgarian 
*  OPUS readme: [rus-bul](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-bul/README.md)

*  model: transformer
* source language(s): rus
* target language(s): bul bul_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-bul/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-bul/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-bul/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.bul 	| 52.3 	| 0.704 |


### System Info: 
- hf_name: rus-bul

- source_languages: rus

- target_languages: bul

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-bul/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'bg']

- src_constituents: {'rus'}

- tgt_constituents: {'bul', 'bul_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-bul/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-bul/opus-2020-07-03.test.txt

- src_alpha3: rus

- tgt_alpha3: bul

- short_pair: ru-bg

- chrF2_score: 0.7040000000000001

- bleu: 52.3

- brevity_penalty: 0.919

- ref_len: 8272.0

- src_name: Russian

- tgt_name: Bulgarian

- train_date: 2020-07-03

- src_alpha2: ru

- tgt_alpha2: bg

- prefer_old: False

- long_pair: rus-bul

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41