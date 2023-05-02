---
language: en
license: mit
tags:
  - ner
widget:
  - text: "These shoes I recently bought from Tommy Hilfiger fit quite well. The shirt, however, has got a hole"
---

### Description

A Named Entity Recognition model trained on a customer feedback data using DistilBert.
Possible labels are in BIO-notation. Performance of the PERS tag could be better because of low data samples:

- PROD: for certain products
- BRND: for brands
- PERS: people names

The following tags are simply in place to help better categorize the previous tags

- MATR: relating to materials, e.g. cloth, leather, seam, etc.
- TIME: time related entities
- MISC: any other entity that might skew the results

### Usage

```
from transformers import AutoTokenizer, AutoModelForTokenClassification

  tokenizer = AutoTokenizer.from_pretrained("CouchCat/ma_ner_v7_distil")

  model = AutoModelForTokenClassification.from_pretrained("CouchCat/ma_ner_v7_distil")
```
