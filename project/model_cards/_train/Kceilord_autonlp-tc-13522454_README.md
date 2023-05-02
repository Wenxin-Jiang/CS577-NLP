---
tags: autonlp
language: en
widget:
- text: "I love AutoNLP 🤗"
datasets:
- Kceilord/autonlp-data-tc
---

# Model Trained Using AutoNLP

- Problem type: Binary Classification
- Model ID: 13522454

## Validation Metrics

- Loss: 0.31450966000556946
- Accuracy: 0.8461538461538461
- Precision: 0.8181818181818182
- Recall: 0.782608695652174
- AUC: 0.9369259032455604
- F1: 0.8

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoNLP"}' https://api-inference.huggingface.co/models/Kceilord/autonlp-tc-13522454
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("Kceilord/autonlp-tc-13522454", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("Kceilord/autonlp-tc-13522454", use_auth_token=True)

inputs = tokenizer("I love AutoNLP", return_tensors="pt")

outputs = model(**inputs)
```