---
language: 
- ar
- it

tags:
- translation

license: apache-2.0
---

### ara-ita

* source group: Arabic 
* target group: Italian 
*  OPUS readme: [ara-ita](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-ita/README.md)

*  model: transformer
* source language(s): ara
* target language(s): ita
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ita/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ita/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ita/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ara.ita 	| 44.2 	| 0.658 |


### System Info: 
- hf_name: ara-ita

- source_languages: ara

- target_languages: ita

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ara-ita/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ar', 'it']

- src_constituents: {'apc', 'ara', 'arq_Latn', 'arq', 'afb', 'ara_Latn', 'apc_Latn', 'arz'}

- tgt_constituents: {'ita'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ita/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ara-ita/opus-2020-07-03.test.txt

- src_alpha3: ara

- tgt_alpha3: ita

- short_pair: ar-it

- chrF2_score: 0.6579999999999999

- bleu: 44.2

- brevity_penalty: 0.9890000000000001

- ref_len: 1495.0

- src_name: Arabic

- tgt_name: Italian

- train_date: 2020-07-03

- src_alpha2: ar

- tgt_alpha2: it

- prefer_old: False

- long_pair: ara-ita

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41