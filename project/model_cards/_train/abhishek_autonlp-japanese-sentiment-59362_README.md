---
tags: autonlp
language: ja
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-japanese-sentiment
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 59362

## Validation Metrics

- Loss: 0.13092292845249176
- Accuracy: 0.9527127414314258
- Precision: 0.9634070704982427
- Recall: 0.9842171959602166
- AUC: 0.9667289746092403
- F1: 0.9737009564152002

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-japanese-sentiment-59362
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-japanese-sentiment-59362", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-japanese-sentiment-59362", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```