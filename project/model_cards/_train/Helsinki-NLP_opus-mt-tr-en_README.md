---
tags:
- translation
license: apache-2.0
---

### opus-mt-tr-en

* source languages: tr
* target languages: en
*  OPUS readme: [tr-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/tr-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-16.zip](https://object.pouta.csc.fi/OPUS-MT-models/tr-en/opus-2020-01-16.zip)
* test set translations: [opus-2020-01-16.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/tr-en/opus-2020-01-16.test.txt)
* test set scores: [opus-2020-01-16.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/tr-en/opus-2020-01-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2016-entr.tr.en 	| 27.6 	| 0.548 |
| newstest2016-entr.tr.en 	| 25.2 	| 0.532 |
| newstest2017-entr.tr.en 	| 24.7 	| 0.530 |
| newstest2018-entr.tr.en 	| 27.0 	| 0.547 |
| Tatoeba.tr.en 	| 63.5 	| 0.760 |

