---
language: 
- lo
- th
- taw
- en

tags:
- translation

license: apache-2.0
---

### taw-eng

* source group: Tai 
* target group: English 
*  OPUS readme: [taw-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/taw-eng/README.md)

*  model: transformer
* source language(s): lao tha
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-28.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/taw-eng/opus-2020-06-28.zip)
* test set translations: [opus-2020-06-28.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/taw-eng/opus-2020-06-28.test.txt)
* test set scores: [opus-2020-06-28.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/taw-eng/opus-2020-06-28.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.lao-eng.lao.eng 	| 1.1 	| 0.133 |
| Tatoeba-test.multi.eng 	| 38.9 	| 0.572 |
| Tatoeba-test.tha-eng.tha.eng 	| 40.6 	| 0.588 |


### System Info: 
- hf_name: taw-eng

- source_languages: taw

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/taw-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['lo', 'th', 'taw', 'en']

- src_constituents: {'lao', 'tha'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/taw-eng/opus-2020-06-28.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/taw-eng/opus-2020-06-28.test.txt

- src_alpha3: taw

- tgt_alpha3: eng

- short_pair: taw-en

- chrF2_score: 0.5720000000000001

- bleu: 38.9

- brevity_penalty: 1.0

- ref_len: 7630.0

- src_name: Tai

- tgt_name: English

- train_date: 2020-06-28

- src_alpha2: taw

- tgt_alpha2: en

- prefer_old: False

- long_pair: taw-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41