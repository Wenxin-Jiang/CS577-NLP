---
language: 
- tr
- ar

tags:
- translation

license: apache-2.0
---

### tur-ara

* source group: Turkish 
* target group: Arabic 
*  OPUS readme: [tur-ara](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tur-ara/README.md)

*  model: transformer
* source language(s): tur
* target language(s): apc_Latn ara ara_Latn arq_Latn
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ara/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ara/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ara/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.tur.ara 	| 14.9 	| 0.455 |


### System Info: 
- hf_name: tur-ara

- source_languages: tur

- target_languages: ara

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/tur-ara/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['tr', 'ar']

- src_constituents: {'tur'}

- tgt_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ara/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/tur-ara/opus-2020-07-03.test.txt

- src_alpha3: tur

- tgt_alpha3: ara

- short_pair: tr-ar

- chrF2_score: 0.455

- bleu: 14.9

- brevity_penalty: 0.988

- ref_len: 6944.0

- src_name: Turkish

- tgt_name: Arabic

- train_date: 2020-07-03

- src_alpha2: tr

- tgt_alpha2: ar

- prefer_old: False

- long_pair: tur-ara

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41