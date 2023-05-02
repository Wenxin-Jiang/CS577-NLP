---
tags:
- translation
license: apache-2.0
---

### opus-mt-es-NORWAY

* source languages: es
* target languages: nb_NO,nb,nn_NO,nn,nog,no_nb,no
*  OPUS readme: [es-nb_NO+nb+nn_NO+nn+nog+no_nb+no](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/es-nb_NO+nb+nn_NO+nn+nog+no_nb+no/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-01-16.zip](https://object.pouta.csc.fi/OPUS-MT-models/es-nb_NO+nb+nn_NO+nn+nog+no_nb+no/opus-2020-01-16.zip)
* test set translations: [opus-2020-01-16.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/es-nb_NO+nb+nn_NO+nn+nog+no_nb+no/opus-2020-01-16.test.txt)
* test set scores: [opus-2020-01-16.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/es-nb_NO+nb+nn_NO+nn+nog+no_nb+no/opus-2020-01-16.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| JW300.es.no 	| 31.6 	| 0.523 |

