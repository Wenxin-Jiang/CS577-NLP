---
language: 
- en
- vi
- km
- mkh

tags:
- translation

license: apache-2.0
---

### eng-mkh

* source group: English 
* target group: Mon-Khmer languages 
*  OPUS readme: [eng-mkh](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-mkh/README.md)

*  model: transformer
* source language(s): eng
* target language(s): kha khm khm_Latn mnw vie vie_Hani
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mkh/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mkh/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mkh/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-kha.eng.kha 	| 0.1 	| 0.015 |
| Tatoeba-test.eng-khm.eng.khm 	| 0.2 	| 0.226 |
| Tatoeba-test.eng-mnw.eng.mnw 	| 0.7 	| 0.003 |
| Tatoeba-test.eng.multi 	| 16.5 	| 0.330 |
| Tatoeba-test.eng-vie.eng.vie 	| 33.7 	| 0.513 |


### System Info: 
- hf_name: eng-mkh

- source_languages: eng

- target_languages: mkh

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-mkh/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'vi', 'km', 'mkh']

- src_constituents: {'eng'}

- tgt_constituents: {'vie_Hani', 'mnw', 'vie', 'kha', 'khm_Latn', 'khm'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mkh/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-mkh/opus-2020-07-27.test.txt

- src_alpha3: eng

- tgt_alpha3: mkh

- short_pair: en-mkh

- chrF2_score: 0.33

- bleu: 16.5

- brevity_penalty: 1.0

- ref_len: 34734.0

- src_name: English

- tgt_name: Mon-Khmer languages

- train_date: 2020-07-27

- src_alpha2: en

- tgt_alpha2: mkh

- prefer_old: False

- long_pair: eng-mkh

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41