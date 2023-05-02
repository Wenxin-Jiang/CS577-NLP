---
tags:
- translation
license: apache-2.0
---

### opus-mt-fr-es

* source languages: fr
* target languages: es
*  OPUS readme: [fr-es](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/fr-es/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-09.zip](https://object.pouta.csc.fi/OPUS-MT-models/fr-es/opus-2020-01-09.zip)
* test set translations: [opus-2020-01-09.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/fr-es/opus-2020-01-09.test.txt)
* test set scores: [opus-2020-01-09.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/fr-es/opus-2020-01-09.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009.fr.es 	| 34.3 	| 0.601 |
| news-test2008.fr.es 	| 32.5 	| 0.583 |
| newstest2009.fr.es 	| 31.6 	| 0.586 |
| newstest2010.fr.es 	| 36.5 	| 0.616 |
| newstest2011.fr.es 	| 38.3 	| 0.622 |
| newstest2012.fr.es 	| 38.1 	| 0.619 |
| newstest2013.fr.es 	| 34.0 	| 0.587 |
| Tatoeba.fr.es 	| 53.2 	| 0.709 |

