---
language: 
- en
- fj
- mi
- ty
- to
- na
- sm
- mh
- pqe

tags:
- translation

license: apache-2.0
---

### eng-pqe

* source group: English 
* target group: Eastern Malayo-Polynesian languages 
*  OPUS readme: [eng-pqe](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-pqe/README.md)

*  model: transformer
* source language(s): eng
* target language(s): fij gil haw lkt mah mri nau niu rap smo tah ton tvl
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqe/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqe/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqe/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-fij.eng.fij 	| 22.1 	| 0.396 |
| Tatoeba-test.eng-gil.eng.gil 	| 41.9 	| 0.673 |
| Tatoeba-test.eng-haw.eng.haw 	| 0.6 	| 0.114 |
| Tatoeba-test.eng-lkt.eng.lkt 	| 0.5 	| 0.075 |
| Tatoeba-test.eng-mah.eng.mah 	| 9.7 	| 0.386 |
| Tatoeba-test.eng-mri.eng.mri 	| 7.7 	| 0.301 |
| Tatoeba-test.eng.multi 	| 11.3 	| 0.306 |
| Tatoeba-test.eng-nau.eng.nau 	| 0.5 	| 0.071 |
| Tatoeba-test.eng-niu.eng.niu 	| 42.5 	| 0.560 |
| Tatoeba-test.eng-rap.eng.rap 	| 3.3 	| 0.122 |
| Tatoeba-test.eng-smo.eng.smo 	| 27.0 	| 0.462 |
| Tatoeba-test.eng-tah.eng.tah 	| 11.3 	| 0.307 |
| Tatoeba-test.eng-ton.eng.ton 	| 27.0 	| 0.528 |
| Tatoeba-test.eng-tvl.eng.tvl 	| 29.3 	| 0.513 |


### System Info: 
- hf_name: eng-pqe

- source_languages: eng

- target_languages: pqe

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-pqe/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'fj', 'mi', 'ty', 'to', 'na', 'sm', 'mh', 'pqe']

- src_constituents: {'eng'}

- tgt_constituents: {'haw', 'gil', 'rap', 'fij', 'tvl', 'mri', 'tah', 'niu', 'ton', 'nau', 'smo', 'mah'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqe/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-pqe/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: pqe

- short_pair: en-pqe

- chrF2_score: 0.306

- bleu: 11.3

- brevity_penalty: 1.0

- ref_len: 5786.0

- src_name: English

- tgt_name: Eastern Malayo-Polynesian languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: pqe

- prefer_old: False

- long_pair: eng-pqe

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41