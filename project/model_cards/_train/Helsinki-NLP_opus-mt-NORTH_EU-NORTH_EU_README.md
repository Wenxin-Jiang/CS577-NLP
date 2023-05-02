---
tags:
- translation
license: apache-2.0
---

### opus-mt-NORTH_EU-NORTH_EU

* source languages: de,nl,fy,af,da,fo,is,no,nb,nn,sv
* target languages: de,nl,fy,af,da,fo,is,no,nb,nn,sv
*  OPUS readme: [de+nl+fy+af+da+fo+is+no+nb+nn+sv-de+nl+fy+af+da+fo+is+no+nb+nn+sv](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/de+nl+fy+af+da+fo+is+no+nb+nn+sv-de+nl+fy+af+da+fo+is+no+nb+nn+sv/README.md)

*  dataset: opus
* model: transformer-align
* pre-processing: normalization + SentencePiece
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus-2020-01-15.zip](https://object.pouta.csc.fi/OPUS-MT-models/de+nl+fy+af+da+fo+is+no+nb+nn+sv-de+nl+fy+af+da+fo+is+no+nb+nn+sv/opus-2020-01-15.zip)
* test set translations: [opus-2020-01-15.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/de+nl+fy+af+da+fo+is+no+nb+nn+sv-de+nl+fy+af+da+fo+is+no+nb+nn+sv/opus-2020-01-15.test.txt)
* test set scores: [opus-2020-01-15.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/de+nl+fy+af+da+fo+is+no+nb+nn+sv-de+nl+fy+af+da+fo+is+no+nb+nn+sv/opus-2020-01-15.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba.de.sv 	| 48.1 	| 0.663 |

