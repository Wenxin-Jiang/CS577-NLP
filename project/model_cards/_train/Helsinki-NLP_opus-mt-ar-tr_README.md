---
language: 
- ar
- tr

tags:
- translation

license: apache-2.0
---

### ara-tur

* source group: Arabic 
* target group: Turkish 
*  OPUS readme: [ara-tur](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-tur/README.md)

*  model: transformer
* source language(s): apc_Latn ara ara_Latn arq_Latn
* target language(s): tur
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-tur/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-tur/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-tur/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ara.tur 	| 33.1 	| 0.619 |


### System Info: 
- hf_name: ara-tur

- source_languages: ara

- target_languages: tur

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-tur/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ar', 'tr']

- src_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- tgt_constituents: {'tur'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-tur/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-tur/opus-2020-07-03.test.txt

- src_alpha3: ara

- tgt_alpha3: tur

- short_pair: ar-tr

- chrF2_score: 0.619

- bleu: 33.1

- brevity_penalty: 0.9570000000000001

- ref_len: 6949.0

- src_name: Arabic

- tgt_name: Turkish

- train_date: 2020-07-03

- src_alpha2: ar

- tgt_alpha2: tr

- prefer_old: False

- long_pair: ara-tur

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41