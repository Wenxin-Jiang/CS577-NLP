---
language: 
- it
- ms

tags:
- translation

license: apache-2.0
---

### ita-msa

* source group: Italian 
* target group: Malay (macrolanguage) 
*  OPUS readme: [ita-msa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-msa/README.md)

*  model: transformer-align
* source language(s): ita
* target language(s): ind zsm_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-msa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-msa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-msa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ita.msa 	| 26.0 	| 0.536 |


### System Info: 
- hf_name: ita-msa

- source_languages: ita

- target_languages: msa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-msa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['it', 'ms']

- src_constituents: {'ita'}

- tgt_constituents: {'zsm_Latn', 'ind', 'max_Latn', 'zlm_Latn', 'min'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-msa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-msa/opus-2020-06-17.test.txt

- src_alpha3: ita

- tgt_alpha3: msa

- short_pair: it-ms

- chrF2_score: 0.536

- bleu: 26.0

- brevity_penalty: 0.9209999999999999

- ref_len: 2765.0

- src_name: Italian

- tgt_name: Malay (macrolanguage)

- train_date: 2020-06-17

- src_alpha2: it

- tgt_alpha2: ms

- prefer_old: False

- long_pair: ita-msa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41