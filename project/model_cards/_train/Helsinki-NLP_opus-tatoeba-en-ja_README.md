---
language:
- en
- ja

tags:
- translation

license: apache-2.0
---
### en-ja

* source group: English 
* target group: Japanese 
*  OPUS readme: [eng-jpn](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-jpn/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): jpn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus+bt-2021-04-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-jpn/opus+bt-2021-04-10.zip)
* test set translations: [opus+bt-2021-04-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-jpn/opus+bt-2021-04-10.test.txt)
* test set scores: [opus+bt-2021-04-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-jpn/opus+bt-2021-04-10.eval.txt)

## Benchmarks

| testset | BLEU  | chr-F | #sent | #words | BP |
|---------|-------|-------|-------|--------|----|
| Tatoeba-test.eng-jpn 	| 15.2 	| 0.258 	| 10000 	| 99206 	| 1.000 |


### System Info: 
- hf_name: en-ja
- source_languages: eng
- target_languages: jpn
- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-jpn/README.md
- original_repo: Tatoeba-Challenge
- tags: ['translation']
- languages: ['en', 'ja']
- src_constituents: ('English', {'eng'})
- tgt_constituents: ('Japanese', {'jpn', 'jpn_Latn', 'jpn_Yiii', 'jpn_Kana', 'jpn_Hira', 'jpn_Hang', 'jpn_Bopo', 'jpn_Hani'})
- src_multilingual: False
- tgt_multilingual: False
- long_pair: eng-jpn
- prepro:  normalization + SentencePiece (spm32k,spm32k)
- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-jpn/opus+bt-2021-04-10.zip
- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-jpn/opus+bt-2021-04-10.test.txt
- src_alpha3: eng
- tgt_alpha3: jpn
- chrF2_score: 0.258
- bleu: 15.2
- src_name: English
- tgt_name: Japanese
- train_date: 2021-04-10 00:00:00
- src_alpha2: en
- tgt_alpha2: ja
- prefer_old: False
- short_pair: en-ja
- helsinki_git_sha: 70b0a9621f054ef1d8ea81f7d55595d7f64d19ff
- transformers_git_sha: 12b4d66a80419db30a15e7b9d4208ceb9887c03b
- port_machine: LM0-400-22516.local
- port_time: 2021-10-12-11:13