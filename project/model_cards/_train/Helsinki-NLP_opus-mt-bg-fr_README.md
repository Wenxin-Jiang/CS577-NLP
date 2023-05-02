---
language: 
- bg
- fr

tags:
- translation

license: apache-2.0
---

### bul-fra

* source group: Bulgarian 
* target group: French 
*  OPUS readme: [bul-fra](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-fra/README.md)

*  model: transformer
* source language(s): bul
* target language(s): fra
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-fra/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-fra/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/bul-fra/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bul.fra 	| 53.7 	| 0.693 |


### System Info: 
- hf_name: bul-fra

- source_languages: bul

- target_languages: fra

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/bul-fra/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['bg', 'fr']

- src_constituents: {'bul', 'bul_Latn'}

- tgt_constituents: {'fra'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-fra/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/bul-fra/opus-2020-07-03.test.txt

- src_alpha3: bul

- tgt_alpha3: fra

- short_pair: bg-fr

- chrF2_score: 0.693

- bleu: 53.7

- brevity_penalty: 0.977

- ref_len: 3669.0

- src_name: Bulgarian

- tgt_name: French

- train_date: 2020-07-03

- src_alpha2: bg

- tgt_alpha2: fr

- prefer_old: False

- long_pair: bul-fra

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41