---
language: 
- fi
- eo

tags:
- translation

license: apache-2.0
---

### fin-epo

* source group: Finnish 
* target group: Esperanto 
*  OPUS readme: [fin-epo](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-epo/README.md)

*  model: transformer-align
* source language(s): fin
* target language(s): epo
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm4k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-epo/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-epo/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/fin-epo/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.fin.epo 	| 22.5 	| 0.413 |


### System Info: 
- hf_name: fin-epo

- source_languages: fin

- target_languages: epo

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/fin-epo/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['fi', 'eo']

- src_constituents: {'fin'}

- tgt_constituents: {'epo'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm4k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/fin-epo/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/fin-epo/opus-2020-06-16.test.txt

- src_alpha3: fin

- tgt_alpha3: epo

- short_pair: fi-eo

- chrF2_score: 0.413

- bleu: 22.5

- brevity_penalty: 0.9490000000000001

- ref_len: 18881.0

- src_name: Finnish

- tgt_name: Esperanto

- train_date: 2020-06-16

- src_alpha2: fi

- tgt_alpha2: eo

- prefer_old: False

- long_pair: fin-epo

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41