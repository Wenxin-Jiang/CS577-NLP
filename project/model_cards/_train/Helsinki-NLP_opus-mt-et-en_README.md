---
tags:
- translation
license: apache-2.0
---

### opus-mt-et-en

* source languages: et
* target languages: en
*  OPUS readme: [et-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/et-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2019-12-18.zip](https://object.pouta.csc.fi/OPUS-MT-models/et-en/opus-2019-12-18.zip)
* test set translations: [opus-2019-12-18.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/et-en/opus-2019-12-18.test.txt)
* test set scores: [opus-2019-12-18.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/et-en/opus-2019-12-18.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2018-enet.et.en 	| 30.1 	| 0.574 |
| newstest2018-enet.et.en 	| 30.3 	| 0.581 |
| Tatoeba.et.en 	| 59.9 	| 0.738 |

