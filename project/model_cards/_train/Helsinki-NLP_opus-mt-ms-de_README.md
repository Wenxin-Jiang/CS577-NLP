---
language: 
- ms
- de

tags:
- translation

license: apache-2.0
---

### msa-deu

* source group: Malay (macrolanguage) 
* target group: German 
*  OPUS readme: [msa-deu](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/msa-deu/README.md)

*  model: transformer-align
* source language(s): ind zsm_Latn
* target language(s): deu
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/msa-deu/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/msa-deu/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/msa-deu/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.msa.deu 	| 36.5 	| 0.584 |


### System Info: 
- hf_name: msa-deu

- source_languages: msa

- target_languages: deu

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/msa-deu/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ms', 'de']

- src_constituents: {'zsm_Latn', 'ind', 'max_Latn', 'zlm_Latn', 'min'}

- tgt_constituents: {'deu'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/msa-deu/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/msa-deu/opus-2020-06-17.test.txt

- src_alpha3: msa

- tgt_alpha3: deu

- short_pair: ms-de

- chrF2_score: 0.584

- bleu: 36.5

- brevity_penalty: 0.966

- ref_len: 4198.0

- src_name: Malay (macrolanguage)

- tgt_name: German

- train_date: 2020-06-17

- src_alpha2: ms

- tgt_alpha2: de

- prefer_old: False

- long_pair: msa-deu

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41