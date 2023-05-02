---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-bcl

* source languages: en
* target languages: bcl
*  OPUS readme: [en-bcl](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-bcl/README.md)

*  dataset: opus+bt
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus+bt-2020-02-26.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-bcl/opus+bt-2020-02-26.zip)
* test set translations: [opus+bt-2020-02-26.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-bcl/opus+bt-2020-02-26.test.txt)
* test set scores: [opus+bt-2020-02-26.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-bcl/opus+bt-2020-02-26.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.en.bcl 	| 54.3 	| 0.722 |

