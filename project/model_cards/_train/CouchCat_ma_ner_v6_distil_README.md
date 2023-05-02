---
language: en
license: mit
tags:
- ner
widget:
- text: "These shoes from Adidas fit quite well"
---

### Description
A Named Entity Recognition model trained on a customer feedback data using DistilBert.
Possible labels are:
- PRD: for certain products
- BRND: for brands

### Usage
```
from transformers import AutoTokenizer, AutoModelForTokenClassification
  
  tokenizer = AutoTokenizer.from_pretrained("CouchCat/ma_ner_v6_distil")
  
  model = AutoModelForTokenClassification.from_pretrained("CouchCat/ma_ner_v6_distil")
```