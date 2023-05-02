---
language: 
- en
- phi

tags:
- translation

license: apache-2.0
---

### eng-phi

* source group: English 
* target group: Philippine languages 
*  OPUS readme: [eng-phi](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-phi/README.md)

*  model: transformer
* source language(s): eng
* target language(s): akl_Latn ceb hil ilo pag war
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-phi/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-phi/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-phi/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-akl.eng.akl 	| 7.1 	| 0.245 |
| Tatoeba-test.eng-ceb.eng.ceb 	| 10.5 	| 0.435 |
| Tatoeba-test.eng-hil.eng.hil 	| 18.0 	| 0.506 |
| Tatoeba-test.eng-ilo.eng.ilo 	| 33.4 	| 0.590 |
| Tatoeba-test.eng.multi 	| 13.1 	| 0.392 |
| Tatoeba-test.eng-pag.eng.pag 	| 19.4 	| 0.481 |
| Tatoeba-test.eng-war.eng.war 	| 12.8 	| 0.441 |


### System Info: 
- hf_name: eng-phi

- source_languages: eng

- target_languages: phi

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-phi/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'phi']

- src_constituents: {'eng'}

- tgt_constituents: {'ilo', 'akl_Latn', 'war', 'hil', 'pag', 'ceb'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-phi/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-phi/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: phi

- short_pair: en-phi

- chrF2_score: 0.392

- bleu: 13.1

- brevity_penalty: 1.0

- ref_len: 30022.0

- src_name: English

- tgt_name: Philippine languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: phi

- prefer_old: False

- long_pair: eng-phi

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41