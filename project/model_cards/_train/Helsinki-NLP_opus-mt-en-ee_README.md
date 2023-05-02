---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-ee

* source languages: en
* target languages: ee
*  OPUS readme: [en-ee](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-ee/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-08.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-ee/opus-2020-01-08.zip)
* test set translations: [opus-2020-01-08.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ee/opus-2020-01-08.test.txt)
* test set scores: [opus-2020-01-08.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ee/opus-2020-01-08.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.en.ee 	| 38.2 	| 0.591 |
| Tatoeba.en.ee 	| 6.0 	| 0.347 |

