---
language: 
- ja
- ar

tags:
- translation

license: apache-2.0
---

### jpn-ara

* source group: Japanese 
* target group: Arabic 
*  OPUS readme: [jpn-ara](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-ara/README.md)

*  model: transformer-align
* source language(s): jpn_Hani jpn_Hira jpn_Kana
* target language(s): acm apc ara arq arz
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-ara/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-ara/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-ara/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.jpn.ara 	| 11.6 	| 0.394 |


### System Info: 
- hf_name: jpn-ara

- source_languages: jpn

- target_languages: ara

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-ara/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ja', 'ar']

- src_constituents: {'jpn_Hang', 'jpn', 'jpn_Yiii', 'jpn_Kana', 'jpn_Hani', 'jpn_Bopo', 'jpn_Latn', 'jpn_Hira'}

- tgt_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-ara/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-ara/opus-2020-06-17.test.txt

- src_alpha3: jpn

- tgt_alpha3: ara

- short_pair: ja-ar

- chrF2_score: 0.39399999999999996

- bleu: 11.6

- brevity_penalty: 1.0

- ref_len: 7089.0

- src_name: Japanese

- tgt_name: Arabic

- train_date: 2020-06-17

- src_alpha2: ja

- tgt_alpha2: ar

- prefer_old: False

- long_pair: jpn-ara

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41