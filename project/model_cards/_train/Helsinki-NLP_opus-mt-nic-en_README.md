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
- nic
- en

tags:
- translation

license: apache-2.0
---

### nic-eng

* source group: Niger-Kordofanian languages 
* target group: English 
*  OPUS readme: [nic-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nic-eng/README.md)

*  model: transformer
* source language(s): bam_Latn ewe fuc fuv ibo kin lin lug nya run sag sna swh toi_Latn tso umb wol xho yor zul
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/nic-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nic-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/nic-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bam-eng.bam.eng 	| 2.4 	| 0.090 |
| Tatoeba-test.ewe-eng.ewe.eng 	| 10.3 	| 0.384 |
| Tatoeba-test.ful-eng.ful.eng 	| 1.2 	| 0.114 |
| Tatoeba-test.ibo-eng.ibo.eng 	| 7.5 	| 0.197 |
| Tatoeba-test.kin-eng.kin.eng 	| 30.7 	| 0.481 |
| Tatoeba-test.lin-eng.lin.eng 	| 3.1 	| 0.185 |
| Tatoeba-test.lug-eng.lug.eng 	| 3.1 	| 0.261 |
| Tatoeba-test.multi.eng 	| 21.3 	| 0.377 |
| Tatoeba-test.nya-eng.nya.eng 	| 31.6 	| 0.502 |
| Tatoeba-test.run-eng.run.eng 	| 24.9 	| 0.420 |
| Tatoeba-test.sag-eng.sag.eng 	| 5.2 	| 0.231 |
| Tatoeba-test.sna-eng.sna.eng 	| 20.1 	| 0.374 |
| Tatoeba-test.swa-eng.swa.eng 	| 4.6 	| 0.191 |
| Tatoeba-test.toi-eng.toi.eng 	| 4.8 	| 0.122 |
| Tatoeba-test.tso-eng.tso.eng 	| 100.0 	| 1.000 |
| Tatoeba-test.umb-eng.umb.eng 	| 9.0 	| 0.246 |
| Tatoeba-test.wol-eng.wol.eng 	| 14.0 	| 0.212 |
| Tatoeba-test.xho-eng.xho.eng 	| 38.2 	| 0.558 |
| Tatoeba-test.yor-eng.yor.eng 	| 21.2 	| 0.364 |
| Tatoeba-test.zul-eng.zul.eng 	| 42.3 	| 0.589 |


### System Info: 
- hf_name: nic-eng

- source_languages: nic

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/nic-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['sn', 'rw', 'wo', 'ig', 'sg', 'ee', 'zu', 'lg', 'ts', 'ln', 'ny', 'yo', 'rn', 'xh', 'nic', 'en']

- src_constituents: {'bam_Latn', 'sna', 'kin', 'wol', 'ibo', 'swh', 'sag', 'ewe', 'zul', 'fuc', 'lug', 'tso', 'lin', 'nya', 'yor', 'run', 'xho', 'fuv', 'toi_Latn', 'umb'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/nic-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/nic-eng/opus2m-2020-08-01.test.txt

- src_alpha3: nic

- tgt_alpha3: eng

- short_pair: nic-en

- chrF2_score: 0.377

- bleu: 21.3

- brevity_penalty: 1.0

- ref_len: 15228.0

- src_name: Niger-Kordofanian languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: nic

- tgt_alpha2: en

- prefer_old: False

- long_pair: nic-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41