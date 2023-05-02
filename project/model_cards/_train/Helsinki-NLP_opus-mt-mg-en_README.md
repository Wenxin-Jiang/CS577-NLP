---
tags:
- translation
license: apache-2.0
---

### opus-mt-mg-en

* source languages: mg
* target languages: en
*  OPUS readme: [mg-en](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/mg-en/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2020-01-09.zip](https://object.pouta.csc.fi/OPUS-MT-models/mg-en/opus-2020-01-09.zip)
* test set translations: [opus-2020-01-09.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/mg-en/opus-2020-01-09.test.txt)
* test set scores: [opus-2020-01-09.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/mg-en/opus-2020-01-09.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| GlobalVoices.mg.en 	| 27.6 	| 0.522 |
| Tatoeba.mg.en 	| 50.2 	| 0.607 |

