---
language: 
- fi
- en

tags:
- translation

license: apache-2.0
---

### fin-eng

* source group: Finnish 
* target group: English 
*  OPUS readme: [fin-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-eng/README.md)

*  model: transformer-align
* source language(s): fin
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-08-05.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opus-2020-08-05.zip)
* test set translations: [opus-2020-08-05.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opus-2020-08-05.test.txt)
* test set scores: [opus-2020-08-05.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opus-2020-08-05.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2015-enfi-fineng.fin.eng 	| 25.3 	| 0.536 |
| newstest2015-enfi-fineng.fin.eng 	| 26.9 	| 0.547 |
| newstest2016-enfi-fineng.fin.eng 	| 29.0 	| 0.571 |
| newstest2017-enfi-fineng.fin.eng 	| 32.3 	| 0.594 |
| newstest2018-enfi-fineng.fin.eng 	| 23.8 	| 0.517 |
| newstest2019-fien-fineng.fin.eng 	| 29.0 	| 0.565 |
| newstestB2016-enfi-fineng.fin.eng 	| 24.5 	| 0.527 |
| newstestB2017-enfi-fineng.fin.eng 	| 27.4 	| 0.557 |
| newstestB2017-fien-fineng.fin.eng 	| 27.4 	| 0.557 |
| Tatoeba-test.fin.eng 	| 53.4 	| 0.697 |


### System Info: 
- hf_name: fin-eng

- source_languages: fin

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['fi', 'en']

- src_constituents: {'fin'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opus-2020-08-05.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opus-2020-08-05.test.txt

- src_alpha3: fin

- tgt_alpha3: eng

- short_pair: fi-en

- chrF2_score: 0.6970000000000001

- bleu: 53.4

- brevity_penalty: 0.99

- ref_len: 74651.0

- src_name: Finnish

- tgt_name: English

- train_date: 2020-08-05

- src_alpha2: fi

- tgt_alpha2: en

- prefer_old: False

- long_pair: fin-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41