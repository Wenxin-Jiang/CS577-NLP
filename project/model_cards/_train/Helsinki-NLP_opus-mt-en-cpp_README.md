---
language: 
- en
- id
- cpp

tags:
- translation

license: apache-2.0
---

### eng-cpp

* source group: English 
* target group: Creoles and pidgins, Portuguese-based 
*  OPUS readme: [eng-cpp](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-cpp/README.md)

*  model: transformer
* source language(s): eng
* target language(s): ind max_Latn min pap tmw_Latn zlm_Latn zsm_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpp/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpp/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpp/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-msa.eng.msa 	| 32.6 	| 0.573 |
| Tatoeba-test.eng.multi 	| 32.7 	| 0.574 |
| Tatoeba-test.eng-pap.eng.pap 	| 42.5 	| 0.633 |


### System Info: 
- hf_name: eng-cpp

- source_languages: eng

- target_languages: cpp

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-cpp/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'id', 'cpp']

- src_constituents: {'eng'}

- tgt_constituents: {'zsm_Latn', 'ind', 'pap', 'min', 'tmw_Latn', 'max_Latn', 'zlm_Latn'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpp/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpp/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: cpp

- short_pair: en-cpp

- chrF2_score: 0.574

- bleu: 32.7

- brevity_penalty: 0.996

- ref_len: 34010.0

- src_name: English

- tgt_name: Creoles and pidgins, Portuguese-based

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: cpp

- prefer_old: False

- long_pair: eng-cpp

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41