---
language:
- en
- ro

tags:
- translation

license: apache-2.0
---
### en-ro

* source group: English 
* target group: Romanian 
*  OPUS readme: [eng-ron](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-ron/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): mol ron
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* valid language labels: 
* download original weights: [opus+bt-2021-03-07.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ron/opus+bt-2021-03-07.zip)
* test set translations: [opus+bt-2021-03-07.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ron/opus+bt-2021-03-07.test.txt)
* test set scores: [opus+bt-2021-03-07.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ron/opus+bt-2021-03-07.eval.txt)

## Benchmarks

| testset | BLEU  | chr-F | #sent | #words | BP |
|---------|-------|-------|-------|--------|----|
| newsdev2016-enro.eng-ron 	| 33.5 	| 0.610 	| 1999 	| 51566 	| 0.984 |
| newstest2016-enro.eng-ron 	| 31.7 	| 0.591 	| 1999 	| 49094 	| 0.998 |
| Tatoeba-test.eng-ron 	| 46.9 	| 0.678 	| 5000 	| 36851 	| 0.983 |


### System Info: 
- hf_name: en-ro
- source_languages: eng
- target_languages: ron
- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-ron/README.md
- original_repo: Tatoeba-Challenge
- tags: ['translation']
- languages: ['en', 'ro']
- src_constituents: ('English', {'eng'})
- tgt_constituents: ('Romanian', {'ron'})
- src_multilingual: False
- tgt_multilingual: False
- long_pair: eng-ron
- prepro:  normalization + SentencePiece (spm32k,spm32k)
- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ron/opus+bt-2021-03-07.zip
- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ron/opus+bt-2021-03-07.test.txt
- src_alpha3: eng
- tgt_alpha3: ron
- chrF2_score: 0.678
- bleu: 46.9
- src_name: English
- tgt_name: Romanian
- train_date: 2021-03-07 00:00:00
- src_alpha2: en
- tgt_alpha2: ro
- prefer_old: False
- short_pair: en-ro
- helsinki_git_sha: 2ef219d5b67f0afb0c6b732cd07001d84181f002
- transformers_git_sha: 12b4d66a80419db30a15e7b9d4208ceb9887c03b
- port_machine: LM0-400-22516.local
- port_time: 2021-11-08-09:31