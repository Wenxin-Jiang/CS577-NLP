---
tags:
- translation
license: apache-2.0
---

### opus-mt-pap-en

* source languages: pap
* target languages: en
*  OPUS readme: [pap-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/pap-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-16.zip](https://object.pouta.csc.fi/OPUS-MT-models/pap-en/opus-2020-01-16.zip)
* test set translations: [opus-2020-01-16.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/pap-en/opus-2020-01-16.test.txt)
* test set scores: [opus-2020-01-16.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/pap-en/opus-2020-01-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.pap.en 	| 47.3 	| 0.634 |
| Tatoeba.pap.en 	| 63.2 	| 0.684 |

