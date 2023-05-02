---
tags:
- translation
license: apache-2.0
---

### opus-mt-sv-fi

* source languages: sv
* target languages: fi
*  OPUS readme: [sv-fi](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/sv-fi/README.md)

*  dataset: opus+bt
* model: transformer-align
* pre-processing: normalization + SentencePiece
* download original weights: [opus+bt-2020-04-07.zip](https://object.pouta.csc.fi/OPUS-MT-models/sv-fi/opus+bt-2020-04-07.zip)
* test set translations: [opus+bt-2020-04-07.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/sv-fi/opus+bt-2020-04-07.test.txt)
* test set scores: [opus+bt-2020-04-07.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/sv-fi/opus+bt-2020-04-07.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| fiskmo_testset.sv.fi 	| 26.9 	| 0.623 |
| Tatoeba.sv.fi 	| 45.2 	| 0.678 |

