---
language: 
- zh
- it

tags:
- translation

license: apache-2.0
---

### zho-ita

* source group: Chinese 
* target group: Italian 
*  OPUS readme: [zho-ita](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zho-ita/README.md)

*  model: transformer-align
* source language(s): cmn cmn_Bopo cmn_Hang cmn_Hani cmn_Hira cmn_Kana cmn_Latn lzh lzh_Hang lzh_Hani lzh_Hira lzh_Yiii wuu_Bopo wuu_Hani wuu_Latn yue_Hani
* target language(s): ita
* model: transformer-align
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* download original weights: [opus-2020-06-17.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ita/opus-2020-06-17.zip)
* test set translations: [opus-2020-06-17.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ita/opus-2020-06-17.test.txt)
* test set scores: [opus-2020-06-17.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ita/opus-2020-06-17.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.zho.ita 	| 27.9 	| 0.508 |


### System Info: 
- hf_name: zho-ita

- source_languages: zho

- target_languages: ita

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/zho-ita/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['zh', 'it']

- src_constituents: {'cmn_Hans', 'nan', 'nan_Hani', 'gan', 'yue', 'cmn_Kana', 'yue_Hani', 'wuu_Bopo', 'cmn_Latn', 'yue_Hira', 'cmn_Hani', 'cjy_Hans', 'cmn', 'lzh_Hang', 'lzh_Hira', 'cmn_Hant', 'lzh_Bopo', 'zho', 'zho_Hans', 'zho_Hant', 'lzh_Hani', 'yue_Hang', 'wuu', 'yue_Kana', 'wuu_Latn', 'yue_Bopo', 'cjy_Hant', 'yue_Hans', 'lzh', 'cmn_Hira', 'lzh_Yiii', 'lzh_Hans', 'cmn_Bopo', 'cmn_Hang', 'hak_Hani', 'cmn_Yiii', 'yue_Hant', 'lzh_Kana', 'wuu_Hani'}

- tgt_constituents: {'ita'}

- src_multilingual: False

- tgt_multilingual: False

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ita/opus-2020-06-17.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/zho-ita/opus-2020-06-17.test.txt

- src_alpha3: zho

- tgt_alpha3: ita

- short_pair: zh-it

- chrF2_score: 0.508

- bleu: 27.9

- brevity_penalty: 0.935

- ref_len: 19684.0

- src_name: Chinese

- tgt_name: Italian

- train_date: 2020-06-17

- src_alpha2: zh

- tgt_alpha2: it

- prefer_old: False

- long_pair: zho-ita

- helsinki_git_sha: 480fcbe0ee1bf4774bcbe6226ad9f58e63f6c535

- transformers_git_sha: 2207e5d8cb224e954a7cba69fa4ac2309e9ff30b

- port_machine: brutasse

- port_time: 2020-08-21-14:41