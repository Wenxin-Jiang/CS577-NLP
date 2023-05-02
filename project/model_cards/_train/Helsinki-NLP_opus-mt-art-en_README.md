---
language: 
- eo
- io
- art
- en

tags:
- translation

license: apache-2.0
---

### art-eng

* source group: Artificial languages 
* target group: English 
*  OPUS readme: [art-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/art-eng/README.md)

*  model: transformer
* source language(s): afh_Latn avk_Latn dws_Latn epo ido ido_Latn ile_Latn ina_Latn jbo jbo_Cyrl jbo_Latn ldn_Latn lfn_Cyrl lfn_Latn nov_Latn qya qya_Latn sjn_Latn tlh_Latn tzl tzl_Latn vol_Latn
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/art-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/art-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/art-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.afh-eng.afh.eng 	| 1.2 	| 0.099 |
| Tatoeba-test.avk-eng.avk.eng 	| 0.4 	| 0.105 |
| Tatoeba-test.dws-eng.dws.eng 	| 1.6 	| 0.076 |
| Tatoeba-test.epo-eng.epo.eng 	| 34.6 	| 0.530 |
| Tatoeba-test.ido-eng.ido.eng 	| 12.7 	| 0.310 |
| Tatoeba-test.ile-eng.ile.eng 	| 4.6 	| 0.218 |
| Tatoeba-test.ina-eng.ina.eng 	| 5.8 	| 0.254 |
| Tatoeba-test.jbo-eng.jbo.eng 	| 0.2 	| 0.115 |
| Tatoeba-test.ldn-eng.ldn.eng 	| 0.7 	| 0.083 |
| Tatoeba-test.lfn-eng.lfn.eng 	| 1.8 	| 0.172 |
| Tatoeba-test.multi.eng 	| 11.6 	| 0.287 |
| Tatoeba-test.nov-eng.nov.eng 	| 5.1 	| 0.215 |
| Tatoeba-test.qya-eng.qya.eng 	| 0.7 	| 0.113 |
| Tatoeba-test.sjn-eng.sjn.eng 	| 0.9 	| 0.090 |
| Tatoeba-test.tlh-eng.tlh.eng 	| 0.2 	| 0.124 |
| Tatoeba-test.tzl-eng.tzl.eng 	| 1.4 	| 0.109 |
| Tatoeba-test.vol-eng.vol.eng 	| 0.5 	| 0.115 |


### System Info: 
- hf_name: art-eng

- source_languages: art

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/art-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eo', 'io', 'art', 'en']

- src_constituents: {'sjn_Latn', 'tzl', 'vol_Latn', 'qya', 'tlh_Latn', 'ile_Latn', 'ido_Latn', 'tzl_Latn', 'jbo_Cyrl', 'jbo', 'lfn_Latn', 'nov_Latn', 'dws_Latn', 'ldn_Latn', 'avk_Latn', 'lfn_Cyrl', 'ina_Latn', 'jbo_Latn', 'epo', 'afh_Latn', 'qya_Latn', 'ido'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/art-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/art-eng/opus2m-2020-07-31.test.txt

- src_alpha3: art

- tgt_alpha3: eng

- short_pair: art-en

- chrF2_score: 0.287

- bleu: 11.6

- brevity_penalty: 1.0

- ref_len: 73037.0

- src_name: Artificial languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: art

- tgt_alpha2: en

- prefer_old: False

- long_pair: art-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41