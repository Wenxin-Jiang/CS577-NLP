---
language: en
license: mit
tags:
- sentiment-analysis
widget:
- text: "I am disappointed in the terrible quality of my dress"
---

### Description
A Sentiment Analysis model trained on customer feedback data using DistilBert.
Possible sentiments are:
* negative
* neutral
* positive

### Usage

```
from transformers import AutoTokenizer, AutoModelForSequenceClassification
  
  tokenizer = AutoTokenizer.from_pretrained("CouchCat/ma_sa_v7_distil")
  
  model = AutoModelForSequenceClassification.from_pretrained("CouchCat/ma_sa_v7_distil")
```