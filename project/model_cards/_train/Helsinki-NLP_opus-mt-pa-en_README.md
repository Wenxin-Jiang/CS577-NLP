---
tags:
- translation
license: apache-2.0
---

### opus-mt-pa-en

* source languages: pa
* target languages: en
*  OPUS readme: [pa-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/pa-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-16.zip](https://object.pouta.csc.fi/OPUS-MT-models/pa-en/opus-2020-01-16.zip)
* test set translations: [opus-2020-01-16.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/pa-en/opus-2020-01-16.test.txt)
* test set scores: [opus-2020-01-16.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/pa-en/opus-2020-01-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.pa.en 	| 20.6 	| 0.320 |
| Tatoeba.pa.en 	| 29.3 	| 0.464 |

