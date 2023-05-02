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
- nic

tags:
- translation

license: apache-2.0
---

### eng-nic

* source group: English 
* target group: Niger-Kordofanian languages 
*  OPUS readme: [eng-nic](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-nic/README.md)

*  model: transformer
* source language(s): eng
* target language(s): bam_Latn ewe fuc fuv ibo kin lin lug nya run sag sna swh toi_Latn tso umb wol xho yor zul
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-nic/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-nic/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-nic/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-bam.eng.bam 	| 6.2 	| 0.029 |
| Tatoeba-test.eng-ewe.eng.ewe 	| 4.5 	| 0.258 |
| Tatoeba-test.eng-ful.eng.ful 	| 0.5 	| 0.073 |
| Tatoeba-test.eng-ibo.eng.ibo 	| 3.9 	| 0.267 |
| Tatoeba-test.eng-kin.eng.kin 	| 6.4 	| 0.475 |
| Tatoeba-test.eng-lin.eng.lin 	| 1.2 	| 0.308 |
| Tatoeba-test.eng-lug.eng.lug 	| 3.9 	| 0.405 |
| Tatoeba-test.eng.multi 	| 11.1 	| 0.427 |
| Tatoeba-test.eng-nya.eng.nya 	| 14.0 	| 0.622 |
| Tatoeba-test.eng-run.eng.run 	| 13.6 	| 0.477 |
| Tatoeba-test.eng-sag.eng.sag 	| 5.5 	| 0.199 |
| Tatoeba-test.eng-sna.eng.sna 	| 19.6 	| 0.557 |
| Tatoeba-test.eng-swa.eng.swa 	| 1.8 	| 0.163 |
| Tatoeba-test.eng-toi.eng.toi 	| 8.3 	| 0.231 |
| Tatoeba-test.eng-tso.eng.tso 	| 50.0 	| 0.789 |
| Tatoeba-test.eng-umb.eng.umb 	| 7.8 	| 0.342 |
| Tatoeba-test.eng-wol.eng.wol 	| 6.7 	| 0.143 |
| Tatoeba-test.eng-xho.eng.xho 	| 26.4 	| 0.620 |
| Tatoeba-test.eng-yor.eng.yor 	| 15.5 	| 0.342 |
| Tatoeba-test.eng-zul.eng.zul 	| 35.9 	| 0.750 |


### System Info: 
- hf_name: eng-nic

- source_languages: eng

- target_languages: nic

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-nic/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'sn', 'rw', 'wo', 'ig', 'sg', 'ee', 'zu', 'lg', 'ts', 'ln', 'ny', 'yo', 'rn', 'xh', 'nic']

- src_constituents: {'eng'}

- tgt_constituents: {'bam_Latn', 'sna', 'kin', 'wol', 'ibo', 'swh', 'sag', 'ewe', 'zul', 'fuc', 'lug', 'tso', 'lin', 'nya', 'yor', 'run', 'xho', 'fuv', 'toi_Latn', 'umb'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-nic/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-nic/opus-2020-07-27.test.txt

- src_alpha3: eng

- tgt_alpha3: nic

- short_pair: en-nic

- chrF2_score: 0.42700000000000005

- bleu: 11.1

- brevity_penalty: 1.0

- ref_len: 10625.0

- src_name: English

- tgt_name: Niger-Kordofanian languages

- train_date: 2020-07-27

- src_alpha2: en

- tgt_alpha2: nic

- prefer_old: False

- long_pair: eng-nic

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41