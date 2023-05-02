---
language: 
- de
- vi

tags:
- translation

license: apache-2.0
---

### deu-vie

* source group: German 
* target group: Vietnamese 
*  OPUS readme: [deu-vie](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-vie/README.md)

*  model: transformer-align
* source language(s): deu
* target language(s): vie
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-vie/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-vie/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-vie/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.deu.vie 	| 25.0 	| 0.443 |


### System Info: 
- hf_name: deu-vie

- source_languages: deu

- target_languages: vie

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-vie/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['de', 'vi']

- src_constituents: {'deu'}

- tgt_constituents: {'vie', 'vie_Hani'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-vie/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-vie/opus-2020-06-17.test.txt

- src_alpha3: deu

- tgt_alpha3: vie

- short_pair: de-vi

- chrF2_score: 0.44299999999999995

- bleu: 25.0

- brevity_penalty: 1.0

- ref_len: 3768.0

- src_name: German

- tgt_name: Vietnamese

- train_date: 2020-06-17

- src_alpha2: de

- tgt_alpha2: vi

- prefer_old: False

- long_pair: deu-vie

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41