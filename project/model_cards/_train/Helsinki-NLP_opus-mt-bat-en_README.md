---
language: 
- lt
- lv
- bat
- en

tags:
- translation

license: apache-2.0
---

### bat-eng

* source group: Baltic languages 
* target group: English 
*  OPUS readme: [bat-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bat-eng/README.md)

*  model: transformer
* source language(s): lav lit ltg prg_Latn sgs
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/bat-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bat-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bat-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2017-enlv-laveng.lav.eng 	| 27.5 	| 0.566 |
| newsdev2019-enlt-liteng.lit.eng 	| 27.8 	| 0.557 |
| newstest2017-enlv-laveng.lav.eng 	| 21.1 	| 0.512 |
| newstest2019-lten-liteng.lit.eng 	| 30.2 	| 0.592 |
| Tatoeba-test.lav-eng.lav.eng 	| 51.5 	| 0.687 |
| Tatoeba-test.lit-eng.lit.eng 	| 55.1 	| 0.703 |
| Tatoeba-test.multi.eng 	| 50.6 	| 0.662 |
| Tatoeba-test.prg-eng.prg.eng 	| 1.0 	| 0.159 |
| Tatoeba-test.sgs-eng.sgs.eng 	| 16.5 	| 0.265 |


### System Info: 
- hf_name: bat-eng

- source_languages: bat

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bat-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['lt', 'lv', 'bat', 'en']

- src_constituents: {'lit', 'lav', 'prg_Latn', 'ltg', 'sgs'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/bat-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/bat-eng/opus2m-2020-07-31.test.txt

- src_alpha3: bat

- tgt_alpha3: eng

- short_pair: bat-en

- chrF2_score: 0.662

- bleu: 50.6

- brevity_penalty: 0.9890000000000001

- ref_len: 30772.0

- src_name: Baltic languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: bat

- tgt_alpha2: en

- prefer_old: False

- long_pair: bat-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41