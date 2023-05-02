---
language:
- he
- it

tags:
- translation

license: apache-2.0
---
### he-it

* source group: Hebrew 
* target group: Italian 
*  OPUS readme: [heb-ita](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-ita/README.md)

*  model: transformer
* source language(s): heb
* target language(s): ita
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-12-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ita/opus-2020-12-10.zip)
* test set translations: [opus-2020-12-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ita/opus-2020-12-10.test.txt)
* test set scores: [opus-2020-12-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ita/opus-2020-12-10.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.heb.ita 	| 41.1 	| 0.643 |


### System Info: 
- hf_name: he-it

- source_languages: heb

- target_languages: ita

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-ita/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['he', 'it']

- src_constituents: ('Hebrew', {'heb'})

- tgt_constituents: ('Italian', {'ita'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: heb-ita

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ita/opus-2020-12-10.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-ita/opus-2020-12-10.test.txt

- src_alpha3: heb

- tgt_alpha3: ita

- chrF2_score: 0.643

- bleu: 41.1

- brevity_penalty: 0.997

- ref_len: 11464.0

- src_name: Hebrew

- tgt_name: Italian

- train_date: 2020-12-10 00:00:00

- src_alpha2: he

- tgt_alpha2: it

- prefer_old: False

- short_pair: he-it

- helsinki_git_sha: b317f78a3ec8a556a481b6a53dc70dc11769ca96

- transformers_git_sha: 1310e1a758edc8e89ec363db76863c771fbeb1de

- port_machine: LM0-400-22516.local

- port_time: 2020-12-11-16:01