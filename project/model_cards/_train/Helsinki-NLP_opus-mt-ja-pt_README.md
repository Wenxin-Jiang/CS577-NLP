---
language: 
- ja
- pt

tags:
- translation

license: apache-2.0
---

### jpn-por

* source group: Japanese 
* target group: Portuguese 
*  OPUS readme: [jpn-por](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-por/README.md)

*  model: transformer-align
* source language(s): jpn jpn_Hani jpn_Hira jpn_Kana jpn_Latn jpn_Yiii
* target language(s): por por_Hira
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-por/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-por/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-por/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.jpn.por 	| 22.2 	| 0.444 |


### System Info: 
- hf_name: jpn-por

- source_languages: jpn

- target_languages: por

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-por/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ja', 'pt']

- src_constituents: {'jpn_Hang', 'jpn', 'jpn_Yiii', 'jpn_Kana', 'jpn_Hani', 'jpn_Bopo', 'jpn_Latn', 'jpn_Hira'}

- tgt_constituents: {'por'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-por/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-por/opus-2020-06-17.test.txt

- src_alpha3: jpn

- tgt_alpha3: por

- short_pair: ja-pt

- chrF2_score: 0.444

- bleu: 22.2

- brevity_penalty: 0.922

- ref_len: 15570.0

- src_name: Japanese

- tgt_name: Portuguese

- train_date: 2020-06-17

- src_alpha2: ja

- tgt_alpha2: pt

- prefer_old: False

- long_pair: jpn-por

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41