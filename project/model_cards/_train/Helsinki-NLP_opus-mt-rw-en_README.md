---
tags:
- translation
license: apache-2.0
---

### opus-mt-rw-en

* source languages: rw
* target languages: en
*  OPUS readme: [rw-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/rw-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-16.zip](https://object.pouta.csc.fi/OPUS-MT-models/rw-en/opus-2020-01-16.zip)
* test set translations: [opus-2020-01-16.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/rw-en/opus-2020-01-16.test.txt)
* test set scores: [opus-2020-01-16.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/rw-en/opus-2020-01-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.rw.en 	| 37.3 	| 0.530 |
| Tatoeba.rw.en 	| 49.8 	| 0.643 |

