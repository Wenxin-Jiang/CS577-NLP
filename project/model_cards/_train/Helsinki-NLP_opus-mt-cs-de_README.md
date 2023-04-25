---
tags:
- translation
license: apache-2.0
---

### opus-mt-cs-de

* source languages: cs
* target languages: de
*  OPUS readme: [cs-de](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/cs-de/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-20.zip](https://object.pouta.csc.fi/OPUS-MT-models/cs-de/opus-2020-01-20.zip)
* test set translations: [opus-2020-01-20.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/cs-de/opus-2020-01-20.test.txt)
* test set scores: [opus-2020-01-20.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/cs-de/opus-2020-01-20.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009.cs.de 	| 22.0 	| 0.525 |
| news-test2008.cs.de 	| 21.1 	| 0.520 |
| newstest2009.cs.de 	| 22.2 	| 0.525 |
| newstest2010.cs.de 	| 22.1 	| 0.527 |
| newstest2011.cs.de 	| 21.6 	| 0.515 |
| newstest2012.cs.de 	| 22.2 	| 0.516 |
| newstest2013.cs.de 	| 24.8 	| 0.538 |
| newstest2019-csde.cs.de 	| 23.6 	| 0.530 |
| Tatoeba.cs.de 	| 51.6 	| 0.687 |

