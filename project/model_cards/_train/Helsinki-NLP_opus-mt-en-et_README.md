---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-et

* source languages: en
* target languages: et
*  OPUS readme: [en-et](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-et/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2019-12-18.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-et/opus-2019-12-18.zip)
* test set translations: [opus-2019-12-18.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-et/opus-2019-12-18.test.txt)
* test set scores: [opus-2019-12-18.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-et/opus-2019-12-18.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2018-enet.en.et 	| 21.8 	| 0.540 |
| newstest2018-enet.en.et 	| 23.3 	| 0.556 |
| Tatoeba.en.et 	| 54.0 	| 0.717 |

