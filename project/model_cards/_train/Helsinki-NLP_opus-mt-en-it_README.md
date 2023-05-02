---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-it

* source languages: en
* target languages: it
*  OPUS readme: [en-it](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-it/README.md)

*  dataset: opus
* model: transformer
* pre-processing: normalization + SentencePiece
* download original weights: [opus-2019-12-04.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-it/opus-2019-12-04.zip)
* test set translations: [opus-2019-12-04.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-it/opus-2019-12-04.test.txt)
* test set scores: [opus-2019-12-04.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-it/opus-2019-12-04.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newssyscomb2009.en.it 	| 30.9 	| 0.606 |
| newstest2009.en.it 	| 31.9 	| 0.604 |
| Tatoeba.en.it 	| 48.2 	| 0.695 |

