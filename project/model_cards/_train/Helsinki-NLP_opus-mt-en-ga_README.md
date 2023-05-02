---
language: 
- en
- ga

tags:
- translation

license: apache-2.0
---

### eng-gle

* source group: English 
* target group: Irish 
*  OPUS readme: [eng-gle](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-gle/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): gle
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gle/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gle/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gle/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.gle 	| 37.5 	| 0.593 |


### System Info: 
- hf_name: eng-gle

- source_languages: eng

- target_languages: gle

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-gle/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'ga']

- src_constituents: {'eng'}

- tgt_constituents: {'gle'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gle/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-gle/opus-2020-06-17.test.txt

- src_alpha3: eng

- tgt_alpha3: gle

- short_pair: en-ga

- chrF2_score: 0.593

- bleu: 37.5

- brevity_penalty: 1.0

- ref_len: 12200.0

- src_name: English

- tgt_name: Irish

- train_date: 2020-06-17

- src_alpha2: en

- tgt_alpha2: ga

- prefer_old: False

- long_pair: eng-gle

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41