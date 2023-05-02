---
tags:
- translation
license: apache-2.0
---

### opus-mt-es-ru

* source languages: es
* target languages: ru
*  OPUS readme: [es-ru](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/es-ru/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-20.zip](https://object.pouta.csc.fi/OPUS-MT-models/es-ru/opus-2020-01-20.zip)
* test set translations: [opus-2020-01-20.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/es-ru/opus-2020-01-20.test.txt)
* test set scores: [opus-2020-01-20.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/es-ru/opus-2020-01-20.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2012.es.ru 	| 20.9 	| 0.489 |
| newstest2013.es.ru 	| 23.4 	| 0.504 |
| Tatoeba.es.ru 	| 47.0 	| 0.657 |

