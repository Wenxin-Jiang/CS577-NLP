---
tags:
- flair
- token-classification
- sequence-tagger-model
language: de
widget:
- text: "April Martin Ansclm, K. Gefangen-Auffehers Georg Sausgruber."
license: mit
---

# Towards Robust Named Entity Recognition for Historic German

Based on [our paper](https://www.aclweb.org/anthology/W19-4312/)
we release a new model trained on the ONB dataset.

**Note:** We use BPEmbeddings instead of the combination of
Wikipedia, Common Crawl and character embeddings (as used in the paper),
so save space and training/inferencing time.

# Results

| Dataset \ Run | Run 1 | Run 2 | Run 3     | Avg.
| ------------- | ----- | ----- | --------- | ------------
| Development   | 86.69 | 86.13 | **87.18** | 86.67
| Test          | 85.27 | 86.05 | 85.75†    | 85.69

Paper reported an averaged F1-score of 85.31.

† denotes that this model is selected for upload.
