---
language:
- es
- he

tags:
- translation

license: apache-2.0
---
### es-he

* source group: Spanish 
* target group: Hebrew 
*  OPUS readme: [spa-heb](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-heb/README.md)

*  model: transformer
* source language(s): spa
* target language(s): heb
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-12-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-heb/opus-2020-12-10.zip)
* test set translations: [opus-2020-12-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-heb/opus-2020-12-10.test.txt)
* test set scores: [opus-2020-12-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-heb/opus-2020-12-10.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.heb 	| 43.6 	| 0.636 |


### System Info: 
- hf_name: es-he

- source_languages: spa

- target_languages: heb

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-heb/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'he']

- src_constituents: ('Spanish', {'spa'})

- tgt_constituents: ('Hebrew', {'heb'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: spa-heb

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-heb/opus-2020-12-10.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-heb/opus-2020-12-10.test.txt

- src_alpha3: spa

- tgt_alpha3: heb

- chrF2_score: 0.636

- bleu: 43.6

- brevity_penalty: 0.992

- ref_len: 12112.0

- src_name: Spanish

- tgt_name: Hebrew

- train_date: 2020-12-10 00:00:00

- src_alpha2: es

- tgt_alpha2: he

- prefer_old: False

- short_pair: es-he

- helsinki_git_sha: b317f78a3ec8a556a481b6a53dc70dc11769ca96

- transformers_git_sha: 1310e1a758edc8e89ec363db76863c771fbeb1de

- port_machine: LM0-400-22516.local

- port_time: 2020-12-11-11:41