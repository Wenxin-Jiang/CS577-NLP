---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-ml

* source languages: en
* target languages: ml
*  OPUS readme: [en-ml](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-ml/README.md)

*  dataset: opus+bt+bt
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus+bt+bt-2020-04-28.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-ml/opus+bt+bt-2020-04-28.zip)
* test set translations: [opus+bt+bt-2020-04-28.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ml/opus+bt+bt-2020-04-28.test.txt)
* test set scores: [opus+bt+bt-2020-04-28.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ml/opus+bt+bt-2020-04-28.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba.en.ml 	| 19.1 	| 0.536 |

