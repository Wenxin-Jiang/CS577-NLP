---
tags:
- translation
license: apache-2.0
---

### opus-mt-lv-en

* source languages: lv
* target languages: en
*  OPUS readme: [lv-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/lv-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2019-12-18.zip](https://object.pouta.csc.fi/OPUS-MT-models/lv-en/opus-2019-12-18.zip)
* test set translations: [opus-2019-12-18.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/lv-en/opus-2019-12-18.test.txt)
* test set scores: [opus-2019-12-18.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/lv-en/opus-2019-12-18.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2017-enlv.lv.en 	| 29.9 	| 0.587 |
| newstest2017-enlv.lv.en 	| 22.1 	| 0.526 |
| Tatoeba.lv.en 	| 53.3 	| 0.707 |

