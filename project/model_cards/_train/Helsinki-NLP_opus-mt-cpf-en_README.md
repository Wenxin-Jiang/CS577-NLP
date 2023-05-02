---
language: 
- ht
- cpf
- en

tags:
- translation

license: apache-2.0
---

### cpf-eng

* source group: Creoles and pidgins, French‑based 
* target group: English 
*  OPUS readme: [cpf-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cpf-eng/README.md)

*  model: transformer
* source language(s): gcf_Latn hat mfe
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus2m-2020-07-31.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cpf-eng/opus2m-2020-07-31.zip)
* test set translations: [opus2m-2020-07-31.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cpf-eng/opus2m-2020-07-31.test.txt)
* test set scores: [opus2m-2020-07-31.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cpf-eng/opus2m-2020-07-31.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.gcf-eng.gcf.eng 	| 8.4 	| 0.229 |
| Tatoeba-test.hat-eng.hat.eng 	| 28.0 	| 0.421 |
| Tatoeba-test.mfe-eng.mfe.eng 	| 66.0 	| 0.808 |
| Tatoeba-test.multi.eng 	| 16.3 	| 0.323 |


### System Info: 
- hf_name: cpf-eng

- source_languages: cpf

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cpf-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ht', 'cpf', 'en']

- src_constituents: {'gcf_Latn', 'hat', 'mfe'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cpf-eng/opus2m-2020-07-31.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cpf-eng/opus2m-2020-07-31.test.txt

- src_alpha3: cpf

- tgt_alpha3: eng

- short_pair: cpf-en

- chrF2_score: 0.32299999999999995

- bleu: 16.3

- brevity_penalty: 1.0

- ref_len: 990.0

- src_name: Creoles and pidgins, French‑based

- tgt_name: English

- train_date: 2020-07-31

- src_alpha2: cpf

- tgt_alpha2: en

- prefer_old: False

- long_pair: cpf-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41