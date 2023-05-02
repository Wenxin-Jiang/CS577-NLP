---
language: 
- en
- euq

tags:
- translation

license: apache-2.0
---

### eng-euq

* source group: English 
* target group: Basque (family) 
*  OPUS readme: [eng-euq](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-euq/README.md)

*  model: transformer
* source language(s): eng
* target language(s): eus
* model: transformer
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-euq/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-euq/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-euq/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.eus 	| 27.9 	| 0.555 |
| Tatoeba-test.eng-eus.eng.eus 	| 27.9 	| 0.555 |


### System Info: 
- hf_name: eng-euq

- source_languages: eng

- target_languages: euq

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-euq/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'euq']

- src_constituents: {'eng'}

- tgt_constituents: {'eus'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-euq/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-euq/opus-2020-07-26.test.txt

- src_alpha3: eng

- tgt_alpha3: euq

- short_pair: en-euq

- chrF2_score: 0.555

- bleu: 27.9

- brevity_penalty: 0.917

- ref_len: 7080.0

- src_name: English

- tgt_name: Basque (family)

- train_date: 2020-07-26

- src_alpha2: en

- tgt_alpha2: euq

- prefer_old: False

- long_pair: eng-euq

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41