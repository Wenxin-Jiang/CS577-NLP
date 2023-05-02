---
language: 
- it
- bg

tags:
- translation

license: apache-2.0
---

### ita-bul

* source group: Italian 
* target group: Bulgarian 
*  OPUS readme: [ita-bul](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-bul/README.md)

*  model: transformer
* source language(s): ita
* target language(s): bul
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-bul/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-bul/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-bul/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ita.bul 	| 47.9 	| 0.664 |


### System Info: 
- hf_name: ita-bul

- source_languages: ita

- target_languages: bul

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-bul/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['it', 'bg']

- src_constituents: {'ita'}

- tgt_constituents: {'bul', 'bul_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-bul/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-bul/opus-2020-07-03.test.txt

- src_alpha3: ita

- tgt_alpha3: bul

- short_pair: it-bg

- chrF2_score: 0.664

- bleu: 47.9

- brevity_penalty: 0.961

- ref_len: 16512.0

- src_name: Italian

- tgt_name: Bulgarian

- train_date: 2020-07-03

- src_alpha2: it

- tgt_alpha2: bg

- prefer_old: False

- long_pair: ita-bul

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41