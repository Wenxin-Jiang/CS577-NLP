---
language: 
- euq
- en

tags:
- translation

license: apache-2.0
---

### euq-eng

* source group: Basque (family) 
* target group: English 
*  OPUS readme: [euq-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/euq-eng/README.md)

*  model: transformer
* source language(s): eus
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/euq-eng/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/euq-eng/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/euq-eng/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eus.eng 	| 41.5 	| 0.594 |
| Tatoeba-test.eus-eng.eus.eng 	| 41.5 	| 0.594 |


### System Info: 
- hf_name: euq-eng

- source_languages: euq

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/euq-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['euq', 'en']

- src_constituents: {'eus'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/euq-eng/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/euq-eng/opus-2020-07-26.test.txt

- src_alpha3: euq

- tgt_alpha3: eng

- short_pair: euq-en

- chrF2_score: 0.594

- bleu: 41.5

- brevity_penalty: 0.9640000000000001

- ref_len: 8157.0

- src_name: Basque (family)

- tgt_name: English

- train_date: 2020-07-26

- src_alpha2: euq

- tgt_alpha2: en

- prefer_old: False

- long_pair: euq-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41