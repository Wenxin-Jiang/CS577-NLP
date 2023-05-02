---
language: 
- en
- pqw

tags:
- translation

license: apache-2.0
---

### eng-pqw

* source group: English 
* target group: Western Malayo-Polynesian languages 
*  OPUS readme: [eng-pqw](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-pqw/README.md)

*  model: transformer
* source language(s): eng
* target language(s): akl_Latn ceb cha dtp hil iba ilo ind jav jav_Java mad max_Latn min mlg pag pau sun tmw_Latn war zlm_Latn zsm_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqw/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqw/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqw/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-akl.eng.akl 	| 3.0 	| 0.143 |
| Tatoeba-test.eng-ceb.eng.ceb 	| 11.4 	| 0.432 |
| Tatoeba-test.eng-cha.eng.cha 	| 1.4 	| 0.189 |
| Tatoeba-test.eng-dtp.eng.dtp 	| 0.6 	| 0.139 |
| Tatoeba-test.eng-hil.eng.hil 	| 17.7 	| 0.525 |
| Tatoeba-test.eng-iba.eng.iba 	| 14.6 	| 0.365 |
| Tatoeba-test.eng-ilo.eng.ilo 	| 34.0 	| 0.590 |
| Tatoeba-test.eng-jav.eng.jav 	| 6.2 	| 0.299 |
| Tatoeba-test.eng-mad.eng.mad 	| 2.6 	| 0.154 |
| Tatoeba-test.eng-mlg.eng.mlg 	| 34.3 	| 0.518 |
| Tatoeba-test.eng-msa.eng.msa 	| 31.1 	| 0.561 |
| Tatoeba-test.eng.multi 	| 17.5 	| 0.422 |
| Tatoeba-test.eng-pag.eng.pag 	| 19.8 	| 0.507 |
| Tatoeba-test.eng-pau.eng.pau 	| 1.2 	| 0.129 |
| Tatoeba-test.eng-sun.eng.sun 	| 30.3 	| 0.418 |
| Tatoeba-test.eng-war.eng.war 	| 12.6 	| 0.439 |


### System Info: 
- hf_name: eng-pqw

- source_languages: eng

- target_languages: pqw

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-pqw/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'pqw']

- src_constituents: {'eng'}

- tgt_constituents: set()

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqw/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqw/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: pqw

- short_pair: en-pqw

- chrF2_score: 0.42200000000000004

- bleu: 17.5

- brevity_penalty: 1.0

- ref_len: 66758.0

- src_name: English

- tgt_name: Western Malayo-Polynesian languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: pqw

- prefer_old: False

- long_pair: eng-pqw

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41