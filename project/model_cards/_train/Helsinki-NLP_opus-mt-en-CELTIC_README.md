---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-INSULAR_CELTIC

* source languages: en
* target languages: ga,cy,br,gd,kw,gv
*  OPUS readme: [en-ga+cy+br+gd+kw+gv](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-ga+cy+br+gd+kw+gv/README.md)

*  dataset: opus+techiaith+bt
* model: transformer-align
* pre-processing: normalization + SentencePiece
* a sentence initial language token is required in the form of `>>id<<` (id = valid target language ID)
* download original weights: [opus+techiaith+bt-2020-04-24.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-ga+cy+br+gd+kw+gv/opus+techiaith+bt-2020-04-24.zip)
* test set translations: [opus+techiaith+bt-2020-04-24.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ga+cy+br+gd+kw+gv/opus+techiaith+bt-2020-04-24.test.txt)
* test set scores: [opus+techiaith+bt-2020-04-24.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-ga+cy+br+gd+kw+gv/opus+techiaith+bt-2020-04-24.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| Tatoeba.en.ga 	| 22.8 	| 0.404 |

