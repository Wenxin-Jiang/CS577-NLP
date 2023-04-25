---
tags:
- translation
license: apache-2.0
---

### opus-mt-cs-en

* source languages: cs
* target languages: en
*  OPUS readme: [cs-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/cs-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2019-12-18.zip](https://object.pouta.csc.fi/OPUS-MT-models/cs-en/opus-2019-12-18.zip)
* test set translations: [opus-2019-12-18.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/cs-en/opus-2019-12-18.test.txt)
* test set scores: [opus-2019-12-18.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/cs-en/opus-2019-12-18.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2014-csen.cs.en 	| 34.1 	| 0.612 |
| newstest2015-encs.cs.en 	| 30.4 	| 0.565 |
| newstest2016-encs.cs.en 	| 31.8 	| 0.584 |
| newstest2017-encs.cs.en 	| 28.7 	| 0.556 |
| newstest2018-encs.cs.en 	| 30.3 	| 0.566 |
| Tatoeba.cs.en 	| 58.0 	| 0.721 |

