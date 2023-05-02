---
language: 
- en
- vi

tags:
- translation

license: apache-2.0
---

### eng-vie

* source group: English 
* target group: Vietnamese 
*  OPUS readme: [eng-vie](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-vie/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): vie vie_Hani
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-vie/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-vie/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-vie/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.vie 	| 37.2 	| 0.542 |


### System Info: 
- hf_name: eng-vie

- source_languages: eng

- target_languages: vie

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-vie/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'vi']

- src_constituents: {'eng'}

- tgt_constituents: {'vie', 'vie_Hani'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-vie/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-vie/opus-2020-06-17.test.txt

- src_alpha3: eng

- tgt_alpha3: vie

- short_pair: en-vi

- chrF2_score: 0.542

- bleu: 37.2

- brevity_penalty: 0.973

- ref_len: 24427.0

- src_name: English

- tgt_name: Vietnamese

- train_date: 2020-06-17

- src_alpha2: en

- tgt_alpha2: vi

- prefer_old: False

- long_pair: eng-vie

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41