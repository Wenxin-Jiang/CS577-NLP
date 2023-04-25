---
language:
- he
- ru

tags:
- translation

license: apache-2.0
---

### he-ru

* source group: Hebrew 
* target group: Russian 
*  OPUS readme: [heb-rus](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-rus/README.md)

*  model: transformer
* source language(s): heb
* target language(s): rus
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-10-04.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-rus/opus-2020-10-04.zip)
* test set translations: [opus-2020-10-04.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-rus/opus-2020-10-04.test.txt)
* test set scores: [opus-2020-10-04.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-rus/opus-2020-10-04.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.heb.rus 	| 40.5 	| 0.599 |


### System Info: 
- hf_name: he-ru

- source_languages: heb

- target_languages: rus

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-rus/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['he', 'ru']

- src_constituents: ('Hebrew', {'heb'})

- tgt_constituents: ('Russian', {'rus'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: heb-rus

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-rus/opus-2020-10-04.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-rus/opus-2020-10-04.test.txt

- src_alpha3: heb

- tgt_alpha3: rus

- chrF2_score: 0.599

- bleu: 40.5

- brevity_penalty: 0.963

- ref_len: 16583.0

- src_name: Hebrew

- tgt_name: Russian

- train_date: 2020-10-04 00:00:00

- src_alpha2: he

- tgt_alpha2: ru

- prefer_old: False

- short_pair: he-ru

- helsinki_git_sha: 61fd6908b37d9a7b21cc3e27c1ae1fccedc97561

- transformers_git_sha: b0a907615aca0d728a9bc90f16caef0848f6a435

- port_machine: LM0-400-22516.local

- port_time: 2020-10-26-16:16