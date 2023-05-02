---
language: 
- en
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

tags:
- translation

license: apache-2.0
---

### eng-alv

* source group: English 
* target group: Atlantic-Congo languages 
*  OPUS readme: [eng-alv](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-alv/README.md)

*  model: transformer
* source language(s): eng
* target language(s): ewe fuc fuv ibo kin lin lug nya run sag sna swh toi_Latn tso umb wol xho yor zul
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-alv/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-alv/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-alv/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-ewe.eng.ewe 	| 4.9 	| 0.212 |
| Tatoeba-test.eng-ful.eng.ful 	| 0.6 	| 0.079 |
| Tatoeba-test.eng-ibo.eng.ibo 	| 3.5 	| 0.255 |
| Tatoeba-test.eng-kin.eng.kin 	| 10.5 	| 0.510 |
| Tatoeba-test.eng-lin.eng.lin 	| 1.1 	| 0.273 |
| Tatoeba-test.eng-lug.eng.lug 	| 5.3 	| 0.340 |
| Tatoeba-test.eng.multi 	| 11.4 	| 0.429 |
| Tatoeba-test.eng-nya.eng.nya 	| 18.1 	| 0.595 |
| Tatoeba-test.eng-run.eng.run 	| 13.9 	| 0.484 |
| Tatoeba-test.eng-sag.eng.sag 	| 5.3 	| 0.194 |
| Tatoeba-test.eng-sna.eng.sna 	| 26.2 	| 0.623 |
| Tatoeba-test.eng-swa.eng.swa 	| 1.0 	| 0.141 |
| Tatoeba-test.eng-toi.eng.toi 	| 7.0 	| 0.224 |
| Tatoeba-test.eng-tso.eng.tso 	| 46.7 	| 0.643 |
| Tatoeba-test.eng-umb.eng.umb 	| 7.8 	| 0.359 |
| Tatoeba-test.eng-wol.eng.wol 	| 6.8 	| 0.191 |
| Tatoeba-test.eng-xho.eng.xho 	| 27.1 	| 0.629 |
| Tatoeba-test.eng-yor.eng.yor 	| 17.4 	| 0.356 |
| Tatoeba-test.eng-zul.eng.zul 	| 34.1 	| 0.729 |


### System Info: 
- hf_name: eng-alv

- source_languages: eng

- target_languages: alv

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-alv/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'sn', 'rw', 'wo', 'ig', 'sg', 'ee', 'zu', 'lg', 'ts', 'ln', 'ny', 'yo', 'rn', 'xh', 'alv']

- src_constituents: {'eng'}

- tgt_constituents: {'sna', 'kin', 'wol', 'ibo', 'swh', 'sag', 'ewe', 'zul', 'fuc', 'lug', 'tso', 'lin', 'nya', 'yor', 'run', 'xho', 'fuv', 'toi_Latn', 'umb'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-alv/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-alv/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: alv

- short_pair: en-alv

- chrF2_score: 0.429

- bleu: 11.4

- brevity_penalty: 1.0

- ref_len: 10603.0

- src_name: English

- tgt_name: Atlantic-Congo languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: alv

- prefer_old: False

- long_pair: eng-alv

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41