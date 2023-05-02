---
language: 
- hr
- mk
- bg
- sl
- zls
- en

tags:
- translation

license: apache-2.0
---

### zls-eng

* source group: South Slavic languages 
* target group: English 
*  OPUS readme: [zls-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zls-eng/README.md)

*  model: transformer
* source language(s): bos_Latn bul bul_Latn hrv mkd slv srp_Cyrl srp_Latn
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bul-eng.bul.eng 	| 54.9 	| 0.693 |
| Tatoeba-test.hbs-eng.hbs.eng 	| 55.7 	| 0.700 |
| Tatoeba-test.mkd-eng.mkd.eng 	| 54.6 	| 0.681 |
| Tatoeba-test.multi.eng 	| 53.6 	| 0.676 |
| Tatoeba-test.slv-eng.slv.eng 	| 25.6 	| 0.407 |


### System Info: 
- hf_name: zls-eng

- source_languages: zls

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zls-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['hr', 'mk', 'bg', 'sl', 'zls', 'en']

- src_constituents: {'hrv', 'mkd', 'srp_Latn', 'srp_Cyrl', 'bul_Latn', 'bul', 'bos_Latn', 'slv'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zls-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zls-eng/opus2m-2020-08-01.test.txt

- src_alpha3: zls

- tgt_alpha3: eng

- short_pair: zls-en

- chrF2_score: 0.6759999999999999

- bleu: 53.6

- brevity_penalty: 0.98

- ref_len: 68623.0

- src_name: South Slavic languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: zls

- tgt_alpha2: en

- prefer_old: False

- long_pair: zls-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41