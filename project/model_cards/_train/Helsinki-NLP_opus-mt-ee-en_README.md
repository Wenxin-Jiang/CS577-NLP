---
tags:
- translation
license: apache-2.0
---

### opus-mt-ee-en

* source languages: ee
* target languages: en
*  OPUS readme: [ee-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/ee-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-08.zip](https://object.pouta.csc.fi/OPUS-MT-models/ee-en/opus-2020-01-08.zip)
* test set translations: [opus-2020-01-08.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/ee-en/opus-2020-01-08.test.txt)
* test set scores: [opus-2020-01-08.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/ee-en/opus-2020-01-08.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.ee.en 	| 39.3 	| 0.556 |
| Tatoeba.ee.en 	| 21.2 	| 0.569 |

