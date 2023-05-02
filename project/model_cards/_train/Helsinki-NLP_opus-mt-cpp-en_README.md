---
language: 
- id
- cpp
- en

tags:
- translation

license: apache-2.0
---

### cpp-eng

* source group: Creoles and pidgins, Portuguese-based 
* target group: English 
*  OPUS readme: [cpp-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cpp-eng/README.md)

*  model: transformer
* source language(s): ind max_Latn min pap tmw_Latn zlm_Latn zsm_Latn
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.msa-eng.msa.eng 	| 39.6 	| 0.580 |
| Tatoeba-test.multi.eng 	| 39.7 	| 0.580 |
| Tatoeba-test.pap-eng.pap.eng 	| 49.1 	| 0.579 |


### System Info: 
- hf_name: cpp-eng

- source_languages: cpp

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cpp-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['id', 'cpp', 'en']

- src_constituents: {'zsm_Latn', 'ind', 'pap', 'min', 'tmw_Latn', 'max_Latn', 'zlm_Latn'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-eng/opus2m-2020-07-31.test.txt

- src_alpha3: cpp

- tgt_alpha3: eng

- short_pair: cpp-en

- chrF2_score: 0.58

- bleu: 39.7

- brevity_penalty: 0.972

- ref_len: 37399.0

- src_name: Creoles and pidgins, Portuguese-based

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: cpp

- tgt_alpha2: en

- prefer_old: False

- long_pair: cpp-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41