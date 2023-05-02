---
language: 
- bg
- de

tags:
- translation

license: apache-2.0
---

### bul-deu

* source group: Bulgarian 
* target group: German 
*  OPUS readme: [bul-deu](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-deu/README.md)

*  model: transformer
* source language(s): bul
* target language(s): deu
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-deu/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-deu/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-deu/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bul.deu 	| 49.3 	| 0.676 |


### System Info: 
- hf_name: bul-deu

- source_languages: bul

- target_languages: deu

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-deu/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bg', 'de']

- src_constituents: {'bul', 'bul_Latn'}

- tgt_constituents: {'deu'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-deu/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-deu/opus-2020-07-03.test.txt

- src_alpha3: bul

- tgt_alpha3: deu

- short_pair: bg-de

- chrF2_score: 0.6759999999999999

- bleu: 49.3

- brevity_penalty: 1.0

- ref_len: 2218.0

- src_name: Bulgarian

- tgt_name: German

- train_date: 2020-07-03

- src_alpha2: bg

- tgt_alpha2: de

- prefer_old: False

- long_pair: bul-deu

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41