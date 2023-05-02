---
language: 
- en
- hr
- mk
- bg
- sl
- zls

tags:
- translation

license: apache-2.0
---

### eng-zls

* source group: English 
* target group: South Slavic languages 
*  OPUS readme: [eng-zls](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-zls/README.md)

*  model: transformer
* source language(s): eng
* target language(s): bos_Latn bul bul_Latn hrv mkd slv srp_Cyrl srp_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-02.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zls/opus2m-2020-08-02.zip)
* test set translations: [opus2m-2020-08-02.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zls/opus2m-2020-08-02.test.txt)
* test set scores: [opus2m-2020-08-02.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zls/opus2m-2020-08-02.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-bul.eng.bul 	| 47.6 	| 0.657 |
| Tatoeba-test.eng-hbs.eng.hbs 	| 40.7 	| 0.619 |
| Tatoeba-test.eng-mkd.eng.mkd 	| 45.2 	| 0.642 |
| Tatoeba-test.eng.multi 	| 42.7 	| 0.622 |
| Tatoeba-test.eng-slv.eng.slv 	| 17.9 	| 0.351 |


### System Info: 
- hf_name: eng-zls

- source_languages: eng

- target_languages: zls

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-zls/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'hr', 'mk', 'bg', 'sl', 'zls']

- src_constituents: {'eng'}

- tgt_constituents: {'hrv', 'mkd', 'srp_Latn', 'srp_Cyrl', 'bul_Latn', 'bul', 'bos_Latn', 'slv'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zls/opus2m-2020-08-02.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zls/opus2m-2020-08-02.test.txt

- src_alpha3: eng

- tgt_alpha3: zls

- short_pair: en-zls

- chrF2_score: 0.622

- bleu: 42.7

- brevity_penalty: 0.9690000000000001

- ref_len: 64788.0

- src_name: English

- tgt_name: South Slavic languages

- train_date: 2020-08-02

- src_alpha2: en

- tgt_alpha2: zls

- prefer_old: False

- long_pair: eng-zls

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41