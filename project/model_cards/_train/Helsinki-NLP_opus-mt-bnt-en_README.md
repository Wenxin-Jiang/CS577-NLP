---
language: 
- sn
- zu
- rw
- lg
- ts
- ln
- ny
- xh
- rn
- bnt
- en

tags:
- translation

license: apache-2.0
---

### bnt-eng

* source group: Bantu languages 
* target group: English 
*  OPUS readme: [bnt-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bnt-eng/README.md)

*  model: transformer
* source language(s): kin lin lug nya run sna swh toi_Latn tso umb xho zul
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/bnt-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bnt-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bnt-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.kin-eng.kin.eng 	| 31.7 	| 0.481 |
| Tatoeba-test.lin-eng.lin.eng 	| 8.3 	| 0.271 |
| Tatoeba-test.lug-eng.lug.eng 	| 5.3 	| 0.128 |
| Tatoeba-test.multi.eng 	| 23.1 	| 0.394 |
| Tatoeba-test.nya-eng.nya.eng 	| 38.3 	| 0.527 |
| Tatoeba-test.run-eng.run.eng 	| 26.6 	| 0.431 |
| Tatoeba-test.sna-eng.sna.eng 	| 27.5 	| 0.440 |
| Tatoeba-test.swa-eng.swa.eng 	| 4.6 	| 0.195 |
| Tatoeba-test.toi-eng.toi.eng 	| 16.2 	| 0.342 |
| Tatoeba-test.tso-eng.tso.eng 	| 100.0 	| 1.000 |
| Tatoeba-test.umb-eng.umb.eng 	| 8.4 	| 0.231 |
| Tatoeba-test.xho-eng.xho.eng 	| 37.2 	| 0.554 |
| Tatoeba-test.zul-eng.zul.eng 	| 40.9 	| 0.576 |


### System Info: 
- hf_name: bnt-eng

- source_languages: bnt

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bnt-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['sn', 'zu', 'rw', 'lg', 'ts', 'ln', 'ny', 'xh', 'rn', 'bnt', 'en']

- src_constituents: {'sna', 'zul', 'kin', 'lug', 'tso', 'lin', 'nya', 'xho', 'swh', 'run', 'toi_Latn', 'umb'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/bnt-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/bnt-eng/opus2m-2020-07-31.test.txt

- src_alpha3: bnt

- tgt_alpha3: eng

- short_pair: bnt-en

- chrF2_score: 0.39399999999999996

- bleu: 23.1

- brevity_penalty: 1.0

- ref_len: 14565.0

- src_name: Bantu languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: bnt

- tgt_alpha2: en

- prefer_old: False

- long_pair: bnt-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41