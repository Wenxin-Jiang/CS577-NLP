---
language: 
- en
- ar

tags:
- translation

license: apache-2.0
---

### eng-ara

* source group: English 
* target group: Arabic 
*  OPUS readme: [eng-ara](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-ara/README.md)

*  model: transformer
* source language(s): eng
* target language(s): acm afb apc apc_Latn ara ara_Latn arq arq_Latn ary arz
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.ara 	| 14.0 	| 0.437 |


### System Info: 
- hf_name: eng-ara

- source_languages: eng

- target_languages: ara

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-ara/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'ar']

- src_constituents: {'eng'}

- tgt_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opus-2020-07-03.test.txt

- src_alpha3: eng

- tgt_alpha3: ara

- short_pair: en-ar

- chrF2_score: 0.43700000000000006

- bleu: 14.0

- brevity_penalty: 1.0

- ref_len: 58935.0

- src_name: English

- tgt_name: Arabic

- train_date: 2020-07-03

- src_alpha2: en

- tgt_alpha2: ar

- prefer_old: False

- long_pair: eng-ara

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41