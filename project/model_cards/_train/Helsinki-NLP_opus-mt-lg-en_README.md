---
tags:
- translation
license: apache-2.0
---

### opus-mt-lg-en

* source languages: lg
* target languages: en
*  OPUS readme: [lg-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/lg-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-09.zip](https://object.pouta.csc.fi/OPUS-MT-models/lg-en/opus-2020-01-09.zip)
* test set translations: [opus-2020-01-09.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/lg-en/opus-2020-01-09.test.txt)
* test set scores: [opus-2020-01-09.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/lg-en/opus-2020-01-09.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.lg.en 	| 32.6 	| 0.480 |
| Tatoeba.lg.en 	| 5.4 	| 0.243 |

