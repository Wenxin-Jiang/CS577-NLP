---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- abhishek/autonlp-data-imdb_eval
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 71421

## Validation Metrics

- Loss: 0.4114699363708496
- Accuracy: 0.8248248248248248
- Precision: 0.8305439330543933
- Recall: 0.8085539714867617
- AUC: 0.9088033420466026
- F1: 0.8194014447884417

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/abhishek/autonlp-imdb_eval-71421
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-imdb_eval-71421", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-imdb_eval-71421", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```