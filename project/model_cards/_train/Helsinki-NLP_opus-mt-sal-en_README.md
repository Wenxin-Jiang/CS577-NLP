---
language: 
- sal
- en

tags:
- translation

license: apache-2.0
---

### sal-eng

* source group: Salishan languages 
* target group: English 
*  OPUS readme: [sal-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sal-eng/README.md)

*  model: transformer
* source language(s): shs_Latn
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-14.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/sal-eng/opus-2020-07-14.zip)
* test set translations: [opus-2020-07-14.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sal-eng/opus-2020-07-14.test.txt)
* test set scores: [opus-2020-07-14.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/sal-eng/opus-2020-07-14.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.multi.eng 	| 38.7 	| 0.572 |
| Tatoeba-test.shs.eng 	| 2.2 	| 0.097 |
| Tatoeba-test.shs-eng.shs.eng 	| 2.2 	| 0.097 |


### System Info: 
- hf_name: sal-eng

- source_languages: sal

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/sal-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['sal', 'en']

- src_constituents: {'shs_Latn'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/sal-eng/opus-2020-07-14.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/sal-eng/opus-2020-07-14.test.txt

- src_alpha3: sal

- tgt_alpha3: eng

- short_pair: sal-en

- chrF2_score: 0.09699999999999999

- bleu: 2.2

- brevity_penalty: 0.8190000000000001

- ref_len: 222.0

- src_name: Salishan languages

- tgt_name: English

- train_date: 2020-07-14

- src_alpha2: sal

- tgt_alpha2: en

- prefer_old: False

- long_pair: sal-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41