---
tags:
- translation
license: apache-2.0
---

### opus-mt-ht-en

* source languages: ht
* target languages: en
*  OPUS readme: [ht-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/ht-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-09.zip](https://object.pouta.csc.fi/OPUS-MT-models/ht-en/opus-2020-01-09.zip)
* test set translations: [opus-2020-01-09.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/ht-en/opus-2020-01-09.test.txt)
* test set scores: [opus-2020-01-09.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/ht-en/opus-2020-01-09.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.ht.en 	| 37.5 	| 0.542 |
| Tatoeba.ht.en 	| 57.0 	| 0.689 |

