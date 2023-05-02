---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-ro

* source languages: en
* target languages: ro
*  OPUS readme: [en-ro](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-ro/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2019-12-18.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-ro/opus-2019-12-18.zip)
* test set translations: [opus-2019-12-18.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ro/opus-2019-12-18.test.txt)
* test set scores: [opus-2019-12-18.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ro/opus-2019-12-18.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newsdev2016-enro.en.ro 	| 30.8 	| 0.592 |
| newstest2016-enro.en.ro 	| 28.8 	| 0.571 |
| Tatoeba.en.ro 	| 45.3 	| 0.670 |

