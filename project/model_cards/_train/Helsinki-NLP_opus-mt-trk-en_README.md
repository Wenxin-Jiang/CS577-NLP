---
language: 
- tt
- cv
- tk
- tr
- ba
- trk
- en

tags:
- translation

license: apache-2.0
---

### trk-eng

* source group: Turkic languages 
* target group: English 
*  OPUS readme: [trk-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/trk-eng/README.md)

*  model: transformer
* source language(s): aze_Latn bak chv crh crh_Latn kaz_Cyrl kaz_Latn kir_Cyrl kjh kum ota_Arab ota_Latn sah tat tat_Arab tat_Latn tuk tuk_Latn tur tyv uig_Arab uig_Cyrl uzb_Cyrl uzb_Latn
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/trk-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/trk-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/trk-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2016-entr-tureng.tur.eng 	| 5.0 	| 0.242 |
| newstest2016-entr-tureng.tur.eng 	| 3.7 	| 0.231 |
| newstest2017-entr-tureng.tur.eng 	| 3.7 	| 0.229 |
| newstest2018-entr-tureng.tur.eng 	| 4.1 	| 0.230 |
| Tatoeba-test.aze-eng.aze.eng 	| 15.1 	| 0.330 |
| Tatoeba-test.bak-eng.bak.eng 	| 3.3 	| 0.185 |
| Tatoeba-test.chv-eng.chv.eng 	| 1.3 	| 0.161 |
| Tatoeba-test.crh-eng.crh.eng 	| 10.8 	| 0.325 |
| Tatoeba-test.kaz-eng.kaz.eng 	| 9.6 	| 0.264 |
| Tatoeba-test.kir-eng.kir.eng 	| 15.3 	| 0.328 |
| Tatoeba-test.kjh-eng.kjh.eng 	| 1.8 	| 0.121 |
| Tatoeba-test.kum-eng.kum.eng 	| 16.1 	| 0.277 |
| Tatoeba-test.multi.eng 	| 12.0 	| 0.304 |
| Tatoeba-test.ota-eng.ota.eng 	| 2.0 	| 0.149 |
| Tatoeba-test.sah-eng.sah.eng 	| 0.7 	| 0.140 |
| Tatoeba-test.tat-eng.tat.eng 	| 4.0 	| 0.215 |
| Tatoeba-test.tuk-eng.tuk.eng 	| 5.5 	| 0.243 |
| Tatoeba-test.tur-eng.tur.eng 	| 26.8 	| 0.443 |
| Tatoeba-test.tyv-eng.tyv.eng 	| 1.3 	| 0.111 |
| Tatoeba-test.uig-eng.uig.eng 	| 0.2 	| 0.111 |
| Tatoeba-test.uzb-eng.uzb.eng 	| 4.6 	| 0.195 |


### System Info: 
- hf_name: trk-eng

- source_languages: trk

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/trk-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['tt', 'cv', 'tk', 'tr', 'ba', 'trk', 'en']

- src_constituents: {'kir_Cyrl', 'tat_Latn', 'tat', 'chv', 'uzb_Cyrl', 'kaz_Latn', 'aze_Latn', 'crh', 'kjh', 'uzb_Latn', 'ota_Arab', 'tuk_Latn', 'tuk', 'tat_Arab', 'sah', 'tyv', 'tur', 'uig_Arab', 'crh_Latn', 'kaz_Cyrl', 'uig_Cyrl', 'kum', 'ota_Latn', 'bak'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/trk-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/trk-eng/opus2m-2020-08-01.test.txt

- src_alpha3: trk

- tgt_alpha3: eng

- short_pair: trk-en

- chrF2_score: 0.304

- bleu: 12.0

- brevity_penalty: 1.0

- ref_len: 18733.0

- src_name: Turkic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: trk

- tgt_alpha2: en

- prefer_old: False

- long_pair: trk-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41