---
language: 
- en
- bg

tags:
- translation

license: apache-2.0
---

### eng-bul

* source group: English 
* target group: Bulgarian 
*  OPUS readme: [eng-bul](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-bul/README.md)

*  model: transformer
* source language(s): eng
* target language(s): bul bul_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bul/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bul/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bul/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.bul 	| 50.6 	| 0.680 |


### System Info: 
- hf_name: eng-bul

- source_languages: eng

- target_languages: bul

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-bul/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'bg']

- src_constituents: {'eng'}

- tgt_constituents: {'bul', 'bul_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bul/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bul/opus-2020-07-03.test.txt

- src_alpha3: eng

- tgt_alpha3: bul

- short_pair: en-bg

- chrF2_score: 0.68

- bleu: 50.6

- brevity_penalty: 0.96

- ref_len: 69504.0

- src_name: English

- tgt_name: Bulgarian

- train_date: 2020-07-03

- src_alpha2: en

- tgt_alpha2: bg

- prefer_old: False

- long_pair: eng-bul

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41