---
language: 
- bg
- tr

tags:
- translation

license: apache-2.0
---

### bul-tur

* source group: Bulgarian 
* target group: Turkish 
*  OPUS readme: [bul-tur](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-tur/README.md)

*  model: transformer
* source language(s): bul bul_Latn
* target language(s): tur
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-tur/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-tur/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-tur/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bul.tur 	| 40.9 	| 0.687 |


### System Info: 
- hf_name: bul-tur

- source_languages: bul

- target_languages: tur

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-tur/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bg', 'tr']

- src_constituents: {'bul', 'bul_Latn'}

- tgt_constituents: {'tur'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-tur/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-tur/opus-2020-07-03.test.txt

- src_alpha3: bul

- tgt_alpha3: tur

- short_pair: bg-tr

- chrF2_score: 0.687

- bleu: 40.9

- brevity_penalty: 0.946

- ref_len: 4948.0

- src_name: Bulgarian

- tgt_name: Turkish

- train_date: 2020-07-03

- src_alpha2: bg

- tgt_alpha2: tr

- prefer_old: False

- long_pair: bul-tur

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41