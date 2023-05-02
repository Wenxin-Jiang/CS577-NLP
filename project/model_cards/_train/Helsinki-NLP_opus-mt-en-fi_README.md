---
tags:
- translation
license: apache-2.0
---

### opus-mt-en-fi

* source languages: en
* target languages: fi
*  OPUS readme: [en-fi](https://github.com/Helsinki-NLP/OPUS-MT-train/blob/master/models/en-fi/README.md)

*  dataset: opus+bt-news
* model: transformer
* pre-processing: normalization + SentencePiece
* download original weights: [opus+bt-news-2020-03-21.zip](https://object.pouta.csc.fi/OPUS-MT-models/en-fi/opus+bt-news-2020-03-21.zip)
* test set translations: [opus+bt-news-2020-03-21.test.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-fi/opus+bt-news-2020-03-21.test.txt)
* test set scores: [opus+bt-news-2020-03-21.eval.txt](https://object.pouta.csc.fi/OPUS-MT-models/en-fi/opus+bt-news-2020-03-21.eval.txt)

## Benchmarks

| testset               | BLEU  | chr-F |
|-----------------------|-------|-------|
| newstest2019-enfi.en.fi 	| 25.7 	| 0.578 |

