---
language: 
- fj
- mi
- ty
- to
- na
- sm
- mh
- pqe
- en

tags:
- translation

license: apache-2.0
---

### pqe-eng

* source group: Eastern Malayo-Polynesian languages 
* target group: English 
*  OPUS readme: [pqe-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/pqe-eng/README.md)

*  model: transformer
* source language(s): fij gil haw mah mri nau niu rap smo tah ton tvl
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-28.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/pqe-eng/opus-2020-06-28.zip)
* test set translations: [opus-2020-06-28.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/pqe-eng/opus-2020-06-28.test.txt)
* test set scores: [opus-2020-06-28.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/pqe-eng/opus-2020-06-28.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.fij-eng.fij.eng 	| 26.9 	| 0.361 |
| Tatoeba-test.gil-eng.gil.eng 	| 49.0 	| 0.618 |
| Tatoeba-test.haw-eng.haw.eng 	| 1.6 	| 0.126 |
| Tatoeba-test.mah-eng.mah.eng 	| 13.7 	| 0.257 |
| Tatoeba-test.mri-eng.mri.eng 	| 7.4 	| 0.250 |
| Tatoeba-test.multi.eng 	| 12.6 	| 0.268 |
| Tatoeba-test.nau-eng.nau.eng 	| 2.3 	| 0.125 |
| Tatoeba-test.niu-eng.niu.eng 	| 34.4 	| 0.471 |
| Tatoeba-test.rap-eng.rap.eng 	| 10.3 	| 0.215 |
| Tatoeba-test.smo-eng.smo.eng 	| 28.5 	| 0.413 |
| Tatoeba-test.tah-eng.tah.eng 	| 12.1 	| 0.199 |
| Tatoeba-test.ton-eng.ton.eng 	| 41.8 	| 0.517 |
| Tatoeba-test.tvl-eng.tvl.eng 	| 42.9 	| 0.540 |


### System Info: 
- hf_name: pqe-eng

- source_languages: pqe

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/pqe-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['fj', 'mi', 'ty', 'to', 'na', 'sm', 'mh', 'pqe', 'en']

- src_constituents: {'haw', 'gil', 'rap', 'fij', 'tvl', 'mri', 'tah', 'niu', 'ton', 'nau', 'smo', 'mah'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/pqe-eng/opus-2020-06-28.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/pqe-eng/opus-2020-06-28.test.txt

- src_alpha3: pqe

- tgt_alpha3: eng

- short_pair: pqe-en

- chrF2_score: 0.268

- bleu: 12.6

- brevity_penalty: 1.0

- ref_len: 4568.0

- src_name: Eastern Malayo-Polynesian languages

- tgt_name: English

- train_date: 2020-06-28

- src_alpha2: pqe

- tgt_alpha2: en

- prefer_old: False

- long_pair: pqe-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41