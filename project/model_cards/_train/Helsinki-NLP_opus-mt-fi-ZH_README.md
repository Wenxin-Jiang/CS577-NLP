---
tags:
- translation
license: apache-2.0
---

### opus-mt-fi-ZH

* source languages: fi
* target languages: cmn,cn,yue,ze_zh,zh_cn,zh_CN,zh_HK,zh_tw,zh_TW,zh_yue,zhs,zht,zh
*  OPUS readme: [fi-cmn+cn+yue+ze_zh+zh_cn+zh_CN+zh_HK+zh_tw+zh_TW+zh_yue+zhs+zht+zh](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/fi-cmn+cn+yue+ze_zh+zh_cn+zh_CN+zh_HK+zh_tw+zh_TW+zh_yue+zhs+zht+zh/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-01-16.zip](https://object.pouta.csc.fi/OPUS-MT-models/fi-cmn+cn+yue+ze_zh+zh_cn+zh_CN+zh_HK+zh_tw+zh_TW+zh_yue+zhs+zht+zh/opus-2020-01-16.zip)
* test set translations: [opus-2020-01-16.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/fi-cmn+cn+yue+ze_zh+zh_cn+zh_CN+zh_HK+zh_tw+zh_TW+zh_yue+zhs+zht+zh/opus-2020-01-16.test.txt)
* test set scores: [opus-2020-01-16.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/fi-cmn+cn+yue+ze_zh+zh_cn+zh_CN+zh_HK+zh_tw+zh_TW+zh_yue+zhs+zht+zh/opus-2020-01-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| bible-uedin.fi.zh 	| 23.4 	| 0.326 |

