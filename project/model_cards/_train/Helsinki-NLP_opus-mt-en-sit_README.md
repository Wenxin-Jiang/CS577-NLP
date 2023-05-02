---
language: 
- en
- sit

tags:
- translation

license: apache-2.0
---

### eng-sit

* source group: English 
* target group: Sino-Tibetan languages 
*  OPUS readme: [eng-sit](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-sit/README.md)

*  model: transformer
* source language(s): eng
* target language(s): bod brx brx_Latn cjy_Hans cjy_Hant cmn cmn_Hans cmn_Hant gan lzh lzh_Hans mya nan wuu yue yue_Hans yue_Hant zho zho_Hans zho_Hant
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus2m-2020-08-01.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sit/opus2m-2020-08-01.zip)
* test set translations: [opus2m-2020-08-01.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sit/opus2m-2020-08-01.test.txt)
* test set scores: [opus2m-2020-08-01.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sit/opus2m-2020-08-01.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2017-enzh-engzho.eng.zho 	| 23.5 	| 0.217 |
| newstest2017-enzh-engzho.eng.zho 	| 23.2 	| 0.223 |
| newstest2018-enzh-engzho.eng.zho 	| 25.0 	| 0.230 |
| newstest2019-enzh-engzho.eng.zho 	| 20.2 	| 0.225 |
| Tatoeba-test.eng-bod.eng.bod 	| 0.4 	| 0.147 |
| Tatoeba-test.eng-brx.eng.brx 	| 0.5 	| 0.012 |
| Tatoeba-test.eng.multi 	| 25.7 	| 0.223 |
| Tatoeba-test.eng-mya.eng.mya 	| 0.2 	| 0.222 |
| Tatoeba-test.eng-zho.eng.zho 	| 29.2 	| 0.249 |


### System Info: 
- hf_name: eng-sit

- source_languages: eng

- target_languages: sit

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-sit/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'sit']

- src_constituents: {'eng'}

- tgt_constituents: set()

- src_multilingual: False

- tgt_multilingual: True

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sit/opus2m-2020-08-01.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-sit/opus2m-2020-08-01.test.txt

- src_alpha3: eng

- tgt_alpha3: sit

- short_pair: en-sit

- chrF2_score: 0.223

- bleu: 25.7

- brevity_penalty: 0.907

- ref_len: 109538.0

- src_name: English

- tgt_name: Sino-Tibetan languages

- train_date: 2020-08-01

- src_alpha2: en

- tgt_alpha2: sit

- prefer_old: False

- long_pair: eng-sit

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41