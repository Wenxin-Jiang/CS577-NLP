---
language: 
- ko
- hu

tags:
- translation

license: apache-2.0
---

### kor-hun

* source group: Korean 
* target group: Hungarian 
*  OPUS readme: [kor-hun](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/kor-hun/README.md)

*  model: transformer-align
* source language(s): kor kor_Hang kor_Latn
* target language(s): hun
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/kor-hun/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/kor-hun/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/kor-hun/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.kor.hun 	| 28.6 	| 0.520 |


### System Info: 
- hf_name: kor-hun

- source_languages: kor

- target_languages: hun

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/kor-hun/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ko', 'hu']

- src_constituents: {'kor_Hani', 'kor_Hang', 'kor_Latn', 'kor'}

- tgt_constituents: {'hun'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/kor-hun/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/kor-hun/opus-2020-06-17.test.txt

- src_alpha3: kor

- tgt_alpha3: hun

- short_pair: ko-hu

- chrF2_score: 0.52

- bleu: 28.6

- brevity_penalty: 0.905

- ref_len: 1615.0

- src_name: Korean

- tgt_name: Hungarian

- train_date: 2020-06-17

- src_alpha2: ko

- tgt_alpha2: hu

- prefer_old: False

- long_pair: kor-hun

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41