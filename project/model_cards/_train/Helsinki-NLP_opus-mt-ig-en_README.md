---
tags:
- translation
license: apache-2.0
---

### opus-mt-ig-en

* source languages: ig
* target languages: en
*  OPUS readme: [ig-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/ig-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-09.zip](https://object.pouta.csc.fi/OPUS-MT-models/ig-en/opus-2020-01-09.zip)
* test set translations: [opus-2020-01-09.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/ig-en/opus-2020-01-09.test.txt)
* test set scores: [opus-2020-01-09.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/ig-en/opus-2020-01-09.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.ig.en 	| 36.7 	| 0.520 |
| Tatoeba.ig.en 	| 46.3 	| 0.528 |

