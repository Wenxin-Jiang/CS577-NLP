---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-ht

* source languages: en
* target languages: ht
*  OPUS readme: [en-ht](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-ht/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-08.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-ht/opus-2020-01-08.zip)
* test set translations: [opus-2020-01-08.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ht/opus-2020-01-08.test.txt)
* test set scores: [opus-2020-01-08.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ht/opus-2020-01-08.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.en.ht 	| 38.3 	| 0.545 |
| Tatoeba.en.ht 	| 45.2 	| 0.592 |

