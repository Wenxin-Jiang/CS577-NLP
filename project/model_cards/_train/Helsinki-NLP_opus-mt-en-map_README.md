---
language: 
- en
- map

tags:
- translation

license: apache-2.0
---

### eng-map

* source group: English 
* target group: Austronesian languages 
*  OPUS readme: [eng-map](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-map/README.md)

*  model: transformer
* source language(s): eng
* target language(s): akl_Latn ceb cha dtp fij gil haw hil iba ilo ind jav jav_Java lkt mad mah max_Latn min mlg mri nau niu pag pau rap smo sun tah tet tmw_Latn ton tvl war zlm_Latn zsm_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-map/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-map/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-map/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-akl.eng.akl 	| 2.2 	| 0.103 |
| Tatoeba-test.eng-ceb.eng.ceb 	| 10.7 	| 0.425 |
| Tatoeba-test.eng-cha.eng.cha 	| 3.2 	| 0.201 |
| Tatoeba-test.eng-dtp.eng.dtp 	| 0.5 	| 0.120 |
| Tatoeba-test.eng-fij.eng.fij 	| 26.8 	| 0.453 |
| Tatoeba-test.eng-gil.eng.gil 	| 59.3 	| 0.762 |
| Tatoeba-test.eng-haw.eng.haw 	| 1.0 	| 0.116 |
| Tatoeba-test.eng-hil.eng.hil 	| 19.0 	| 0.517 |
| Tatoeba-test.eng-iba.eng.iba 	| 15.5 	| 0.400 |
| Tatoeba-test.eng-ilo.eng.ilo 	| 33.6 	| 0.591 |
| Tatoeba-test.eng-jav.eng.jav 	| 7.8 	| 0.301 |
| Tatoeba-test.eng-lkt.eng.lkt 	| 1.0 	| 0.064 |
| Tatoeba-test.eng-mad.eng.mad 	| 1.1 	| 0.142 |
| Tatoeba-test.eng-mah.eng.mah 	| 9.1 	| 0.374 |
| Tatoeba-test.eng-mlg.eng.mlg 	| 35.4 	| 0.526 |
| Tatoeba-test.eng-mri.eng.mri 	| 7.6 	| 0.309 |
| Tatoeba-test.eng-msa.eng.msa 	| 31.1 	| 0.565 |
| Tatoeba-test.eng.multi 	| 17.6 	| 0.411 |
| Tatoeba-test.eng-nau.eng.nau 	| 1.4 	| 0.098 |
| Tatoeba-test.eng-niu.eng.niu 	| 40.1 	| 0.560 |
| Tatoeba-test.eng-pag.eng.pag 	| 16.8 	| 0.526 |
| Tatoeba-test.eng-pau.eng.pau 	| 1.9 	| 0.139 |
| Tatoeba-test.eng-rap.eng.rap 	| 2.7 	| 0.090 |
| Tatoeba-test.eng-smo.eng.smo 	| 24.9 	| 0.453 |
| Tatoeba-test.eng-sun.eng.sun 	| 33.2 	| 0.439 |
| Tatoeba-test.eng-tah.eng.tah 	| 12.5 	| 0.278 |
| Tatoeba-test.eng-tet.eng.tet 	| 1.6 	| 0.140 |
| Tatoeba-test.eng-ton.eng.ton 	| 25.8 	| 0.530 |
| Tatoeba-test.eng-tvl.eng.tvl 	| 31.1 	| 0.523 |
| Tatoeba-test.eng-war.eng.war 	| 12.8 	| 0.436 |


### System Info: 
- hf_name: eng-map

- source_languages: eng

- target_languages: map

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-map/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'map']

- src_constituents: {'eng'}

- tgt_constituents: set()

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-map/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-map/opus-2020-07-27.test.txt

- src_alpha3: eng

- tgt_alpha3: map

- short_pair: en-map

- chrF2_score: 0.41100000000000003

- bleu: 17.6

- brevity_penalty: 1.0

- ref_len: 66963.0

- src_name: English

- tgt_name: Austronesian languages

- train_date: 2020-07-27

- src_alpha2: en

- tgt_alpha2: map

- prefer_old: False

- long_pair: eng-map

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41