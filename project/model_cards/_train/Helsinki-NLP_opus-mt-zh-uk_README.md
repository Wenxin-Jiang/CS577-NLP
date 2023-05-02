---
language: 
- zh
- uk

tags:
- translation

license: apache-2.0
---

### zho-ukr

* source group: Chinese 
* target group: Ukrainian 
*  OPUS readme: [zho-ukr](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zho-ukr/README.md)

*  model: transformer-align
* source language(s): cmn cmn_Bopo cmn_Hang cmn_Hani cmn_Kana cmn_Latn cmn_Yiii yue_Bopo yue_Hang yue_Hani yue_Hira yue_Kana
* target language(s): ukr
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm4k)
* download original weights: [opus-2020-06-16.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ukr/opus-2020-06-16.zip)
* test set translations: [opus-2020-06-16.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ukr/opus-2020-06-16.test.txt)
* test set scores: [opus-2020-06-16.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ukr/opus-2020-06-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.zho.ukr 	| 10.4 	| 0.259 |


### System Info: 
- hf_name: zho-ukr

- source_languages: zho

- target_languages: ukr

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zho-ukr/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['zh', 'uk']

- src_constituents: {'cmn_Hans', 'nan', 'nan_Hani', 'gan', 'yue', 'cmn_Kana', 'yue_Hani', 'wuu_Bopo', 'cmn_Latn', 'yue_Hira', 'cmn_Hani', 'cjy_Hans', 'cmn', 'lzh_Hang', 'lzh_Hira', 'cmn_Hant', 'lzh_Bopo', 'zho', 'zho_Hans', 'zho_Hant', 'lzh_Hani', 'yue_Hang', 'wuu', 'yue_Kana', 'wuu_Latn', 'yue_Bopo', 'cjy_Hant', 'yue_Hans', 'lzh', 'cmn_Hira', 'lzh_Yiii', 'lzh_Hans', 'cmn_Bopo', 'cmn_Hang', 'hak_Hani', 'cmn_Yiii', 'yue_Hant', 'lzh_Kana', 'wuu_Hani'}

- tgt_constituents: {'ukr'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm4k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ukr/opus-2020-06-16.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ukr/opus-2020-06-16.test.txt

- src_alpha3: zho

- tgt_alpha3: ukr

- short_pair: zh-uk

- chrF2_score: 0.259

- bleu: 10.4

- brevity_penalty: 0.9059999999999999

- ref_len: 9193.0

- src_name: Chinese

- tgt_name: Ukrainian

- train_date: 2020-06-16

- src_alpha2: zh

- tgt_alpha2: uk

- prefer_old: False

- long_pair: zho-ukr

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41