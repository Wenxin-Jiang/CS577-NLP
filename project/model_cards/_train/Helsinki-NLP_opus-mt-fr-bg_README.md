---
language: 
- fr
- bg

tags:
- translation

license: apache-2.0
---

### fra-bul

* source group: French 
* target group: Bulgarian 
*  OPUS readme: [fra-bul](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fra-bul/README.md)

*  model: transformer
* source language(s): fra
* target language(s): bul
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-bul/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-bul/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-bul/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.fra.bul 	| 46.3 	| 0.657 |


### System Info: 
- hf_name: fra-bul

- source_languages: fra

- target_languages: bul

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fra-bul/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['fr', 'bg']

- src_constituents: {'fra'}

- tgt_constituents: {'bul', 'bul_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/fra-bul/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/fra-bul/opus-2020-07-03.test.txt

- src_alpha3: fra

- tgt_alpha3: bul

- short_pair: fr-bg

- chrF2_score: 0.657

- bleu: 46.3

- brevity_penalty: 0.953

- ref_len: 3286.0

- src_name: French

- tgt_name: Bulgarian

- train_date: 2020-07-03

- src_alpha2: fr

- tgt_alpha2: bg

- prefer_old: False

- long_pair: fra-bul

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41