---
language: 
- zh
- bg

tags:
- translation

license: apache-2.0
---

### zho-bul

* source group: Chinese 
* target group: Bulgarian 
*  OPUS readme: [zho-bul](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zho-bul/README.md)

*  model: transformer
* source language(s): cmn cmn_Hans cmn_Hant zho zho_Hans zho_Hant
* target language(s): bul
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-07-03.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-bul/opus-2020-07-03.zip)
* test set translations: [opus-2020-07-03.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-bul/opus-2020-07-03.test.txt)
* test set scores: [opus-2020-07-03.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-bul/opus-2020-07-03.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.cmn_Hani.bul 	| 29.6 	| 0.497 |
| Tatoeba-test.zho.bul 	| 29.6 	| 0.497 |


### System Info: 
- hf_name: zho-bul

- source_languages: zho

- target_languages: bul

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zho-bul/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['zh', 'bg']

- src_constituents: {'cmn_Hans', 'nan', 'nan_Hani', 'gan', 'yue', 'cmn_Kana', 'yue_Hani', 'wuu_Bopo', 'cmn_Latn', 'yue_Hira', 'cmn_Hani', 'cjy_Hans', 'cmn', 'lzh_Hang', 'lzh_Hira', 'cmn_Hant', 'lzh_Bopo', 'zho', 'zho_Hans', 'zho_Hant', 'lzh_Hani', 'yue_Hang', 'wuu', 'yue_Kana', 'wuu_Latn', 'yue_Bopo', 'cjy_Hant', 'yue_Hans', 'lzh', 'cmn_Hira', 'lzh_Yiii', 'lzh_Hans', 'cmn_Bopo', 'cmn_Hang', 'hak_Hani', 'cmn_Yiii', 'yue_Hant', 'lzh_Kana', 'wuu_Hani'}

- tgt_constituents: {'bul', 'bul_Latn'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zho-bul/opus-2020-07-03.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zho-bul/opus-2020-07-03.test.txt

- src_alpha3: zho

- tgt_alpha3: bul

- short_pair: zh-bg

- chrF2_score: 0.49700000000000005

- bleu: 29.6

- brevity_penalty: 0.883

- ref_len: 3113.0

- src_name: Chinese

- tgt_name: Bulgarian

- train_date: 2020-07-03

- src_alpha2: zh

- tgt_alpha2: bg

- prefer_old: False

- long_pair: zho-bul

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41