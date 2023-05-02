---
language: 
- de
- tl

tags:
- translation

license: apache-2.0
---

### deu-tgl

* source group: German 
* target group: Tagalog 
*  OPUS readme: [deu-tgl](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-tgl/README.md)

*  model: transformer-align
* source language(s): deu
* target language(s): tgl_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-tgl/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-tgl/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-tgl/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.deu.tgl 	| 21.2 	| 0.541 |


### System Info: 
- hf_name: deu-tgl

- source_languages: deu

- target_languages: tgl

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-tgl/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['de', 'tl']

- src_constituents: {'deu'}

- tgt_constituents: {'tgl_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-tgl/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-tgl/opus-2020-06-17.test.txt

- src_alpha3: deu

- tgt_alpha3: tgl

- short_pair: de-tl

- chrF2_score: 0.541

- bleu: 21.2

- brevity_penalty: 1.0

- ref_len: 2329.0

- src_name: German

- tgt_name: Tagalog

- train_date: 2020-06-17

- src_alpha2: de

- tgt_alpha2: tl

- prefer_old: False

- long_pair: deu-tgl

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41