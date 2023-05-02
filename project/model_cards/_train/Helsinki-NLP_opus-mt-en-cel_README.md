---
language: 
- en
- gd
- ga
- br
- kw
- gv
- cy
- cel

tags:
- translation

license: apache-2.0
---

### eng-cel

* source group: English 
* target group: Celtic languages 
*  OPUS readme: [eng-cel](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-cel/README.md)

*  model: transformer
* source language(s): eng
* target language(s): bre cor cym gla gle glv
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cel/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cel/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cel/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-bre.eng.bre 	| 11.5 	| 0.338 |
| Tatoeba-test.eng-cor.eng.cor 	| 0.3 	| 0.095 |
| Tatoeba-test.eng-cym.eng.cym 	| 31.0 	| 0.549 |
| Tatoeba-test.eng-gla.eng.gla 	| 7.6 	| 0.317 |
| Tatoeba-test.eng-gle.eng.gle 	| 35.9 	| 0.582 |
| Tatoeba-test.eng-glv.eng.glv 	| 9.9 	| 0.454 |
| Tatoeba-test.eng.multi 	| 18.0 	| 0.342 |


### System Info: 
- hf_name: eng-cel

- source_languages: eng

- target_languages: cel

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-cel/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'gd', 'ga', 'br', 'kw', 'gv', 'cy', 'cel']

- src_constituents: {'eng'}

- tgt_constituents: {'gla', 'gle', 'bre', 'cor', 'glv', 'cym'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cel/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cel/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: cel

- short_pair: en-cel

- chrF2_score: 0.342

- bleu: 18.0

- brevity_penalty: 0.9590000000000001

- ref_len: 45370.0

- src_name: English

- tgt_name: Celtic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: cel

- prefer_old: False

- long_pair: eng-cel

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41