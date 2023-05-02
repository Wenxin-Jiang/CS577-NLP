---
language: 
  - en
tags:
  - mbart-50
license: apache-2.0
datasets:
  - SLURP
metrics:
  - accuracy
  - slu-f1
---

This model is `mbart-large-50-many-to-many-mmt` model fine-tuned on the text part of [SLURP](https://github.com/pswietojanski/slurp) spoken language understanding dataset.

The scores on the test set are 85.68% and 79.00% for Intent accuracy and SLU-F1 respectively.