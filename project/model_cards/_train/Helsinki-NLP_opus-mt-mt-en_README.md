---
tags:
- translation
license: apache-2.0
---

### opus-mt-mt-en

* source languages: mt
* target languages: en
*  OPUS readme: [mt-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/mt-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-16.zip](https://object.pouta.csc.fi/OPUS-MT-models/mt-en/opus-2020-01-16.zip)
* test set translations: [opus-2020-01-16.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/mt-en/opus-2020-01-16.test.txt)
* test set scores: [opus-2020-01-16.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/mt-en/opus-2020-01-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.mt.en 	| 49.0 	| 0.655 |
| Tatoeba.mt.en 	| 53.3 	| 0.685 |

