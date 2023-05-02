---
language: 
- gd
- ga
- br
- kw
- gv
- cy
- cel
- en

tags:
- translation

license: apache-2.0
---

### cel-eng

* source group: Celtic languages 
* target group: English 
*  OPUS readme: [cel-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cel-eng/README.md)

*  model: transformer
* source language(s): bre cor cym gla gle glv
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cel-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cel-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cel-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bre-eng.bre.eng 	| 17.2 	| 0.385 |
| Tatoeba-test.cor-eng.cor.eng 	| 3.0 	| 0.172 |
| Tatoeba-test.cym-eng.cym.eng 	| 41.5 	| 0.582 |
| Tatoeba-test.gla-eng.gla.eng 	| 15.4 	| 0.330 |
| Tatoeba-test.gle-eng.gle.eng 	| 50.8 	| 0.668 |
| Tatoeba-test.glv-eng.glv.eng 	| 11.0 	| 0.297 |
| Tatoeba-test.multi.eng 	| 22.8 	| 0.398 |


### System Info: 
- hf_name: cel-eng

- source_languages: cel

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cel-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['gd', 'ga', 'br', 'kw', 'gv', 'cy', 'cel', 'en']

- src_constituents: {'gla', 'gle', 'bre', 'cor', 'glv', 'cym'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cel-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cel-eng/opus2m-2020-07-31.test.txt

- src_alpha3: cel

- tgt_alpha3: eng

- short_pair: cel-en

- chrF2_score: 0.39799999999999996

- bleu: 22.8

- brevity_penalty: 1.0

- ref_len: 42097.0

- src_name: Celtic languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: cel

- tgt_alpha2: en

- prefer_old: False

- long_pair: cel-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41