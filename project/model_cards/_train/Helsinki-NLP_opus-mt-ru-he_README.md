---
language:
- ru
- he

tags:
- translation

license: apache-2.0
---

### ru-he

* source group: Russian 
* target group: Hebrew 
*  OPUS readme: [rus-heb](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-heb/README.md)

*  model: transformer
* source language(s): rus
* target language(s): heb
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-10-04.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-heb/opus-2020-10-04.zip)
* test set translations: [opus-2020-10-04.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-heb/opus-2020-10-04.test.txt)
* test set scores: [opus-2020-10-04.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/rus-heb/opus-2020-10-04.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.rus.heb 	| 36.1 	| 0.569 |


### System Info: 
- hf_name: ru-he

- source_languages: rus

- target_languages: heb

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/rus-heb/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['ru', 'he']

- src_constituents: ('Russian', {'rus'})

- tgt_constituents: ('Hebrew', {'heb'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: rus-heb

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-heb/opus-2020-10-04.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/rus-heb/opus-2020-10-04.test.txt

- src_alpha3: rus

- tgt_alpha3: heb

- chrF2_score: 0.569

- bleu: 36.1

- brevity_penalty: 0.9990000000000001

- ref_len: 15028.0

- src_name: Russian

- tgt_name: Hebrew

- train_date: 2020-10-04 00:00:00

- src_alpha2: ru

- tgt_alpha2: he

- prefer_old: False

- short_pair: ru-he

- helsinki_git_sha: 61fd6908b37d9a7b21cc3e27c1ae1fccedc97561

- transformers_git_sha: b0a907615aca0d728a9bc90f16caef0848f6a435

- port_machine: LM0-400-22516.local

- port_time: 2020-10-26-16:16