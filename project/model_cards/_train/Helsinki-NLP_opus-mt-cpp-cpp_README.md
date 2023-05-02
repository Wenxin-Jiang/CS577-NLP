---
language: 
- id
- cpp

tags:
- translation

license: apache-2.0
---

### cpp-cpp

* source group: Creoles and pidgins, Portuguese-based 
* target group: Creoles and pidgins, Portuguese-based 
*  OPUS readme: [cpp-cpp](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cpp-cpp/README.md)

*  model: transformer
* source language(s): ind pap
* target language(s): ind pap
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-26.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-cpp/opus-2020-07-26.zip)
* test set translations: [opus-2020-07-26.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-cpp/opus-2020-07-26.test.txt)
* test set scores: [opus-2020-07-26.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-cpp/opus-2020-07-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.msa-msa.msa.msa 	| 0.7 	| 0.149 |
| Tatoeba-test.msa-pap.msa.pap 	| 31.7 	| 0.577 |
| Tatoeba-test.multi.multi 	| 21.1 	| 0.369 |
| Tatoeba-test.pap-msa.pap.msa 	| 17.7 	| 0.197 |


### System Info: 
- hf_name: cpp-cpp

- source_languages: cpp

- target_languages: cpp

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/cpp-cpp/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['id', 'cpp']

- src_constituents: {'zsm_Latn', 'ind', 'pap', 'min', 'tmw_Latn', 'max_Latn', 'zlm_Latn'}

- tgt_constituents: {'zsm_Latn', 'ind', 'pap', 'min', 'tmw_Latn', 'max_Latn', 'zlm_Latn'}

- src_multilingual: True

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-cpp/opus-2020-07-26.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/cpp-cpp/opus-2020-07-26.test.txt

- src_alpha3: cpp

- tgt_alpha3: cpp

- short_pair: cpp-cpp

- chrF2_score: 0.369

- bleu: 21.1

- brevity_penalty: 0.882

- ref_len: 18.0

- src_name: Creoles and pidgins, Portuguese-based

- tgt_name: Creoles and pidgins, Portuguese-based

- train_date: 2020-07-26

- src_alpha2: cpp

- tgt_alpha2: cpp

- prefer_old: False

- long_pair: cpp-cpp

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41