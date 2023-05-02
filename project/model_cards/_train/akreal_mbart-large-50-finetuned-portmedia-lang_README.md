---
language:
  - it
tags:
  - mbart-50
license: apache-2.0
datasets:
  - PortMEDIA-Lang
metrics:
  - cer
  - cver
---

This model is `mbart-large-50-many-to-many-mmt` model fine-tuned on the text part of [PortMEDIA-Lang](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0371/) spoken language understanding dataset.

The scores on the test set are 40.76% and 43.93% for CER and CVER respectively.
