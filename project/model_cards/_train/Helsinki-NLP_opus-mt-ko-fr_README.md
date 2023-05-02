---
language: 
- ko
- fr

tags:
- translation

license: apache-2.0
---

### kor-fra

* source group: Korean 
* target group: French 
*  OPUS readme: [kor-fra](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/kor-fra/README.md)

*  model: transformer-align
* source language(s): kor kor_Hang kor_Hani kor_Latn
* target language(s): fra
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/kor-fra/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/kor-fra/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/kor-fra/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.kor.fra 	| 30.4 	| 0.503 |


### System Info: 
- hf_name: kor-fra

- source_languages: kor

- target_languages: fra

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/kor-fra/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ko', 'fr']

- src_constituents: {'kor_Hani', 'kor_Hang', 'kor_Latn', 'kor'}

- tgt_constituents: {'fra'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/kor-fra/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/kor-fra/opus-2020-06-17.test.txt

- src_alpha3: kor

- tgt_alpha3: fra

- short_pair: ko-fr

- chrF2_score: 0.503

- bleu: 30.4

- brevity_penalty: 0.9179999999999999

- ref_len: 2714.0

- src_name: Korean

- tgt_name: French

- train_date: 2020-06-17

- src_alpha2: ko

- tgt_alpha2: fr

- prefer_old: False

- long_pair: kor-fra

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41