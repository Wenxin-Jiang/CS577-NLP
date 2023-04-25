---
language:
- it
- he

tags:
- translation

license: apache-2.0
---
### it-he

* source group: Italian 
* target group: Hebrew 
*  OPUS readme: [ita-heb](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-heb/README.md)

*  model: transformer
* source language(s): ita
* target language(s): heb
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-12-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-heb/opus-2020-12-10.zip)
* test set translations: [opus-2020-12-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-heb/opus-2020-12-10.test.txt)
* test set scores: [opus-2020-12-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/ita-heb/opus-2020-12-10.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.ita.heb 	| 38.5 	| 0.593 |


### System Info: 
- hf_name: it-he

- source_languages: ita

- target_languages: heb

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/ita-heb/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['it', 'he']

- src_constituents: ('Italian', {'ita'})

- tgt_constituents: ('Hebrew', {'heb'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: ita-heb

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-heb/opus-2020-12-10.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/ita-heb/opus-2020-12-10.test.txt

- src_alpha3: ita

- tgt_alpha3: heb

- chrF2_score: 0.593

- bleu: 38.5

- brevity_penalty: 0.985

- ref_len: 9796.0

- src_name: Italian

- tgt_name: Hebrew

- train_date: 2020-12-10 00:00:00

- src_alpha2: it

- tgt_alpha2: he

- prefer_old: False

- short_pair: it-he

- helsinki_git_sha: b317f78a3ec8a556a481b6a53dc70dc11769ca96

- transformers_git_sha: 1310e1a758edc8e89ec363db76863c771fbeb1de

- port_machine: LM0-400-22516.local

- port_time: 2020-12-11-16:02