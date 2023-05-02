---
language:
- en
- he

tags:
- translation

license: apache-2.0
---
### en-he

* source group: English 
* target group: Hebrew 
*  OPUS readme: [eng-heb](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-heb/README.md)

*  model: transformer-align
* source language(s): eng
* target language(s): heb
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus+bt-2021-04-13.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-heb/opus+bt-2021-04-13.zip)
* test set translations: [opus+bt-2021-04-13.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-heb/opus+bt-2021-04-13.test.txt)
* test set scores: [opus+bt-2021-04-13.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-heb/opus+bt-2021-04-13.eval.txt)

## Benchmarks

| testset | BLEU  | chr-F | #sent | #words | BP |
|---------|-------|-------|-------|--------|----|
| Tatoeba-test.eng-heb 	| 37.8 	| 0.601 	| 10000 	| 60359 	| 1.000 |


### System Info: 
- hf_name: en-he
- source_languages: eng
- target_languages: heb
- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-heb/README.md
- original_repo: Tatoeba-Challenge
- tags: ['translation']
- languages: ['en', 'he']
- src_constituents: ('English', {'eng'})
- tgt_constituents: ('Hebrew', {'heb'})
- src_multilingual: False
- tgt_multilingual: False
- long_pair: eng-heb
- prepro:  normalization + SentencePiece (spm32k,spm32k)
- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-heb/opus+bt-2021-04-13.zip
- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-heb/opus+bt-2021-04-13.test.txt
- src_alpha3: eng
- tgt_alpha3: heb
- chrF2_score: 0.601
- bleu: 37.8
- src_name: English
- tgt_name: Hebrew
- train_date: 2021-04-13 00:00:00
- src_alpha2: en
- tgt_alpha2: he
- prefer_old: False
- short_pair: en-he
- helsinki_git_sha: c4e978d8de47875b482653b423dcfe968979d7d5
- transformers_git_sha: 56b83cf049823ed074a655eceb28f31e2077c6eb
- port_machine: LAPIN4GLQ2G3
- port_time: 2022-06-22-19:47