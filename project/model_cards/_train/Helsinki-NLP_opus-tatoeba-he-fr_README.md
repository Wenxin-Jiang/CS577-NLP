---
language:
- he
- fr

tags:
- translation

license: apache-2.0
---
### he-fr

* source group: Hebrew 
* target group: French 
*  OPUS readme: [heb-fra](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-fra/README.md)

*  model: transformer
* source language(s): heb
* target language(s): fra
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-12-10.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-fra/opus-2020-12-10.zip)
* test set translations: [opus-2020-12-10.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-fra/opus-2020-12-10.test.txt)
* test set scores: [opus-2020-12-10.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/heb-fra/opus-2020-12-10.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.heb.fra 	| 47.3 	| 0.644 |


### System Info: 
- hf_name: he-fr

- source_languages: heb

- target_languages: fra

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/heb-fra/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['he', 'fr']

- src_constituents: ('Hebrew', {'heb'})

- tgt_constituents: ('French', {'fra'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: heb-fra

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-fra/opus-2020-12-10.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/heb-fra/opus-2020-12-10.test.txt

- src_alpha3: heb

- tgt_alpha3: fra

- chrF2_score: 0.644

- bleu: 47.3

- brevity_penalty: 0.9740000000000001

- ref_len: 26123.0

- src_name: Hebrew

- tgt_name: French

- train_date: 2020-12-10 00:00:00

- src_alpha2: he

- tgt_alpha2: fr

- prefer_old: False

- short_pair: he-fr

- helsinki_git_sha: b317f78a3ec8a556a481b6a53dc70dc11769ca96

- transformers_git_sha: 1310e1a758edc8e89ec363db76863c771fbeb1de

- port_machine: LM0-400-22516.local

- port_time: 2020-12-11-16:03