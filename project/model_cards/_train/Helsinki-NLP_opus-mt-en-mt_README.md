---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-mt

* source languages: en
* target languages: mt
*  OPUS readme: [en-mt](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-mt/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-08.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-mt/opus-2020-01-08.zip)
* test set translations: [opus-2020-01-08.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-mt/opus-2020-01-08.test.txt)
* test set scores: [opus-2020-01-08.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-mt/opus-2020-01-08.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.en.mt 	| 47.5 	| 0.640 |
| Tatoeba.en.mt 	| 25.0 	| 0.620 |

