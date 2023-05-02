---
tags:
- translation
license: apache-2.0
---

### opus-mt-ha-en

* source languages: ha
* target languages: en
*  OPUS readme: [ha-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/ha-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-09.zip](https://object.pouta.csc.fi/OPUS-MT-models/ha-en/opus-2020-01-09.zip)
* test set translations: [opus-2020-01-09.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/ha-en/opus-2020-01-09.test.txt)
* test set scores: [opus-2020-01-09.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/ha-en/opus-2020-01-09.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.ha.en 	| 35.0 	| 0.506 |
| Tatoeba.ha.en 	| 39.0 	| 0.497 |

