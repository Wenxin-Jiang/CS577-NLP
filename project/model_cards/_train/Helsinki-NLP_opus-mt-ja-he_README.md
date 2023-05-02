---
language: 
- ja
- he

tags:
- translation

license: apache-2.0
---

### jpn-heb

* source group: Japanese 
* target group: Hebrew 
*  OPUS readme: [jpn-heb](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-heb/README.md)

*  model: transformer-align
* source language(s): jpn_Hani jpn_Hira jpn_Kana
* target language(s): heb
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-heb/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-heb/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-heb/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.jpn.heb 	| 20.2 	| 0.397 |


### System Info: 
- hf_name: jpn-heb

- source_languages: jpn

- target_languages: heb

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-heb/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ja', 'he']

- src_constituents: {'jpn_Hang', 'jpn', 'jpn_Yiii', 'jpn_Kana', 'jpn_Hani', 'jpn_Bopo', 'jpn_Latn', 'jpn_Hira'}

- tgt_constituents: {'heb'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-heb/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-heb/opus-2020-06-17.test.txt

- src_alpha3: jpn

- tgt_alpha3: heb

- short_pair: ja-he

- chrF2_score: 0.397

- bleu: 20.2

- brevity_penalty: 1.0

- ref_len: 1598.0

- src_name: Japanese

- tgt_name: Hebrew

- train_date: 2020-06-17

- src_alpha2: ja

- tgt_alpha2: he

- prefer_old: False

- long_pair: jpn-heb

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41