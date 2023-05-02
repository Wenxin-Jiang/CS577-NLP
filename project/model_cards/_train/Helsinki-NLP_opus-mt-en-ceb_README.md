---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-ceb

* source languages: en
* target languages: ceb
*  OPUS readme: [en-ceb](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-ceb/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-08.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-ceb/opus-2020-01-08.zip)
* test set translations: [opus-2020-01-08.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ceb/opus-2020-01-08.test.txt)
* test set scores: [opus-2020-01-08.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ceb/opus-2020-01-08.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.en.ceb 	| 51.3 	| 0.704 |
| Tatoeba.en.ceb 	| 31.3 	| 0.600 |

