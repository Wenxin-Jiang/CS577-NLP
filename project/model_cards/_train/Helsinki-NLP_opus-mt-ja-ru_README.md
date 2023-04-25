---
language: 
- ja
- ru

tags:
- translation

license: apache-2.0
---

### jpn-rus

* source group: Japanese 
* target group: Russian 
*  OPUS readme: [jpn-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-rus/README.md)

*  model: transformer-align
* source language(s): jpn jpn_Bopo jpn_Hani jpn_Hira jpn_Kana jpn_Latn jpn_Yiii
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-rus/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-rus/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-rus/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.jpn.rus 	| 23.2 	| 0.441 |


### System Info: 
- hf_name: jpn-rus

- source_languages: jpn

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ja', 'ru']

- src_constituents: {'jpn_Hang', 'jpn', 'jpn_Yiii', 'jpn_Kana', 'jpn_Hani', 'jpn_Bopo', 'jpn_Latn', 'jpn_Hira'}

- tgt_constituents: {'rus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-rus/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-rus/opus-2020-06-17.test.txt

- src_alpha3: jpn

- tgt_alpha3: rus

- short_pair: ja-ru

- chrF2_score: 0.441

- bleu: 23.2

- brevity_penalty: 0.9740000000000001

- ref_len: 70820.0

- src_name: Japanese

- tgt_name: Russian

- train_date: 2020-06-17

- src_alpha2: ja

- tgt_alpha2: ru

- prefer_old: False

- long_pair: jpn-rus

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41