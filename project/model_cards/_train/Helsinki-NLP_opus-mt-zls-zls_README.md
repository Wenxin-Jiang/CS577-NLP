---
language: 
- hr
- mk
- bg
- sl
- zls

tags:
- translation

license: apache-2.0
---

### zls-zls

* source group: South Slavic languages 
* target group: South Slavic languages 
*  OPUS readme: [zls-zls](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zls-zls/README.md)

*  model: transformer
* source language(s): bul mkd srp_Cyrl
* target language(s): bul mkd srp_Cyrl
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-zls/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-zls/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zls-zls/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bul-hbs.bul.hbs 	| 19.3 	| 0.514 |
| Tatoeba-test.bul-mkd.bul.mkd 	| 31.9 	| 0.669 |
| Tatoeba-test.hbs-bul.hbs.bul 	| 18.0 	| 0.636 |
| Tatoeba-test.hbs-mkd.hbs.mkd 	| 19.4 	| 0.322 |
| Tatoeba-test.mkd-bul.mkd.bul 	| 44.6 	| 0.679 |
| Tatoeba-test.mkd-hbs.mkd.hbs 	| 5.5 	| 0.152 |
| Tatoeba-test.multi.multi 	| 26.5 	| 0.563 |


### System Info: 
- hf_name: zls-zls

- source_languages: zls

- target_languages: zls

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zls-zls/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['hr', 'mk', 'bg', 'sl', 'zls']

- src_constituents: {'hrv', 'mkd', 'srp_Latn', 'srp_Cyrl', 'bul_Latn', 'bul', 'bos_Latn', 'slv'}

- tgt_constituents: {'hrv', 'mkd', 'srp_Latn', 'srp_Cyrl', 'bul_Latn', 'bul', 'bos_Latn', 'slv'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zls-zls/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zls-zls/opus-2020-07-27.test.txt

- src_alpha3: zls

- tgt_alpha3: zls

- short_pair: zls-zls

- chrF2_score: 0.563

- bleu: 26.5

- brevity_penalty: 1.0

- ref_len: 58.0

- src_name: South Slavic languages

- tgt_name: South Slavic languages

- train_date: 2020-07-27

- src_alpha2: zls

- tgt_alpha2: zls

- prefer_old: False

- long_pair: zls-zls

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41