---
language: 
- ms
- fr

tags:
- translation

license: apache-2.0
---

### msa-fra

* source group: Malay (macrolanguage) 
* target group: French 
*  OPUS readme: [msa-fra](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/msa-fra/README.md)

*  model: transformer-align
* source language(s): ind zsm_Latn
* target language(s): fra
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/msa-fra/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/msa-fra/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/msa-fra/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.msa.fra 	| 43.7 	| 0.609 |


### System Info: 
- hf_name: msa-fra

- source_languages: msa

- target_languages: fra

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/msa-fra/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ms', 'fr']

- src_constituents: {'zsm_Latn', 'ind', 'max_Latn', 'zlm_Latn', 'min'}

- tgt_constituents: {'fra'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/msa-fra/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/msa-fra/opus-2020-06-17.test.txt

- src_alpha3: msa

- tgt_alpha3: fra

- short_pair: ms-fr

- chrF2_score: 0.609

- bleu: 43.7

- brevity_penalty: 0.9740000000000001

- ref_len: 7808.0

- src_name: Malay (macrolanguage)

- tgt_name: French

- train_date: 2020-06-17

- src_alpha2: ms

- tgt_alpha2: fr

- prefer_old: False

- long_pair: msa-fra

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41