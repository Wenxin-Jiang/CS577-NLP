---
tags:
- translation
license: apache-2.0
---

### opus-mt-ny-en

* source languages: ny
* target languages: en
*  OPUS readme: [ny-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/ny-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-16.zip](https://object.pouta.csc.fi/OPUS-MT-models/ny-en/opus-2020-01-16.zip)
* test set translations: [opus-2020-01-16.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/ny-en/opus-2020-01-16.test.txt)
* test set scores: [opus-2020-01-16.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/ny-en/opus-2020-01-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.ny.en 	| 39.7 	| 0.547 |
| Tatoeba.ny.en 	| 44.2 	| 0.562 |
