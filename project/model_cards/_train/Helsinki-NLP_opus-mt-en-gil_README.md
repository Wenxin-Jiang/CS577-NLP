---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-gil

* source languages: en
* target languages: gil
*  OPUS readme: [en-gil](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-gil/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-20.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-gil/opus-2020-01-20.zip)
* test set translations: [opus-2020-01-20.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-gil/opus-2020-01-20.test.txt)
* test set scores: [opus-2020-01-20.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-gil/opus-2020-01-20.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.en.gil 	| 38.8 	| 0.604 |
