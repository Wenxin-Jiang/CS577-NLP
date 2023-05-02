---
language:
- en
- tr

tags:
- translation

license: apache-2.0
---
### en-tr

* source group: English 
* target group: Turkish 
*  OPUS readme: [eng-tur](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-tur/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): tur
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus+bt-2021-04-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tur/opus+bt-2021-04-10.zip)
* test set translations: [opus+bt-2021-04-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tur/opus+bt-2021-04-10.test.txt)
* test set scores: [opus+bt-2021-04-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tur/opus+bt-2021-04-10.eval.txt)

## Benchmarks

| testset | BLEU  | chr-F | #sent | #words | BP |
|---------|-------|-------|-------|--------|----|
| newsdev2016-entr.eng-tur 	| 21.5 	| 0.575 	| 1001 	| 16127 	| 1.000 |
| newstest2016-entr.eng-tur 	| 21.4 	| 0.558 	| 3000 	| 50782 	| 0.986 |
| newstest2017-entr.eng-tur 	| 22.8 	| 0.572 	| 3007 	| 51977 	| 0.960 |
| newstest2018-entr.eng-tur 	| 20.8 	| 0.561 	| 3000 	| 53731 	| 0.963 |
| Tatoeba-test.eng-tur 	| 41.5 	| 0.684 	| 10000 	| 60469 	| 0.932 |


### System Info: 
- hf_name: en-tr
- source_languages: eng
- target_languages: tur
- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-tur/README.md
- original_repo: Tatoeba-Challenge
- tags: ['translation']
- languages: ['en', 'tr']
- src_constituents: ('English', {'eng'})
- tgt_constituents: ('Turkish', {'tur'})
- src_multilingual: False
- tgt_multilingual: False
- long_pair: eng-tur
- prepro:  normalization + SentencePiece (spm32k,spm32k)
- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tur/opus+bt-2021-04-10.zip
- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tur/opus+bt-2021-04-10.test.txt
- src_alpha3: eng
- tgt_alpha3: tur
- chrF2_score: 0.684
- bleu: 41.5
- src_name: English
- tgt_name: Turkish
- train_date: 2021-04-10 00:00:00
- src_alpha2: en
- tgt_alpha2: tr
- prefer_old: False
- short_pair: en-tr
- helsinki_git_sha: a6bd0607aec9603811b2b635aec3f566f3add79d
- transformers_git_sha: 12b4d66a80419db30a15e7b9d4208ceb9887c03b
- port_machine: LM0-400-22516.local
- port_time: 2021-10-05-12:13