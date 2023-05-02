---
language: 
  - en
tags:
  - mbart-50
license: apache-2.0
datasets:
  - SLUE-VoxPopuli
metrics:
  - f1
  - label-f1
---

This model is `mbart-large-50-many-to-many-mmt` model fine-tuned on the text part of [SLUE-VoxPopuli](https://github.com/asappresearch/slue-toolkit) spoken language understanding dataset.

The scores on the dev set are 83.25% and 87.76% for F1 and label-F1 respectively.
