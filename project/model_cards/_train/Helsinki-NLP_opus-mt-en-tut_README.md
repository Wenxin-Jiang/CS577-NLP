---
language: 
- en
- tut

tags:
- translation

license: apache-2.0
---

### eng-tut

* source group: English 
* target group: Altaic languages 
*  OPUS readme: [eng-tut](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-tut/README.md)

*  model: transformer
* source language(s): eng
* target language(s): aze_Latn bak chv crh crh_Latn kaz_Cyrl kaz_Latn kir_Cyrl kjh kum mon nog ota_Arab ota_Latn sah tat tat_Arab tat_Latn tuk tuk_Latn tur tyv uig_Arab uig_Cyrl uzb_Cyrl uzb_Latn xal
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-02.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tut/opus2m-2020-08-02.zip)
* test set translations: [opus2m-2020-08-02.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tut/opus2m-2020-08-02.test.txt)
* test set scores: [opus2m-2020-08-02.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tut/opus2m-2020-08-02.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2016-entr-engtur.eng.tur 	| 10.4 	| 0.438 |
| newstest2016-entr-engtur.eng.tur 	| 9.1 	| 0.414 |
| newstest2017-entr-engtur.eng.tur 	| 9.5 	| 0.414 |
| newstest2018-entr-engtur.eng.tur 	| 9.5 	| 0.415 |
| Tatoeba-test.eng-aze.eng.aze 	| 27.2 	| 0.580 |
| Tatoeba-test.eng-bak.eng.bak 	| 5.8 	| 0.298 |
| Tatoeba-test.eng-chv.eng.chv 	| 4.6 	| 0.301 |
| Tatoeba-test.eng-crh.eng.crh 	| 6.5 	| 0.342 |
| Tatoeba-test.eng-kaz.eng.kaz 	| 11.8 	| 0.360 |
| Tatoeba-test.eng-kir.eng.kir 	| 24.6 	| 0.499 |
| Tatoeba-test.eng-kjh.eng.kjh 	| 2.2 	| 0.052 |
| Tatoeba-test.eng-kum.eng.kum 	| 8.0 	| 0.229 |
| Tatoeba-test.eng-mon.eng.mon 	| 10.3 	| 0.362 |
| Tatoeba-test.eng.multi 	| 19.5 	| 0.451 |
| Tatoeba-test.eng-nog.eng.nog 	| 1.5 	| 0.117 |
| Tatoeba-test.eng-ota.eng.ota 	| 0.2 	| 0.035 |
| Tatoeba-test.eng-sah.eng.sah 	| 0.7 	| 0.080 |
| Tatoeba-test.eng-tat.eng.tat 	| 10.8 	| 0.320 |
| Tatoeba-test.eng-tuk.eng.tuk 	| 5.6 	| 0.323 |
| Tatoeba-test.eng-tur.eng.tur 	| 34.2 	| 0.623 |
| Tatoeba-test.eng-tyv.eng.tyv 	| 8.1 	| 0.192 |
| Tatoeba-test.eng-uig.eng.uig 	| 0.1 	| 0.158 |
| Tatoeba-test.eng-uzb.eng.uzb 	| 4.2 	| 0.298 |
| Tatoeba-test.eng-xal.eng.xal 	| 0.1 	| 0.061 |


### System Info: 
- hf_name: eng-tut

- source_languages: eng

- target_languages: tut

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-tut/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'tut']

- src_constituents: {'eng'}

- tgt_constituents: set()

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tut/opus2m-2020-08-02.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tut/opus2m-2020-08-02.test.txt

- src_alpha3: eng

- tgt_alpha3: tut

- short_pair: en-tut

- chrF2_score: 0.451

- bleu: 19.5

- brevity_penalty: 1.0

- ref_len: 57472.0

- src_name: English

- tgt_name: Altaic languages

- train_date: 2020-08-02

- src_alpha2: en

- tgt_alpha2: tut

- prefer_old: False

- long_pair: eng-tut

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41