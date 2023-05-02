---
language: 
- en
- sal

tags:
- translation

license: apache-2.0
---

### eng-sal

* source group: English 
* target group: Salishan languages 
*  OPUS readme: [eng-sal](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-sal/README.md)

*  model: transformer
* source language(s): eng
* target language(s): shs_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-14.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sal/opus-2020-07-14.zip)
* test set translations: [opus-2020-07-14.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sal/opus-2020-07-14.test.txt)
* test set scores: [opus-2020-07-14.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sal/opus-2020-07-14.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.multi 	| 32.6 	| 0.585 |
| Tatoeba-test.eng.shs 	| 1.1 	| 0.072 |
| Tatoeba-test.eng-shs.eng.shs 	| 1.2 	| 0.065 |


### System Info: 
- hf_name: eng-sal

- source_languages: eng

- target_languages: sal

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-sal/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'sal']

- src_constituents: {'eng'}

- tgt_constituents: {'shs_Latn'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sal/opus-2020-07-14.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sal/opus-2020-07-14.test.txt

- src_alpha3: eng

- tgt_alpha3: sal

- short_pair: en-sal

- chrF2_score: 0.07200000000000001

- bleu: 1.1

- brevity_penalty: 1.0

- ref_len: 199.0

- src_name: English

- tgt_name: Salishan languages

- train_date: 2020-07-14

- src_alpha2: en

- tgt_alpha2: sal

- prefer_old: False

- long_pair: eng-sal

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41