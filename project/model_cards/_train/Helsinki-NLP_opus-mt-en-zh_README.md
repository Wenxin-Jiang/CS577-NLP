---
language:
- en
- zh
tags:
- translation
license: apache-2.0
---

### eng-zho

* source group: English 
* target group: Chinese 
*  OPUS readme: [eng-zho](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-zho/README.md)

*  model: transformer
* source language(s): eng
* target language(s): cjy_Hans cjy_Hant cmn cmn_Hans cmn_Hant gan lzh lzh_Hans nan wuu yue yue_Hans yue_Hant
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-07-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zho/opus-2020-07-17.zip)
* test set translations: [opus-2020-07-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zho/opus-2020-07-17.test.txt)
* test set scores: [opus-2020-07-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zho/opus-2020-07-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.eng.zho 	| 31.4 	| 0.268 |


### System Info: 
- hf_name: eng-zho

- source_languages: eng

- target_languages: zho

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-zho/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['en', 'zh']

- src_constituents: {'eng'}

- tgt_constituents: {'cmn_Hans', 'nan', 'nan_Hani', 'gan', 'yue', 'cmn_Kana', 'yue_Hani', 'wuu_Bopo', 'cmn_Latn', 'yue_Hira', 'cmn_Hani', 'cjy_Hans', 'cmn', 'lzh_Hang', 'lzh_Hira', 'cmn_Hant', 'lzh_Bopo', 'zho', 'zho_Hans', 'zho_Hant', 'lzh_Hani', 'yue_Hang', 'wuu', 'yue_Kana', 'wuu_Latn', 'yue_Bopo', 'cjy_Hant', 'yue_Hans', 'lzh', 'cmn_Hira', 'lzh_Yiii', 'lzh_Hans', 'cmn_Bopo', 'cmn_Hang', 'hak_Hani', 'cmn_Yiii', 'yue_Hant', 'lzh_Kana', 'wuu_Hani'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zho/opus-2020-07-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/eng-zho/opus-2020-07-17.test.txt

- src_alpha3: eng

- tgt_alpha3: zho

- short_pair: en-zh

- chrF2_score: 0.268

- bleu: 31.4

- brevity_penalty: 0.8959999999999999

- ref_len: 110468.0

- src_name: English

- tgt_name: Chinese

- train_date: 2020-07-17

- src_alpha2: en

- tgt_alpha2: zh

- prefer_old: False

- long_pair: eng-zho

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41
