---
language: 
- eo
- fi

tags:
- translation

license: apache-2.0
---

### epo-fin

* source group: Esperanto 
* target group: Finnish 
*  OPUS readme: [epo-fin](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-fin/README.md)

*  model: transformer-align
* source language(s): epo
* target language(s): fin
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-fin/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-fin/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/epo-fin/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.epo.fin 	| 15.9 	| 0.371 |


### System Info: 
- hf_name: epo-fin

- source_languages: epo

- target_languages: fin

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/epo-fin/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['eo', 'fi']

- src_constituents: {'epo'}

- tgt_constituents: {'fin'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-fin/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/epo-fin/opus-2020-06-16.test.txt

- src_alpha3: epo

- tgt_alpha3: fin

- short_pair: eo-fi

- chrF2_score: 0.371

- bleu: 15.9

- brevity_penalty: 0.894

- ref_len: 15881.0

- src_name: Esperanto

- tgt_name: Finnish

- train_date: 2020-06-16

- src_alpha2: eo

- tgt_alpha2: fi

- prefer_old: False

- long_pair: epo-fin

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41