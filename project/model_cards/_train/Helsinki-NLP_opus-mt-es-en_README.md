---
language: 
- es
- en

tags:
- translation

license: apache-2.0
---

### spa-eng

* source group: Spanish 
* target group: English 
*  OPUS readme: [spa-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-eng/README.md)

*  model: transformer
* source language(s): spa
* target language(s): eng
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-08-18.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eng/opus-2020-08-18.zip)
* test set translations: [opus-2020-08-18.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eng/opus-2020-08-18.test.txt)
* test set scores: [opus-2020-08-18.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eng/opus-2020-08-18.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009-spaeng.spa.eng 	| 30.6 	| 0.570 |
| news-test2008-spaeng.spa.eng 	| 27.9 	| 0.553 |
| newstest2009-spaeng.spa.eng 	| 30.4 	| 0.572 |
| newstest2010-spaeng.spa.eng 	| 36.1 	| 0.614 |
| newstest2011-spaeng.spa.eng 	| 34.2 	| 0.599 |
| newstest2012-spaeng.spa.eng 	| 37.9 	| 0.624 |
| newstest2013-spaeng.spa.eng 	| 35.3 	| 0.609 |
| Tatoeba-test.spa.eng 	| 59.6 	| 0.739 |


### System Info: 
- hf_name: spa-eng

- source_languages: spa

- target_languages: eng

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-eng/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'en']

- src_constituents: {'spa'}

- tgt_constituents: {'eng'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eng/opus-2020-08-18.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-eng/opus-2020-08-18.test.txt

- src_alpha3: spa

- tgt_alpha3: eng

- short_pair: es-en

- chrF2_score: 0.7390000000000001

- bleu: 59.6

- brevity_penalty: 0.9740000000000001

- ref_len: 79376.0

- src_name: Spanish

- tgt_name: English

- train_date: 2020-08-18 00:00:00

- src_alpha2: es

- tgt_alpha2: en

- prefer_old: False

- long_pair: spa-eng

- helsinki_git_sha: d2f0910c89026c34a44e331e785dec1e0faa7b82

- transformers_git_sha: f7af09b4524b784d67ae8526f0e2fcc6f5ed0de9

- port_machine: brutasse

- port_time: 2020-08-24-18:20