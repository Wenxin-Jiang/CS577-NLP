---
language: 
- ja
- ms

tags:
- translation

license: apache-2.0
---

### jpn-msa

* source group: Japanese 
* target group: Malay (macrolanguage) 
*  OPUS readme: [jpn-msa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-msa/README.md)

*  model: transformer-align
* source language(s): jpn jpn_Hani jpn_Hira jpn_Kana
* target language(s): ind zlm_Latn zsm_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-msa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-msa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-msa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.jpn.msa 	| 21.5 	| 0.469 |


### System Info: 
- hf_name: jpn-msa

- source_languages: jpn

- target_languages: msa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/jpn-msa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ja', 'ms']

- src_constituents: {'jpn_Hang', 'jpn', 'jpn_Yiii', 'jpn_Kana', 'jpn_Hani', 'jpn_Bopo', 'jpn_Latn', 'jpn_Hira'}

- tgt_constituents: {'zsm_Latn', 'ind', 'max_Latn', 'zlm_Latn', 'min'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-msa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/jpn-msa/opus-2020-06-17.test.txt

- src_alpha3: jpn

- tgt_alpha3: msa

- short_pair: ja-ms

- chrF2_score: 0.469

- bleu: 21.5

- brevity_penalty: 0.9259999999999999

- ref_len: 17028.0

- src_name: Japanese

- tgt_name: Malay (macrolanguage)

- train_date: 2020-06-17

- src_alpha2: ja

- tgt_alpha2: ms

- prefer_old: False

- long_pair: jpn-msa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41