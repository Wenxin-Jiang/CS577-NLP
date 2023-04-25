---
tags:
- translation
license: apache-2.0
---

### opus-mt-ru-fr

* source languages: ru
* target languages: fr
*  OPUS readme: [ru-fr](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/ru-fr/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-26.zip](https://object.pouta.csc.fi/OPUS-MT-models/ru-fr/opus-2020-01-26.zip)
* test set translations: [opus-2020-01-26.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/ru-fr/opus-2020-01-26.test.txt)
* test set scores: [opus-2020-01-26.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/ru-fr/opus-2020-01-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2012.ru.fr 	| 18.3 	| 0.497 |
| newstest2013.ru.fr 	| 21.6 	| 0.516 |
| Tatoeba.ru.fr 	| 51.5 	| 0.670 |

