---
language:
- fi
- en

tags:
- translation

license: apache-2.0
---
### fi-en

* source group: Finnish 
* target group: English 
*  OPUS readme: [fin-eng](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-eng/README.md)

*  model: transformer-align
* source language(s): fin
* target language(s): eng
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opusTCv20210807+bt-2021-08-25.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opusTCv20210807+bt-2021-08-25.zip)
* test set translations: [opusTCv20210807+bt-2021-08-25.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opusTCv20210807+bt-2021-08-25.test.txt)
* test set scores: [opusTCv20210807+bt-2021-08-25.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opusTCv20210807+bt-2021-08-25.eval.txt)

## Benchmarks

| testset | BLEU  | chr-F | #sent | #words | BP |
|---------|-------|-------|-------|--------|----|
| newsdev2015-enfi.fin-eng 	| 27.1 	| 0.550 	| 1500 	| 32104 	| 0.988 |
| newstest2015-enfi.fin-eng 	| 28.5 	| 0.560 	| 1370 	| 27356 	| 0.980 |
| newstest2016-enfi.fin-eng 	| 31.7 	| 0.586 	| 3000 	| 63043 	| 1.000 |
| newstest2017-enfi.fin-eng 	| 34.6 	| 0.610 	| 3002 	| 61936 	| 0.988 |
| newstest2018-enfi.fin-eng 	| 25.4 	| 0.530 	| 3000 	| 62325 	| 0.981 |
| newstest2019-fien.fin-eng 	| 30.6 	| 0.577 	| 1996 	| 36227 	| 0.994 |
| newstestB2016-enfi.fin-eng 	| 25.8 	| 0.538 	| 3000 	| 63043 	| 0.987 |
| newstestB2017-enfi.fin-eng 	| 29.6 	| 0.572 	| 3002 	| 61936 	| 0.999 |
| newstestB2017-fien.fin-eng 	| 29.6 	| 0.572 	| 3002 	| 61936 	| 0.999 |
| Tatoeba-test-v2021-08-07.fin-eng 	| 54.1 	| 0.700 	| 10000 	| 75212 	| 0.988 |


### System Info: 
- hf_name: fi-en
- source_languages: fin
- target_languages: eng
- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-eng/README.md
- original_repo: Tatoeba-Challenge
- tags: ['translation']
- languages: ['fi', 'en']
- src_constituents: ('Finnish', {'fin'})
- tgt_constituents: ('English', {'eng'})
- src_multilingual: False
- tgt_multilingual: False
- long_pair: fin-eng
- prepro:  normalization + SentencePiece (spm32k,spm32k)
- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opusTCv20210807+bt-2021-08-25.zip
- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/fin-eng/opusTCv20210807+bt-2021-08-25.test.txt
- src_alpha3: fin
- tgt_alpha3: eng
- chrF2_score: 0.7
- bleu: 54.1
- src_name: Finnish
- tgt_name: English
- train_date: 2021-08-25 00:00:00
- src_alpha2: fi
- tgt_alpha2: en
- prefer_old: False
- short_pair: fi-en
- helsinki_git_sha: 2ef219d5b67f0afb0c6b732cd07001d84181f002
- transformers_git_sha: 12b4d66a80419db30a15e7b9d4208ceb9887c03b
- port_machine: LM0-400-22516.local
- port_time: 2021-11-04-21:36