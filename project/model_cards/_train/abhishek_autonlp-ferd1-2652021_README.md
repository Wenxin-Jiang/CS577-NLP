---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-ferd1
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 2652021

## Validation Metrics

- Loss: 0.3934604227542877
- Accuracy: 0.8411030860144452
- Precision: 0.8201550387596899
- Recall: 0.8076335877862595
- AUC: 0.8946767157983608
- F1: 0.8138461538461538

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-ferd1-2652021
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-ferd1-2652021", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-ferd1-2652021", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```