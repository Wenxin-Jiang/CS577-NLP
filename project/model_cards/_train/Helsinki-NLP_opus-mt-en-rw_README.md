---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-rw

* source languages: en
* target languages: rw
*  OPUS readme: [en-rw](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-rw/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-08.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-rw/opus-2020-01-08.zip)
* test set translations: [opus-2020-01-08.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-rw/opus-2020-01-08.test.txt)
* test set scores: [opus-2020-01-08.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-rw/opus-2020-01-08.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.en.rw 	| 33.3 	| 0.569 |
| Tatoeba.en.rw 	| 13.8 	| 0.503 |

