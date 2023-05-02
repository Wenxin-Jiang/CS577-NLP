---
tags:
- translation
license: apache-2.0
---

### opus-mt-it-en

* source languages: it
* target languages: en
*  OPUS readme: [it-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/it-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2019-12-18.zip](https://object.pouta.csc.fi/OPUS-MT-models/it-en/opus-2019-12-18.zip)
* test set translations: [opus-2019-12-18.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/it-en/opus-2019-12-18.test.txt)
* test set scores: [opus-2019-12-18.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/it-en/opus-2019-12-18.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009.it.en 	| 35.3 	| 0.600 |
| newstest2009.it.en 	| 34.0 	| 0.594 |
| Tatoeba.it.en 	| 70.9 	| 0.808 |

