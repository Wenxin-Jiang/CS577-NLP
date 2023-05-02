---
language: 
- war
- en

tags:
- translation

license: apache-2.0
---

### war-eng

* source group: Waray (Philippines) 
* target group: English 
*  OPUS readme: [war-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/war-eng/README.md)

*  model: transformer-align
* source language(s): war
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/war-eng/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/war-eng/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/war-eng/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.war.eng 	| 12.3 	| 0.308 |


### System Info: 
- hf_name: war-eng

- source_languages: war

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/war-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['war', 'en']

- src_constituents: {'war'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/war-eng/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/war-eng/opus-2020-06-16.test.txt

- src_alpha3: war

- tgt_alpha3: eng

- short_pair: war-en

- chrF2_score: 0.308

- bleu: 12.3

- brevity_penalty: 1.0

- ref_len: 11345.0

- src_name: Waray (Philippines)

- tgt_name: English

- train_date: 2020-06-16

- src_alpha2: war

- tgt_alpha2: en

- prefer_old: False

- long_pair: war-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41