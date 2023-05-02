---
tags:
- translation
license: apache-2.0
---

### opus-mt-kl-en

* source languages: kl
* target languages: en
*  OPUS readme: [kl-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/kl-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-09.zip](https://object.pouta.csc.fi/OPUS-MT-models/kl-en/opus-2020-01-09.zip)
* test set translations: [opus-2020-01-09.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/kl-en/opus-2020-01-09.test.txt)
* test set scores: [opus-2020-01-09.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/kl-en/opus-2020-01-09.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.kl.en 	| 26.4 	| 0.432 |
| Tatoeba.kl.en 	| 35.5 	| 0.443 |

