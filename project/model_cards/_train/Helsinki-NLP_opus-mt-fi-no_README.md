---
language: 
- fi
- no

tags:
- translation

license: apache-2.0
---

### fin-nor

* source group: Finnish 
* target group: Norwegian 
*  OPUS readme: [fin-nor](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-nor/README.md)

*  model: transformer-align
* source language(s): fin
* target language(s): nno nob
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-nor/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-nor/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-nor/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.fin.nor 	| 23.5 	| 0.426 |


### System Info: 
- hf_name: fin-nor

- source_languages: fin

- target_languages: nor

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-nor/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['fi', 'no']

- src_constituents: {'fin'}

- tgt_constituents: {'nob', 'nno'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/fin-nor/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/fin-nor/opus-2020-06-17.test.txt

- src_alpha3: fin

- tgt_alpha3: nor

- short_pair: fi-no

- chrF2_score: 0.426

- bleu: 23.5

- brevity_penalty: 1.0

- ref_len: 14768.0

- src_name: Finnish

- tgt_name: Norwegian

- train_date: 2020-06-17

- src_alpha2: fi

- tgt_alpha2: no

- prefer_old: False

- long_pair: fin-nor

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41