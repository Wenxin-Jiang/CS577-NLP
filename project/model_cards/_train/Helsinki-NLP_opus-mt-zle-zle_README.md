---
language: 
- be
- ru
- uk
- zle

tags:
- translation

license: apache-2.0
---

### zle-zle

* source group: East Slavic languages 
* target group: East Slavic languages 
*  OPUS readme: [zle-zle](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-zle/README.md)

*  model: transformer
* source language(s): bel bel_Latn orv_Cyrl rus ukr
* target language(s): bel bel_Latn orv_Cyrl rus ukr
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-27.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zle/opus-2020-07-27.zip)
* test set translations: [opus-2020-07-27.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zle/opus-2020-07-27.test.txt)
* test set scores: [opus-2020-07-27.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zle/opus-2020-07-27.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.bel-rus.bel.rus 	| 57.1 	| 0.758 |
| Tatoeba-test.bel-ukr.bel.ukr 	| 55.5 	| 0.751 |
| Tatoeba-test.multi.multi 	| 58.0 	| 0.742 |
| Tatoeba-test.orv-rus.orv.rus 	| 5.8 	| 0.226 |
| Tatoeba-test.orv-ukr.orv.ukr 	| 2.5 	| 0.161 |
| Tatoeba-test.rus-bel.rus.bel 	| 50.5 	| 0.714 |
| Tatoeba-test.rus-orv.rus.orv 	| 0.3 	| 0.129 |
| Tatoeba-test.rus-ukr.rus.ukr 	| 63.9 	| 0.794 |
| Tatoeba-test.ukr-bel.ukr.bel 	| 51.3 	| 0.719 |
| Tatoeba-test.ukr-orv.ukr.orv 	| 0.3 	| 0.106 |
| Tatoeba-test.ukr-rus.ukr.rus 	| 68.7 	| 0.825 |


### System Info: 
- hf_name: zle-zle

- source_languages: zle

- target_languages: zle

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zle-zle/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['be', 'ru', 'uk', 'zle']

- src_constituents: {'bel', 'orv_Cyrl', 'bel_Latn', 'rus', 'ukr', 'rue'}

- tgt_constituents: {'bel', 'orv_Cyrl', 'bel_Latn', 'rus', 'ukr', 'rue'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zle/opus-2020-07-27.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zle-zle/opus-2020-07-27.test.txt

- src_alpha3: zle

- tgt_alpha3: zle

- short_pair: zle-zle

- chrF2_score: 0.742

- bleu: 58.0

- brevity_penalty: 1.0

- ref_len: 62731.0

- src_name: East Slavic languages

- tgt_name: East Slavic languages

- train_date: 2020-07-27

- src_alpha2: zle

- tgt_alpha2: zle

- prefer_old: False

- long_pair: zle-zle

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41