---
language: 
- en
- vi
- km
- aav

tags:
- translation

license: apache-2.0
---

### eng-aav

* source group: English 
* target group: Austro-Asiatic languages 
*  OPUS readme: [eng-aav](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-aav/README.md)

*  model: transformer
* source language(s): eng
* target language(s): hoc hoc_Latn kha khm khm_Latn mnw vie vie_Hani
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aav/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aav/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aav/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-hoc.eng.hoc 	| 0.1 	| 0.033 |
| Tatoeba-test.eng-kha.eng.kha 	| 0.4 	| 0.043 |
| Tatoeba-test.eng-khm.eng.khm 	| 0.2 	| 0.242 |
| Tatoeba-test.eng-mnw.eng.mnw 	| 0.8 	| 0.003 |
| Tatoeba-test.eng.multi 	| 16.1 	| 0.311 |
| Tatoeba-test.eng-vie.eng.vie 	| 33.2 	| 0.508 |


### System Info: 
- hf_name: eng-aav

- source_languages: eng

- target_languages: aav

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-aav/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'vi', 'km', 'aav']

- src_constituents: {'eng'}

- tgt_constituents: {'mnw', 'vie', 'kha', 'khm', 'vie_Hani', 'khm_Latn', 'hoc_Latn', 'hoc'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aav/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-aav/opus-2020-07-26.test.txt

- src_alpha3: eng

- tgt_alpha3: aav

- short_pair: en-aav

- chrF2_score: 0.311

- bleu: 16.1

- brevity_penalty: 1.0

- ref_len: 38261.0

- src_name: English

- tgt_name: Austro-Asiatic languages

- train_date: 2020-07-26

- src_alpha2: en

- tgt_alpha2: aav

- prefer_old: False

- long_pair: eng-aav

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41