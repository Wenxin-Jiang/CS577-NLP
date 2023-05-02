---
language: 
- zh
- ms

tags:
- translation

license: apache-2.0
---

### zho-msa

* source group: Chinese 
* target group: Malay (macrolanguage) 
*  OPUS readme: [zho-msa](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zho-msa/README.md)

*  model: transformer-align
* source language(s): cmn_Bopo cmn_Hani cmn_Latn hak_Hani yue_Bopo yue_Hani
* target language(s): ind zsm_Latn
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-msa/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-msa/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-msa/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.zho.msa 	| 13.9 	| 0.390 |


### System Info: 
- hf_name: zho-msa

- source_languages: zho

- target_languages: msa

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zho-msa/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['zh', 'ms']

- src_constituents: {'cmn_Hans', 'nan', 'nan_Hani', 'gan', 'yue', 'cmn_Kana', 'yue_Hani', 'wuu_Bopo', 'cmn_Latn', 'yue_Hira', 'cmn_Hani', 'cjy_Hans', 'cmn', 'lzh_Hang', 'lzh_Hira', 'cmn_Hant', 'lzh_Bopo', 'zho', 'zho_Hans', 'zho_Hant', 'lzh_Hani', 'yue_Hang', 'wuu', 'yue_Kana', 'wuu_Latn', 'yue_Bopo', 'cjy_Hant', 'yue_Hans', 'lzh', 'cmn_Hira', 'lzh_Yiii', 'lzh_Hans', 'cmn_Bopo', 'cmn_Hang', 'hak_Hani', 'cmn_Yiii', 'yue_Hant', 'lzh_Kana', 'wuu_Hani'}

- tgt_constituents: {'zsm_Latn', 'ind', 'max_Latn', 'zlm_Latn', 'min'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zho-msa/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zho-msa/opus-2020-06-17.test.txt

- src_alpha3: zho

- tgt_alpha3: msa

- short_pair: zh-ms

- chrF2_score: 0.39

- bleu: 13.9

- brevity_penalty: 0.9229999999999999

- ref_len: 2762.0

- src_name: Chinese

- tgt_name: Malay (macrolanguage)

- train_date: 2020-06-17

- src_alpha2: zh

- tgt_alpha2: ms

- prefer_old: False

- long_pair: zho-msa

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41