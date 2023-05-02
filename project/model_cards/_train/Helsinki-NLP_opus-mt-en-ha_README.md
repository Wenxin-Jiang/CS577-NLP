---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-ha

* source languages: en
* target languages: ha
*  OPUS readme: [en-ha](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-ha/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-08.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-ha/opus-2020-01-08.zip)
* test set translations: [opus-2020-01-08.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ha/opus-2020-01-08.test.txt)
* test set scores: [opus-2020-01-08.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ha/opus-2020-01-08.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.en.ha 	| 34.1 	| 0.544 |
| Tatoeba.en.ha 	| 17.6 	| 0.498 |

