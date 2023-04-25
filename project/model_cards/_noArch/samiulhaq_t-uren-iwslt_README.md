---
language:
- ur
- en
license: apache-2.0
datasets:
- iwslt2017
metrics:
- bleu
library_name: tensorflowtts
pipeline_tag: translation
---

### urd-eng

* source group: Urdu 
* target group: English 
*  OPUS readme: [urd-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/urd-eng/README.md)

*  model: transformer-align
* source language(s): urd
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/urd-eng/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/urd-eng/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/urd-eng/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.urd.eng 	| 23.2 	| 0.435 |


### System Info: 
- hf_name: urd-eng
- source_languages: urd

- target_languages: eng
- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/urd-eng/README.md
- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ur', 'en']

- src_constituents: {'urd'}
- tgt_constituents: {'eng'}

- src_multilingual: False
- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/urd-eng/opus-2020-06-17.zip
- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/urd-eng/opus-2020-06-17.test.txt
- src_alpha3: urd

- tgt_alpha3: eng
- short_pair: ur-en

- chrF2_score: 0.435
- bleu: 23.2
- brevity_penalty: 0.975

- ref_len: 12029.0
- src_name: Urdu

- tgt_name: English
- train_date: 2020-06-17

- src_alpha2: ur
- tgt_alpha2: en

- prefer_old: False
- long_pair: urd-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse
- port_time: 2020-08-21-14:41