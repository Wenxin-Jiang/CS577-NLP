---
tags:
- translation
license: apache-2.0
---

### opus-mt-ru-es

* source languages: ru
* target languages: es
*  OPUS readme: [ru-es](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/ru-es/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-21.zip](https://object.pouta.csc.fi/OPUS-MT-models/ru-es/opus-2020-01-21.zip)
* test set translations: [opus-2020-01-21.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/ru-es/opus-2020-01-21.test.txt)
* test set scores: [opus-2020-01-21.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/ru-es/opus-2020-01-21.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2012.ru.es 	| 26.1 	| 0.527 |
| newstest2013.ru.es 	| 28.2 	| 0.538 |
| Tatoeba.ru.es 	| 49.4 	| 0.675 |

