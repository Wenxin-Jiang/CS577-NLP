---
language: 
- en
- tt
- cv
- tk
- tr
- ba
- trk

tags:
- translation

license: apache-2.0
---

### eng-trk

* source group: English 
* target group: Turkic languages 
*  OPUS readme: [eng-trk](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-trk/README.md)

*  model: transformer
* source language(s): eng
* target language(s): aze_Latn bak chv crh crh_Latn kaz_Cyrl kaz_Latn kir_Cyrl kjh kum ota_Arab ota_Latn sah tat tat_Arab tat_Latn tuk tuk_Latn tur tyv uig_Arab uig_Cyrl uzb_Cyrl uzb_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-trk/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-trk/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-trk/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2016-entr-engtur.eng.tur 	| 10.1 	| 0.437 |
| newstest2016-entr-engtur.eng.tur 	| 9.2 	| 0.410 |
| newstest2017-entr-engtur.eng.tur 	| 9.0 	| 0.410 |
| newstest2018-entr-engtur.eng.tur 	| 9.2 	| 0.413 |
| Tatoeba-test.eng-aze.eng.aze 	| 26.8 	| 0.577 |
| Tatoeba-test.eng-bak.eng.bak 	| 7.6 	| 0.308 |
| Tatoeba-test.eng-chv.eng.chv 	| 4.3 	| 0.270 |
| Tatoeba-test.eng-crh.eng.crh 	| 8.1 	| 0.330 |
| Tatoeba-test.eng-kaz.eng.kaz 	| 11.1 	| 0.359 |
| Tatoeba-test.eng-kir.eng.kir 	| 28.6 	| 0.524 |
| Tatoeba-test.eng-kjh.eng.kjh 	| 1.0 	| 0.041 |
| Tatoeba-test.eng-kum.eng.kum 	| 2.2 	| 0.075 |
| Tatoeba-test.eng.multi 	| 19.9 	| 0.455 |
| Tatoeba-test.eng-ota.eng.ota 	| 0.5 	| 0.065 |
| Tatoeba-test.eng-sah.eng.sah 	| 0.7 	| 0.030 |
| Tatoeba-test.eng-tat.eng.tat 	| 9.7 	| 0.316 |
| Tatoeba-test.eng-tuk.eng.tuk 	| 5.9 	| 0.317 |
| Tatoeba-test.eng-tur.eng.tur 	| 34.6 	| 0.623 |
| Tatoeba-test.eng-tyv.eng.tyv 	| 5.4 	| 0.210 |
| Tatoeba-test.eng-uig.eng.uig 	| 0.1 	| 0.155 |
| Tatoeba-test.eng-uzb.eng.uzb 	| 3.4 	| 0.275 |


### System Info: 
- hf_name: eng-trk

- source_languages: eng

- target_languages: trk

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-trk/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'tt', 'cv', 'tk', 'tr', 'ba', 'trk']

- src_constituents: {'eng'}

- tgt_constituents: {'kir_Cyrl', 'tat_Latn', 'tat', 'chv', 'uzb_Cyrl', 'kaz_Latn', 'aze_Latn', 'crh', 'kjh', 'uzb_Latn', 'ota_Arab', 'tuk_Latn', 'tuk', 'tat_Arab', 'sah', 'tyv', 'tur', 'uig_Arab', 'crh_Latn', 'kaz_Cyrl', 'uig_Cyrl', 'kum', 'ota_Latn', 'bak'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-trk/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-trk/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: trk

- short_pair: en-trk

- chrF2_score: 0.455

- bleu: 19.9

- brevity_penalty: 1.0

- ref_len: 57072.0

- src_name: English

- tgt_name: Turkic languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: trk

- prefer_old: False

- long_pair: eng-trk

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41