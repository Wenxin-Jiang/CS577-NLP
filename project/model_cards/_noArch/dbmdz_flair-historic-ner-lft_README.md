---
tags:
- flair
- token-classification
- sequence-tagger-model
language: de
inference: false
license: mit
---

# Towards Robust Named Entity Recognition for Historic German

Based on [our paper](https://www.aclweb.org/anthology/W19-4312/)
we release a new model trained on the LFT dataset.

**Note:** We use BPEmbeddings instead of the combination of
Wikipedia, Common Crawl and character embeddings (as used in the paper),
so save space and training/inferencing time.

# Results

| Dataset \ Run | Run 1 | Run 2 | Run 3†    | Avg.
| ------------- | ----- | ----- | --------- | ------------
| Development   | 76.32 | 76.13 | **76.36** | 76.27
| Test          | 77.07 | 77.35 | 77.20     | 77.21

Paper reported an averaged F1-score of 77.51.

† denotes that this model is selected for upload.
