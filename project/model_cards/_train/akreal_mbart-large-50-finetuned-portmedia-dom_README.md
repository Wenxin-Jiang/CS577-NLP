---
language:
  - fr
tags:
  - mbart-50
license: apache-2.0
datasets:
  - PortMEDIA-Dom
metrics:
  - cer
  - cver
---

This model is `mbart-large-50-many-to-many-mmt` model fine-tuned on the text part of [PortMEDIA-Dom](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0371/) spoken language understanding dataset.

The scores on the test set are 23.49% and 26.59% for CER and CVER respectively.
