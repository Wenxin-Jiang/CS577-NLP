---
language:
- he
- es

tags:
- translation

license: apache-2.0
---
### he-es

* source group: Hebrew 
* target group: Spanish 
*  OPUS readme: [heb-spa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-spa/README.md)

*  model: transformer
* source language(s): heb
* target language(s): spa
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-12-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-spa/opus-2020-12-10.zip)
* test set translations: [opus-2020-12-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-spa/opus-2020-12-10.test.txt)
* test set scores: [opus-2020-12-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-spa/opus-2020-12-10.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.heb.spa 	| 51.3 	| 0.689 |


### System Info: 
- hf_name: he-es

- source_languages: heb

- target_languages: spa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-spa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['he', 'es']

- src_constituents: ('Hebrew', {'heb'})

- tgt_constituents: ('Spanish', {'spa'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: heb-spa

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-spa/opus-2020-12-10.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-spa/opus-2020-12-10.test.txt

- src_alpha3: heb

- tgt_alpha3: spa

- chrF2_score: 0.6890000000000001

- bleu: 51.3

- brevity_penalty: 0.97

- ref_len: 14213.0

- src_name: Hebrew

- tgt_name: Spanish

- train_date: 2020-12-10 00:00:00

- src_alpha2: he

- tgt_alpha2: es

- prefer_old: False

- short_pair: he-es

- helsinki_git_sha: b317f78a3ec8a556a481b6a53dc70dc11769ca96

- transformers_git_sha: 1310e1a758edc8e89ec363db76863c771fbeb1de

- port_machine: LM0-400-22516.local

- port_time: 2020-12-11-09:15