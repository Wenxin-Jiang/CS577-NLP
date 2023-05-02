---
language:
- fr
- it

tags:
- translation

license: apache-2.0
---
### fr-it

* source group: French 
* target group: Italian 
*  OPUS readme: [fra-ita](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fra-ita/README.md)

*  model: transformer-align
* source language(s): fra
* target language(s): ita
* raw source language(s): fra
* raw target language(s): ita
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opusTCv20210807-2021-11-11.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-ita/opusTCv20210807-2021-11-11.zip)
* test set translations: [opusTCv20210807-2021-11-11.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-ita/opusTCv20210807-2021-11-11.test.txt)
* test set scores: [opusTCv20210807-2021-11-11.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fra-ita/opusTCv20210807-2021-11-11.eval.txt)

## Benchmarks

| testset | BLEU  | chr-F | #sent | #words | BP |
|---------|-------|-------|-------|--------|----|
| Tatoeba-test-v2021-08-07.fra-ita 	| 54.8 	| 0.737 	| 10000 	| 61517 	| 0.953 |


### System Info: 
- hf_name: fr-it
- source_languages: fra
- target_languages: ita
- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fra-ita/README.md
- original_repo: Tatoeba-Challenge
- tags: ['translation']
- languages: ['fr', 'it']
- src_constituents: ('French', {'fra'})
- tgt_constituents: ('Italian', {'ita'})
- src_multilingual: False
- tgt_multilingual: False
- long_pair: fra-ita
- prepro:  normalization + SentencePiece (spm32k,spm32k)
- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/fra-ita/opusTCv20210807-2021-11-11.zip
- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/fra-ita/opusTCv20210807-2021-11-11.test.txt
- src_alpha3: fra
- tgt_alpha3: ita
- chrF2_score: 0.737
- bleu: 54.8
- src_name: French
- tgt_name: Italian
- train_date: 2021-11-11 00:00:00
- src_alpha2: fr
- tgt_alpha2: it
- prefer_old: False
- short_pair: fr-it
- helsinki_git_sha: 7ab0c987850187e0b10342bfc616cd47c027ba18
- transformers_git_sha: df1f94eb4a18b1a27d27e32040b60a17410d516e
- port_machine: LM0-400-22516.local
- port_time: 2021-11-11-19:40