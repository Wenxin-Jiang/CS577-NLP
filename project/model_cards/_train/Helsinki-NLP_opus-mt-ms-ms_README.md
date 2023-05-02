---
language: 
- ms

tags:
- translation

license: apache-2.0
---

### msa-msa

* source group: Malay (macrolanguage) 
* target group: Malay (macrolanguage) 
*  OPUS readme: [msa-msa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/msa-msa/README.md)

*  model: transformer-align
* source language(s): ind max_Latn min zlm_Latn zsm_Latn
* target language(s): ind max_Latn min zlm_Latn zsm_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/msa-msa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/msa-msa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/msa-msa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.msa.msa 	| 18.6 	| 0.418 |


### System Info: 
- hf_name: msa-msa

- source_languages: msa

- target_languages: msa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/msa-msa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ms']

- src_constituents: {'zsm_Latn', 'ind', 'max_Latn', 'zlm_Latn', 'min'}

- tgt_constituents: {'zsm_Latn', 'ind', 'max_Latn', 'zlm_Latn', 'min'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/msa-msa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/msa-msa/opus-2020-06-17.test.txt

- src_alpha3: msa

- tgt_alpha3: msa

- short_pair: ms-ms

- chrF2_score: 0.418

- bleu: 18.6

- brevity_penalty: 1.0

- ref_len: 6029.0

- src_name: Malay (macrolanguage)

- tgt_name: Malay (macrolanguage)

- train_date: 2020-06-17

- src_alpha2: ms

- tgt_alpha2: ms

- prefer_old: False

- long_pair: msa-msa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41