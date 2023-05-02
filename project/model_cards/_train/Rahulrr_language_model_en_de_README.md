---
language:
- en
- de

tags:
- translation

license: apache-2.0
---
### en-de

* source group: English 
* target group: German 
*  OPUS readme: [eng-deu](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-deu/README.md)

*  model: transformer-big
* source language(s): eng
* target language(s): deu
* raw source language(s): eng
* raw target language(s): deu
* model: transformer-big
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opusTCv20210807+bt-2021-12-08.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-deu/opusTCv20210807+bt-2021-12-08.zip)
* test set translations: [opusTCv20210807+bt-2021-12-08.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-deu/opusTCv20210807+bt-2021-12-08.test.txt)
* test set scores: [opusTCv20210807+bt-2021-12-08.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-deu/opusTCv20210807+bt-2021-12-08.eval.txt)

## Benchmarks

| testset | BLEU  | chr-F | #sent | #words | BP |
|---------|-------|-------|-------|--------|----|
| newssyscomb2009.eng-deu 	| 24.3 	| 0.5462 	| 502 	| 11271 	| 0.993 |
| news-test2008.eng-deu 	| 24.7 	| 0.5412 	| 2051 	| 47427 	| 1.000 |
| newstest2009.eng-deu 	| 23.6 	| 0.5385 	| 2525 	| 62816 	| 0.999 |
| newstest2010.eng-deu 	| 26.9 	| 0.5589 	| 2489 	| 61511 	| 0.966 |
| newstest2011.eng-deu 	| 24.1 	| 0.5364 	| 3003 	| 72981 	| 0.990 |
| newstest2012.eng-deu 	| 24.6 	| 0.5375 	| 3003 	| 72886 	| 0.972 |
| newstest2013.eng-deu 	| 28.3 	| 0.5636 	| 3000 	| 63737 	| 0.988 |
| newstest2014-deen.eng-deu 	| 30.9 	| 0.6084 	| 3003 	| 62964 	| 1.000 |
| newstest2015-ende.eng-deu 	| 33.2 	| 0.6106 	| 2169 	| 44260 	| 1.000 |
| newstest2016-ende.eng-deu 	| 39.8 	| 0.6595 	| 2999 	| 62670 	| 0.993 |
| newstest2017-ende.eng-deu 	| 32.0 	| 0.6047 	| 3004 	| 61291 	| 1.000 |
| newstest2018-ende.eng-deu 	| 48.8 	| 0.7146 	| 2998 	| 64276 	| 1.000 |
| newstest2019-ende.eng-deu 	| 45.0 	| 0.6821 	| 1997 	| 48969 	| 0.995 |
| Tatoeba-test-v2021-08-07.eng-deu 	| 43.7 	| 0.6442 	| 10000 	| 85728 	| 1.000 |


### System Info: 
- hf_name: en-de
- source_languages: eng
- target_languages: deu
- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-deu/README.md
- original_repo: Tatoeba-Challenge
- tags: ['translation']
- languages: ['en', 'de']
- src_constituents: ('English', {'eng'})
- tgt_constituents: ('German', {'deu'})
- src_multilingual: False
- tgt_multilingual: False
- long_pair: eng-deu
- prepro:  normalization + SentencePiece (spm32k,spm32k)
- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-deu/opusTCv20210807+bt-2021-12-08.zip
- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-deu/opusTCv20210807+bt-2021-12-08.test.txt
- src_alpha3: eng
- tgt_alpha3: deu
- chrF2_score: 0.6442
- bleu: 43.7
- src_name: English
- tgt_name: German
- train_date: 2021-12-08 00:00:00
- src_alpha2: en
- tgt_alpha2: de
- prefer_old: False
- short_pair: en-de
- helsinki_git_sha: c4e978d8de47875b482653b423dcfe968979d7d5
- transformers_git_sha: 56b83cf049823ed074a655eceb28f31e2077c6eb
- port_machine: LAPIN4GLQ2G3
- port_time: 2022-06-27-16:10