---
language:
- de
- ro

tags:
- translation

license: apache-2.0
---
### de-ro

* source group: German 
* target group: Romanian 
*  OPUS readme: [deu-ron](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-ron/README.md)

*  model: transformer-align
* source language(s): deu
* target language(s): mol ron
* raw source language(s): deu
* raw target language(s): mol ron
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* valid language labels: >>mol<< >>ron<<
* download original weights: [opusTCv20210807-2021-10-22.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ron/opusTCv20210807-2021-10-22.zip)
* test set translations: [opusTCv20210807-2021-10-22.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ron/opusTCv20210807-2021-10-22.test.txt)
* test set scores: [opusTCv20210807-2021-10-22.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ron/opusTCv20210807-2021-10-22.eval.txt)

## Benchmarks

| testset | BLEU  | chr-F | #sent | #words | BP |
|---------|-------|-------|-------|--------|----|
| Tatoeba-test-v2021-08-07.deu-ron 	| 42.0 	| 0.636 	| 1141 	| 7432 	| 0.976 |


### System Info: 
- hf_name: de-ro
- source_languages: deu
- target_languages: ron
- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/deu-ron/README.md
- original_repo: Tatoeba-Challenge
- tags: ['translation']
- languages: ['de', 'ro']
- src_constituents: ('German', {'deu'})
- tgt_constituents: ('Romanian', {'ron'})
- src_multilingual: False
- tgt_multilingual: False
- long_pair: deu-ron
- prepro:  normalization + SentencePiece (spm32k,spm32k)
- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ron/opusTCv20210807-2021-10-22.zip
- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/deu-ron/opusTCv20210807-2021-10-22.test.txt
- src_alpha3: deu
- tgt_alpha3: ron
- chrF2_score: 0.636
- bleu: 42.0
- src_name: German
- tgt_name: Romanian
- train_date: 2021-10-22 00:00:00
- src_alpha2: de
- tgt_alpha2: ro
- prefer_old: False
- short_pair: de-ro
- helsinki_git_sha: 2ef219d5b67f0afb0c6b732cd07001d84181f002
- transformers_git_sha: df1f94eb4a18b1a27d27e32040b60a17410d516e
- port_machine: LM0-400-22516.local
- port_time: 2021-11-08-16:45