---
language:
- af
- ru

tags:
- translation

license: apache-2.0
---
### af-ru

* source group: Afrikaans 
* target group: Russian 
*  OPUS readme: [afr-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afr-rus/README.md)

*  model: transformer-align
* source language(s): afr
* target language(s): rus
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-09-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/afr-rus/opus-2020-09-10.zip)
* test set translations: [opus-2020-09-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afr-rus/opus-2020-09-10.test.txt)
* test set scores: [opus-2020-09-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/afr-rus/opus-2020-09-10.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.afr.rus 	| 38.2 	| 0.580 |


### System Info: 
- hf_name: af-ru

- source_languages: afr

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/afr-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['af', 'ru']

- src_constituents: ('Afrikaans', {'afr'})

- tgt_constituents: ('Russian', {'rus'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: afr-rus

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/afr-rus/opus-2020-09-10.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/afr-rus/opus-2020-09-10.test.txt

- src_alpha3: afr

- tgt_alpha3: rus

- chrF2_score: 0.58

- bleu: 38.2

- brevity_penalty: 0.992

- ref_len: 1213

- src_name: Afrikaans

- tgt_name: Russian

- train_date: 2020-01-01 00:00:00

- src_alpha2: af

- tgt_alpha2: ru

- prefer_old: False

- short_pair: af-ru

- helsinki_git_sha: e8c308a96c1bd0b4ca6a8ce174783f93c3e30f25

- transformers_git_sha: 31245775e5772fbded1ac07ed89fbba3b5af0cb9

- port_machine: LM0-400-22516.local

- port_time: 2021-02-12-14:52