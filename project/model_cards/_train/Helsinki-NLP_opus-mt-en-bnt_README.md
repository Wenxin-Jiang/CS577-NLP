---
language: 
- en
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

tags:
- translation

license: apache-2.0
---

### eng-bnt

* source group: English 
* target group: Bantu languages 
*  OPUS readme: [eng-bnt](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-bnt/README.md)

*  model: transformer
* source language(s): eng
* target language(s): kin lin lug nya run sna swh toi_Latn tso umb xho zul
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bnt/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bnt/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bnt/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-kin.eng.kin 	| 12.5 	| 0.519 |
| Tatoeba-test.eng-lin.eng.lin 	| 1.1 	| 0.277 |
| Tatoeba-test.eng-lug.eng.lug 	| 4.8 	| 0.415 |
| Tatoeba-test.eng.multi 	| 12.1 	| 0.449 |
| Tatoeba-test.eng-nya.eng.nya 	| 22.1 	| 0.616 |
| Tatoeba-test.eng-run.eng.run 	| 13.2 	| 0.492 |
| Tatoeba-test.eng-sna.eng.sna 	| 32.1 	| 0.669 |
| Tatoeba-test.eng-swa.eng.swa 	| 1.7 	| 0.180 |
| Tatoeba-test.eng-toi.eng.toi 	| 10.7 	| 0.266 |
| Tatoeba-test.eng-tso.eng.tso 	| 26.9 	| 0.631 |
| Tatoeba-test.eng-umb.eng.umb 	| 5.2 	| 0.295 |
| Tatoeba-test.eng-xho.eng.xho 	| 22.6 	| 0.615 |
| Tatoeba-test.eng-zul.eng.zul 	| 41.1 	| 0.769 |


### System Info: 
- hf_name: eng-bnt

- source_languages: eng

- target_languages: bnt

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-bnt/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'sn', 'zu', 'rw', 'lg', 'ts', 'ln', 'ny', 'xh', 'rn', 'bnt']

- src_constituents: {'eng'}

- tgt_constituents: {'sna', 'zul', 'kin', 'lug', 'tso', 'lin', 'nya', 'xho', 'swh', 'run', 'toi_Latn', 'umb'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bnt/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-bnt/opus-2020-07-26.test.txt

- src_alpha3: eng

- tgt_alpha3: bnt

- short_pair: en-bnt

- chrF2_score: 0.449

- bleu: 12.1

- brevity_penalty: 1.0

- ref_len: 9989.0

- src_name: English

- tgt_name: Bantu languages

- train_date: 2020-07-26

- src_alpha2: en

- tgt_alpha2: bnt

- prefer_old: False

- long_pair: eng-bnt

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41