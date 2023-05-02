---
language:
- es
- zh

tags:
- translation

license: apache-2.0
---
### es-zh

* source group: Spanish 
* target group: Chinese 
*  OPUS readme: [spa-zho](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-zho/README.md)

*  model: transformer
* source language(s): spa
* target language(s): cjy_Hans cjy_Hant cmn cmn_Hans cmn_Hant hsn hsn_Hani lzh nan wuu yue_Hans yue_Hant
* model: transformer
* pre-processing: normalization + SentencePiece (spm32k,spm32k)
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2021-01-04.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-zho/opus-2021-01-04.zip)
* test set translations: [opus-2021-01-04.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-zho/opus-2021-01-04.test.txt)
* test set scores: [opus-2021-01-04.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/spa-zho/opus-2021-01-04.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba-test.spa.zho 	| 38.8 	| 0.324 |


### System Info: 
- hf_name: es-zh

- source_languages: spa

- target_languages: zho

- opus_readme_url: https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/spa-zho/README.md

- original_repo: Tatoeba-Challenge

- tags: ['translation']

- languages: ['es', 'zh']

- src_constituents: ('Spanish', {'spa'})

- tgt_constituents: ('Chinese', {'wuu_Bopo', 'wuu', 'cmn_Hang', 'lzh_Kana', 'lzh', 'wuu_Hani', 'lzh_Yiii', 'yue_Hans', 'cmn_Hani', 'cjy_Hans', 'cmn_Hans', 'cmn_Kana', 'zho_Hans', 'zho_Hant', 'yue', 'cmn_Bopo', 'yue_Hang', 'lzh_Hans', 'wuu_Latn', 'yue_Hant', 'hak_Hani', 'lzh_Bopo', 'cmn_Hant', 'lzh_Hani', 'lzh_Hang', 'cmn', 'lzh_Hira', 'yue_Bopo', 'yue_Hani', 'gan', 'zho', 'cmn_Yiii', 'yue_Hira', 'cmn_Latn', 'yue_Kana', 'cjy_Hant', 'cmn_Hira', 'nan_Hani', 'nan'})

- src_multilingual: False

- tgt_multilingual: False

- long_pair: spa-zho

- prepro:  normalization + SentencePiece (spm32k,spm32k)

- url_model: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-zho/opus-2021-01-04.zip

- url_test_set: https://object.pouta.csc.fi/Tatoeba-MT-models/spa-zho/opus-2021-01-04.test.txt

- src_alpha3: spa

- tgt_alpha3: zho

- chrF2_score: 0.324

- bleu: 38.8

- brevity_penalty: 0.878

- ref_len: 22762.0

- src_name: Spanish

- tgt_name: Chinese

- train_date: 2021-01-04 00:00:00

- src_alpha2: es

- tgt_alpha2: zh

- prefer_old: False

- short_pair: es-zh

- helsinki_git_sha: dfdcef114ffb8a8dbb7a3fcf84bde5af50309500

- transformers_git_sha: 1310e1a758edc8e89ec363db76863c771fbeb1de

- port_machine: LM0-400-22516.local

- port_time: 2021-01-04-18:53