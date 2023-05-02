---
language: 
- en
- hi

tags:
- translation

license: apache-2.0
---

### eng-hin

* source group: English 
* target group: Hindi 
*  OPUS readme: [eng-hin](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-hin/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): hin
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hin/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hin/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hin/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2014.eng.hin 	| 6.9 	| 0.296 |
| newstest2014-hien.eng.hin 	| 9.9 	| 0.323 |
| Tatoeba-test.eng.hin 	| 16.1 	| 0.447 |


### System Info: 
- hf_name: eng-hin

- source_languages: eng

- target_languages: hin

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-hin/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'hi']

- src_constituents: {'eng'}

- tgt_constituents: {'hin'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hin/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-hin/opus-2020-06-17.test.txt

- src_alpha3: eng

- tgt_alpha3: hin

- short_pair: en-hi

- chrF2_score: 0.447

- bleu: 16.1

- brevity_penalty: 1.0

- ref_len: 32904.0

- src_name: English

- tgt_name: Hindi

- train_date: 2020-06-17

- src_alpha2: en

- tgt_alpha2: hi

- prefer_old: False

- long_pair: eng-hin

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41