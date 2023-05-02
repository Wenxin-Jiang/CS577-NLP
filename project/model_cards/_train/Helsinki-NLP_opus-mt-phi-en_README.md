---
language: 
- phi
- en

tags:
- translation

license: apache-2.0
---

### phi-eng

* source group: Philippine languages 
* target group: English 
*  OPUS readme: [phi-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/phi-eng/README.md)

*  model: transformer
* source language(s): akl_Latn ceb hil ilo pag war
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm12k,spm12k)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/phi-eng/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/phi-eng/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/phi-eng/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.akl-eng.akl.eng 	| 11.6 	| 0.321 |
| Tatoeba-test.ceb-eng.ceb.eng 	| 21.7 	| 0.393 |
| Tatoeba-test.hil-eng.hil.eng 	| 17.6 	| 0.371 |
| Tatoeba-test.ilo-eng.ilo.eng 	| 36.6 	| 0.560 |
| Tatoeba-test.multi.eng 	| 21.5 	| 0.391 |
| Tatoeba-test.pag-eng.pag.eng 	| 27.5 	| 0.494 |
| Tatoeba-test.war-eng.war.eng 	| 17.3 	| 0.380 |


### System Info: 
- hf_name: phi-eng

- source_languages: phi

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/phi-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['phi', 'en']

- src_constituents: {'ilo', 'akl_Latn', 'war', 'hil', 'pag', 'ceb'}

- tgt_constituents: {'eng'}

- src_multilingual: True

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm12k,spm12k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/phi-eng/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/phi-eng/opus2m-2020-08-01.test.txt

- src_alpha3: phi

- tgt_alpha3: eng

- short_pair: phi-en

- chrF2_score: 0.391

- bleu: 21.5

- brevity_penalty: 1.0

- ref_len: 2380.0

- src_name: Philippine languages

- tgt_name: English

- train_date: 2020-08-01

- src_alpha2: phi

- tgt_alpha2: en

- prefer_old: False

- long_pair: phi-eng

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41