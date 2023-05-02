---
language: 
- en
- ht
- cpf

tags:
- translation

license: apache-2.0
---

### eng-cpf

* source group: English 
* target group: Creoles and pidgins, French‑based 
*  OPUS readme: [eng-cpf](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-cpf/README.md)

*  model: transformer
* source language(s): eng
* target language(s): gcf_Latn hat mfe
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpf/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpf/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpf/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng-gcf.eng.gcf 	| 6.2 	| 0.262 |
| Tatoeba-test.eng-hat.eng.hat 	| 25.7 	| 0.451 |
| Tatoeba-test.eng-mfe.eng.mfe 	| 80.1 	| 0.900 |
| Tatoeba-test.eng.multi 	| 15.9 	| 0.354 |


### System Info: 
- hf_name: eng-cpf

- source_languages: eng

- target_languages: cpf

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-cpf/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'ht', 'cpf']

- src_constituents: {'eng'}

- tgt_constituents: {'gcf_Latn', 'hat', 'mfe'}

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpf/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-cpf/opus-2020-07-26.test.txt

- src_alpha3: eng

- tgt_alpha3: cpf

- short_pair: en-cpf

- chrF2_score: 0.354

- bleu: 15.9

- brevity_penalty: 1.0

- ref_len: 1012.0

- src_name: English

- tgt_name: Creoles and pidgins, French‑based

- train_date: 2020-07-26

- src_alpha2: en

- tgt_alpha2: cpf

- prefer_old: False

- long_pair: eng-cpf

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41