---
language: 
- tl
- en

tags:
- translation

license: apache-2.0
---

### tgl-eng

* source group: Tagalog 
* target group: English 
*  OPUS readme: [tgl-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tgl-eng/README.md)

*  model: transformer-align
* source language(s): tgl_Latn
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-eng/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-eng/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-eng/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.tgl.eng 	| 35.0 	| 0.542 |


### System Info: 
- hf_name: tgl-eng

- source_languages: tgl

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tgl-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['tl', 'en']

- src_constituents: {'tgl_Latn'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-eng/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/tgl-eng/opus-2020-06-17.test.txt

- src_alpha3: tgl

- tgt_alpha3: eng

- short_pair: tl-en

- chrF2_score: 0.542

- bleu: 35.0

- brevity_penalty: 0.975

- ref_len: 18168.0

- src_name: Tagalog

- tgt_name: English

- train_date: 2020-06-17

- src_alpha2: tl

- tgt_alpha2: en

- prefer_old: False

- long_pair: tgl-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41