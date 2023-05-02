---
language: 
- sn
- rw
- wo
- ig
- sg
- ee
- zu
- lg
- ts
- ln
- ny
- yo
- rn
- xh
- alv
- en

tags:
- translation

license: apache-2.0
---

### alv-eng

* source group: Atlantic-Congo languages 
* target group: English 
*  OPUS readme: [alv-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/alv-eng/README.md)

*  model: transformer
* source language(s): ewe fuc fuv ibo kin lin lug nya run sag sna swh toi_Latn tso umb wol xho yor zul
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/alv-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/alv-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/alv-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ewe-eng.ewe.eng 	| 6.3 	| 0.328 |
| Tatoeba-test.ful-eng.ful.eng 	| 0.4 	| 0.108 |
| Tatoeba-test.ibo-eng.ibo.eng 	| 4.5 	| 0.196 |
| Tatoeba-test.kin-eng.kin.eng 	| 30.7 	| 0.511 |
| Tatoeba-test.lin-eng.lin.eng 	| 2.8 	| 0.213 |
| Tatoeba-test.lug-eng.lug.eng 	| 3.4 	| 0.140 |
| Tatoeba-test.multi.eng 	| 20.9 	| 0.376 |
| Tatoeba-test.nya-eng.nya.eng 	| 38.7 	| 0.492 |
| Tatoeba-test.run-eng.run.eng 	| 24.5 	| 0.417 |
| Tatoeba-test.sag-eng.sag.eng 	| 5.5 	| 0.177 |
| Tatoeba-test.sna-eng.sna.eng 	| 26.9 	| 0.412 |
| Tatoeba-test.swa-eng.swa.eng 	| 4.9 	| 0.196 |
| Tatoeba-test.toi-eng.toi.eng 	| 3.9 	| 0.147 |
| Tatoeba-test.tso-eng.tso.eng 	| 76.7 	| 0.957 |
| Tatoeba-test.umb-eng.umb.eng 	| 4.0 	| 0.195 |
| Tatoeba-test.wol-eng.wol.eng 	| 3.7 	| 0.170 |
| Tatoeba-test.xho-eng.xho.eng 	| 38.9 	| 0.556 |
| Tatoeba-test.yor-eng.yor.eng 	| 25.1 	| 0.412 |
| Tatoeba-test.zul-eng.zul.eng 	| 46.1 	| 0.623 |


### System Info: 
- hf_name: alv-eng

- source_languages: alv

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/alv-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['sn', 'rw', 'wo', 'ig', 'sg', 'ee', 'zu', 'lg', 'ts', 'ln', 'ny', 'yo', 'rn', 'xh', 'alv', 'en']

- src_constituents: {'sna', 'kin', 'wol', 'ibo', 'swh', 'sag', 'ewe', 'zul', 'fuc', 'lug', 'tso', 'lin', 'nya', 'yor', 'run', 'xho', 'fuv', 'toi_Latn', 'umb'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/alv-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/alv-eng/opus2m-2020-07-31.test.txt

- src_alpha3: alv

- tgt_alpha3: eng

- short_pair: alv-en

- chrF2_score: 0.376

- bleu: 20.9

- brevity_penalty: 1.0

- ref_len: 15208.0

- src_name: Atlantic-Congo languages

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: alv

- tgt_alpha2: en

- prefer_old: False

- long_pair: alv-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41