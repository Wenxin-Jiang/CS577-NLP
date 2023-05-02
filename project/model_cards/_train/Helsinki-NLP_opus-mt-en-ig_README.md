---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-ig

* source languages: en
* target languages: ig
*  OPUS readme: [en-ig](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-ig/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-08.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-ig/opus-2020-01-08.zip)
* test set translations: [opus-2020-01-08.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ig/opus-2020-01-08.test.txt)
* test set scores: [opus-2020-01-08.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ig/opus-2020-01-08.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.en.ig 	| 39.5 	| 0.546 |
| Tatoeba.en.ig 	| 3.8 	| 0.297 |

