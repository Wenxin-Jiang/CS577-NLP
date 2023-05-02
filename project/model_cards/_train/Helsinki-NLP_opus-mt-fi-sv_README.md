---
tags:
- translation
license: apache-2.0
---

### opus-mt-fi-sv

* source languages: fi
* target languages: sv
*  OPUS readme: [fi-sv](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/fi-sv/README.md)

*  dataset: opus+bt
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus+bt-2020-04-11.zip](https://object.pouta.csc.fi/OPUS-MT-models/fi-sv/opus+bt-2020-04-11.zip)
* test set translations: [opus+bt-2020-04-11.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/fi-sv/opus+bt-2020-04-11.test.txt)
* test set scores: [opus+bt-2020-04-11.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/fi-sv/opus+bt-2020-04-11.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| fiskmo_testset.fi.sv 	| 27.4 	| 0.605 |
| Tatoeba.fi.sv 	| 54.7 	| 0.709 |

