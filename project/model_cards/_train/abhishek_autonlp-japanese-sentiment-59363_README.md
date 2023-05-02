---
tags: autonlp
language: ja
widget:
- text: "🤗AutoNLPが大好きです"
datasets:
- abhishek/autonlp-data-japanese-sentiment
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 59363

## Validation Metrics

- Loss: 0.12651239335536957
- Accuracy: 0.9532079853817648
- Precision: 0.9729688278823665
- Recall: 0.9744633462616643
- AUC: 0.9717333684823413
- F1: 0.9737155136027014

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-japanese-sentiment-59363
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-japanese-sentiment-59363", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-japanese-sentiment-59363", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```