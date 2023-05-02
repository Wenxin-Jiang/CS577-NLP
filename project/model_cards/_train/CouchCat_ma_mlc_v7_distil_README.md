---
language: en
license: mit
tags:
- multi-label
widget:
- text: "I would like to return these pants and shoes"
---

### Description
A Multi-label text classification model trained on a customer feedback data using DistilBert.
Possible labels are:
- Delivery (delivery status, time of arrival, etc.)
- Return (return confirmation, return label requests, etc.)
- Product (quality, complaint, etc.)
- Monetary (pending transactions, refund, etc.)

### Usage
```
from transformers import AutoTokenizer, AutoModelForSequenceClassification
  
  tokenizer = AutoTokenizer.from_pretrained("CouchCat/ma_mlc_v7_distil")
  
  model = AutoModelForSequenceClassification.from_pretrained("CouchCat/ma_mlc_v7_distil") 
```