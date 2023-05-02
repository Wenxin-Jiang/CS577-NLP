---
language: 
- ca
- fr

tags:
- translation

license: apache-2.0
---

### cat-fra

* source group: Catalan 
* target group: French 
*  OPUS readme: [cat-fra](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-fra/README.md)

*  model: transformer-align
* source language(s): cat
* target language(s): fra
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-fra/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-fra/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cat-fra/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.cat.fra 	| 52.4 	| 0.694 |


### System Info: 
- hf_name: cat-fra

- source_languages: cat

- target_languages: fra

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cat-fra/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ca', 'fr']

- src_constituents: {'cat'}

- tgt_constituents: {'fra'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-fra/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cat-fra/opus-2020-06-16.test.txt

- src_alpha3: cat

- tgt_alpha3: fra

- short_pair: ca-fr

- chrF2_score: 0.6940000000000001

- bleu: 52.4

- brevity_penalty: 0.987

- ref_len: 5517.0

- src_name: Catalan

- tgt_name: French

- train_date: 2020-06-16

- src_alpha2: ca

- tgt_alpha2: fr

- prefer_old: False

- long_pair: cat-fra

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41