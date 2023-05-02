---
language: 
- de
- ms

tags:
- translation

license: apache-2.0
---

### deu-msa

* source group: German 
* target group: Malay (macrolanguage) 
*  OPUS readme: [deu-msa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-msa/README.md)

*  model: transformer-align
* source language(s): deu
* target language(s): ind zsm_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-msa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-msa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-msa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.deu.msa 	| 34.0 	| 0.607 |


### System Info: 
- hf_name: deu-msa

- source_languages: deu

- target_languages: msa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-msa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['de', 'ms']

- src_constituents: {'deu'}

- tgt_constituents: {'zsm_Latn', 'ind', 'max_Latn', 'zlm_Latn', 'min'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-msa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-msa/opus-2020-06-17.test.txt

- src_alpha3: deu

- tgt_alpha3: msa

- short_pair: de-ms

- chrF2_score: 0.607

- bleu: 34.0

- brevity_penalty: 0.9540000000000001

- ref_len: 3729.0

- src_name: German

- tgt_name: Malay (macrolanguage)

- train_date: 2020-06-17

- src_alpha2: de

- tgt_alpha2: ms

- prefer_old: False

- long_pair: deu-msa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41