---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 31154

## Validation Metrics

- Loss: 0.19292379915714264
- Accuracy: 0.9395
- Precision: 0.9569557080474111
- Recall: 0.9204
- AUC: 0.9851040399999998
- F1: 0.9383219492302988

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-imdb_sentiment_classification-31154
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-imdb_sentiment_classification-31154", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-imdb_sentiment_classification-31154", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```